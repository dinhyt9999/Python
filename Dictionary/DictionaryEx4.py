import Function

print('input dictionary 1:\n')
dict1 = Function.create_new_dictionary()
print('input dictionary 2:\n')
dict2 = Function.create_new_dictionary()

dict1 = Function.merge_dictionary(dict1,dict2)
print('new dictionary:',dict1)
