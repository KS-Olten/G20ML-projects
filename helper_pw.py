# Dieses Skript definiert die Helfer-Klasse. Sie enthält sämtliche Logik, welche nicht in das Streamlit Skript gehört.

from pyparsing import WordStart

    #Hier haben wir eine Fuktion definiert, die uns sagt, ob der Satz, der eingeben worden ist die korrekte Länge erhält.
class Helper:
    def has_correct_lenth(self, text):
        words = text.split(' ')
        print(words)
        if len(words) <= 7:
            return True
        else:
            return False
    #Hier haben wir eine Funktion definiert, die jeweils, den ersten Buchstaben eines einzelnen Wortes ausgibt   
    def the_first_letter(self,text):
        initials = ""
        for word in text.split():
                initials += word[0]
        print(initials.upper())
        return initials
    #Hier haben wir eine Funktion definiert, welche die Länge des Wortes ausgibt. 
    def the_amount_letters(self, text): 
         amount_word = 0
         for word in text.split(): 
             amount_word = len(word)
         return amount_word
    #Auch diese Funktion dient dazu, die länge, also die Anzahl Buchstaben eines Wortes auszugeben.
    def the_initials_len(self,text):
        initials = ""
        for word in text.split():
                initials += word[0]
        amount = text.split()

        numbers = ""
        for word in amount:
             numbers = numbers + str(len(word))

        password = initials + numbers
        return password 
    
    
