# Dieses Skript definiert die Helfer-Klasse. Sie enthält sämtliche Logik, welche nicht in das Streamlit Skript gehört.

from random import randint # Importiere randint um zufällige Zahlen zu erstellen

class Helper:

    def __init__(self, rezepte):
        # Beim erstellen der Helferklasse muss ein Parameter rezepte mitgegeben werden.
        # Der Parameter übergibt die Rezepte an den Helfer für die Verwendung in weiteren Funktionen.
        self.my_rezepte = rezepte
    
    def deinFavorit(self, favorite, pref):
        top_score = 0
        self.my_favorite = favorite
        self.my_pref = pref

        for rezept in self.my_rezepte:
            score = 0 
    
            for i in range(3):
                if self.my_pref[i] == rezept[i+1]:
                    score = score + 1
            if score > top_score:
                top_score = score 
                self.my_favorite = rezept[0]
        #print('Lieblingsrezept', favorite, 'mit', top_score, 'Punkten')
        return self.my_favorite
    

    
