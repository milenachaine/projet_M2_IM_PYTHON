import sys
import os.path


def usage(titre):
    sep ="_"*40;
    usage = "Usage correct : python3 {} <file_tournage_with_separator>".format(titre);
    print(sep)
    print(usage)
    print(sep)
    exit();


def file2array(filename, param):
    data_f = open(file_tournage, "r")
    data = [line for line in data_f if param in line]
    data_f.close()
    return data


def formatXML(rows_low, line, counter):

    film = "<film id=\"{}\">\n".format(counter + 1)
    
    line = line.lower().split(";")

    print (line)

    #counter = 0



    #rows = [titre, realisateur, adresse, organisme_demandeur, type_de_tournage, arrondissement, date_debut, date_fin, xy]


    for i in range(len(rows_low)):
        balises = "\t\t<{}>{}</{}>\n".format(rows_low[i], line[i], rows_low[i])
        film += balises
    film += "\t</film>"
    return film


def array2arrayxXML(data): 
    
    dataXML = []
    counter = 0
    for line in data:
        counter =+1
        rows_low = data[0]
        rows_final = rows_low.replace(" ","_").lower().split(";")
        film = formatXML(rows_final, line, counter)
        dataXML.append(film)
    return dataXML
        

    #rows_final = [titre, realisateur, adresse, organisme_demandeur, type_de_tournage, arrondissement, date_debut, date_fin, xy]
   
   


def printXML(dataXML):
    print('<?xml version="1.0" encoding="UTF-8"?>')
    print("<tournages>")
    for row in dataXML:
        print(row)
    print("</tournages>")


def printXML2File(dataXML):
    data_out = open("output2.xml","w",encoding="utf-8")
    data_out.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    data_out.write("<tournages\n")

    for row in dataXML:
        data_out.write('\t')
        data_out.write(row)
        data_out.write('\n')

    data_out.write("</tournages>\n")
    data_out.close()



# Main
## Gestion des arguments
if((len(sys.argv) != 2) or (not(os.path.isfile(sys.argv[1])))):
    usage(sys.argv[0])

## content
file_tournage = sys.argv[1]
data = file2array(file_tournage, ";")
dataXML = array2arrayxXML(data)
#printXML(dataXML)
printXML2File(dataXML)
