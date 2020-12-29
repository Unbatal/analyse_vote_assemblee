# libraries
from bs4 import BeautifulSoup
import urllib.request
import csv
import re

def GetVote(urlpage, vote):
    '''renvoie la liste des députés ayant voté $vote
    
    Keyword arguments :
    urlpage : page de vote de l'AN type : https://www2.assemblee-nationale.fr/scrutins/detail/(legislature)/??/(num)/????
    vote : Pour / Contre / Abstention / Non-votant
    '''
    listeRetour = list()
    #requete site et retour html
    page = urllib.request.urlopen(urlpage)
    #coller avec BS et stockage dans var
    soup = BeautifulSoup(page, 'html.parser')
    #trouver les résultats
    table = soup.find_all('div', class_= "Pour clearfix")
    for groupes in table:
        groupe = groupes.find_all('li')
        for item in groupe:
            item = str(item)
            # item = item.replace('<li>','')
            # item = item.replace(' ', '')
            # item = item.replace('</li>', '')
            # item = item.replace('<b>', '')
            # item = item.replace('</b>', '')
            listeRetour.append(item)
