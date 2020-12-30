import os
import pickle
import csv
import pandas as pd
import networkx as nx

matrice = list()
with open('matricePour', 'rb') as fichierExport :
    m_depickler = pickle.Unpickler(fichierExport)
    matrice = m_depickler.load()

with open('listeDeputes', 'rb') as fichierExport :
    m_depickler = pickle.Unpickler(fichierExport)
    deputes = m_depickler.load()

listeDeputes = list()

for depute in deputes:
    listeDeputes.append(depute)

df = pd.DataFrame(matrice, index = listeDeputes, columns = listeDeputes)
#print(df)
G = nx.from_pandas_adjacency(df)
nx.draw_networkx(G)