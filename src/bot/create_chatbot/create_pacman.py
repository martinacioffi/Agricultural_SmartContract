from src.bot.create_chatbot.helpers import create_intent, agrisc_id, create_entity, create_entity_type, get_entity_id
from src.bot.create_chatbot.create_contract import create_name, create_tp, create_mt
from src.bot.create_chatbot.holder_name import holder_name, holder_tp, holder_mt, holder_params
from src.bot.create_chatbot.farm_location import location_name, location_tp, location_mt, location_params
from src.bot.create_chatbot.land_size import size_name, size_tp, size_mt, size_params
from src.bot.create_chatbot.danger import danger_name, danger_tp, danger_mt, danger_params
from src.bot.create_chatbot.contract_type import type_name, type_tp, type_mt, type_params
from src.bot.create_chatbot.month import month_name, month_tp, month_mt, month_params

print('Creating Pacman entities...')

create_entity_type(project_id=agrisc_id, display_name='danger', kind='KIND_MAP')
danger_id = get_entity_id(project_id=agrisc_id, entity_type='person')

create_entity(project_id=agrisc_id, entity_type_id=danger_id, entity_value='rainfall', synonyms=['rainfall', 'rain',
                                                                                                 'precipitation'])
create_entity(project_id=agrisc_id, entity_type_id=danger_id, entity_value='wind speed', synonyms=['wind speed',
                                                                                                   'wind'])
create_entity(project_id=agrisc_id, entity_type_id=danger_id, entity_value='temperature', synonyms=['temperature',
                                                                                                    'hot', 'cold',
                                                                                                    'degrees'])

create_entity_type(project_id=agrisc_id, display_name='contract-type', kind='KIND_MAP')
contract_id = get_entity_id(project_id=agrisc_id, entity_type='contract-type')

create_entity(project_id=agrisc_id, entity_type_id=contract_id, entity_value='standard', synonyms=['standard',
                                                                                                   'defined',
                                                                                                   'predefined',
                                                                                                   'pre-defined'])
create_entity(project_id=agrisc_id, entity_type_id=contract_id, entity_value='customizable', synonyms=['customizable',
                                                                                                       'customized',
                                                                                                       'personalized',
                                                                                                       'my own'])

print('\nDone. Now creating Pacman intents...')

create_intent(project_id=agrisc_id, display_name=create_name,
              training_phrases=create_tp,
              message_texts=create_mt,
              output_contexts_names={'awaiting_name': 1, 'session_vars': 50},
              action=create_name)

create_intent(project_id=agrisc_id, display_name=holder_name,
              training_phrases=holder_tp,
              message_texts=holder_mt,
              input_context_names=['awaiting_name'],
              output_contexts_names={'awaiting_location': 1},
              action=holder_name,
              parameters=holder_params)

create_intent(project_id=agrisc_id, display_name=location_name,
              training_phrases=location_tp,
              message_texts=location_mt,
              input_context_names=['awaiting_location'],
              output_contexts_names={'awaiting_land_size': 1},
              action=location_name,
              parameters=location_params)

create_intent(project_id=agrisc_id, display_name=size_name,
              training_phrases=size_tp,
              message_texts=size_mt,
              input_context_names=['awaiting_land_size'],
              output_contexts_names={'awaiting_danger': 1},
              action=size_name,
              parameters=size_params)

create_intent(project_id=agrisc_id, display_name=danger_name,
              training_phrases=danger_tp,
              message_texts=danger_mt,
              input_context_names=['awaiting_danger'],
              output_contexts_names={'awaiting_contract_type': 1},
              action=danger_name,
              parameters=danger_params)

create_intent(project_id=agrisc_id, display_name=type_name,
              training_phrases=type_tp,
              message_texts=type_mt,
              input_context_names=['awaiting_contract_type'],
              output_contexts_names={'awaiting_month': 1},
              action=type_name,
              parameters=type_params)

create_intent(project_id=agrisc_id, display_name=month_name,
              training_phrases=month_tp,
              message_texts=month_mt,
              input_context_names=['awaiting_month'],
              output_contexts_names={'confirm_proceed': 1},
              action=month_name,
              parameters=month_name)
