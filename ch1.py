# libraries
from bs4 import BeautifulSoup
import urllib.request
import csv
import re

#url
urlpage = 'https://www2.assemblee-nationale.fr/scrutins/detail/(legislature)/15/(num)/3313'

#requete site et retour html
page = urllib.request.urlopen(urlpage)
#coller avec BS et stockage dans var
soup = BeautifulSoup(page, 'html.parser')

# print(soup)

#trouver les résultats
table = soup.find_all('div', class_= "Pour clearfix")
#print(table)
#pours = table[2].find_all('li')
#print(pours)
for groupes in table:
    groupe = groupes.find_all('li')
    for item in groupe:
        item = str(item)
        item = item.replace('<li>','')
        item = item.replace(' ', '')
        item = item.replace('</li>', '')
        item = item.replace('<b>', '')
        item = item.replace('</b>', '')
        print(item)