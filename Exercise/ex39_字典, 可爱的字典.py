#建立缩写表
states = {
    'Oregon':'OR',
    'Florida':'FL',
    'California':'CA',
    'New York':'NY',
    'Michigan':'MI'
}

#建立一些州与城市的对应关系
cities = {
    'CA':'San Francisco',
    'MI':'Detroit',
    'FL':'Jacksonville'
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print('-'*20)
print('NY State has',cities['NY'])
print('OR State has',cities['OR'])

print('-'*30)
print("Michigan's abbreviation is",states['Michigan'])
print("Florida's abbreviation is",states['Florida'])

print('-'*30)
for state,abbreviation in states.items():
    print("%s's abbreviation is %s"%(state,abbreviation))

print('-' * 50)
for state,abbreviation in states.items():
    print("%s's abbreviation is %s and has city %s"%(state,abbreviation,cities[abbreviation]))

print('-'*50)
print("Find Texas's abbreviation if it's in dic.")
abb = states.get('Taxas',None)

if not abb:
    print("Sorry, Taxas is not in states dic.")
print('-'*50)
print("Find Texas's city if it's in cities dic.")
city = cities.get('Taxas','Does Not Exist')
print("The city in Taxas is %s"%city)