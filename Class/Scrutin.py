from bs4 import BeautifulSoup
import urllib.request
import csv
import re

class Scrutin:
    """Classe représentant un scrutin :
    - legislature
    - numero
    - intitulé
    - liste des députés ayant voté pour
    - liste des députés ayant voté contre
    - liste des abstentions
    - liste des non votants
    - Parti du vote
    """

    def __init__(self, legislature, numero):
        """Constructeur
        Args:
            legislature (int): numéro de législature
            numero (int): numéro du scrutin dans la législature
        """

        self.intitule = ""
        urlpage = str('https://www2.assemblee-nationale.fr/scrutins/detail/(legislature)/'+str(legislature)+'/(num)/' + str(numero))
        self.listePour = GetVote(urlpage, 'Pour')
        self.listeContre = GetVote(urlpage, 'Contre')
        self.listeAbstention = GetVote(urlpage, 'Abstention')
        self.listeNonvotant = GetVote(urlpage, 'Non-votant')
        self.parti = ""

def GetVote(urlpage, vote):
    '''renvoie la liste des députés ayant voté $vote
    
    Keyword arguments :
    urlpage : page de vote de l'AN type : https://www2.assemblee-nationale.fr/scrutins/detail/(legislature)/??/(num)/????
    vote : Pour / Contre / Abstention / Non-votant
    '''
    listeRetour = list()
    typeVote = vote + " clearfix"
    #requete site et retour html
    page = urllib.request.urlopen(urlpage)
    #coller avec BS et stockage dans var
    soup = BeautifulSoup(page, 'html.parser')
    #trouver les résultats
    table = soup.find_all('div', class_= typeVote)
    for groupes in table:
        groupe = groupes.find_all('li')
        for item in groupe:
            item = str(item)
            item = item.replace('<li>','')
            item = item.replace(' ', '')
            item = item.replace('</li>', '')
            item = item.replace('<b>', '')
            item = item.replace('</b>', '')
            item = item.replace('''\xa0''', ' ')
            listeRetour.append(item)
    return listeRetour 