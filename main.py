import os
import pickle
#import pandas as import pd
import numpy as np
import networkx as nx
from GetVote import *

#import du dictionnaire liste des deputes
with open('listeDeputes', 'rb') as fichierExport :
    m_depickler = pickle.Unpickler(fichierExport)
    DictDeputes = m_depickler.load()
#creation d'une liste contenant les députés
listDeputes = list()
matricePour = list()
for depute in DictDeputes:
    listDeputes.append(depute)
#import de la matrice adjacente
with open('matricePour', 'rb') as fichierExport :
    m_depickle = pickle.Unpickler(fichierExport)
    matricePour = m_depickle.load(matricePour)

