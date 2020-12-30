import os
import pickle
from GetVote import *

#import du dictionnaire liste des deputes
with open('listeDeputes', 'rb') as fichierExport :
    m_depickler = pickle.Unpickler(fichierExport)
    DictDeputes = m_depickler.load()
print(DictDeputes)
#url
urlpage = 'https://www2.assemblee-nationale.fr/scrutins/detail/(legislature)/15/(num)/3313'

#récupère la liste des députés ayant voté pour
#print(GetVote(urlpage, 'Pour'))