

x = ('key1', 'key2', 'key3')
thisdict = dict.fromkeys(x)
print(type(x))
print(thisdict)

car = {
  'brand': 'Ford',
  'model': 'Mustang',
  'year': 1964
}
car.clear()
print(car)




car = {
  'brand': 'Ford',
  'model': 'Mustang',
  'year': 1964
}
x = car.copy()
print(type(x))
print(x)


car = {
  'brand': 'Ford',
  'model': 'Mustang',
  'year': 1964
}
x = car.get('price', 15000)
print(type(x))
print(x)


car = {
  'brand': 'Ford',
  'model': 'Mustang',
  'year': 1964
}
x = car.items()
car['year'] = 2018
print(type(x))
print(x)


car = {
  'brand': 'Ford',
  'model': 'Mustang',
  'year': 1964
}
x = car.keys()
car['color'] = 'white'
print(type(x))
print(x)

car = {
  'brand': 'Ford',
  'model': 'Mustang',
  'year': 1964
}
#car.pop('model')
print(car.pop('model'))

car = {
  'brand': 'Ford',
  'model': 'Mustang',
  'year': 1964
}
# car.popitem()
print(car.popitem())

car = {
  'brand': 'Ford',
  'model': 'Mustang',
  'year': 1964
}
print(type(car.setdefault('color', 'white')))
print(car)

car = {
  'brand': 'Ford',
  'model': 'Mustang',
  'year': 1964
}
car.update({'color': 'White'})
print(car.update({'color': 'White'}))

car = {
  'brand': 'Ford',
  'model': 'Mustang',
  'year': 1964
}
x = car.values()
car['year'] = 2018
  
print(i)

car = {
    's' : 2,
    'b' : 1
}

print(car)

car['s'] += 1 
car['a'] = 1 


print(car)
