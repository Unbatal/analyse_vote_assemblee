# libraries
from ssl import ALERT_DESCRIPTION_UNEXPECTED_MESSAGE
from bs4 import BeautifulSoup
import urllib.request
import os
import sys
import pickle
import re
sys.path.append(os.getcwd())
from Class.ClassDepute import Depute
from Class.Scrutin import Scrutin

'''constitution de la liste des députés : "Prenom + Nom" : "prenom", "nom" , Groupe'''
deputes = {}
urlListe = 'https://www2.assemblee-nationale.fr/deputes/liste/groupe-politique'
#requete
page = urllib.request.urlopen(urlListe)
#coller dans BS
soup = BeautifulSoup(page, 'html.parser')
#découpage par groupe en retirant le premier artcle qui ne sert à rien
articles = soup.find_all('article')
articles.reverse()
articles.pop()
#pour chaque article, extrait le nom du groupe puis balaye les députés (en retirant le M. ou le Mme) pour renseigner le dictionnaire
for groupe in articles:
    donneGroupe =  groupe.find('a')
    nomGroupe = re.split(r'"', str(donneGroupe))
    deputesGroupe = groupe.find_all('li')
    for unDepute in deputesGroupe:
        unDepute = re.split(r"[<>]", str(unDepute))
        unDepute = re.split(r'(M\.\s|Mme\s)',unDepute[4])
        unDepute = unDepute[2].replace('\xa0', ' ')
        deputes[unDepute] = nomGroupe[3]
dictDeputes = {}
#ranger les deputes dans un dictionnaire
for clef in deputes:
    depute = Depute(clef)
    dictDeputes[clef] = depute
    dictDeputes[clef].groupe  = deputes[clef]

#enregistrement de tous les scrutins de la mandature
nbscrutin = 3316
listScrutin = []
for i in range(nbscrutin - 1):
    m_scrutin = (Scrutin(15, i + 1))
    listScrutin.append(m_scrutin)
# print(listScrutin[0].listeContre)
#ajout dans chaque objet deputé de ses votes Pour Contre et Abstention
for vote in listScrutin:
    listePour = vote.listePour
    listeContre = vote.listeContre
    listeAbstention = vote.listeAbstention
    for nom in listePour:
        try :
            dictDeputes[nom].votesPour.append((vote.legislature, vote.numero))
        except KeyError:
                pass
    for nom in listeContre:
        try:
            dictDeputes[nom].votesContre.append((vote.legislature, vote.numero))
        except KeyError:
                pass
    for nom in listeAbstention:
        try:
            dictDeputes[nom].abstentions.append((vote.legislature, vote.numero))
        except KeyError:
                pass   

with open('dictDeputes', 'wb') as fichierExport :
    m_pickler = pickle.Pickler(fichierExport)
    m_pickler.dump(dictDeputes)