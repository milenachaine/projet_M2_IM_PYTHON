# Projet dans le cadre d'un cours de XML et de langages de scripts (Master 2 INALCO, 2018-2019)
## Contexte
Ce projet a été réalisé dans le cadre du [master TAL à l'INALCO](http://www.tal.univ-paris3.fr/plurital/) par [Milena Chaîne](http://www.github.com/milenachaine) et [Ferial Yahiaoui](http://www.github.com/feryah).

Nous avons choisi de nous intéresser à la problématique du logement social sur Paris, et pour ce faire, nous avons exploité des données au format CSV créées par la Mairie de Paris, ainsi que la région Île-de-France. Ces données sont des données publiques françaises disponibles dans le cadre de l'ouverture des données (Open Data), ayant pour but de faciliter leur réutilisation par d'autres acteurs que l'administration française.

## Sources des données exploitées
- [Logements sociaux financés à Paris (2001-2017)](http://www.data.gouv.fr/fr/datasets/logements-sociaux-finances-a-paris/)
- [Quartiers prioritaires de la politique de la ville (Paris)](http://data.iledefrance.fr/explore/dataset/qp-politiquedelaville-shp/)
- [Arrondissements parisiens](http://www.data.gouv.fr/fr/datasets/arrondissements-1/)

## Arborescence du projet
- data : contient les données brutes (au format CSV)
- scripts : contient les scripts Python qui ont permis de formater les données
- output : contient les données formatées en XML
- grammaires : contient les grammaires DTD et RelaxNG de chaque fichier XML
- web : contient les fichiers HTML, CSS, et JS constituant le site Web final
