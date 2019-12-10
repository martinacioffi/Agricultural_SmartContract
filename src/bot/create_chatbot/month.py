month_name = 'Month'

month_tp = [
    [{'text': 'i would like my crops to be covered for ',
      'entity_type': None,
      'alias': None,
      'user_defined': False},
     {'text': 'march',
      'entity_type': '@sys.date-period',
      'alias': 'date-period',
      'user_defined': True}],
    [{'text': 'for ',
      'entity_type': None,
      'alias': None,
      'user_defined': False},
     {'text': 'february',
      'entity_type': '@sys.date-period',
      'alias': 'date-period',
      'user_defined': True}],
    [{'text': 'december',
      'entity_type': '@sys.date-period',
      'alias': 'date-period',
      'user_defined': True}],
    [{'text': 'i want to insure for ',
      'entity_type': None,
      'alias': None,
      'user_defined': False},
     {'text': 'the month of may',
      'entity_type': '@sys.date-period',
      'alias': 'date-period',
      'user_defined': True}],
    [{'text': 'for ',
      'entity_type': None,
      'alias': None,
      'user_defined': False},
     {'text': 'july',
      'entity_type': '@sys.date-period',
      'alias': 'date-period',
      'user_defined': True}]
]

month_mt = ['Alright, you will be insured for the month of $date-period . If you want to confirm, type PROCEED.']

month_params = [{'name': '',
                 'display_name': 'date-period',
                 'value': 'date-period',
                 'mandatory': True,
                 'entity_type_display_name': '@sys.date-period',
                 'prompts': ['For which month again?'],
                 'is_list': False}
                ]
