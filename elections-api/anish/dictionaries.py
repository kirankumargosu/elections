list1 = [1, 2, 3]
tuple1 = (1, 2, 3)
dict1 = {'a': 1, 
         'b': 2, 
         'c': 3}
set1 = {1, 2, 3}


students = {
    6: "Anish",
    2: "Anish",
    4: "Suresh",
    5: "Ramesh",
    11: "Ganesh",
    4: "Mahesh",
    100: "Rajesh"
}
print(students)



# dictionaries has key value pairs
# keys are unique
# values can be duplicate

# potatoes 100
# tomatoes 80
# onions 50
# carrots 40

vegetables = {
    'potatoes': 100,
    'tomatoes': 80,
    'onions': 50,
    'carrots': 40
}
print(type(vegetables))
print(vegetables['onions'])
# how to add a new key value pair to the dictionary
vegetables['beans'] = 70
print(vegetables)
# how to update a value for a given key
vegetables['carrots'] = 45
print(vegetables)
# how to remove a key value pair from the dictionary
vegetables.pop('tomatoes')
print(vegetables)
# how to get all keys from the dictionary
print(vegetables.keys())
# how to get all values from the dictionary
print(vegetables.values())
# how to get all key value pairs from the dictionary
print(vegetables.items())

# how to loop through all key value pairs in the dictionary
for k, v in vegetables.items():
    print(k, v)

# how to check if a key is present in the dictionary
if 'onions' in vegetables:
    print("onions is present in the dictionary")
else:
    print("onions is not present in the dictionary")

# how to check if a value is present in the dictionary
if 100 in vegetables.values():
    print("100 is present in the dictionary")
else:
    print("100 is not present in the dictionary")

# how to get the value for a given key
print(vegetables.get('carrots'))
print(vegetables['carrots'])

# how to get the value for a given key if the key is not present in the dictionary
print(vegetables.get('cabbage')) # None because cabbage is not present in the dictionary
print(vegetables.get('cabbage', 500))

# print(vegetables['cabbage']) # KeyError because cabbage is not present in the dictionary

# how to get the number of key value pairs in the dictionary
print(len(vegetables))

# how to clear the dictionary
vegetables.clear()
print(vegetables)




X = {'Jeevan': 25, 'Anish': 24, 'Suresh': 26}

print('Jeevan' in X, 24 in X.values(), sep='#')


dic = {'Nitin': (1, 'NIIT'), 'Anish': (2, 'NIIT'), 'Suresh': (3, 'NIIT')}
print(dic)
print(str(dic))
result = [(k, i, j) for k, (i, j) in dic.items()]
print(result)

result = [(k, v[0], v[1]) for k, v in dic.items()]
print(result)
