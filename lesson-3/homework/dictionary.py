dict1 = {
    1: "one",
    2: "two",
    3: "three",
}

dict2 = {
    "x": "a",
    "y": "b",
    "z": "c",
    "t": "a",
    "w": "a",
}

dict3 = {}

# task-1
# key1 = 1
# if key1 in dict1.keys():
#   print(dict1[key1])
# else:
#   print("Key doesn't exist")

# task-2
# key1 = 1
# if key1 in dict1.keys():
#   print("Key exist in dictionary")
# else:
#   print("Key not exist")

# task-3
# print(len(dict1.keys()))

# task-4
# list1 = list(dict1.keys())
# print(list1)

# task-5
# list1 = list(dict1.values())
# print(list1)

# task-6
# new_dict = dict1 | dict2
# print(new_dict)

# task-7
# key1 = 1
# if key1 in dict1.keys():
#   dict1.pop(key1)
# else:
#   print("Key not in dictionary")
# print(dict1)

# task-8
# new_dict = dict1.clear()
# print(new_dict)

# task-9
# if dict3 == {}:
#   print("Dictionary is empty")
# else:
#   print("Dictionary is not empty")

# task-10
# key1 = 1
# if key1 in dict1.keys():
#   print(key1,dict1[key1])
# else:
#   print("Key doesn't exist in dictionary")

# task-11
# new_value = 1
# dict1[new_value] = 'bir'
# print(dict1)

# task-12
# valuee = 'a'
# print(list(dict2.values()).count(valuee))

# task-13
# new_dict = {}
# for i,j in dict1.items():
#   new_dict[j] = i
# print(new_dict)

# task-14
# valuee = 'a'
# keys_list = []
# for i,j in dict2.items():
#   if j == valuee:
#     keys_list.append(i)
# print(keys_list)

# task-15
# list1 = [1,2,3]
# list2 = ['a','b','c']
# new_dict = {}
# for i in range(len(list1)):
#   new_dict[list1[i]] = list2[i]
# print(new_dict)

# task-16
# nested_dict = {
#   'a':1,
#   'b':2,
#   'c':{
#     'x':'x1',
#     'y':'y1'
#   },
#   'd':4
# }

# is_nested = False

# for i in nested_dict.keys():
#   if type(nested_dict[i]) == dict:
#     print('Exist nested value')
#     is_nested = True
# if not is_nested:
#   print('No nested value')

# task-17
# nested_dict = {
#   'a':1,
#   'b':2,
#   'c':{
#     'x':'x1',
#     'y':'y1'
#   },
#   'd':4
# }

# is_nested = False

# for i in nested_dict.keys():
#   if type(nested_dict[i]) == dict:
#     print(nested_dict[i])
#     is_nested = True
# if not is_nested:
#   print('No nested value')


# task-18
# def get_value(dictt,key,def_value):
#   return dictt[key] if key in dictt else def_value

# default_value = 0
# my_dict = {
#   'a':10,
#   'b':50
# }

# print(get_value(my_dict,'a',default_value))
# print(get_value(my_dict,'b',default_value))
# print(get_value(my_dict,'c',default_value))

# task-19
# set1 = set(dict2.values())
# print(len(set1))

# task-20
# sorted_dict = {key:dict2[key] for key in sorted(dict2)}
# print(sorted_dict)

# task-21
# sorted_dict = {key:value for key,value in sorted(dict2.items(),key=lambda item:item[1])}
# print(sorted_dict)

# task-22
# dict0 = {
#   'a':3,
#   'b':7,
#   'c':2,
#   'd':8,
#   'e':11,
# }

# new_dict = {key:value for key,value in dict0.items() if value > 5}
# print(new_dict)

# task-23
# dict01 = {
#   'a':1,
#   'b':3,
#   'c':5
# }

# dict02 = {
#   'a':5,
#   'b':6,
#   'd':7
# }

# is_common = False

# for i in dict01.keys():
#   if i in dict02.keys():
#     is_common = True
#     break
# if is_common:
#   print('Exist common keys')
# else:
#   print('No common keys')

# task-24
# tpl = ((1,2),(3,4),(5,6))
# new_dict = {}
# for i in tpl:
#   new_dict[i[0]] = i[1]
# print(new_dict)


# task-25
# if dict1 != {}:
#   for i in dict1.keys():
#     print(i,dict1[i])
#     break
# else:
#   print('Dictionary is empty')
