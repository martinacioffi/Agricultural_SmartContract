create_name = 'CreateContract'

create_tp = [
    [{'text': 'Start a new contract',
      'entity_type': None,
      'alias': None,
      'user_defined': False}
     ],
    [{'text': 'I would like to initiate a new contract',
      'entity_type': None,
      'alias': None,
      'user_defined': False}],
    [{'text': 'make a contract',
      'entity_type': None,
      'alias': None,
      'user_defined': False}
     ],
    [{'text': 'I want to start a new contract',
      'entity_type': None,
      'alias': None,
      'user_defined': False}]
]

create_mt = ['I can sure help you with that. ',
             'We can do that together. ',
             'I can get you started. ']

add = '\nCan you please start by telling me your full name?'

for i in range(len(create_mt)):
    create_mt[i] = create_mt[i] + add
