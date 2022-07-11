# tre modi per comporre una stringa dinamica in Python

nome = "Davide"
frase = "Ei, ciao " + nome + ". Come va?"

print(frase)

# OUTPUT
# Ei, ciao Davide. Come va?

nome = "Davide"
frase = f"Ei, ciao {nome}. Come va?"

print(frase)

# OUTPUT
# Ei, ciao Davide. Come va?

nome = "Davide"
frase = "Ei, ciao {}. Come va?".format(nome)

print(frase)

# OUTPUT
# Ei, ciao Davide. Come va?

