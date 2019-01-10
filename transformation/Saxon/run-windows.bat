@ECHO OFF

SET CLASSPATH=_bin\SaxonHE9-6-0-2J\saxon9he.jar;_bin\xml-commons-resolver-1.2\resolver.jar;

java net.sf.saxon.Transform -catalog:_etc/XMLCatalog.xml -s:%1 -xsl:%2 -o:%~n1_out.html