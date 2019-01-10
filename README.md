# Projet dans le cadre d'un cours de XML et de langages de scripts (Master 2 INALCO, 2018-2019)
## Contexte
Ce projet a été réalisé dans le cadre du [master TAL à l'INALCO](http://www.tal.univ-paris3.fr/plurital/) par [Milena Chaîne](http://www.github.com/milenachaine) et [Ferial Yahiaoui](http://www.linkedin.com/in/ferial-yahiaoui-nlp19/).

Il s'agissait d'explorer une thématique précise en exploitant des données structurées au format XML, puis de présenter une visualisation de ces données dans un site Web statique. Nous avons choisi de nous intéresser à la problématique du logement social sur Paris, et avons choisi d'exploiter des données créées par la Mairie de Paris, ainsi que la région Île-de-France.

## Sources des données exploitées
- [Logements sociaux financés à Paris (2001-2017)](http://www.data.gouv.fr/fr/datasets/logements-sociaux-finances-a-paris/)
- [Quartiers prioritaires de la politique de la ville (Paris)](http://data.iledefrance.fr/explore/dataset/qp-politiquedelaville-shp/)
- [Arrondissements parisiens](http://www.data.gouv.fr/fr/datasets/arrondissements-1/)

## Arborescence du projet
- data : contient les données brutes (au format CSV)
- script : contient les scripts Python qui permettent de formater les données
- xml : contient les données formatées en XML
- grammaire : contient les grammaires DTD et RelaxNG de chaque fichier XML
- transformation : contient les fichiers XML et XSLT qui serviront à créer le site Web final
- web : contient les fichiers HTML, CSS, et JS constituant le site Web