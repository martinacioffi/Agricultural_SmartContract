size_name = 'LandSize'

size_tp = [
    [{'text': '45 meters',
      'entity_type': '@sys.unit-length',
      'alias': 'unit-length',
      'user_defined': True},
     {'text': ' by ',
      'entity_type': None,
      'alias': None,
      'user_defined': False},
     {'text': '7',
      'entity_type': '@sys.number',
      'alias': 'number',
      'user_defined': True}],
    [{'text': '50 squared meters',
      'entity_type': '@sys.unit-area',
      'alias': 'unit-area',
      'user_defined': True}],
    [{'text': '2 hectares',
      'entity_type': '@sys.unit-area',
      'alias': 'unit-area',
      'user_defined': True}],
    [{'text': '1.18 hectares',
      'entity_type': '@sys.unit-area',
      'alias': 'unit-area',
      'user_defined': True}]
]

size_mt = [('Alright, I got your land size. What\'s your crop affected by? '
            'As of now, we offer protection against Rainfall, Temperature and Wind Speed.')]

size_params = [{'name': '',
                'display_name': 'unit-area',
                'value': 'unit-area',
                'mandatory': True,
                'entity_type_display_name': '@sys.unit-area',
                'prompts': ['Please, enter a valid area.'],
                'is_list': False},
               {'name': '',
                'display_name': 'unit-length',
                'value': '$unit-length',
                'mandatory': False,
                'entity_type_display_name': '@sys.unit-length',
                'is_list': False},
               {'name': '',
                'display_name': 'number',
                'value': '$number',
                'mandatory': False,
                'entity_type_display_name': '@sys.number',
                'is_list': False}
               ]
