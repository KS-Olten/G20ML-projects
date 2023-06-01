# Helfer-Klasse


#Berechung von e rekursiv

def e_funktion(x):
    if x == 0:
        return 1
    else:
        return 1/factorial(x) + e_funktion(x-1)

#rekursive Faktorisierungs-funktion   

def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)