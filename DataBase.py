# libraries
from bs4 import BeautifulSoup
import urllib.request
import os
import pickle
import re

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
    #print(deputes)
with open('listeDeputes', 'wb') as fichierExport :
    m_pickler = pickle.Pickler(fichierExport)
    m_pickler.dump(deputes)