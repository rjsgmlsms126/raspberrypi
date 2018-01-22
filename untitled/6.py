dict1={
    'a':('a','b','c'),
    'b':[1,2,3],
    'c': {'name': 'hong',
           'age': 23
    }
}


print(dict1)
print(dict1['a'])
dict1['b']=7;
print(dict1)
print(len(dict1))


print(dict1['c'])
print(dict1['c']['name'])
dict1['c']['age']=25
print(dict1)