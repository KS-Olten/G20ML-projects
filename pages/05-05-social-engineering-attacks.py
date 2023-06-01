# Dies ist die Streamlit App. Sie enthält nur Code, welcher für die Darstellung relevant ist

import streamlit as st # Lade streamlit Bibliothek


st.title("Social Engineering Attacken")
st.header("Was ist eine Social Engineering Attacke?")
st.markdown("Social Engineering Attacken sind zwischenmenschliche Beeinflussungen, um Menschen/Käufer zu manipulieren.")

st.markdown("Der Ablauf einer Social Engineering Attacke ist 1) Recherche: Das Sammeln von Informationen über das Opfer und die Planung für eine Angriffsmethode., 2) Ködern: Der Versand falscher Informationen, so geht das Opfer in die Falle. , 3) Kontrolle: Der Angriff und somit Diebstahl der gewünschten Daten. , 4) Flucht: Der unauffällige Rückzug nach erfolgtem Diebstahl.")
st.markdown("verschiedene Arten von Attacken:")
st.markdown("-> Dumpster Diving: Beispielsweise wühlen Hacker den Papierkorb durch und suchen nach Hinweisen über das Soziale Umfeld des Opfers. Durch einen darauffolgenden Anruf, kann das Vertrauen des Opfers und somit weitere Informationen über das Opfer gewonnen werden.")
st.markdown("-> USB-Drop: Hier erhalten Opfer, zum Beispiel Mitarbeiter einer Firma infizierte USB-Sticks, die ihren PC infizieren, womit Hacker Zugriff auf das interne Netzwerk der Firma erhalten.")
st.markdown("-> Phishing: Hier werden falsche E-Mails versendet, in welchen steht, dass ein bestimmter Dienst einen neuen URL hat und man sich neu einloggen muss. So gelangen die Angreifer in den Besitz von Loginname und Passwort. Um noch mehr über Phishing zu erfahren, drücken Sie auf den folgenden Knopf:")


if st.button("Phishing"):
    st.write("Das Hauptziel des Phishing besteht darin, den Benutzer dazu zu verleiten, vertrauliche Informationen preiszugeben, indem sich der Hacker als eine vertrauenswürdige Quelle ausgibt. Dazu nutzt man die Täuschende Kommunikation: Hier sendet der Angreifer eine gefälschte E-Mail an das potenzielle Opfer. Diese Nachricht wird so gestaltet, dass sie von einer vertrauenswürdigen Quelle, wie einer Bank, einem Sozialen Netzwerk oder einem Unternehmen stammen könnte. Ihre Nachricht wird graphisch so gestaltet, dass sie der echten Kommunikation der vertrauenswürdigen Quelle ähneln. Dies soll das Opfer dazu verleiten, die gefälschte Nachricht für legitim zu halten. Darin stehen manipulative Inhalte, gefälschte Links oder Anhänge wodurch das Opfer schlussendlich ihre persönlichen Daten preisgeben wird.")


st.subheader("Aufgabe zu Phishing")


checkbox_1 = st.checkbox("johnsmith@gmail.com.de")
if checkbox_1:
    st.write('Korrekt. Diese E-Mail-Adresse ist falsch, da sie eine ungewöhnliche Kombination von Buchstaben und Punkten enthält, die nicht der offiziellen Domain von Gmail entspricht.')

checkbox_2 = st.checkbox('christina.hof@kantiolten.ch')
if checkbox_2:
    st.write('Falsch.')

checkbox_3 = st.checkbox('support@amazon-security.com')
if checkbox_3:
    st.write('Korrekt. Diese E-Mail-Adresse ist falsch, da sie den Namen eines bekannten Unternehmens enthält, aber nicht die offizielle Domain von Amazon verwendet.')

checkbox_4 = st.checkbox('service@pay-pal.com')
if checkbox_4:
    st.write('Korrekt. Diese E-Mail-Adresse ist falsch, da sie den Namen eines bekannten Unternehmens enthält, aber nicht die offizielle Schreibweise von PayPal verwendet.')

checkbox_5 = st.checkbox('annabel.a@hotmail.ch')
if checkbox_5:
    st.write('Falsch.')

checkbox_6 = st.checkbox('mailservice@youcinema.ch')
if checkbox_6:
    st.write('Falsch.')

checkbox_7 = st.checkbox('bankofamerica@usa.com')
if checkbox_7:
    st.write('Korrekt. Diese E-Mail-Adresse ist falsch, da sie den Namen einer bekannten Bank enthält, aber nicht die offizielle Domain von Bank of America verwendet.')

checkbox_8 = st.checkbox('srf.info@kontakt.de')
if checkbox_8:
    st.write('Korrekt. Diese E-Mail-Adresse ist falsch, da SRF eine Schweizer Firma ist, .de aber ein deutscher Domain.')