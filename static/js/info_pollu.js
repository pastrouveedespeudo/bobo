function meteo(){
  var div = document.getElementById("soleil_texte");
  div.innerHTML = '<p>Quoi de mieux qu\'un temps d\'\u00e9t\u00e9 ? On peut sortir, \u00eatre avec ses amis, on adore \u00e7a ! '
                  + 'Cela est inscrit dans nos coutumes, dans la m\u00e9moire Humaine. '
                  + 'Nos anc\u00eatres un singe nu, un Gaulois, '
                  + "un chevalier, un napol\u00e9onien... a peut-\u00eatre d'\u00e9velopp\u00e9 une maladie sous la pluie et sous le froid du coup "
                  + 'il a donn\u00e9e \u00e0 son fils, ton anc\u00e8tre le pouvoir de se m\u00e9fier de la pluie et du froid. On appelle \u00e7a la transmission culturelle. '
                  + "De plus le soleil rend agressif (En Californie y fait chaud et le taux d\'aggression et le plus \u00e9lev\u00e9) "
                  + "et que la baisse de la temp\u00e9rature suite \u00e0 un long \u00e9pisode de chaleur provoqu\u00e9 un petit cafard ? Donc l\'absence de lumi\u00e8re "
                  + 'Donc le temps est tr\u00e8s important pour nous ! '
                  + 'Mais aussi pour la pollution! Mais alors pourquoi ? De fait, le temps et surtout la condition du beau temps '
                  + "va pouvoir permettre \u00e0 certains polluants de se concentrer. "
                  + 'Par exemple un anticyclone est li\u00e9 au beau temps, c\'est un truc qui permet \u00e9 '
                  + 'la pollution de rester dans notre zone d\'air respirable. '
                  + 'On a par exemple une zone haute de 4 immeubles de 10 \u00e9tages ok ? et plus haut que ces 40 \u00e9tages il y a la '
                  + 'haute atmosph\u00e8re. Cette altitude c\'est une zone plus froide que la notre. Enfete par a + b l\'air froid '
                  + 'de la haute atmosph\u00e8re permet d\'\u00e9vacuer l\'air chaud de notre zone (les 4 \u00e9tages). Un anticyclone c\'est '
                  + 'un ph\u00e9nom\u00e8ne qui applique une pression de plus de 1030 hpa et qui va r\u00e9chauffer l\'air de la haute atmosph\u00e8re '
                  + "et qui va emp\u00e9cher d\'\u00e9vacuer l\'air chaud et la pollution de notre zone ! "
                  + 'Le beau temps la pollution \u00e0 case des rayons UV ! Ces rayons-l\u00e0 qui nous font bronzer vont pouvoir faire r\u00e9agir '
                  + 'et former des polluants.</p>'
                  + "<br>"
                  + '<input type="button" value="Fermer" onclick="fermer()">'
};


function fermer(){
document.getElementById("soleil_texte").innerHTML = "<h2>La temp\u00e9rature ?</h2>";
}









function vent(){
  
    var div = document.getElementById("vent_text");
    div.innerHTML = "<p> le vent est ralenti et augmente la temp\u00e9rature de la plan\u00e8te *1. De plus les temp\u00eates seront beaucoup plus intenses " +
                     "Mais cela change aussi sa direction*1. Et peut-\u00eatre nous atteindre. Imaginez des temp\u00eates \u00e0 r\u00e9p\u00e9tition chez vous ! "    +                                                                                                 
                     "Imaginez une canicule. Imaginez une petite brise et l'\u00e9motion de  bien-\u00eatre. Imaginez maintenant un monde sans "+
                     "petites brises... Souvenez-vous des fois ou \u00e0 cause de votre parapluie low cost le mauvais temps vous \u00e0 d\u00e9coiff\u00e9 "+
                     "dans 5 ans ca sera votre quotidien... "+
                     "Les voitures produisent 2000 briques de lait de CO2 toutes les 4secondes*2 "+
                     "c'est comme si Emma 1 mois fumait une cigarette dans une chambre mal a\u00e9r\u00e9e qui en plus ne s'a\u00e9rera pas. Il n'y a plus de vent "+
                     "Mais en vrai on s'en fout un b\u00e9b\u00e9 ca ne fume pas, et il faut bien se d\u00e9placer "
                    + "<br><br></p>"
                    + '<input type="button" value="Fermer" onclick="fermer_vent()">';

}




function saison(){
  
  var div = document.getElementById("saison_text");
  div.innerHTML = '<p>La vie est courte. Et encore plus courte avec la pollution. Mais elle l\'\u00e9tait encore plus pour nos ain\u00e9es. '+
                   'Imaginez ! parcourir des centaines de kilom\u00e8tres \u00e0 cheval pendant plusieurs semaines. '+
                    'allez voir son cousin Robert \u00e0 50 kilom\u00e8tres leur prenez 6 heures en moyenne comme pour faire un v =d/t '+
                      'alors imaginez 6h pour une vie de 25 ans en moyenne, c\'\u00e9tait beaucoup. '+
                    'Nous avons donc invent\u00e9 la voiture ! Gr\u00e2ce \u00e0 cet engin, nos d\u00e9placements ont quadrupl\u00e9 voir quintupl\u00e9 '+
                      'en terme de vitesse ! Nous avons donc gagn\u00e9 en temps en esp\u00e9rance de vie mais aussi en pollution. '+
                    'En effet, La cause principale de Pollution est le traffic routier direct et indirect. '+
                   'Selon BMW magazine, (une entreprise de voiture \u00e9lectrique) la construction d\'une voiture '+
                    'serait l\\u00e9quivalent d\au moins 18 0000 km (soit 2200 heure \u00e0 dos de cheval) parcourus '+
                    'Comment reconnaitre la pollution \u00e0 travers nos corps ? un troisi\u00e8me oeil ? non non mais qui sait pour dans 100 ans ? '+
                   "par contre ton enfant de 2 ans le saura. Les cons\u00e9quences sont les yeux qui piques, l'\hypertension, "+
                  + '</p>'
                  + "<br>"
                  + '<input type="button" value="Fermer" onclick="fermer_saison()">';

};



function fermer_saison(){
var div = document.getElementById("saison_text").innerHTML = '<h2>Les saisons ?</h2>';

}







function trafic(){
  
    var div = document.getElementById("trafic_text");
    div.innerHTML = "<p>Le trafic routier nous a permis de pouvoir acc\u00e9l\u00e9rer le temps, de r\u00e9duire la distance entre nous "+
                " mais il est l'un des plus facteurs de la pollution. En effet, les voitures "+
                "influent gravement au r\u00e9chauffement climatique par l\'effet de serre. "+
                "L'effet de serre c'est quoi ? c'est l'\u00e9l\u00e9vation de la temp\u00e9rature \u00e0 la surface de la plan\u00e8te. "+
                 "Par exemple le vent a besoin d'air chaud et d'air froid pour pouvoir circuler. Par ce r\u00e9chauffement "+
                 "le vent est ralenti et augmente la temp\u00e9rature de la plan\u00e8te *1. De plus les temp\u00eates seront beaucoup plus intenses "+
                 "Mais cela change aussi sa direction*1. Et peut-\u00eatre nous atteindre. Imaginez des temp\u00eates \u00e0 r\u00e9p\u00e9tition chez vous ! "  +                                                                                                   
                 "Imaginez une canicule. Imaginez une petite brise et l'\u00e9motion de  bien-\u00eatre. Imaginez maintenant un monde sans "+
                 "petites brises... Souvenez-vous des fois ou \u00e0 cause de votre parapluie low cost le mauvais temps vous \u00e0 d\u00e9coiff\u00e9 "+
                 "dans 5 ans ca sera votre quotidien... "+
                 "Les voitures produisent 2000 briques de lait de CO2 toutes les 4secondes*2 "+
                 "c'est comme si Emma 1 mois fumait une cigarette dans une chambre mal a\u00e9r\u00e9e qui en plus ne s'a\u00e9rera pas. Il n'y a plus de vent "+
                 "Mais en vrai on s'en fout un b\u00e9b\u00e9 ca ne fume pas, et il faut bien se d\u00e9placer "+
                 "<br>"+

                    + "<br>" 
                    + "<a href ='https://www.planetoscope.com/automobile/311-emissions-de-co2-par-les-voitures-en-europe.html' style='color:black;'>*1</a><br>"
                    + "<a href='http://www.wikistrike.com/article-les-gaz-a-effet-de-serre-changent-bien-la-circulation-atmospherique-118770875.html' style='color:black;'>*2</a><br>"
                    + '<br><input type="button" value="Fermer" onclick="fermer_traffic()"></p>'
}

function fermer_traffic(){
var div = document.getElementById("trafic_text").innerHTML = '<h2>Le traffique routier ?</h2>';

}




function indus(){
  
    var div = document.getElementById("indus_text");
    div.innerHTML = "Les industries nous ont permi de pouvoir produire en masse et donc de mettre des ressources a forte disposition. "
                  + "Permettant ainsi de baisser le prix et d'augmenter l'acc\u00e9sibilit\u00e9. Ainsi jo paysant \u00e0 pu avoir acc\u00e8s au papier. "
                  + "Remi aggriculteur \u00e0 pu avoir l'\u00e9lectricit\u00e9. Gr\u00e2ce aux deux r\u00e9volutions industrielles "
                  + "nous avons pu faire un bond en avant. "
                  + "Mais elles sont propices \u00e0 la polution de l'air et donc \u00e0 trois ou quattres bonds en arri\u00e8re. "
                  + "En effet, afin de faire nos m\u00e9dicaments, du ciment, des engrais... "
                  + "Les industries rejettent du gaz et de la poussi\u00e8re dans l'air. "
                  + "Par exemple, les mintes de charbon et l'\u00e9levage produisent du m\u00e9thane. Les raffineries, les usines \u00e0 papier rejettent "
                  + "du dioxyde de soufre et vont participer au r\u00e9chauffement climatique "
                  + '<br><br><input type="button" value="Fermer" onclick="fermer_indus()">';

}

function fermer_indus(){
var div = document.getElementById("indus_text").innerHTML = '<h2>Les poles industrielles ?</h2>';

}






