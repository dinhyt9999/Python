def create_new_dictionary():
    new_dictionary = {}
    key = ' '
    while key != '':
        key = input('key: ')
        if key != '':
            value = input('value: ')
            new_dictionary[key] = value
    return new_dictionary

def paragraph_split(paragraph):
    dictionary = {}
    words = paragraph.split()
    for item in words:
        if item not in dictionary:
            dictionary[item] = 1
        else:
            dictionary[item] += 1
    return dictionary

def value_to_int(dictionary):
    for key,value in dictionary.items():
        dictionary[key] = int(value)
    return dictionary

def merge_dictionary(dict1,dict2):
    value_to_int(dict1)
    value_to_int(dict2)
    for key,value in dict2.items():
        if key not in dict1:
            dict1[key] = value
        else:
            dict1[key] += value
    return dict1

def sort_by_key(dictionary):
    list = []
    new_dict = {}
    for key in dictionary:
        list.append(key)
    list.sort()
    for item in list:
        new_dict[item] = dictionary[item]
    return new_dict


def swap(list,p1,p2):
    list[p1], list[p2] = list[p2], list[p1]
    return list

def sort_two_list(list_key, list_value):
    for i in range(len(list_value)-1):
        for j in range(i+1, len(list_value)):
            if list_value[i] > list_value[j]:
                swap(list_value,i,j)
                swap(list_key,i,j)
    return (list_key, list_value)

def sort_by_value(dictionary):
    list_value = []
    list_key = []
    new_dict = {}
    for key,value in dictionary.items():
        list_value.append(value)
        list_key.append(key)
    sort_two_list(list_key,list_value)
    for i in range(len(list_value))
        new_dict[list_key[i]] = list_value[i]
    return new_dict
