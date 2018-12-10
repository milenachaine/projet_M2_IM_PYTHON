# github.com/feryah/projet_M2_IM_XML
# v2
# description : ce programme attend un fichier de données structuré en CSV, renvoie ces données structurées en XML
# en gros : récupère la première ligne, puis traite chaque ligne non vide, la segmente et la formate
# => envoie tout en XML dans nouveau fichier
# ex : python3 csv2xml <chemin_fichier>
# ici on travaille sur le fichier arrondissements.csv sans modifier particulièrement sa structure

# modules
import sys
import os.path

# fonctions


def usage(nom, output):
	"""
	contrôler les arguments fournis au programme
    :param nom:  nom de ce fichier (argv[0])
    :param output: emplacement du fichier de sortie
    :return: ligne au terminal indiquant le problème ou l'absence de problème
    """
	sep = "-"*70
	message = "Usage : python3 {} <fichier_a_formater>".format(nom)
	if len(sys.argv) != 2:
		print(sep)
		print("Nombre d'arguments incorrect")
		print(message)
		print(sep)
		exit()
	elif not os.path.isfile(sys.argv[1]):
		print(sep)
		print("{} est introuvable".format(sys.argv[1]))
		print(message)
		print(sep)
		exit()
	else:
		print("Emplacement du fichier XML en sortie : {}".format(output))


def lecture_fichier(fic, sep):
	"""
    lire le fichier CSV et le transformer en liste de listes contenant toutes ses lignes non vides triées par séparateur
    :param fic: fichier CSV
	:param sep: séparateur entre chaque futur balise (pour du CSV, ";")
    :return: liste de toutes les lignes non vides
    """
	with open(fic, "r") as fichier:
		lignes = [ligne.strip().split(sep) for ligne in fichier]
	return lignes


def liste2xml(liste):
	"""
	récupérer une liste de lignes formatées, les modéliser en XML
	la première ligne est traitée à part pour récupérer les noms de balise
	:param liste: liste de lignes
	:return:
	"""
	ligne1 = [s.replace(" ", "_") for s in liste[0]]
	liste.pop(0)
	liste.sort(key=lambda x: int(x[1])) #le fichier original ne trie pas les arrondissements numériquement
	compteur_total = len(ligne1)
	fichier_XML=[]

	for ligne in liste:
		fichier_XML.append("<arrondissement id=\"{}\">".format(ligne[1]))
		fichier_XML.append("\t<{0}>{1}</{0}>".format(ligne1[0], ligne[0]))
		compteur = 2
		while compteur < compteur_total:
			fichier_XML.append("\t<{0}>{1}</{0}>".format(ligne1[compteur], ligne[compteur]))
			compteur += 1
		fichier_XML.append("</arrondissement>")
	return fichier_XML


def xml2fichier(dataXML, output):
	"""
	imprimer le résultat dans un fichier XML correctement formaté
	:param dataXML: la liste de listes obtenue plus haut
	:param output: l'emplacement du fichier de sortie
	"""
	with open(output, "w", encoding="utf-8") as data_out:
		data_out.write('<?xml version="1.0" encoding="UTF-8"?>\n')
		data_out.write("<ARRONDISSEMENTS>\n")
		for ligne in dataXML:
			data_out.write("\t")
			data_out.write(ligne)
			data_out.write("\n")
		data_out.write("</ARRONDISSEMENTS>")
		data_out.close()


# main
#emplacement de l'output

output = "../output/arrondissements.xml"

#gestion des arguments/aspect visuel au terminal

usage(sys.argv[0], output)

#traitement du contenu

file_student = sys.argv[1]
data = lecture_fichier(file_student, ";")
data_XML = liste2xml(data)
xml2fichier(data_XML, output)