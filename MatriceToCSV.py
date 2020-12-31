import os
import pickle
import csv
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import igraph

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
A = df.to_numpy()
# G = nx.from_pandas_adjacency(df)
# nx.draw(G, with_labels=True)
# layout = nx.circular_layout(G)
# #nx.draw_networkx_edge_labels(G, pos=layout)
# plt.show()
# G = igraph.Graph.Adjacency(matrice)
# G.vs['label'] = listeDeputes
# layout = G.layout_drl()
# igraph.plot(G, layout = layout).show()

exportCSV = df.to_csv('exportCSV.csv', index=True)
print('\nCSV String:\n', exportCSV)