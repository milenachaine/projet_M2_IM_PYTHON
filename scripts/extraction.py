# contexte : github.com/(feryah/projet_M2_IM_XML|milenachaine/projet_M2_IM_PYTHON)
# module de fonctions liées à l'extraction et au formatage de fichiers CSV en XML

import sys
import os.path


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


def arrondissements_xml(liste):
    """
    spécifique au script arrondissements
    récupérer une liste de lignes formatées, les modéliser en XML
    la première ligne est traitée à part pour récupérer les noms de balise
    :param liste: liste de lignes
    :return: la liste contenant les données formatées
    """
    ligne1 = [s.replace(" ", "_") for s in liste[0]]
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
    ligne1 = [s.replace(" ", "_") for s in liste[0]]
    compteur_total = len(ligne1)
    liste.pop(0)

    liste = [ligne for ligne in liste if ligne[7] == "75"] #le fichier original contient des informations sur toute l'IDF
    liste.sort(key=lambda x: int(x[2])) #le fichier original ne trie pas les arrondissements numériquement

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