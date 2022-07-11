# rimuovere elementi da una lista

frutti = ['Mela Verde', 'Ananas', 'Banana', 'Pera', 'Mela Jazz']

frutti.remove('Mela Jazz') # remove

print(frutti)

# OUTPUT

# ['Mela Verde', 'Ananas', 'Banana', 'Pera']

frutti = ['Mela Verde', 'Ananas', 'Banana', 'Pera', 'Mela Jazz']

frutti.pop(1) # pop

print(frutti)

# OUTPUT

# ['Mela Verde', 'Banana', 'Pera', 'Mela Jazz']

## commento al codice:
# .remove() rimuove l'elemento dato (se trovato)
# .pop() rimuove l'elemento in base all'indice