# reset o eliminazione di una lista

squadre = ["Napoli", "Milan", "Inter"]

squadre.clear()

print(squadre)

# OUTPUT

# []

squadre = ["Napoli", "Milan", "Inter"]

del squadre

print(squadre)

# OUTPUT

# ---------------------------------------------------------------------------
# NameError                                 Traceback (most recent call last)
# <ipython-input-28-2406284cf35d> in <module>()
#       1 del squadre
# ----> 2 print(squadre)
# NameError: name 'squadre' is not defined

# commento al codice:
# Python è andato in errore perché la lista "squadre" non esiste più

