# import libraries
from bs4 import BeautifulSoup
import urllib.request
import csv

#open file
fichier = open("Maine-et-Loire.csv","a")
fichier.write('Nom Prenom;Adresse;Code postale Ville;\n')


for i in range(110):
    print('Page ' + str(i) + ' done')
    # specify the url
    urlpage = 'https://www.assistantsmaternels49.fr/index.php?id=1577&page_directe=' + str(i+1)

    # query the website and return the html to the variable 'page'
    page = urllib.request.urlopen(urlpage)
    # parse the html using beautiful soup and store in variable 'soup'
    soup = BeautifulSoup(page, 'html.parser')

    strsoup = str(soup)
    index = strsoup.find('<!-- LIGNES DE RESULTATS -->')+28+211+3
    strsoup = strsoup[index:]
    index = strsoup.find('<')
    
    if i == 109:
        rangee = 8
    else:
        rangee = 88
            
    for y in range(rangee):
        index = strsoup.find('Voir la fiche de')+16
        strsoup =strsoup[index:]
        index = strsoup.find('"')
        nom_prenom = (strsoup[1:index]) 
        strsoup = strsoup[index:]
        index = strsoup.find('</td><td>')+9
        strsoup = strsoup[index:]
        index = strsoup.find('Voir la fiche</a>') + 21
        strsoup = strsoup[index:]
        index = strsoup.find(', 49')
        adresse = (strsoup[:index]) 
        strsoup = strsoup[index+2:]
        index = strsoup.find('MAINE ET LOIRE')-1
        cp_ville = (strsoup[:index]) 
        fichier.write(nom_prenom+';'+adresse+';'+cp_ville+';\n')

                

fichier.close()