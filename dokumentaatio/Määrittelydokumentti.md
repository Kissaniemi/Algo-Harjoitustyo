# Määrittelydokumentti

## Algoritmit ja Tekoäly Harjoitustyö

Tietojenkäsittelytieteen kandiohjelma (TKT)

Harjoitustyön toteutus: Python
Koodissa käytetty kieli: Englanti
Dokumentoinnin kieli: Suomi

Vertaisarviointi mahdollista muille Python-projekteille, joissa käytetty kieli joko Suomi/Englanti


## Harjoitustyön aihe ja vaatimusmäärittely

Harjoitustyön aihe on kurssin valmiista aihe-ehdotuksista valittu MiniMax-algoritmi Connect4/Neljän suora-pelille.
Vaatimusmäärittely perustuu täysin valmiiksi annettuun määrittelyyn.

Ohjelman ydin on minimax-algoritmi joka generoi mahdollisimman hyvän siirron. Algoritmia tehostetaan alpha-beta-karsinnalla ja iteratiivisella syvenemisellä.

Vähimmäisvaatimuksena koodin pitää toimia komentoriviltä, graafinen käyttöliittymä ei oleellista työn ytimen kannalta.

Tarkoitus on pystyä antamaan ohjelmalle pelilaudan tilanne ja kumman pelaajan vuoro, jonka perusteella se generoi seuraavan siirron järkevässä ajassa.

Lukemani perusteella mitä tehottomampi minmax-algoritmi on, sitä kauemmin sillä kestää hakea seuraava siirto, joten vaikka algoritmi toimisi eli hakisi seuraavan siirron,
voi se viedä paljonkin aikaa. Minmax-algoritmi alpha-beta karsinnalla vie pahimmillaan O(b^m) aikaa (eli sama kuin minmax-algoritmi ilman karsintaa) ja ideaalitilanteessa O(b^m/2) aikaa. 
Tässä b on haarautumisen määrä (siirtomahdollisuuksien määrä) ja m syvyys (kuinka monta siirtoa eteenpäin lasketaan). [1]

## Connect4:sta

Kahden pelaajan peli, joka pelataan 7x6 kokoisella pelilaudalla. Pelaajat "tiputtavat" laudalle vuoron perään kiekkoja (kummallakin pelaajalla oma värinsä). Voittaja on se joka saa ensin vaakasuoraan, pystysuoraan tai diagonaaliin 4 kiekkoa peräkkäin. Esimerkiksi ristinollasta poiketen, kiekkoa ei voi pistää mihin kohtaan peliruutua tahansa, vaan sillä on aina maksimissaan 7 mahdollista kohtaa mihin se voi tulla. Joko pelilaudan alareunaan jos sarakkeessa ei ole jo toista kiekkoa tai toisen kiekon päälle. Mahdollisia pelitilanteita kuitenkin n. 4,5 triljoonaa. Connect4 on ratkaistu peli, jos aloittava pelaaja pelaa täydellisesti tämä voittaa aina. [2]

### Viitteet

[1]. JavatPoint, Alpha-Beta-Pruning, [viitattu 13.7.24] Saatavissa: https://www.javatpoint.com/ai-alpha-beta-pruning

[2]. Wikipedia, Connect Four, [viitattu 13.7.24] Saatavissa: https://en.wikipedia.org/wiki/Connect_Four
