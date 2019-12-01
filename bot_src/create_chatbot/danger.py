danger_name = 'SpecifyDanger'

danger_tp = [
    [{'text': 'I am afraid of too much ',
      'entity_type': None,
      'alias': None,
      'user_defined': False},
     {'text': 'rain',
      'entity_type': '@danger',
      'alias': 'danger',
      'user_defined': True}],
    [{'text': 'My income gets very low due to ',
      'entity_type': None,
      'alias': None,
      'user_defined': False},
     {'text': 'precipitation',
      'entity_type': '@danger',
      'alias': 'danger',
      'user_defined': True}],
    [{'text': 'I get poor when the ',
      'entity_type': None,
      'alias': None,
      'user_defined': False},
     {'text': 'wind',
      'entity_type': '@danger',
      'alias': 'danger',
      'user_defined': True},
     {'text': ' is too fast.',
      'entity_type': None,
      'alias': None,
      'user_defined': False}],
    [{'text': 'My crops are affected by the ',
      'entity_type': None,
      'alias': None,
      'user_defined': False},
     {'text': 'rain',
      'entity_type': '@danger',
      'alias': 'danger',
      'user_defined': True}]
]

danger_mt = [('Okay, we can insure you against $danger . '
              'Would you like to use a standard contract or write a customized one?')]

danger_params = [{'name': '',
                  'display_name': 'danger',
                  'value': 'danger',
                  'mandatory': True,
                  'entity_type_display_name': '@danger',
                  'prompts': ['Please, specify what would you like to insure against.'],
                  'is_list': False}
                 ]
