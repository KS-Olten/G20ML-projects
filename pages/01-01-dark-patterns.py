import streamlit as st #Lade Streamlit Bibliothek



st.title('Dark Patterns')

st.image('oma.jpg') #Zeige ein Bild, welches die Person beeinflussen soll, die Cookies zu Akzeptieren.

st.header('Möchtest du die Cookies akzeptieren?')

st.caption('Wir verwenden Cookies, um dir die best möglichen, personalisierten Anzeigen anbieten zu können. Nur wenn du die Cookies akzeptierst, kannst du den ganzen Inhalt der Webseite sehen.')

if st.button('AKZEPTIEREN'): #Wenn die Person die Cookies akzeptiert, zeige Erklärtext 
    st.write('Dark Patterns, auf Deutsch "Dunkle Muster" ist ein Design, welches in Webseiten und Apps oft genutzt wird, um die NutzerInnen zu einer Handlung zu verlocken. Dies kann beispielsweise sein, dass die NutzerInnen, die die Cookies nicht akzeptieren wollen, sich lange durch die Einstellungen kämpfen müssen, um die Webseite trotzdem zu besuchen oder den NutzerInnen wird angezeigt, dass es von einem bestimmten Produkt nur noch eine kleine Anzahl zur Verfügung hätte, damit sich die KundInnen unter Druck gesetzt fühlen und das Produkt sofort kaufen, ohne darüber nachzudenken.')
    
    st.write('Häufig werden zusätzlichen Kosten erst im letzten Schritt der Bestellung angezeigt und werden als :blue["Hidden Costs"] bezeichnet. Zu den Hidden Costs gehören unter anderem auch Lieferkosten und Steuern wie zum Beispiel Mehrwertsteuern, die am Anfang noch nicht ersichtlich waren.')

    st.write('Unter :blue["Cookie Consent Tricking"] wird verstanden, dass bei der Frage, ob die UserInnen die Cookies akzeptieren wollen, der Knopf zum Akzeptieren gross und mit einer Farbe hervorgehoben erscheint und der Knopf zum Ablehnen klein und leicht übersehbar ist.')
    
    st.write('Dazu kommt :blue["Visuelle Manipulation"], die dazu dient, die Cookies durch Bilder zu verharmlosen. Süsse oder lustige Bilder von Cookie-fressenden Monstern werden gezeigt, die die Tracking-Cookies verharmlosen oder ein Bild eines Cookies (Gebäck) erscheint neben der Frage, um den BesucherInnen ein positives Bild von den Cookies zu vermitteln. Rabatt verleitet potenzielle KundInnen dazu, etwas zu kaufen.')
    st.write(':violet[-> In dieser Webseite erscheint ein Bild von einer Oma mit frischgebackenen Cookies, welches das Ablehnen der Tracking-Cookies für BesucherInnen emotional erschweren soll.]')
    st.write(':violet[-> Ausserdem erscheint ein Bild, welches eine Werbung nachstellen sollte. Dieses Bild ist eigenständig kreiert, es zeigt auf, wie manipulativ die Sprache der Werbung ist.]')

    st.write('Wird ein kostenloses Probeabonnement abgeschlossen, bei welchem man jedoch im Voraus die Kreditkartendaten hinterlegen muss, besteht die Gefahr von :blue["Forced Continuity"]. Dabei wird den KundInnen  keine Erinnerung zugestellt, wenn die kostenlose Probeabo-Zeit abläuft und ihm automatisch Geld abzieht, solange das Abonnement nicht durch mühsame Kündigung beendet wird. Die Kündigung wird den UserInnen dabei extra erschwert.')

    st.write('Unter :blue["Road Block"] wird verstanden, dass den NutzerInnen das Verlassen einer Webseite erschwert wird. Dieser Vorgang wird beispielsweise durch ein Pop-Up-Fenster verursacht, welches BesucherInnen einen Rabatt verspricht. Dies aber nur, wenn der Kauf jetzt gerade getätigt wird. Oder beim Verlassen der Seite erscheint ein Pop-Up-Fenster, welches die BesucherInnen bestätigen lässt, dass sie die Seite wirklich verlassen wollen.') 
    st.write(':violet[-> In dieser Webseite steht am Ende der Webseite "Willst du die Seite wirklich schon verlassen?"]')

    st.write('Die :blue["Misdirection"] sorgt dafür, dass die Aufmerksamkeit der UserInnen von einem Inhalt auf einen anderen Inhalt gelenkt wird.')
    
    st.write('Dark Patterns manipulieren UserInnen um durch Cookies an persönliche Daten heranzukommen oder um ihnen Geld aus der Tasche zu ziehen. Einerseits bekommen alle NutzerInnen durch die Dark Patterns benutzerspezifische Anzeigen, andererseits wird so in die Privatsphäre eingegriffen, der Datenschutz missachtet und die manipulierten Webseitenbesucher geben mehr Geld aus, als von diesen beabsichtigt wurde.')
    st.image('Darkpattern_FINAL-.jpg') #Zeige selbstgemachtes Bild als Beispiel für manipulierende Werbung.


if st.button('ablehnen'): #Wenn auf Ablehnen gedrückt wird, frage nach, ob die Cookies nicht doch akzeptiert werden wollen.
    ablehnen=st.radio(
        ':red[Willst du die Cookies nicht doch akzeptieren?]', #Zeige Text in roter Farbe 
        ('AKZEPTIEREN', 'ablehnen'))

    if ablehnen!='ablehnen': #Zeige Erklärtext
        st.write('Dark Patterns, auf Deutsch "Dunkle Muster" ist ein Design, welches in Webseiten und Apps oft genutzt wird, um die NutzerInnen zu einer Handlung zu verlocken. Dies kann beispielsweise sein, dass die NutzerInnen, die die Cookies nicht akzeptieren wollen, sich lange durch die Einstellungen kämpfen müssen, um die Webseite trotzdem zu besuchen oder den NutzerInnen wird angezeigt, dass es von einem bestimmten Produkt nur noch eine kleine Anzahl zur Verfügung hätte, damit sich die KundInnen unter Druck gesetzt fühlen und das Produkt sofort kaufen, ohne darüber nachzudenken.')
    
    st.write('Häufig werden zusätzlichen Kosten erst im letzten Schritt der Bestellung angezeigt und werden als :blue["Hidden Costs"] bezeichnet. Zu den Hidden Costs gehören unter anderem auch Lieferkosten und Steuern wie zum Beispiel Mehrwertsteuern, die am Anfang noch nicht ersichtlich waren.')

    st.write('Unter :blue["Cookie Consent Tricking"] wird verstanden, dass bei der Frage, ob die UserInnen die Cookies akzeptieren wollen, der Knopf zum Akzeptieren gross und mit einer Farbe hervorgehoben erscheint und der Knopf zum Ablehnen klein und leicht übersehbar ist.')
    
    st.write('Dazu kommt :blue["Visuelle Manipulation"], die dazu dient, die Cookies durch Bilder zu verharmlosen. Süsse oder lustige Bilder von Cookie-fressenden Monstern werden gezeigt, die die Tracking-Cookies verharmlosen oder ein Bild eines Cookies (Gebäck) erscheint neben der Frage, um den BesucherInnen ein positives Bild von den Cookies zu vermitteln. Rabatt verleitet potenzielle KundInnen dazu, etwas zu kaufen.')
    st.write(':violet[-> In dieser Webseite erscheint ein Bild von einer Oma mit frischgebackenen Cookies, welches das Ablehnen der Tracking-Cookies für BesucherInnen emotional erschweren soll.]')
    st.write(':violet[-> Ausserdem erscheint ein Bild, welches eine Werbung nachstellen sollte. Dieses Bild ist eigenständig kreiert, es zeigt auf, wie manipulativ die Sprache der Werbung ist.]')

    st.write('Wird ein kostenloses Probeabonnement abgeschlossen, bei welchem man jedoch im Voraus die Kreditkartendaten hinterlegen muss, besteht die Gefahr von :blue["Forced Continuity"]. Dabei wird den KundInnen  keine Erinnerung zugestellt, wenn die kostenlose Probeabo-Zeit abläuft und ihm automatisch Geld abzieht, solange das Abonnement nicht durch mühsame Kündigung beendet wird. Die Kündigung wird den UserInnen dabei extra erschwert.')

    st.write('Unter :blue["Road Block"] wird verstanden, dass den NutzerInnen das Verlassen einer Webseite erschwert wird. Dieser Vorgang wird beispielsweise durch ein Pop-Up-Fenster verursacht, welches BesucherInnen einen Rabatt verspricht. Dies aber nur, wenn der Kauf jetzt gerade getätigt wird. Oder beim Verlassen der Seite erscheint ein Pop-Up-Fenster, welches die BesucherInnen bestätigen lässt, dass sie die Seite wirklich verlassen wollen.') 
    st.write(':violet[-> In dieser Webseite steht am Ende der Webseite "Willst du die Seite wirklich schon verlassen?"]')

    st.write('Die :blue["Misdirection"] sorgt dafür, dass die Aufmerksamkeit der UserInnen von einem Inhalt auf einen anderen Inhalt gelenkt wird.')
    
    st.write('Dark Patterns manipulieren UserInnen um durch Cookies an persönliche Daten heranzukommen oder um ihnen Geld aus der Tasche zu ziehen. Einerseits bekommen alle NutzerInnen durch die Dark Patterns benutzerspezifische Anzeigen, andererseits wird so in die Privatsphäre eingegriffen, der Datenschutz missachtet und die manipulierten Webseitenbesucher geben mehr Geld aus, als von diesen beabsichtigt wurde.')
    st.image('Darkpattern_FINAL-.jpg') #Zeige selbstgemachtes Bild als Beispiel für manipulierende Werbung.

   

st.subheader('Wenn du alles verstanden hast, beantworte die folgenden Fragen:')

#Stelle Fragen zum testen, ob das Thema Dark Patterns verstanden wurde
st.write("Dark Patterns werden verwendet, ...")
if st.button("... damit Daten von NutzerInnen gesammelt werden können."):
    st.write("Falsch!")
if st.button("... um die NutzerInnen zu einer bestimmten Handlung zu verlocken."):
    st.write("Richtig!")
if st.button("... um Webseiten schöner gestalten zu können."):
    st.write("Falsch!")

st.write("Zu welcher Kategorie gehören Werbeaussagen wie 'Nur noch 3 Stücke vorhanden'?")
if st.button("Misdirection"):
    st.write("Falsch!")
if st.button("Forced Continuity"):
    st.write("Falsch!")
if st.button("Visuelle Manipulation"):
    st.write("Richtig!")
        
st.write("Warum ist der Knopf, um die Cookies zu akzeptieren, durch Grösse und Farbe hervorgehoben und der Knopf zum Ablehnen leicht zu übersehen?")
if st.button("Damit NutzerInnen gezwungen sind, die Cookies zu akzeptieren."):
    st.write("Falsch!")
if st.button("Dadurch ist die Wahrscheinlichkeit grösser, dass die Cookies von NutzerInnen akzeptiert werden."):
    st.write("Richtig!")    
if st.button("Damit man als NutzerIn die Cookies bewusst akzeptiert oder ablehnt."):
    st.write("Falsch!")

st.write("Was versteht man unter 'Forced Continuity'?")
if st.button("NutzerInnen wird durch die Cookies personalisiert Werbung angezeigt. Dies führt dazu, dass das Interesse der NutzerInnen hoch bleibt und sie mehr Zeit online verbringen und Geld ausgeben."):
    st.write("Falsch!")
if st.button("Ein gratis Probeabonnement wird ohne das Wissen der KundInnen kostenpflichtig verlängert"):
    st.write("Richtig!")
if st.button("NutzerInnen bekommen Rabatte, damit sie sofort Einkäufe tätigen und Artikel nicht im Warenkorb oder auf der Wunschliste lassen."):
    st.write("Falsch!")

st.write("Durch Visuelle Manipulation werden UserInnen dazu verleitet, ...")
if st.button("... kostenpflichtige Abos abzuschliessen."):
    st.write("Falsch!")
if st.button("... alle Cookies zu akzeptieren und mehr Geld auszugeben als sie geplant hatten."):
    st.write("Richtig!")
if st.button("... auf einer Webseite zu bleiben."):
    st.write("Falsch!")



#Ende der Webseite
if st.button("Seite verlassen"): #Wenn man auf 'Seite verlassen' drückt, zeige ein Bild und frage nach, ob die Person die Seite wirklich verlassen will.
    st.image('36807-4-sad-emoji-clipart.png')

    bye=st.radio(
        "Bist du dir sicher, dass du die Seite schon verlassen willst?",
        ('ja', 'nein')) #Wenn Nein gedrückt wird, zeige die Frage nicht mehr an.
    
    if bye=='ja': #Wenn Ja gedrückt wird, verabschiede die Person.
        st.write ('Auf Wiedersehen!')
   







