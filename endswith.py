# controllare se una stringa inizia o finisce con un certo pattern in Python

contacts = ["davide@gmail.com", "alessandra@gmail.it"]

for contact in contacts:
	print(contact.endswith("com")) # controllo se finisce con "com"

# OUTPUT

# True
# False

# commento al codice:
# il primo contatto finisce con "com" e quindi Python mi restituisce True
# il secondo contatto non finisce con "com" e quindi Python mi restituisce False

for contact in contacts:
	print(contact.startswith("alessandra")) # controllo se inizia con "alessandra"

# OUTPUT

# False
# True