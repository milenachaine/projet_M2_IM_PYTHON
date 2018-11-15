#!/usr/bin/python3
# coding: utf-8
## V1 POUR PROJET GROS GROS GROS CHANGEMENTS A VENIR
## ATTENTION AUX &
### Milena Chaîne
### description : attend un fichier de données structuré, renvoie ces données structurées en XML
### ex : python3 csv2xml <file_student_with_separator>

# modules
import sys
import os.path


# fonctions

## quitter si usage incorrect
def usage(name):
    sep = "_"*40
    usage = "Usage correct : python3 {} <file_student_with_separator>".format(name)
    print(sep)
    print(usage)
    print(sep)
    exit()

def file2array(filename):
    """file2array attend un fichier
    et renvoie une liste de ces lignes, sans espaces en fin de ligne
    """
    with open(filename, "r") as fichier:
    	lignes = [ligne.strip() for ligne in fichier]
    return lignes
 
def array2XML(liste, sep):
	"""array2XML attend une liste de lignes formatées
	la sépare grâce au séparateur
	puis la formate
	le cas où xy n'est pas renseigné est géré car cats[8] existe (mais il est vide)
	"""
	dataXML=[]
	compteur = 0
	for ligne in liste:
		compteur +=1
		dataXML.append("<logement id=\"{}\">".format(compteur))
		cats = ligne.split(sep)
		dataXML.append("\t<geo_point_2d>{}</geo_point_2d>".format(cats[0]))
		dataXML.append("\t<geo_shape>{}</geo_shape>".format(cats[1]))
		dataXML.append("\t<n_livr>{}</n_livr>".format(cats[2]))
		dataXML.append("\t<adr>{}</adr>".format(cats[3]))
		dataXML.append("\t<ann>{}</ann>".format(cats[4]))
		dataXML.append("\t<bs>{}</bs>".format(cats[5]))
		dataXML.append("\t<nb_logt>{}</nb_logt>".format(cats[6]))
		dataXML.append("\t<nb_plai>{}</nb_plai>".format(cats[7]))
		dataXML.append("\t<nb_plus>{}</nb_plus>".format(cats[8]))
		dataXML.append("\t<nb_pluscd>{}</nb_pluscd>".format(cats[9]))
		dataXML.append("\t<nb_pls>{}</nb_pls>".format(cats[10]))
		dataXML.append("\t<mode_real>{}</mode_real>".format(cats[11]))
		dataXML.append("\t<comm>{}</comm>".format(cats[12]))
		dataXML.append("\t<arr>{}</arr>".format(cats[13]))
		dataXML.append("\t<nat_prog>{}</nat_prog>".format(cats[14]))
		dataXML.append("\t<coord_x_l9>{}</coord_x_l9>".format(cats[15]))
		dataXML.append("\t<coord_y_l9>{}</coord_y_l9>".format(cats[16]))
		dataXML.append("</logement>")
	return dataXML
	
    
def printXML2file(dataXML):
    data_out = open("paris_V1_milena.xml","w",encoding="utf-8")
    data_out.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    data_out.write("<LOGEMENTS>\n")
    for ligne in dataXML:
        data_out.write("\t")
        data_out.write(ligne)
        data_out.write("\n")
    data_out.write("</LOGEMENTS>")
    data_out.close()


# main
## gestion des arguments
if((len(sys.argv) != 2) or (not(os.path.isfile(sys.argv[1])))):
    usage(sys.argv[0])

## contenu
file_student = sys.argv[1]
data = file2array(file_student)
dataXML = array2XML(data, ";")
printXML2file(dataXML)
