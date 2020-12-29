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
nomGroupe =  articles[6].find('a')
nomGroupe = re.split(r'"', str(nomGroupe))
print(nomGroupe[3])
# for groupe in articles:
#     nomGroupe = re.findall( , )