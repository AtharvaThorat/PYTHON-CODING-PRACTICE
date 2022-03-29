dict_value = {'Madrid': 'Spain', 'Paris': 'France', 'Rome': 'Italy'}

list_inside = ['Football', 'Cricket']

dict_copy = dict_value.copy()
list_inside.append(dict_copy)

# accessing dictionary values inside list
dict_access = list_inside[2]
dict_access1 = list_inside[2]['Paris']
dict_access2 = list_inside[2]['Rome']


print(dict_access)
print(dict_access1)
print(dict_access2)


