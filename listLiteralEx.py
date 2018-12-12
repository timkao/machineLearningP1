all_data = [
  ['John', 'Emily', 'Michael', 'Mary', 'Steven'],
  ['Maria', 'Juan', 'Javier', 'Natalia', 'Pilar']
]

def flatten(arr):
  return [
    name for names in arr for name in names if name.count('e') >= 2
  ]

print(flatten(all_data))
