# github.com/feryah/projet_M2_IM_XML
# v2
# description : ce programme attend un fichier de données structuré en CSV, renvoie ces données structurées en XML
# en gros : récupère la première ligne, la traite pour récupérer noms de balise, puis traite chaque ligne non vide, la segmente et la formate => envoie tout en XML dans nouveau fichier
# ex : python3 csv2xml <chemin_fichier>
# ici on travaille sur le fichier arrondissements.csv sans modifier particulièrement sa structure

# modules
import sys
import os.path

# fonctions

def usage(nom):
	"""
    contrôler les arguments fournis au programme
    :param nom:  nom de ce fichier (argv[0])
    :return: ligne au terminal indiquant le problème
    """
	sep = "-"*70
	usage = "Usage : python3 {} <fichier_a_formater>".format(nom)
	if len(sys.argv) != 2:
		print(sep)
		print("Nombre d'arguments incorrect")
		print(usage)
		print(sep)
		exit()
	elif not os.path.isfile(sys.argv[1]):
		print(sep)
		print("{} est introuvable".format(sys.argv[1]))
		print(usage)
		print(sep)
		exit()
	else:
		print("Fichier traité : {}".format(sys.argv[1]))

def lecture_fichier(fic):
	"""
    lire le fichier CSV et le transformer en liste contenant toutes ses lignes non vides
    :param fic: fichier CSV
    :return: liste de toutes les lignes non vides
    """
	with open(fic, "r") as fichier:
		lignes = [ligne.strip() for ligne in fichier]
	return lignes


def liste2XML(liste, sep):
	"""
	récupérer une liste de lignes formatées, les modéliser en XML
	la première ligne est traitée à part pour récupérer les noms de balise
	:param liste: liste de lignes
	:param sep: séparateur entre chaque futur balise (pour du CSV, ";")
	:return:
	"""
	fichier_XML=[]
	ligne1 = liste[0].split(sep)
	liste.pop(0)
	for ligne in liste:
		cats = ligne.split(sep)
		fichier_XML.append("<arrondissement id=\"{}\">".format(cats[1]))
		fichier_XML.append("\t<{}>{}</{}>".format(ligne1[0],cats[0],ligne1[0]))
		fichier_XML.append("\t<{}>{}</{}>".format(ligne1[2],cats[2],ligne1[2]))
		fichier_XML.append("\t<{}>{}</{}>".format(ligne1[3],cats[3],ligne1[3]))
		fichier_XML.append("</arrondissement>")
	return fichier_XML


def XML2fichier(dataXML):
    data_out = open("arrondissements.xml","w",encoding="utf-8")
    data_out.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    data_out.write("<ARRONDISSEMENTS>\n")
    for ligne in dataXML:
        data_out.write("\t")
        data_out.write(ligne)
        data_out.write("\n")
    data_out.write("</ARRONDISSEMENTS>")
    data_out.close()



# main
#gestion des arguments
usage(sys.argv[0])

#traitement du contenu
file_student = sys.argv[1]
data = lecture_fichier(file_student)
dataXML = liste2XML(data, ";")
XML2fichier(dataXML)
