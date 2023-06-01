# Dies ist die Streamlit App. Sie enthält nur Code, welcher für die Darstellung relevant ist

import streamlit as st # Lade streamlit Bibliothek
from helper_pw import Helper # Lade Helfer-Klasse aus helper.py

#Hier wird die Variable h für "Helper" definiert.
h=Helper()
# Hier steht der Titel und einen Text mit Anweisungen.
st.title("Ihr eigenes Passwort")
st.text("Geben sie ein Satz ein mit genau 7 Wörtern")
passphrase = st.text_input("Geben sie ihr Satz ein")

#Hier wird getestet, ob der Satz die richtige länge hat. Damit meinen wir die richtige Anzahl Worte in einem Satz.
length_check = h.has_correct_lenth(passphrase)

#Hier steht, wenn die länge in Ordnung ist wird ("korrekte Länge, machen wir weiter ausgegeben"), wenn nicht dann wird ("Änder die Länge") ausgegeben.
#Dann wird jeweils der erste Buchstabe des Wortes ausgegeben.
#Daraufhin wird die Anazahl der Buchstaben, der jeweiligen Wörter ausgegegben. 
#Am Ende hat man dann sein eigenes, erstelltes Passwort. 
if length_check:
    st.write('Korrekte Länge, machen wir weiter')
    first_letters = h.the_first_letter(passphrase)
    st.write(first_letters)
    amount_letter = h.the_amount_letters(passphrase)
    st.write(amount_letter)
    initials_len = h.the_initials_len(passphrase)
    st.write(initials_len)
else:
    st.write('Ändere die Länge')

# Beispielaufruf:
def create_link(link_text, url):
        return f'<a href="{url}">{link_text}</a>'
link = create_link("Besuchen Sie diese Website,um die stärke ihres Passworts zu testen","<https://bitwarden.com/de-DE/password-strength/>")
st.markdown(link, unsafe_allow_html=True)
