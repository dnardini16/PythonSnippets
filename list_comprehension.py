# list comprehension in Python
# aggiungere sia il print sia la condition

frutti = ["Ananas", "Mela", "Pera"]

nuovi_frutti = [x for x in frutti if "e" in x]

print(nuovi_frutti)

# OUTPUT

# ["Mela", "Pera"]