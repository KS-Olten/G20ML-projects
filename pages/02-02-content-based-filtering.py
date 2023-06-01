# Dies ist die Streamlit App. Sie enthält nur Code, welcher für die Darstellung relevant ist

import streamlit as st # Lade streamlit Bibliothek

#Ansatz mit Klassen, wieder verworfen
from helper_content_based_filtering import Helper # Lade Helfer-Klasse aus helper.py



# Rezepte -> Text, süss, salzig, vegetarisch 
rezept_1 = ['Ei im Töpfchen: https://migusto.migros.ch/de/rezepte/ei-im-toepfchen', False, True, True]
rezept_2 = ['Mango-Vaocado-Garnelen-Salat: https://trickytine.com/exotischer-garnelen-mango-avocado-salat/', True, True, False]
rezept_3 = ['cookies mit Beeren-Jogurt: https://fooby.ch/de/rezepte/13706/fruehstuecks-cookies-mit-beeren-jogurt?startAuto1=0', True , False  , True ]
rezept_4 = ['Pancakes: https://fooby.ch/de/rezepte/20239/mini-fruehstuecks-pancakes?startAuto1=0', True, False, True]
rezept_5 = ['SChoggi-Weggli: https://fooby.ch/de/rezepte/21658/schoggi-weggli?startAuto1=0', True, False, True]
rezept_6 = ['Mexikanische Frühstückeier: https://fooby.ch/de/rezepte/15611/mexikanische-fruehstueckseier--huevos-rancheros-?startAuto1=0', False, True, False]
rezept_7 = ['Blauer kartoffelsalat mit Lachs: https://fooby.ch/de/rezepte/19114/blauer-kartoffelsalat-mit-lachs?startAuto1=0', False, True, False]

# Rezeptenliste
rezepte = [rezept_1, rezept_2, rezept_3, rezept_4, rezept_5, rezept_6, rezept_7]

# Helper Objekt mit den Rezepten anlegen für spätere Funktionen
h = Helper(rezepte) # Erstelle Helfer-Objekt

#Titel 
st.title('Das perfekte Frühstück für dich')



# Erklärungstext an den Nutzer der App 
st.write('Diese Website erstellt das perfekt zu dir passende Frühstück, basierend auf dem System des Content Based Filtering. Bei dieser Methode wird anhand von mehreren Bildern ein Nutzungsprofil von dir erstellt und auf diesem basierend werden dir passende Rezepte vorgeschlagen.')




#Anzeige der Kriterienauswahl mit Bildern
st.header('Nutzungsprofilgenerator')
name = st.text_input('Gib deinen Namen ein.')

# Bild1 
col1, col2 = st.columns(2)
with col1:
    st.image ('müsli.jpg')
with col2:
    Frage1 = st.radio( 'auswahl1', ['Gefällt mir', 'Gefällt mir nicht'])

#Bild2
col3, col4 = st.columns(2)
with col3:
    st.image ('englishbreakfast.jpg')
with col4:
    Frage2 = st.radio( 'auswahl2', ['Gefällt mir', 'Gefällt mir nicht'])

#Bild3
col5, col6 = st.columns(2)
with col5:
    st.image ('avocado.jpg')
with col6:
    Frage3 = st.radio( 'auswahl3', ['Gefällt mir', 'Gefällt mir nicht'])


#Funktionalitäten 
# Setze Nutzer Präferenzen
if Frage1 == 'Gefällt mir':
    suess = True
else:
    suess = False

if Frage2 == 'Gefällt mir':
    vegetarisch = False
else:
    vegetarisch = True

if Frage3 == 'Gefällt mir':
    salzig = True
else:
    salzig = False

#Setzen der gewählten Eigenschaften
pref = [suess, salzig, vegetarisch]
st.subheader(name)
st.subheader("Rezepte für dein perfektes Frühstück")


#Anzeige der ermittelten Eigenschaften 
Begruendung = "Deine gewählten Eigenschaften: "
if pref[0] == True:
    Begruendung = Begruendung + " süss,"
else:
    Begruendung = Begruendung + " nicht süss,"

if pref[1] == True:
    Begruendung = Begruendung + " salzig,"
else:
    Begruendung = Begruendung + " nicht salzig,"

if pref[2] == True:
    Begruendung = Begruendung + " vegetarisch"
else: 
    Begruendung = Begruendung + " nicht vegetarisch."

st.write(Begruendung)


# Ermittlung des passensten Rezeptes, das mit dem höchsten Treffer 
st.header('') #Für Abstand zwischen den Zeilen 
st.markdown('##### Dein passenstes Rezept')

favorite = "Leider hat es kein Rezept für Dich ;("
favorite = h.deinFavorit(favorite, pref)


#kontrollausgabe ins Terminal 
st.write (favorite)

#Ermittlung aller Rezepte mit den gewählten Kriterien - könnte man wie das Favoriten Rezept in den helper auslagern 
gefilterteRezepte =[]
st.header('') #Für Abstand zwischen den Zeilen 
st.markdown('##### Rezepte, die mit deinen Kriterien übereinstimmen:')
for rezept in rezepte:
    passung = True
    for i in range(3):
        if pref[i] != rezept[i+1]:
            passung = False
            break
    if passung == True:
        gefilterteRezepte.append(rezept)

for rezept in gefilterteRezepte:
    st.write(rezept[0]) 
    


            



        









     

