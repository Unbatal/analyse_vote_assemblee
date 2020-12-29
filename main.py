from GetVote import *

#url
urlpage = 'https://www2.assemblee-nationale.fr/scrutins/detail/(legislature)/15/(num)/3313'

#récupère la liste des députés ayant voté pour
print(GetVote(urlpage, 'Pour'))