# import libraries
from bs4 import BeautifulSoup
import urllib.request
import csv

#open file
fichier = open("Bas-Rhin.csv","a")
fichier.write('Nom Prenom;Adresse;Code postale Ville;\n')


for i in range(7574):
    if(i%100 == 0):
        print(str(i) + ' done')
    # specify the url
    urlpage = 'https://www.bas-rhin.fr/carte-assistants-maternels-bas-rhin/?start='+str((i))+'&rows=1&pt=48.57,7.73'

    # query the website and return the html to the variable 'page'
    page = urllib.request.urlopen(urlpage)
    # parse the html using beautiful soup and store in variable 'soup'
    soup = BeautifulSoup(page, 'html.parser')

    strsoup = str(soup)
    
    #if i == 70:
     #   rangee = 14
    #else:
     #   rangee = 108
            
    #for y in range(rangee):
    index = strsoup.find('search-results__entry-title')+28
    strsoup = strsoup[index:]
    index = strsoup.find('</h3>')
    nom_prenom = (strsoup[1:index]).replace('\t','')
    strsoup = strsoup[index:]
    index = strsoup.find('search-results__entry-address">')+31
    strsoup = strsoup[index:]
    index = strsoup.find('<br/>')
    adresse = (strsoup[1:index]).replace('\t','')
    strsoup = strsoup[index+5:]
    index = strsoup.find('<br/>')
    cp_ville = (strsoup[1:index]).replace('\t','')
    fichier.write(nom_prenom+';'+adresse+';'+cp_ville+';\n')

                

fichier.close()