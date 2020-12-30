import os
import pickle
from GetVote import *

#import du dictionnaire liste des deputes
with open('listeDeputes', 'rb') as fichierExport :
    m_depickler = pickle.Unpickler(fichierExport)
    DictDeputes = m_depickler.load()
#creation d'une liste contenant les députés
listDeputes = list()
matricePour= list()
for depute in DictDeputes:
    listDeputes.append(depute)
    matricePour.append([0]* len(DictDeputes))

for numvote in range(3315):
    #url
    scrutin = numvote + 1
    urlpage = str('https://www2.assemblee-nationale.fr/scrutins/detail/(legislature)/15/(num)/' + str(scrutin))

    #récupère la liste des députés ayant voté pour
    votePour = GetVote(urlpage, 'Pour')
    for item in votePour:
        try:
            index = listDeputes.index(item)
        except ValueError:
            pass
        for jtem in votePour:
            try :
                jndex = (listDeputes.index(jtem))
                matricePour[index][jndex] += 1
            except ValueError:
                pass
#Enregistrement de la matrice dans un fichier
with open('matricePour', 'wb') as fichierExport :
    m_pickler = pickle.Pickler(fichierExport)
    m_pickler.dump(matricePour)
