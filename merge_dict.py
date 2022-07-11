# merge di due dizionari in Python

dict_1 = {'Italia': 'Roma', 'Olanda': 'Amsterdam'}
dict_2 = {'Portogallo': 'Lisbona', 'Francia': 'Parigi'}

new_dict = {**dict_1, **dict_2}

print(new_dict)

# OUTPUT

# {'Italia': 'Roma', 'Olanda': 'Amsterdam', 'Portogallo': 'Lisbona', 'Francia': 'Parigi'}

