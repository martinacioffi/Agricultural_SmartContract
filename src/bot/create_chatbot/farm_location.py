location_name = 'FarmLocation'

location_tp = [
    [{'text': 'It is in ',
      'entity_type': None,
      'alias': None,
      'user_defined': False},
     {'text': 'Kenya',
      'entity_type': '@sys.geo-country',
      'alias': 'geo-country',
      'user_defined': True}],
    [{'text': 'Dutton',
      'entity_type': '@sys.geo-city',
      'alias': 'geo-city',
      'user_defined': True},
     {'text': ', ',
      'entity_type': None,
      'alias': None,
      'user_defined': False},
     {'text': 'Montana',
      'entity_type': '@sys.geo-state',
      'alias': 'geo-state',
      'user_defined': True}],
    [{'text': 'It is located in ',
      'entity_type': None,
      'alias': None,
      'user_defined': False},
     {'text': 'Great Falls',
      'entity_type': '@sys.geo-city',
      'alias': 'geo-city',
      'user_defined': True}],
    [{'text': 'Milan',
      'entity_type': '@sys.geo-city',
      'alias': 'geo-city',
      'user_defined': True},
     {'text': ', ',
      'entity_type': None,
      'alias': None,
      'user_defined': False},
     {'text': 'Italy',
      'entity_type': '@sys.geo-state',
      'alias': 'geo-state',
      'user_defined': True},
     {'text': ', ',
      'entity_type': None,
      'alias': None,
      'user_defined': False},
     {'text': '20135',
      'entity_type': '@sys.zip-code',
      'alias': 'zip-code',
      'user_defined': True}],
    [{'text': 'It is in ',
      'entity_type': None,
      'alias': None,
      'user_defined': False},
     {'text': 'France',
      'entity_type': '@sys.geo-country',
      'alias': 'geo-country',
      'user_defined': True}],
    [{'text': 'Zimbabwe',
      'entity_type': '@sys.geo-state',
      'alias': 'geo-state',
      'user_defined': True},
     {'text': ', ',
      'entity_type': None,
      'alias': None,
      'user_defined': False},
     {'text': '45231',
      'entity_type': '@sys.zip-code',
      'alias': 'zip-code',
      'user_defined': True}],
    [{'text': 'In ',
      'entity_type': None,
      'alias': None,
      'user_defined': False},
     {'text': 'Mexico',
      'entity_type': '@sys.geo-country',
      'alias': 'geo-country',
      'user_defined': True}],
    [{'text': 'My farm is located in ',
      'entity_type': None,
      'alias': None,
      'user_defined': False},
     {'text': 'India',
      'entity_type': '@sys.geo-state',
      'alias': 'geo-state',
      'user_defined': True},
     {'text': ', ',
      'entity_type': None,
      'alias': None,
      'user_defined': False},
     {'text': 'Maharashtra',
      'entity_type': '@sys.geo-city',
      'alias': 'geo-city',
      'user_defined': True},
     {'text': ', ',
      'entity_type': None,
      'alias': None,
      'user_defined': False},
     {'text': '99887',
      'entity_type': '@sys.zip-code',
      'alias': 'zip-code',
      'user_defined': True}]
]

location_mt = ['Okay, I got your farm\'s address. Can you plase tell me your land\'s size?']

location_params = [{'name': '',
                    'display_name': 'geo-country',
                    'value': '$geo-country',
                    'mandatory': True,
                    'entity_type_display_name': '@sys.geo-country',
                    'prompts': ['Please, specify also the country is located.'],
                    'is_list': False},
                   {'name': '',
                    'display_name': 'zip-code',
                    'value': 'zip-code',
                    'mandatory': True,
                    'entity_type_display_name': '@sys.zip-code',
                    'prompts': ['What\'s the zip code?'],
                    'is_list': False},
                   {'name': '',
                    'display_name': 'geo-city',
                    'value': '$geo-city',
                    'mandatory': True,
                    'entity_type_display_name': '@sys.geo-city',
                    'prompts': ['In which city is your farm located again?'],
                    'is_list': False},
                   {'name': '',
                    'display_name': 'geo-state',
                    'value': '$geo-state',
                    'mandatory': False,
                    'entity_type_display_name': '@sys.geo-state',
                    'is_list': False}
                   ]