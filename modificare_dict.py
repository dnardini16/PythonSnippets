# modificare valore di una chiave in un dizionario in Python

dizionario = {"Matematica": 7, "Filosofia": 8, "Italiano": 9}

dizionario["Matematica"] = 10

print(dizionario)

'''
{'Matematica': 10, 'Filosofia': 8, 'Italiano': 9}
'''

dizionario.update({"Matematica": 10})

print(dizionario)

'''
{'Matematica': 10, 'Filosofia': 8, 'Italiano': 9}
'''