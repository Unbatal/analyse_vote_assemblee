import os
import pickle
import csv
import pandas as pd

matrice = list()
with open('matricePour', 'rb') as fichierExport :
    m_depickler = pickle.Unpickler(fichierExport)
    matrice = m_depickler.load()

with open('listeDeputes', 'rb') as fichierExport :
    m_depickler = pickle.Unpickler(fichierExport)
    deputes = m_depickler.load()

listeDeputes = list()

for depute in deputes:
    listeDeputes.append(deputes)

df = pd.DataFrame(matrice, columns = listeDeputes)
print(df)