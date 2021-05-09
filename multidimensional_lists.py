menus = [['Egg Sandwich', 'Bagel', 'Coffe'], ['BLT', 'PB&J', 'Turkey'], ['Soup', 'Salad', 'Spaghetti', 'Taco']]

print('Breakfast menu:\t', menus[0])
print('Lunch menu:\t', menus[1])
print('Dinner menu:\t', menus[2])

menus_list = {'Breakfast': ['Egg Sandwich', 'Bagel', 'Coffe'], 
'Lunch': ['BLT', 'PB&J', 'Turkey'],
'Dinner': ['Soup', 'Salad', 'Spaghetti', 'Taco']}

for key, value in menus_list.items():
    print('key', key, 'value', value )

person = {'name': 'Rick',
'last name' : 'Rex',
'age': 29}

print(person.get('name') , 'is' , person.get('age'), 'years old')

import requests
response = requests.get('http://api.open-notify.org/astros.json')
json = response.json()
print(json)
print('the people in space now are:')
for person in json['people']:
    print(person['name'])
