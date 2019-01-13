<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:output method="html" encoding="UTF-8"/>

<!-- ACCUEIL -->
    <xsl:template match="/index">
        <html xmlns="http://www.w3.org/1999/xhtml">
            <head>
                <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
                <title>Milena Chaîne  &amp; Ferial Yahiaoui - XML</title>
                <meta name="keywords" content="" />
                <meta name="explication" content="" />
                <link href="http://fonts.googleapis.com/css?family=Source+Sans+Pro:200,300,400,600,700,900|Quicksand:400,700|Questrial" rel="stylesheet" />
                <link href="../css/projet.css" rel="stylesheet" type="text/css" media="all" />
                <!--[if IE 6]><link href="default_ie6.css" rel="stylesheet" type="text/css" /><![endif]-->
            </head>
            <body>
                <div id="header-wrapper">
                    <div id="header" class="container">
                        <div id="logo">
                            <img src="../css/xml_logo.png" alt="logo" class="logo"/>
                            <h1><xsl:value-of select="//name"/></h1>
                        </div>
                        <section id = "onglets_milena_ferial">
                          <aside>
                          <a href="index.html">Accueil</a>
                          <a href="presentation.html">Présentation</a>
                          <a href="visualisation.html">Visualisation</a>
                          </aside>
                        </section>
                    </div>
                </div>
                <div class="wrapper">
                    <div class="content">
                      <table><tr>
                        <td class="table">
                          <xsl:for-each select="//about">
                        <xsl:for-each select="//explication">
                            <p><xsl:value-of select="text()"/></p>
                        </xsl:for-each>
                      </xsl:for-each>
                    </td></tr></table>
                    </div>
                </div>
                <div id ="footer-wrapper">
                  <footer id ="footer" class="container">
                    <div class="row">
                      <p class="footer">
                        Milena Chaîne  &amp; Ferial Yahiaoui - XML
                      </p>
                      <p class="footer">

                      </p>
                    </div>
                  </footer>
                </div>
            </body>
        </html>
    </xsl:template>


<!-- PRESENTATION -->
    <xsl:template match="/presentation">
        <html xmlns="http://www.w3.org/1999/xhtml">
            <head>
                <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
                <title>Milena Chaîne  &amp; Ferial Yahiaoui - XML</title>
                <meta name="keywords" content="" />
                <meta name="explication" content="" />
                <link href="http://fonts.googleapis.com/css?family=Source+Sans+Pro:200,300,400,600,700,900|Quicksand:400,700|Questrial" rel="stylesheet" />
                <link href="../css/projet.css" rel="stylesheet" type="text/css" media="all" />
                <!--[if IE 6]><link href="default_ie6.css" rel="stylesheet" type="text/css" /><![endif]-->
            </head>
            <body>
                <div id="header-wrapper">
                    <div id="header" class="container">
                        <div id="logo">
                            <img src="../css/xml_logo.png" alt="logo" class="logo"/>
                            <h1><xsl:value-of select="//name"/></h1>
                        </div>
                        <section id = "onglets_milena_ferial">
                          <aside>
                          <a href="index.html">Accueil</a>
                          <a href="presentation.html">Présentation</a>
                          <a href="visualisation.html">Visualisation</a>
                          </aside>
                        </section>
                    </div>
                </div>
                <div class="wrapper">
                    <div class="content">
                      <table><tr>
                        <td class="table">
                        <xsl:for-each select="//about/explication">
                            <p><xsl:value-of select="text()"/></p>
                        </xsl:for-each>
                                            </td></tr></table>
                        <h2>Nettoyage des données</h2>
                        <table><tr>
                          <td class="table">
                        <xsl:for-each select="//nettoyage/explication">
                            <p><xsl:value-of select="text()"/></p>
                        </xsl:for-each>
                                            </td></tr></table>
                        <h2>Modélisation des données</h2>
                        <table><tr>
                          <td class="table">
                        <xsl:for-each select="//modelisation/explication">
                            <p><xsl:value-of select="text()"/></p>
                        </xsl:for-each>
                                            </td></tr></table>
                        <h2>Validation des fichiers</h2>
                        <table><tr>
                          <td class="table">
                        <xsl:for-each select="//validation/explication">
                            <p><xsl:value-of select="text()"/></p>
                        </xsl:for-each>
                                            </td></tr></table>


                    </div>


                </div>

                <h2>Tableau des données </h2>
<p>Ce tableau permet d'accéder aux données et résultats.</p>

                <table style="float:center">
    <tr>
    <th>Données</th>
    <th>Grammaires</th>
    <th>Résultats</th>
  </tr>
  <tr>
    <td><a href="../../data/CSV/hlm_paris.csv">HLM_PARIS.CSV</a></td>
    <td><a href="../../grammaire/hlm_paris/auto_hlm_paris.dtd">AUTO_HLM_PARIS.DTD</a> <a href="../../grammaire/hlm_paris/auto_hlm_paris.rng">AUTO_HLM_PARIS.RNG</a> <a href="../../grammaire/hlm_paris/hlm_paris.dtd">HLM_PARIS.DTD</a> <a href="../../grammaire/hlm_paris/hlm_paris.rng">HLM_PARIS.RNG</a></td>
    <td><a href="../../xml/hlm_paris.xml">HLM_PARIS.XML</a></td>
  </tr>
  <tr>
    <td><a href="../../data/CSV/qp.csv">QP_POLITIQUE_DE_LA_VILLE.CSV</a></td>
    <td><a href="../../grammaire/qp/qp.dtd">QP.DTD</a> <a href="../../grammaire/qp/qp.rng">QP.RNG</a></td>
    <td><a href="../../xml/qp.xml">QP_POLITIQUE_DE_LA_VILLE.XML</a></td>
  </tr>
  <tr>
    <td><a href="../../data/CSV/arrondissements.csv">ARRONDISSEMENTS.CSV</a></td>
    <td><a href="../../grammaire/arrondissements/arrondissements.dtd">ARRONDISSEMENT.DTD</a> <a href="../../grammaire/arrondissements/arrondissements.rng">ARRONDISSEMENT.RNG</a></td>
    <td><a href="../../xml/arrondissements.xml">ARRONDISSEMENTS.XML</a></td>
  </tr>
</table>

                <div id ="footer-wrapper">
                  <footer id ="footer" class="container">
                    <div class="row">
                      <p class="footer">
                        Milena Chaîne  &amp; Ferial Yahiaoui - XML
                      </p>
                      <p class="footer">

                      </p>
                    </div>
                  </footer>
                </div>
            </body>
        </html>
    </xsl:template>

    <!-- Visualisation -->
<xsl:template match="/visualisation">
  <html xmlns="http://www.w3.org/1999/xhtml">

      <head>
        <meta charset="utf-8"/>
          <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
          <title>Milena Chaîne &amp; Ferial Yahiaoui - XML</title>
          <meta name="keywords" content="" />
          <meta name="explication" content="" />
          <link href="http://fonts.googleapis.com/css?family=Source+Sans+Pro:200,300,400,600,700,900|Quicksand:400,700|Questrial" rel="stylesheet" />

          <link href="../css/projet.css" rel="stylesheet" type="text/css" media="all" />

  </head>

            <body>


                    <div id="header" class="container">
                        <div id="logo">
                            <img src="../css/xml_logo.png" alt="logo" class="logo"/>
                            <h1><xsl:value-of select="//name"/></h1>
                        </div>
                        <section id = "onglets_milena_ferial">
                          <aside>
                          <a href="index.html">Accueil</a>
                          <a href="presentation.html">Présentation</a>
                          <a href="visualisation.html">Visualisation</a>
                          </aside>
                        </section>
                    </div>




                <div class="wrapper">
                    <div class="content">
                        <xsl:for-each select="//explication">
                            <p><xsl:value-of select="text()"/></p>

                        </xsl:for-each>
                        <table style="float:center">
            <tr>
            <th>Lien</th>
            <th>Description</th>
          </tr>
          <tr>
            <td><a href="../js/carte.html">Répartition des quartiers prioritaires</a></td>
            <td>Représentation visuelle de la répartition des quartiers prioritaires de la politique de la ville par arrondissement parisien. La taille des cercles correspond au nombre de quartiers.</td>
          </tr><tr>
            <td><a href="../js/pie_qp_paris.html">Nombre de quartiers prioritaires parisiens par arrondissement</a></td>
            <td>Equivalent de la représentation géographique sous forme de graphe.</td>
            </tr><tr>
            <td><a href="../js/combo_evol_chro_hlm.html">Catégorie de financement des logements sociaux à Paris : 2010 - 2016</a></td>
            <td>Analyse de la répartition des catégories des logements financés.</td>
            </tr><tr>
            <td><a href="../js/histog_evol_hlm.html">Évolution chronologique du nombre de logements sociaux financés dans la ville de Paris : 2001 - 2017</a></td>
            <td>Analyse du nombre moyen de logements sociaux financés par intervention (une intervention correspondant à un site géographique).</td>
          </tr><tr>
            <td><a href="../js/lines_16_18_chrono.html">Évolution chronologique des logements sociaux financés dans les 16e et 18e arrondissements de Paris</a></td>
            <td>Comparaison du nombre de logements sociaux financés par année dans un arrondissement avec peu de quartiers prioritaires (16ème) et un arrondissement en comportant beaucoup (18ème).</td>
            </tr><tr>
            <td><a href="../js/pie_2008_arr_hlm.html">Logements sociaux financés à Paris par arrondissement pour l'année 2008</a></td>
            <td>Le choix de l'année 2008 s'explique par le fait que c'est l'année durant laquelle il y a eu le moins de financements.</td>
            </tr><tr>
            <td><a href ="../js/pie_2016_arr_hlm.html">Logements sociaux financés à Paris par arrondissement pour l'année 2016</a></td>
            <td>Le choix de l'année 2016 s'explique par le fait que c'est l'année durant laquelle il y a eu le plus de financements.</td>
          </tr>
        </table>
              <div id="top_x_div" style="width: 900px; height: 700px;"></div>
                    </div>
                </div>
                <div id ="footer-wrapper">
                  <footer id ="footer" class="container">
                    <div class="row">
                      <p class="footer">
                        Milena Chaîne  &amp; Ferial Yahiaoui - XML
                      </p>
                      <p class="footer">

                      </p>
                    </div>
                  </footer>
                </div>
            </body>
        </html>
    </xsl:template>




</xsl:stylesheet>
