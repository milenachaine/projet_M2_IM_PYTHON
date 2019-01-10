#!/bin/bash
###############
###SYNOPSIS####
###############
#
#Date : 07/12/16
#
#But : Lancement de Saxon
#
#Usage : bash run-unix.sh <doc.xml> <doc.xsl>
#
###############

usage()
{
	echo "usage correct : bash run-unix.sh <doc.xml> <doc.xsl>";
	exit;
}

if [[ -z $1 || -z $2  ]]
then
	usage
fi

CLASSPATH=_bin/SaxonHE9-6-0-2J/saxon9he.jar:_bin/xml-commons-resolver-1.2/resolver.jar
filename=$(basename "$1")
filename="${filename%.*}"
mkdir ./$filename;
java -cp $CLASSPATH net.sf.saxon.Transform -catalog:_etc/XMLCatalog.xml -s:$1 -xsl:$2 -o:./$filename/${filename}.html
