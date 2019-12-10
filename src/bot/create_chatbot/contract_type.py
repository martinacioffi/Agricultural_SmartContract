type_name = 'ContractType'

type_tp = [
    [{'text': 'A ',
      'entity_type': None,
      'alias': None,
      'user_defined': False},
     {'text': 'standard',
      'entity_type': '@contract-type',
      'alias': 'contract-type',
      'user_defined': True},
     {'text': ' contract should be enough.',
      'entity_type': None,
      'alias': None,
      'user_defined': False}],
    [{'text': 'I would like a ',
      'entity_type': None,
      'alias': None,
      'user_defined': False},
     {'text': 'customizable',
      'entity_type': '@contract-type',
      'alias': 'contract-type',
      'user_defined': True},
     {'text': ' one.',
      'entity_type': None,
      'alias': None,
      'user_defined': False}],
    [{'text': 'Let\'s do a ',
      'entity_type': None,
      'alias': None,
      'user_defined': False},
     {'text': 'personalied',
      'entity_type': '@contract-type',
      'alias': 'contract-type',
      'user_defined': True},
     {'text': ' contract.',
      'entity_type': None,
      'alias': None,
      'user_defined': False}],
    [{'text': 'I can use a',
      'entity_type': None,
      'alias': None,
      'user_defined': False},
     {'text': 'standard',
      'entity_type': '@contract-type',
      'alias': 'contract-type',
      'user_defined': True},
     {'text': ' one',
      'entity_type': None,
      'alias': None,
      'user_defined': False}],
    [{'text': 'I want to write ',
      'entity_type': None,
      'alias': None,
      'user_defined': False},
     {'text': 'my own',
      'entity_type': '@contract-type',
      'alias': 'contract-type',
      'user_defined': True},
     {'text': ' contract.',
      'entity_type': None,
      'alias': None,
      'user_defined': False}],
]

type_mt = [('Alright, we can proceed with a $contract-type contract. '
            'For which month would you like to insure your crops?')]

type_params = [{'name': '',
                'display_name': 'contract-type',
                'value': 'contract-type',
                'mandatory': True,
                'entity_type_display_name': '@contract-type',
                'prompts': ['Which type of contract do you prefer? Standard or customized?'],
                'is_list': False}
               ]
