# creating a dictionary in Python
data = {1:'name1', 2:'name2', 3:'name3'}
print(data)
# retreving a value from the dictionary
print(data[3])

print(data.get(1))

# if u dont have any value in the dictionary then u can assign key  with a value not found in get method but if u have a value then it will print that value
print(data.get(4,'Not found'))
print(data.get(2,'Not found'))

# create dictionary with lists 
keys = ["Name1","Name2","Name3"]
values = [1,2,3]
# creating dict using zip
datadict = dict(zip(keys,values))
print(datadict)
#creating dict using dict
datadict1 = dict(keys=keys, values=values)
print(datadict1)

#to add a values in dict
data[4] = 'name4'
print(data)
#to delete a value from dict
del data[4]
print(data)

#a nested dictionary
nested_dict = {
    'dict1': {'key1': 'value1', 'key2': 'value2'},
    'dict2': {'key3': 'value3', 'key4': 'value4'}
}
print(nested_dict)
# to access a nested dict
print(nested_dict['dict2']['key4'])

# more combination of dictionary and list 
combdict ={'JS':'user1','cs':'user2','python':['user3','user4'],'java':{'jse':'user5','jee':'user6'}}
print(combdict)
print(combdict['python'][1])
print(combdict['java']['jse'])
