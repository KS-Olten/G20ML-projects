import streamlit as st # Lade streamlit Bibliothek

st.title('Brute-Force-Attacken')
st.divider()

#Brute-Force-Attacken Erklärung
st.header('Was sind Brute-Force-Attacken')

st.write('Ein Brute-Force-Angriff ist eine Methode, um Passwörter zu knacken oder verschlüsselte Daten zu entschlüsseln. Bei diesem Angriff versucht ein Angreifer, durch systematisches Ausprobieren aller möglichen Passwörter oder Schlüssel Zugang zu einem gesicherten System oder einer verschlüsselten Datei zu erlangen. Der Name "Brute Force" bedeutet auf Deutsch "brutale Kraft". Der Name kommt von der Idee, dass der Angreifer mit "brutaler Kraft" vorgeht und alle möglichen Kombinationen von Passwörtern durchprobiert, um schließlich das richtige Passwort herauszufinden. Die Anzahl der benötigten Versuche, um das richtige Passwort oder den richtigen Schlüssel zu erraten, hängt von der Länge und Komplexität des Passworts beziehungsweise des Schlüssels ab. Je komplizierter dein Passwort ist, umso schwieriger wird es für den Angreiffer sein, dein Passwort herauszufinden. Moderne Computer können bereits sehr schnell viele mögliche Kombinationen durchprobieren, wodurch Brute-Force-Angriffe schneller und effektiver geworden sind.')
st.divider()
#Erklärung Schutzmassnahmen
st.header('Schutzmassnahmen')

st.write('Um Brute-Force-Angriffe zu erschweren, ist es empfehlenswert, komplexe Passwörter und lange Schlüssel zu verwenden. Zudem kann die Anzahl der zulässigen Fehlversuche beim Einloggen begrenzt werden, um automatisierte Angriffe zu verhindern. Durch diese Maßnahmen können die Erfolgsaussichten von Brute-Force-Angriffen deutlich reduziert werden. ')
st.subheader('_Verwendung starker Passwörter_')
st.write('Damit dein Account bestmöglich geschützt ist gegen solche Angriffe kannst du bestimmte Schutzmassnahmen einsetzten. Verwende ein starkes Passwort. "123ABC" wäre beispielsweise ein schwaches Passwort. Weiter unten erklären wir dir wie du ein starkes Passwort erstellen kannst.')
st.subheader('_Mehrstufige Authentifizierung_')
st.write('Wenn du dich einloggst, dann brauchst du dein Passwort und Nutzername. Damit nun nicht jeder der diese Daten hat sich auch in deinem Konto einloggen kann, aktiviere auf deinem Konto in den Einstellungen die Mehrstufige Authentifizierung. Das heisst, dass du per SMS oder E-Mail einen Code zugesendet bekommst den du beim einloggen eingeben musst. Jemand der keinen Zugriff auf deine Nachrichten oder Mails hat, kann diesen Code nicht kennen.')
st.subheader('_Verwendung von Captcha_')
st.write('Mit der Verwendung von Captchas beim einloggen, erhöhst du den Schutz. Captchas bedeutet "Completely Automated Public Turing Test" mit dem sich Computer von Menschen unterscheiden lassen. Häufig werden verzerrte Buchstaben und Zahlen gezeigt und der Benutzer muss diese erkennen und eingeben.')
st.subheader('_Verwendung von limitierten Anmeldeversuchen_')
st.write('Du kannst die Anzahl Anmeldeversuche ein einschränken. Gibt es also zu viele Fehlversuche beim Login, so wird dein Konto vorübergehend gesperrt, bis du es wieder aufhebst.')
st.divider()

#Aufklärung über gutes Passwort

st.header("Was ist ein gutes Passwort?")
st.write("Um ein gutes Passwort zu erstellen, solltest du folgende Punkte beachten:")
col1, col2 = st.columns(2)

with col1:
   st.subheader("Do")
   st.write("Dein Passwort sollte mindestens 12 Zeichen lang sein. Je länger dein Passwort ist, umso sicherer ist es.")
   st.write("Dein Passwort sollte sowohl Klein- als auch Grossbuchstaben beinhalten und du solltest Ziffern, Satz- und Sonderzeichen nutzen.")
   st.write("Du solltest dein Passwort regelmässig ändern.")
   st.write("Am besten verwendest du einen Password-Manager, der kann automatisch einzigartige Passwörter für jedes Konto generieren und speichern. ")

with col2:
   st.subheader("Don't")
   st.write("Passwörter sollten keinen persönlichen Bezug zu dir haben, also beispielsweise dein eigener Name oder Geburtsdatum.")
   st.write("Benutze keine Wörter aus Wörterbüchern.")
   st.write("Du solltest nicht überall das gleiche Passwort haben.")
   st.write("Du solltest deine Passwörter nie weitergeben, weder an Freunden noch Mitarbeitern.")

st.divider()


#Quiz
st.header ('Quiz')

choice = st.radio('Welche Schutzmassnahme ist die sicherste?', ['Starkes Passwort', 'Mehrstufige Authentifizierung', 'Alle sind gleich sicher', 'Limitierte Anmeldeversuche'])

if st.button('Überprüfe'):
    if choice == 'Mehrstufige Authentifizierung': # Zeige eine zufällige Zahl, wenn die Option 'Einfach so' ausgewählt wurde
        st.success('Richtig!')
    else: # Zeige die zufällige Zahl erst nach dem klicken eines Buttons, wenn die Option 'Über Umwege' ausgewählt wurde
        st.error('Leider falsch!')
else:
    st.write("Wähle eine Option")
st.divider()

#Passwort Tester
st.header ('Wie sicher ist mein Passwort?')
passwort = st.text_input("Passwort")

#Länge
i = 0  
if len(passwort) < 12 :
	i = i+1 
else:
    i = i

#Grossbuchstaben
GB = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
x = 0
y = 0
while x < len(passwort):
    if passwort[x] in GB:
        y = y + 1
    else:
        y = y
    x = x + 1
if y == 0:
    i = i + 1
else:
    i = i

#Zahlen
NB = ["0","1", "2", "3", "4", "5", "6", "7", "8", "9"]
q = 0
p = 0
while q < len(passwort):
    if passwort[q] in NB:
        p = p + 1
    else:
        p = p
    q = q + 1
if p == 0:
    i = i + 1
else:
    i = i

#Sonderzeichen
SZ = ["+","¦","@","*","#","°","%","§","%","&","¬","/","|","(","¢",")","?","=","^","!","]","[","{","}","$","£","-",".",",",";",":","_","<",">",]
f = 0
g = 0
while f < len(passwort):
    if passwort[f] in SZ:
        g = g + 1
    else:
        g = g
    f = f + 1
if g == 0:
    i = i + 1
else:
    i = i

if st.button("Passwort Check"):
    if i == 0:
        st.success('Dein Passwort ist sicher.')
        st.balloons()
    else:
        st.error('Dein Passwort ist nicht sicher.')
else:
    st.write("Teste dein Passwort")

