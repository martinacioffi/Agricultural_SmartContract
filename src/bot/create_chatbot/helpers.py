import dialogflow_v2 as dialogflow
from typing import List, Dict, Tuple, Optional
import os

# agrisc_id = 'agrisc-tafasq'
agrisc_id = os.environ['PROJECT_ID']


def create_intent(project_id: str, display_name: str, training_phrases: List[List[Dict]],
                  message_texts: List[str], input_context_names: List[str] = None,
                  output_contexts_names: Dict[str, int] = None, action: str = None,
                  parameters: List[Dict] = None, webhook_state: bool = True, priority: int = 500000):

    """Create an intent of the given intent type."""

    intents_client = dialogflow.IntentsClient()
    parent = intents_client.project_agent_path(project_id)

    annotated_training_phrases = []
    for training_phrase in training_phrases:
        annos = []
        for part in training_phrase:
            annotated_part = dialogflow.types.Intent.TrainingPhrase.Part(text=part['text'],
                                                                         entity_type=part['entity_type'],
                                                                         alias=part['alias'],
                                                                         user_defined=part['user_defined'])
            annos.append(annotated_part)
        annotated_training_phrase = dialogflow.types.Intent.TrainingPhrase(parts=annos)
        annotated_training_phrases.append(annotated_training_phrase)

    text = dialogflow.types.Intent.Message.Text(text=message_texts)
    message = dialogflow.types.Intent.Message(text=text)

    if output_contexts_names:
        output_contexts = [dialogflow.types.Context(name=f'projects/{project_id}/agent/sessions/-/contexts/{cont}',
                                                    lifespan_count=output_contexts_names[cont])
                           for cont in output_contexts_names.keys()]
    else:
        output_contexts = None

    if input_context_names:
        input_contexts = [f'projects/{project_id}/agent/sessions/-/contexts/{cont}' for cont in input_context_names]
    else:
        input_contexts = None

    intent = dialogflow.types.Intent(
        display_name=display_name,
        training_phrases=annotated_training_phrases,
        messages=[message],
        input_context_names=input_contexts,
        output_contexts=output_contexts,
        action=action,
        parameters=parameters,
        webhook_state=webhook_state,
        priority=priority
    )

    response = intents_client.create_intent(parent, intent)

    print('Intent created: {}'.format(response))


def create_entity_type(project_id: str, display_name: str, kind: str):

    """Create an entity type with the given display name."""

    entity_types_client = dialogflow.EntityTypesClient()
    parent = entity_types_client.project_agent_path(project_id)

    entity_type = dialogflow.types.EntityType(
        display_name=display_name, kind=kind)

    response = entity_types_client.create_entity_type(parent, entity_type)

    print('Entity type created: \n{}'.format(response))


def get_entity_id(project_id: str, entity_type: str) -> Optional[str]:

    """Returns the ID of the specified entity."""

    client = dialogflow.EntityTypesClient()
    parent = client.project_agent_path(project_id)
    for element in client.list_entity_types(parent):
        if element.display_name == entity_type:
            return element.name.split('/')[-1]


def create_entity(project_id: str, entity_type_id: str, entity_value: str, synonyms: List[str]):

    """Create an entity of the given entity type."""

    entity_types_client = dialogflow.EntityTypesClient()
    synonyms = synonyms or [entity_value]

    entity_type_path = entity_types_client.entity_type_path(
        project_id, entity_type_id)

    entity = dialogflow.types.EntityType.Entity()
    entity.value = entity_value
    entity.synonyms.extend(synonyms)

    response = entity_types_client.batch_create_entities(
        entity_type_path, [entity])

    print('Entity created: {}'.format(response))


def detect_intent_texts(project_id: str, session_id: str, text: str, language_code: str = 'en') -> Tuple:

    """Detects the intent for a specific agent, given the user's query."""

    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)

    if text:
        text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
        query_input = dialogflow.types.QueryInput(text=text_input)
        response = session_client.detect_intent(session=session, query_input=query_input)
        return response.query_result.action, response.query_result.fulfillment_text


def get_params(project_id: str, session_id: str, text: str, language_code: str = 'en') -> Tuple[str, int]:

    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)

    text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.types.QueryInput(text=text_input)
    response = session_client.detect_intent(session=session, query_input=query_input)
    params = response.query_result.output_contexts[0].parameters
    location = params.fields['geo-city'].string_value
    month = int(params.fields['date-period'].struct_value.fields['startDate'].string_value.split('-')[1][-1])
    return location, month
