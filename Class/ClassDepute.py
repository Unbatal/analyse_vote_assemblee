# from Scrutin import Scrutin

class Depute:
    """Classe représentant un deputé :
    - Nom + Prenom
    - Groupe d'appartenance
    - liste des scrutins pour lesquels il a voté Pour
    - liste des scrutins pour lesquels il a voté Contre
    - liste des scrutins pour lesquels il s'est abstenu
    """

    def __init__(self, Nom):
        self.groupe = ""
        self.votesPour = []
        self.votesContre = []
        self.abstentions = []
    
    # def updateVote(self, unScrutin):
    #     if ((unScrutin.legislature, unScrutin.numero) in self.votesPour):
    #         pass
    #     elif ((unScrutin.legislature, unScrutin.numero) in self.votesContre):
    #         pass
    #     elif ((unScrutin.legislature, unScrutin.numero) in self.abstentions):
    #         pass
    #     else :
    #         if self.Nom in unScrutin.listePour:
    #             self.votesPour.append(unScrutin.legislature, unScrutin.numero)
    #         elif self.Nom in unScrutin.listeContre:
    #             self.votesContre.append(unScrutin.legislature, unScrutin.numero)
    #         elif self.Nom in unScrutin.listeAbstention:
    #             self.abstentions.append(unScrutin.legislature, unScrutin.numero)
    #         else:
    #             pass