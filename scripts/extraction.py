# contexte : github.com/(feryah/projet_M2_IM_XML|milenachaine/projet_M2_IM_PYTHON)
# module de fonctions liées à l'extraction et au formatage de fichiers CSV en XML

import re
import sys
import os.path
import extraction as e

# -------- FONCTIONS GENERALES --------


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
		print(sep)
		print("Emplacement du fichier XML en sortie : {}".format(output))
		print(sep)


def balise_xml(balise):
	"""
	normalise une chaîne de caractères afin de pouvoir l'utiliser comme nom de balise XML
	enlève notamment les espaces, les caractères de ponctuation, et les caractères potentiellement problématiques comme les accents
	:param balise: une chaîne de caractères
	:return: cette chaîne normalisée
	"""
	#balise = re.sub(r'[\(\)\,\;\:\.\ ]',"_", balise)
	
	balise = re.sub(r'[\(\,\;\:\.\ ]',"_", balise)
	if '__' in balise:
		balise = re.sub(r'__','_', balise)


	balise = re.sub(r'[\)]','',balise)
	balise = re.sub(r'[éèê]','e',balise)




	return balise

def contenu_balise(cont):
	"""
	normalise une chaîne de caractères afin de pouvoir l'utiliser comme contenu de balise et rendre le fichier xml valide
	remplace certains caractères par leurs références d'entité. Exemple : & --> &amp;
	:param balise: une chaîne de caractères
	:return: cette chaîne normalisée
	"""

	

	cont = re.sub(r'[&]','&amp;', cont)

	#liste non exhaustive


	return cont

def lecture_csv(fic, sep):
	"""
	lire le fichier CSV et le transformer en liste de listes contenant toutes ses lignes non vides triées par séparateur
	:param fic: fichier CSV
	:param sep: séparateur entre chaque futur balise (pour du CSV, ";")
	:return: liste de toutes les lignes non vides
	"""
	with open(fic, "r") as fichier:
		lignes = [ligne.strip().split(sep) for ligne in fichier]
	return lignes


def xml2fichier(data, output, racine):
	"""
	imprimer le résultat dans un fichier XML correctement formaté en UTF-8
	:param data: la liste de listes obtenue plus haut
	:param output: l'emplacement du fichier de sortie
	:param racine: nom qu'on souhaite donner à la racine du fichier XML
	"""
	with open(output, "w", encoding="utf-8") as data_out:
		data_out.write('<?xml version="1.0" encoding="UTF-8"?>\n')
		data_out.write("<{}>\n".format(racine))
		for ligne in data:
			data_out.write("\t")
			data_out.write(ligne)
			data_out.write("\n")
		data_out.write("</{}>".format(racine))
		data_out.close()


# -------- FONCTIONS SPECIFIQUES --------


def arrondissements_xml(liste):
	"""
	spécifique au script arrondissements
	récupérer une liste de lignes formatées, les modéliser en XML
	la première ligne est traitée à part pour récupérer les noms de balise
	:param liste: liste de lignes
	:return: la liste contenant les données formatées
	"""
	ligne1 = [e.balise_xml(s) for s in liste[0]]
	compteur_total = len(ligne1)
	liste.pop(0)

	liste.sort(key=lambda x: int(x[1])) #le fichier original ne trie pas les arrondissements numériquement

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


def qp_xml(liste):
	"""
	spécifique au script qp
	récupérer une liste de lignes formatées, les modéliser en XML
	la première ligne est traitée à part pour récupérer les noms de balise
	:param liste: liste de lignes
	:return: la liste contenant les données formatées
	"""
	ligne1 = [e.balise_xml(s) for s in liste[0]]

	compteur_total = len(ligne1)
	liste.pop(0)

	liste = [ligne for ligne in liste if ligne[7] == "75"] # le fichier original contient des informations sur toute l'IDF
	liste.sort(key=lambda x: int(x[2])) # le fichier original ne trie pas les arrondissements numériquement

	fichier_XML=[]

	for ligne in liste:
		fichier_XML.append("<qp id=\"{}\">".format(ligne[2]))
		fichier_XML.append("\t<{0}>{1}</{0}>".format(ligne1[0], ligne[0]))
		fichier_XML.append("\t<{0}>{1}</{0}>".format(ligne1[1], ligne[1]))
		compteur = 3
		while compteur < compteur_total:
			fichier_XML.append("\t<{0}>{1}</{0}>".format(ligne1[compteur], ligne[compteur]))
			compteur += 1
		fichier_XML.append("</qp>")
	return fichier_XML


def hlm_paris_xml(liste):
	"""
	spécifique au script hlm_paris
	récupérer une liste de lignes formatées, les modéliser en XML
	la première ligne est traitée à part pour récupérer les noms de balise
	:param liste: liste de lignes
	:return: la liste contenant les données formatées
	""" 
	ligne1 = [e.balise_xml(s) for s in liste[0]]
	liste.pop(0)

	liste.sort(key=lambda x: int(x[4])) #le fichier original ne trie pas les années numériquement

	fichier_XML=[]


	compteur_log = 1

	for ligne in liste:

		fichier_XML.append("\t<annee id=\"{}\">".format(ligne[4]))


		fichier_XML.append("\t\t<logements id=\"{}\">".format(compteur_log))
		compteur_log += 1

	
		fichier_XML.append("\t\t\t<localisation>")
		fichier_XML.append("\t\t\t\t<{0}>{1}</{0}>".format(ligne1[0], e.contenu_balise(ligne[0])))
		fichier_XML.append("\t\t\t\t<{0}>{1}</{0}>".format(ligne1[1], e.contenu_balise(ligne[1])))
		fichier_XML.append("\t\t\t\t<{0}>{1}</{0}>".format(ligne1[3], e.contenu_balise(ligne[3])))
		fichier_XML.append("\t\t\t\t<{0}>{1}</{0}>".format(ligne1[13], e.contenu_balise(ligne[13])))
		fichier_XML.append("\t\t\t</localisation>")

		fichier_XML.append("\t\t\t<nb_par_type_logement>")
		fichier_XML.append("\t\t\t\t<{0}>{1}".format(ligne1[6], e.contenu_balise(ligne[6])))
		fichier_XML.append("\t\t\t\t\t<{0}>{1}</{0}>".format(ligne1[7], e.contenu_balise(ligne[7])))
		fichier_XML.append("\t\t\t\t\t<{0}>{1}</{0}>".format(ligne1[8], e.contenu_balise(ligne[8])))
		fichier_XML.append("\t\t\t\t\t<{0}>{1}</{0}>".format(ligne1[9], e.contenu_balise(ligne[9])))
		fichier_XML.append("\t\t\t\t\t<{0}>{1}</{0}>".format(ligne1[10], e.contenu_balise(ligne[10])))
		fichier_XML.append("\t\t\t\t</{0}>".format(ligne1[6]))
		fichier_XML.append("\t\t\t</nb_par_type_logement>")

		fichier_XML.append("\t\t\t<realisation>")
		fichier_XML.append("\t\t\t\t<{0}>{1}</{0}>".format(ligne1[5], e.contenu_balise(ligne[5])))
		fichier_XML.append("\t\t\t\t<{0}>{1}</{0}>".format(ligne1[2], e.contenu_balise(ligne[2])))
		fichier_XML.append("\t\t\t\t<{0}>{1}</{0}>".format(ligne1[11], e.contenu_balise(ligne[11])))
		fichier_XML.append("\t\t\t\t<{0}>{1}</{0}>".format(ligne1[15], e.contenu_balise(ligne[15])))
		fichier_XML.append("\t\t\t\t<{0}>{1}</{0}>".format(ligne1[14], e.contenu_balise(ligne[14])))
		fichier_XML.append("\t\t\t</realisation>")


		fichier_XML.append("\t\t</logements>")

		fichier_XML.append("\t</annee>")


		

   
	return fichier_XML