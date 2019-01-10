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
                <link href="projet.css" rel="stylesheet" type="text/css" media="all" />
                <!--[if IE 6]><link href="default_ie6.css" rel="stylesheet" type="text/css" /><![endif]-->
            </head>
            <body>
                <div id="header-wrapper">
                    <div id="header" class="container">
                        <div id="logo">
                            <img src="xml_logo.png" alt="logo" class="logo"/>
                            <h1><xsl:value-of select="//name"/></h1>
                        </div>
                        <section id = "onglets_milena_ferial">
                          <aside>
                          <a href="index.xml">Accueil</a>
                          <a href="presentation.xml">Présentation</a>
                          <a href="visualisation.xml">Visualisation</a>
                          </aside>
                        </section>
                    </div>
                </div>
                <div class="wrapper">
                    <div class="content">
                        <xsl:for-each select="//explication">
                            <p><xsl:value-of select="text()"/></p>
                        </xsl:for-each>
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
                <link href="projet.css" rel="stylesheet" type="text/css" media="all" />
                <!--[if IE 6]><link href="default_ie6.css" rel="stylesheet" type="text/css" /><![endif]-->
            </head>
            <body>
                <div id="header-wrapper">
                    <div id="header" class="container">
                        <div id="logo">
                            <img src="xml_logo.png" alt="logo" class="logo"/>
                            <h1><xsl:value-of select="//name"/></h1>
                        </div>
                        <section id = "onglets_milena_ferial">
                          <aside>
                          <a href="index.xml">Accueil</a>
                          <a href="presentation.xml">Présentation</a>
                          <a href="visualisation.xml">Visualisation</a>
                          </aside>
                        </section>
                    </div>
                </div>
                <div class="wrapper">
                    <div class="content">
                        <xsl:for-each select="//explication">
                            <p><xsl:value-of select="text()"/></p>
                        </xsl:for-each>


                    </div>


                </div>

                <h2>Tableau des données </h2>
<p>Ce tableau permet d'accéder aux données et résultats.</p>

                <table style="float:center">
    <tr>
    <th>Données</th>
    <th>XSL</th> 
    <th>Résultats</th>
  </tr>
  <tr>
    <td><a href="../../data/CSV/hlm_paris.csv">HLM_PARIS.CSV</a></td>
    <td><a href="../../data/CSV/hlm_paris.xsl">HLM_PARIS.XSL</a></td>
    <td><a href="../../data/CSV/hlm_paris.html">HLM_PARIS.HTML</a></td>
  </tr>
  <tr>
    <td><a href="../../data/CSV/qp.csv">QP_POLITIQUE_DE_LA_VILLE.CSV</a></td>
    <td><a href="../../data/CSV/qp.xsl">QP_POLITIQUE_DE_LA_VILLE.XSL</a></td>
    <td><a href="../../data/CSV/qp.xsl">QP_POLITIQUE_DE_LA_VILLE.HTML</a></td>
  </tr>
  <tr>
    <td><a href="../../data/CSV/arrondissements.csv">ARRONDISSEMENTS.CSV</a></td>
    <td><a href="../../data/CSV/arrondissements.xsl">ARRONDISSEMENTS.XSL</a></td>
    <td><a href="../../data/CSV/arrondissements.html">ARRONDISSEMENTS.HTML</a></td>
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

          <link href="projet.css" rel="stylesheet" type="text/css" media="all" />

<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type="text/javascript">
      google.charts.load('current', {'packages':['bar']});  
      google.charts.setOnLoadCallback(drawStuff);

      function drawStuff() {
        var data = new google.visualization.arrayToDataTable([
          ['Année', 'Moyenne'],
          ["2001", 40],
          ["2002", 32],
          ["2003", 33],
          ["2004", 26],
          ["2005", 26],
          ["2006", 32],
          ["2007", 23],
          ["2008", 22],
          ["2009", 22],
          ["2010", 25],
          ["2011", 29],
          ["2012", 30],
          ["2013", 34],
          ["2014", 40],
          ["2015", 37],
          ["2016", 43],
          ["2017", 36]
        ]);

        var options = {
          width: 800,
          legend: { position: 'center' },
          chart: {
            title: 'Évolution chronologique du nombre de logements sociaux financés dans la ville de Paris : 2001 - 2017',
            subtitle: 'nombre total de logements financés par nombre d\'interventions' },
          axes: {
            x: {
              0: { side: 'top', label: ''} 
            }
          },
          bar: { groupWidth: "60%" }
        };

        var chart = new google.charts.Bar(document.getElementById('top_x_div'));
       
        chart.draw(data, google.charts.Bar.convertOptions(options));
      };
    </script>
  </head>

            <body>


                    <div id="header" class="container">
                        <div id="logo">
                            <img src="xml_logo.png" alt="logo" class="logo"/>
                            <h1><xsl:value-of select="//name"/></h1>
                        </div>
                        <section id = "onglets_milena_ferial">
                          <aside>
                          <a href="index.xml">Accueil</a>
                          <a href="presentation.xml">Présentation</a>
                          <a href="visualisation.xml">Visualisation</a>
                          </aside>
                        </section>
                    </div>
                



                <div class="wrapper">
                    <div class="content">
                        <xsl:for-each select="//explication">
                            <p><xsl:value-of select="text()"/></p>
                                
                        </xsl:for-each>

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





