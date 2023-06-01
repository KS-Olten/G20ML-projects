import streamlit as st
import pandas as pd
import numpy as np
from helper_rekursion import e_funktion
from helper_rekursion import factorial

#Text zur allgemeinen Information und Formeln

st.title("Rekursion")
st.subheader("Info_Projekt 2023 Luca")
st.text_area(
    "Rekursion ist eine mathematische Methode die vor allem in der Analytik verwendet wird. "
    "Wegweisend ist dabei das 'sich auf etwas vor oder nachher zu beziehen' . Also wird eine Operation oder eine Codezeile "
    "So oft ausgeführt, bis man an den Ausgangspunkt, den Startwert zurückgelangt. So spart man sich Codezeilen, da man in "
    "nur kurzen Befehlen den Computer zu 100en Berechnungen verleiten kann. Dies findet allerdings in der heutigen Informatik "
    "weniger Verwendung, da man versucht die Rechnungskapazität eines Computers zu schonen und durch Codeoptimierung erzielt, "
    "dass ein Programm schneller und weniger belastend ist. "
    "Anhand der Mathematik erkennt man auch, dass für viele rekursive Berechnungen auch explizite Formeln exitieren, welche "
    "mit einer einzigen Berechnung einen Grenzwert berechnen können, was natürlich die eleganteste Lösung ist, wenn man ein mathematisches "
    "Problem lösen muss. "
)
  
st.write("die Formeln um die eulersche Zahl 'e' zu berechnen: ")
st.latex(r'''
    e = 1 + \frac{1}{1} + \frac{1}{1 * 2} + \frac{1}{1 * 2 * 3} + (...) = \sum_{n=1}^{\infty} \frac{1}{n!} = 2.71828
    ''')

st.write("Wir versuchen eine Näherung: Je höher die Anzahl Rekursionen, desto genauer wird unsere Rechung der eulerschen Zahl")

#Userinteraction durch Slider um mit der Näherung an e zu experimentieren

Näherung = st.slider('schiebe den Regler zwischen 1 und 20 hin und her!', 1, 20, 7)

#Berechnung:

st.write("e =", e_funktion(Näherung))