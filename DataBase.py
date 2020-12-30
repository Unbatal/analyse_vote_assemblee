# libraries
from bs4 import BeautifulSoup
import urllib.request
import csv
import re

'''constitution de la liste des députés : "Prenom + Nom" : "prenom", "nom" , Groupe'''
deputes = {}
urlListe = 'https://www2.assemblee-nationale.fr/deputes/liste/groupe-politique'
#requete
page = urllib.request.urlopen(urlListe)
#coller dans BS
soup = BeautifulSoup(page, 'html.parser')
#découpage par groupe
articles = soup.find_all('article')
articles.reverse()
articles.pop()
for groupe in articles:
    donneGroupe =  groupe.find('a')
    nomGroupe = re.split(r'"', str(donneGroupe))
    deputesGroupe = groupe.find_all('li')
    for unDepute in deputesGroupe:
        unDepute = re.split(r"[<>]", str(unDepute))
        unDepute = re.split(r'(M\.\s|Mme\s)',unDepute[4])
        #print(unDepute[2], nomGroupe[3])
        deputes[unDepute[2]]= nomGroupe[3]
    print(deputes)
    # for groupe in articles:
    #     nomGroupe = re.findall( , )