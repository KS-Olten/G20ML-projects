import streamlit as st  #importiere streamlit funktionalitäten

st.title('Sicherheit und Kryptografie') # füge Titel hinzu
st.divider() #fügt eine Linie hinzu
st.header('Denial of service attack') # fügt den Titel hinzu
# fügt den Untertitel hinzu
st.caption('Im folgenden Text wird das Konzept von Denial of service attack erklärt.Im Eingabefeld unterhalb des Textes können die grün markierten wörter und Begriffe bei Verständnisproblemen eingetippt werden. Daraufhin erscheint ein Erklärtext dazu.')

# fügt einen Text hinzu
st.write('Denial of Service Attack ist die Nichtverfügbarkeit eines :green[Internetdienstes] das eigentlich im normalen Zustand vorhanden sein sollte. Es basiert auf der Grundlage von einer Vielzahl von verschiedenen Anfragen. So geschieht eine Überlastung des :green[Datennetzes].Es kann auf verschiedene Arten verursacht werden: Unbeabsichtigt, durch einen konzentrierten Angriff oder durch einen anderen :green[Komponenten] des Datennetzes. Ausserdem kann auch eine Vielzahl von verschiedenen Anfragen von einer grossen Anzahl verschiedener Rechner ausgehen, was in den Bereich von Distributed Denial of Service Attack fällt.Denial of Service Attacks die bewusst verübt werden, sind :green[Cyberverbrechen]. Die Täter sind oft Cyber- Kriminelle die ihre Dienste gegen Bezahlung anbieten um gezielt der Konkurrenz des Auftraggebers zu schaden. Andere Angriffe werden von unzufriedenen Nutzer eine Internetdienstes verübt. In einigen Fällen ist das Motiv :green[Spionage], Protest oder :green[Vandalismus] aus politischer Motivation.')
st.write('Eine der ersten größeren :green[DDoS]-Attacken hatte große US-amerikanische Banken zum Ziel. Dabei griffen Unbekannte unter anderem die Bank of America, JP Morgan Chase, U.S. Bancorp, Citigroup und die PNC Bank an. Die Angreifer gingen dabei ziemlich phantasievoll und ausgeklügelt vor. Statt nur einen Typ von DDoS-Attacke zu nutzen, verfolgten sie mehrere unterschiedliche Strategien, um möglichst viel Schaden zu verursachen. Der Angriff erfolgte im Jahr 2012, Abwehrtechniken gegen die Angriffe waren in vielen Unternehmen bereits implementiert, allerdings meist nur gegen einen einzigen Angriffstyp. Dadurch und aufgrund des damals hohen Datenverkehrs von bis zu 60 GB pro Sekunde, der durch hunderte gekaperte Server ausgelöst wurde, war die Attacke gravierender als viele der zuvor durchgeführten DDoS-Angriffe.')
st.write('weitere Beispiele für bekannte DDoS Attacken sind :green[GitHub 2018], :green[GitHub 2015], :green[Mafiaboy 2000] oder :green[Estland 2007]. ')

st.divider()# fügt eine Linie hinzu
eingabe = st.text_input('Texteingabe') #fügt ein Eingabefeld hinzu
st.write('Du hast '+ eingabe + ' eingetippt')

#lässt den Erklärtext zum eingegebenen Wort im Eingabefeld erscheinen.
if eingabe == 'Internetdienst':
      st.write('Ein Internetdienst ist eine Anwendung des Internets im technischen Sinne. Das Internet selbst stellt lediglich die Infrastruktur zur Übertragung der Daten zur Verfügung.')
if eingabe == 'Datennetz':
      st.write('Ein Datennetz ist eine Infrastruktur die die Übertragung von von Daten zwischen Rechner und mobilen Endgeräten dient.')
if eingabe == 'Komponenten':
      st.write('Eine Komponente ist ein Teil einer Software, die mit anderen Softwareteilen zusammenwirken. Es ist ein kleiner Teil eines Systems. ')
if eingabe == 'Cyberverbrechen':
      st.write('Cyberverbrechen sind Straftaten die im Internet oder mit speziellen Mitteln des Internets durchgeführt werden. Dabei muss aber nicht primär der Computer benutzt werden. ')
if eingabe == 'Spionage':
      st.write('Eine Spionage ist eine verdeckte, geheime Ermittlung oder Beschaffung. Meistens werden dabei Informationen für jemanden besorgt, die einen Auftrag stellten. ')
if eingabe == 'Vandalismus':
      st.write('Vandalismus ist die Beschädigung von einer Sache, privat oder öffentlich. Es kann soweit zur Folge haben dass Körperverletzung oder Tierquälerei entsteht. ')
if eingabe == 'GitHub 2018':
      st.write('Einer der größten jemals verzeichneten und überprüfbaren DDoS-Angriffe richtete sich gegen GitHub, einen beliebten Onlinecode-Management-Dienst, der von Millionen von Entwicklern genutzt wird. Der Angriff erreichte 1,3 Tbit/s, wobei 126,9 Millionen Pakete pro Sekunde versandt wurden.Die Attacke auf GitHub erfolgte in Form eines Memcached-DDoS-Angriffs, weshalb keine Botnetze beteiligt waren. Stattdessen nutzten die Angreifer den Verstärkungseffekt eines beliebten Datenbank-Cache-Systems namens Memcached. Durch die Überflutung von Memcached-Servern mit Spoofing-Anfragen konnte der Angriff etwa um das 50.000-Fache verstärkt werden.Glücklicherweise benutzte GitHub einen DDoS-Schutzdienst, der innerhalb von zehn Minuten nach Beginn des Angriffs automatisch benachrichtigt wurde. Diese Warnung löste einen Abwehrprozess aus, sodass GitHub den Angriff schnell stoppen konnte. Letztlich dauerte die großangelegte Attacke deshalb nur rund 20 Minuten.')
if eingabe == 'GitHub 2015':
      st.write('Dieser DDoS-Angriff, damals der bedeutendste aller Zeiten, richtete sich ebenfalls gegen GitHub und war politisch motiviert. Er dauerte mehrere Tage und passte sich an die eingesetzten DDoS-Abwehrstrategien an. Der DDoS-Traffic kam aus China und nahm gezielt die URLs von zwei GitHub-Projekten ins Visier, die sich mit Möglichkeiten zur Umgehung der chinesischen Staatszensur befassten. Es wird spekuliert, dass GitHub durch den Angriff dazu gebracht werden sollte, diese Vorhaben einzustellen.')
if eingabe == 'Mafiaboy 2000':
      st.write('Im Jahr 2000 legte ein 15-jähriger Hacker mit dem Pseudonym „Mafiaboy“ mehrere große Websites lahm, darunter CNN, Dell, E-Trade, eBay sowie Yahoo, die damals beliebteste Suchmaschine der Welt. Dieser Angriff hatte verheerende Folgen und führte unter anderem zu Chaos an der Börse.Mafiaboy, der sich später als der Highschool-Schüler Michael Calce herausstellte, koordinierte den Angriff, indem er sich in die Netzwerke mehrerer Universitäten hackte und ihre Server nutzte, um den DDoS-Angriff auszuführen. Im Anschluss an diesen Vorfall wurden viele der heutigen Gesetze gegen Cyberkriminalität geschaffen.')
if eingabe == 'Estland 2007':
      st.write('Im April 2007 war Estland mit einem massiven DDoS-Angriff auf Regierungsdienste, Finanzinstitute und Medien konfrontiert. Die Auswirkungen waren fatal, da die estnische Regierung früh begonnen hatte, Online-Dienste anzubieten und zu diesem Zeitpunkt praktisch papierlos funktionierte; selbst Wahlen wurden in dem baltischen Staat online durchgeführt.Der Angriff, der von vielen als erster Akt der Cyber-Kriegsführung angesehen wird, war die Reaktion auf einen politischen Konflikt mit Russland bezüglich der Umsiedlung des „Bronzesoldaten von Tallinn“, einem Denkmal des Zweiten Weltkriegs. Die russische Regierung steht im Verdacht, daran beteiligt gewesen zu sein, und ein estnischer Staatsangehöriger aus Russland wurde daraufhin verhaftet. Moskau erlaubte es den estnischen Strafverfolgungsbehörden jedoch nicht, weitere Ermittlungen in Russland durchzuführen. Diese Affäre hatte zur Folge, dass internationale Gesetze gegen Cyberkriminalität geschaffen wurden.')
if eingabe == 'DDoS':
      st.write('Bei einer DDoS-Attacke ist der Server im Gegendast zu Dos-attacke Ziel von mehreren Angreifern. Dabei übernimmt ein Computer normalerweise die Führung und koordiniert die anderen Computer, welche weltweit verteilt sind. Das führt zu großen Problemen, da Ihr Server aufgrund der Attacke aus mehreren Richtungen die Verbindung nicht so leicht identifizieren und schließen kann.Der Server wird sich dann darauf konzentrieren, die Vielzahl an Verbindungen zu schließen und dafür seine ganze Rechenkraft verwenden. Dadurch bleiben jedoch keine Ressourcen für die eigentliche Website übrig.Vor allem wird der Server an Bandbreite verlieren, wovon auch die „guten“ Computer betroffen sind, die ganz normal Ihre Website besuchen möchten. Der Server kann die Anfragen dieser Personen nicht bedienen, da er mit den Angreifern beschäftigt ist. Als Ergebnis können diese Personen Ihre Website entweder gar nicht aufrufen oder nur mit sehr langen Ladezeiten.')
      
st.divider() #fügt eine Linie hinzu

genre = st.radio(   # fügt Radio Button hinzu
    "Hast du das Thema verstanden?",
    ('Ja', 'Nein'))

if genre == 'Nein':
    st.write('Das untenstehende Video erklärt dir nochmals was Denial of service attacks sind.')
    st.video('https://www.youtube.com/watch?v=GVEUtdmtYhs')
else:
    st.write("Super. Als Belohnung ein Witz:")
    st.write('Was ist der Unterschied zwischen einem Informatiker und einem Physiker?')
    st.write('Der Physiker glaubt, ein Kilobyte sind 1000 Byte.')
    st.write('Der Informatiker glaubt, ein Kilometer sind 1024 Meter.')


