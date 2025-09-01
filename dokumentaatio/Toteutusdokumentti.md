# Koodin toteutus 

## Lähteet

Projektin tekemiseen ei ole käytetty laajoja kielimalleja. Minmax funktion soveltamiseen on käytetty wikipedian minmax algoritmia https://en.wikipedia.org/wiki/Minimax, ja sen sekä connect.py tiedoston funktioissa on myös käytetty apuna koodia https://roboticsproject.readthedocs.io/en/latest/ConnectFourAlgorithm.html. 

## Funktioiden aika- ja tilavaativuudet

Algoritmi ehtii keskimäärin syvyysteen 9 aikakatkaisun ollessa 3 sekuntia. Jos heuristiikan vaihtaa ns. nollaheuristiikaksi saavutetaan syvyys 13.
Jokaisella syvyydellä pelitilanne haarautuu maksimissaan seitsemään eri haaraan, jolloin esimerkiksi syvyydellä kuusi eri pelitilanteiden määrä voi olla maksimissaan 7⁶= 117 649. Syvyydellä 9 eri haaroja on 40 353 607 ja syvyydellä 13 haaroja on 96 889 010 407.


### minmax.py
Minmax algoritmin pitäisi toimia alussa määritellyn mukaisesti pahimmillaan O(b^m) ajassa ja ideaalitilanteessa O(b^m/2) ajassa, missä b merkitsee mahdollisten siirtojen määrää ja m syvyyttä. Mahdollisia siirtoja on maksimissaan 7 ja maksimisyvyyden rajaksi on asetettu 42, mutta tähän syvyyteen ei kuitenkaan koskaan päästä, koska ohjelma ei ole tarpeeksi tehokas ja iteratiivinen syveneminen on aikarajoitettu. Tämän lisäksi minmax algoritmi käyttää kolmea connect.py:n funktiota: possible_columns, score_position, drop_piece.
Näistä possible_columns vie aikaa O(n), jossa n arvo on pelilaudan rivien määrä 6, eli O(6). Drop_piece funktion aikavaativuus on myös O(n), jossa n on sarakkeitten määrä 7, eli O(7).
Score_position aikavaativuus on score vertical silmukan takia O(7^2). Funktio kutsuu ulommassa silmukassa evaluation funktiota, jonka aikavaativuus on O(n), missä n arvo vaihtelee 4-7 välillä, eli O(7). 

### connect.py
Ui_start, playing_stage funktion aikavaativuudet jätetty huomiotta. 
Drop_piece funktion aikavaativuus on O(7), kuten myös check_full funktion. Ne käyvät pelilaudan sarakkeet läpi silmukassa kerran.
print_board funktion aikavaativuus on O(7²), koska sisäkkäisessä silmukassa käydään jokainen pelilauta listan rivi ja sarake kohta läpi ja ne lisätään pakkaan. 
Check_top funktion aikavaativuus on O(6), funktio käy pelilaudan yhden sarakkeen läpi.
Check_winner funktio kutsuu seitsemää muuta funktiota, check_winner_vertical, -horizontal_left, -horizontal_right, -up_right, -up_left, -down_right, -down_left 
joiden aikavaativuudet ovat O(6) tai O(7), koska ne käyvät yhtä pelilaudan vaaka-, pysty- tai diagonaalisuoraa läpi.
Score_position aikavaativuus on score vertical silmukan takia O(7^2). Funktio kutsuu ulommassa silmukassa evaluation funktiota, jonka aikavaativuus on O(7). 


## Projektin puutteet

Projektissa on edelleen parannettavaa. Koodissa olisi vielä optimoitavaa ja minmax algoritmi ei toimi kaikissa tilanteissa parhaalla mahdollisella tavalla. Testeissä ei tätä näy, mutta kun AI saa aloittaa vuoronsa toisena, se pelaa huonommin kuin jos se pääsee aloittamaan ensimmäisenä. Algoritmin heuristiikkaa voisi nopeuttaa ottamalla käyttöön bittikartat ja tarkentaa arvoja ottamalla huomioon myös diagonaalit. Välimuistia voisi parantaa ottamalla käyttöön alpha ja beta ylä- ja ala-arvot ja karsinta myös siinä kohtaa.


## Koodin funktioiden ja toiminnan yksityiskohtainen selitys

### app.py
Koodi ajetaan ap.py tiedoston kautta, joka kutsuu connect_py:n funktiota ui_start.

### connect.py

#### menu_ui
Pääkäyttöliittymä, menu.
ui_start funktio alustaa ensin tyhjän pelipohja/lautamuuttujan "board" (mahdollista vaihtaa tilalle toinen pelipohja/aloitustilanne. Huom. Täyden aloituslaudan antaminen johtaa virheeseen).
Ohjelma ilmoittaa ensin että ohjelmasta pääsee pois kirjoittamalla "exit" syöteriville.
Seuraavaksi koodi esittää syötekysymyksen haluatko pelata tekoälyä vastaan vai ei. Syötteenä hyväksytään "yes" ja "no", 
muuten syötettä ei hyväksytä ja menu_ui funktiota kutsutaan uudestaan alusta. Jos syöte on "yes", lisäsyötteenä pyydetään antamaan joko "1" tai "2", muutoin kusutaan menu_ui funktiota alusta. Jos syöte on "1", kutsutaan playing_stage_ui funktiota argumenteilla (1, board, True, False). 
Jos syöte on "2", kutsutaan samaista funktiota argumenteilla (2, board, True, False). 
Jos aiempi syöte oli "no", kutsutaan playing_stage_ui funktiota argumenteilla (1, board). Argumenteista lisää playing_stage_ui funktion selitteissä.

#### playing_stage_ui
Peliosuuden käyttöliittymä.
Argumenteissa (player, board, ai=False, ai_turn=False) luku 1 tai 2 erottaa pelaajat toisistaan. AI on aina pelaaja 2. 
Toisena annettu syöte "board" on pelilauta, joka kulkee mukana listana listoja. Seuraavaksi on asetettu ai=False ja ai_turn=False, 
jos näitä ei ole erikseen funktiota kutsuttaessa muutettu. Näillä pidetään kirjaa siitä, onko pelivastustajana AI ja onko tällä hetkellä AI:n vuoro.

Jos ai_turn == False (Tämä osuus ajetaan myös silloin kun ei pelata AI:ta vastaan, eli ai=False), pyydetään syötteenä sarake, johon pelimerkki halutaan tiputtaa. Hyväksyttyjä merkkejä ovat numerot välillä 1-7, 
muuten playing_stage funktiota kutsutaan alusta alkuperäisillä argumenteillä. Syöteestä tarkistetaan ensin ettei se ole tyhjä ja että se ei ole numero. 
Sen jälkeen tarkistetaan että syöte on välillä 1-7.
Hyväksytyn syötteen jälkeen haetaan muuttujalle "new_board" arvo drop_piece funktiolla argumenteilla (player, board, int(column)-1).
Aiemmasta syötteestä siis miinustetaan yksi, koska pelaajalle laudalla sarakkeet on merkitty luvuin 1-7, mutta listana käsiteltäessä sarakkeet ovat välillä 0-6.
Nyt jos "new_board" muuttujan arvo on False, eli haluttu siirto ei onnistunut (sarake täynnä), kutsutaan playing_stage_ui funktiota taas alusta.
Muutoin "new_board" sai arvokseen uuden muutetun pelilaudan ja se printataan print_board funktiolla. 
Tämän jälkeen tarkistetaan check_winner funktiolla oliko viimeksi tehty siirto voittoon johtava liike.
Funktiolle on annetaan argumentit (new_board, int(column)-1, player), eli uusi pelilauta, aiemmin syöteenä saatu siirto ja pelaaja kenen vuoro on kyseessä.
Jos voittaja löytyy, tieto tulostetaan näkyviin ja menu_ui funktiota kutsutaan alusta.
Seuraavaksi tarkistetaan ettei pelilauta ole täynnä check_full funktiolla jolle annetaan argumenttina uusi lauta. Jos lauta on täynnä, kutsutaan menu_ui funktiota.

Nyt jos ai=False kutsutaan seuraavaksi sitä pelaajaa jonka vuoro ei nyt ollut playing_stage_ui funktiolla, vastakkaisen pelaajan numero ja uusi pelilauta syötteenä. 
Muutoin ai=True, ja koska nyt käytiin ai_turn=False vuoro, niin kutsutaan playing_stage_ui funktiota argumenteilla (2, new_board, True, True).

Muutoin jos kyseessä on ai_turn=True, haetaan best_move muuttujalle arvo kutsumalla iterative_deepening funktiota minmax.py:stä. Funktiolle annetaan argumentteina (board, 2, -1000000, 1000000),
eli tämän hetkinen pelilauta, pelaajan numero 2, sekä -1000000 ja 1000000. 

Uusi pelilauta "new_board" haetaan drop_piece funktiolla syötteellä (2, board, best_move), eli pelaajan numerolla, edellisellä laudalla ja minmax funktiolla saadulla parhaalla siirrolla.
Uuden pelilaudan oikeellisuutta ei tässä vaiheessa tarkisteta, koska siirron oikeellisuus tarkistetaan minmax funktiossa.
"new_board" tulostetaan näkyviin ja tarkistetaan check_winner funktiolla ja check_full funktiolla, oliko viimeisin siirto voittosiirto tai onko pelilauta täynnä.
Jos jompikumpi on totta, kutsutaan menu_ui funktiota alusta. 
Muutoin siirretään vuoro ei manuaaliselle pelaajalle argumenteilla (1, new_board, True).

#### drop_piece
Tarkistaa onko annettu siirto mahdollinen ja palauttaa uuden pelilaudan johon siirto on tehty.
Funktio ottaa argumenttina (player, board, column), missä ensimmäisenä on pelaajan numero, seuraavana pelilauta listana ja sarake mitä halutaan muuttaa.
Funktio käy annetun pelilaudan läpi käänteisessä järjestyksessä (alimmasta rivilistasta ylimpään rivilistaan). Funktio tarkistaa jokaisen rivin saraketta vastaavan kohdan ja heti kun vastaan tulee arvo 0, kohta laudasta muutetaan pelaajan numeroksi ja palautetaan kopio laudasta eli uusi lauta.
Jos nollaa ei tule vastaan, ei sarake ole vapaa eikä siirto siihen mahdollinen joten palautetaan False.

#### possible_columns
Generoi ja palauttaa listan sarakkeista joihin siirron tekeminen on mahdollista.
Funktio saa argumenttina pelaajan numeron ja pelilaudan ja käy läpi silmukassa laudan joka sarakkeen ja testaa onko sarakkeeseen siirron tekeminen mahdollista drop_piece funktiolla. Order pakkaan on valmiiksi laitettu siirrot "parhaaseen" järjestykseen. Jos siirron tekeminen mahdollista, lisätään sarakepakkaan sarakkeen numeron. Palauttaa lopuksi pakan sarakkeista.

#### check_full
Tarkistaa onko pelilauta täynnä.
Funktio saa argumenttina pelilaudan listana, josta tarkistetaan vain ylin rivi(lista), koska pelissä lauta täyttyy alhaalta ylös, jolloin kaikkien rivien tarkistus ei ole tarpeen. Heti jos vastaan tulee 0, palautetaan False (lauta ei ole täynnä). Jos rivi käydään läpi niin ettei yhtään nollaa tule vastaan, on lauta täynnä ja palautetaan True. 

#### print_board
Tulostaa pelilaudan näkyville.
Funktio saa argumenttina pelilaudan listana ja se käy läpi listan jokaisen rivin ja rivin jokaisen slotin. Silmukassa alustetaan ensin print_row lista, johon lisätään vasen "seinä", tämän jälkeen ensimmäisen rivin slotit käydään läpi ja jos vastaan tulee 1, lisätään print_row listaan "○". Jos vastaan tulee 2, lisätään listaan "●". Muutoin jos slotissa on muuta (0), lisätään listaan tyhjä kohta. Jokaisen lisäyksen perään lisätään myös oikea "seinä"
Jokaisen rivin läpikäymisen jälkeen koko print_row lista yhdistetään tulostettavaan muotoon ja tulostetaan yhdessä rivierotusta ennen. Silmukka alustaa tämän jälkeen uuden print_row listan ja käy tätä läpi kunnes koko pelilauta on käyty läpi ja tulostettu. Lopuksi tulostetaan vielä sarakeluvut.

#### check_top
Palauttaa annetun sarakkeen ylimmän rivin.
Funktio saa argumenttina pelilaudan ja sarakkeen joka tarkistetaan. Rivilasku aloitetaan -6:sta (pelilaudan ylin rivi) ja funktio käy silmukassa pelilaudan annetun sarakkeen läpi rivi kerrallaan. Heti kun vastaan tulee luku joka ei ole 0, palautetaan rivilasku. Tämän on annetun sarakkeen ylin rivi. Rivilaskua kasvatetaan joka kierroksella. Jos koko sarake käydään läpi niin että vastaan tulee pelkkiä nollia, palautetaan 0 (sarakkeessa ei siis yhtään pelimerkkejä)


#### check_winner
Tarkistaa oliko viimeksi tehty siirto voittosiirto.
Funktio saa argumenttina pelilaudan, sarakkeen ja pelaajan numeron. 
Hakee row muuttujalle arvon eli sarakkeen ylimmän rivin check_top funktiolla.
Funktio kutsuu sitten pystysuoran, vaakasuoran ja kahden eri suuntaisen diagonaalin voittorivin tarkistusfunktiota. Jos yksikin funktioista palauttaa True, palauttaa myös funktio True.

#### check_winner_vertical
Tarkistaa löytyykö neljän suoraa pystysuorassa ylhäältä alaspäin.
Funktio saa argumenttina pelilaudan, sarakkeen, rivin ja pelaajan numeron. 
Alustetaan laskuri "count" arvoksi 1.
Asetetaan r arvoksi nykyinen rivi+alempi rivi (liikutaan alaspäin).
Asetetaan c arvoksi tämän hetkinen sarake (liikutaan koko ajan samassa sarakkeessa pystysuunnassa).
Sitten niin kauan kun pelilaudan sarakkeen rivillä on sama pelaajamerkki, lisätään "count" muuttujaan 1 ja r muuttujaan 1 (liikutaan riviä alemmas). 
Jos laskuri pääsee neljään, neljän suora löytynyt ja funktio palauttaa True, muuten funktio palauttaa False.


#### check_winner_horizontal
Funktio tarkistaa löytyykö neljän suoraa vaakasuorassa vasemmalta oikealla ja oikealta vasemmalle.
Funktio ottaa argumentteina pelilaudan, sarakkeen, rivin ja pelaajan numeron.
Funktio tarkistaa ensin viimeksi tehdystä siirrosta vasemmalle päin ja sitten oikealle päin.
Funktioissa alustetaan ensin laskuri arvoksi 1 ja r muuttujan arvoksi rivin arvo (liikutaan koko ajan samalla rivillä), sekä c muutujan arvoksi sarake-1 tai sarake+1 riippuen kumpaan suuntaan ollaan tarkistamassa.

Niin kauan kun c arvo on vähintään 0 ja vastaan tulee laudalla samaa pelimerkkiä, nostetaan laskuria yhdellä ja vähennetään c arvoa yhdellä (liikutaan sarakkeissa vasemmalle). Tämän jälkeen jos laskurin arvo on vähintään 4, palautetaan True.
Tämän jälkeen niin kauan kuin c arvo on enintään 6 ja vastaan tulee laudalla samaa pelimerkkiä, nostetaan laskuria yhdellä ja kasvatetaan c arvoa yhdellä (liikutaan sarakkeissa oikealle). Tämän jälkeen jos laskurin arvo on vähintään 4, palautetaan True ja muuten False.


#### check_winner_diagonal_1 ja check_winner_diagonal_2
Funktiot tarkistavat löytyykö neljän suoraa vinottain liikuttaessa viimeisimmästä siirrosta oikealle ylös, oikealle alas, vasemmalle alas ja vasemmalle ylös.
Funktiot ottavat argumenttina pelilaudan, sarakkeen, rivin ja pelaajan numeron. Laskuri "count" alustetaan arvoltaan yhdeksi ja r arvoksi tulee nykyinen rivi+1 tai rivi-1 ja d arvoksi nykyinen sarake+1 tai sarake-1 riippuen kumpi funktio ja kumpi suunta on kyseessä (liikutaanko diagonaalissa oikealle vai vasemmalle). 
Sen jälkeen niin kauan kuin c ja r arvot ovat sallituissa rajoissa (pelilaudan sisäpuolella) ja vastaan tulee samaa pelimerkkiä, liikutaan pelilaudalla diagonaalissa oikealle tai vasemmalle riippuen kumpi funktio ja vaihe on kyseessä. Jos vastaan on tullut 4 samaa pelimerkkiä palautetaan True, muuten False.


#### score_position
Pelilaudan arvon saamiseen käytettävä funktio. Ottaa argumenttina pelilaudan.
Funktio jakaa pelilaudan rivejä ja sarakkeita osiin ja antaa ne evaluate funktiolle pisteytettäväksi.
Funktio alustaa muuttujan score arvoksi 0. 

Tämän jälkeen jaetaan pelilauta pystysuoriin ja vaakasuoriin riveihin ja kasvatetaan scorea evaluate funktion palauttamalla arvolla. Ensin silmukassa annetaan pelilaudan rivit evaluate funktiolle pisteytettäväksi ja saatu arvo lisätään score muuttujaan.
Seuraavaksi silmukassa luodaan pystysuora rivilista johon lisätään pelilaudan sarakkeita riveiksi ja annetaan evaluate funktiolle pisteytettäväksi. Saadut arvot lisätään score muuttujaan. Funktio palauttaa lopulta score arvon.


#### evaluate
Ottaa argumenttina osion ja laskee osiolle arvon.
Etsii mahdollisia pareja ja kolmen rivejä annetusta osiosta. Laskee plussaa pelaajan 2 merkeistä ja miinusta pelaajan 1 merkeistä. Minmaxin puolella tätä muutetaan sen perusteella ollaanko maximoimassa vai minimoimassa.


### minmax.py

#### iterative_deepening
Funktio ottaa argumentteina pelilaudan, pelaajan numeron sekä alpha- ja beta-arvon.
Funktiossa asetetaan ensin aloitusaika start_time, aikaraja time_limit 2 sekuntia ja maksimisyvyys depth_limit rajaksi 43 (tähän syvyyteen ei tämän hetkisillä optimoinneilla koskaan päästä, mutta hyvä olla jokin maksimiraja).
Sen jälkeen silmukassa kutsutaan syvyydestä yksi maksimiisyvyyteen asti minmax_funktiota ja parasta siirtoa ja sen arvoa.
Jos minmax funktion kutsunnan jälkeen aikaraja on ylittynyt (aikaraja siis yleensä menee yli kahden sekunnin, koska aikaraja tarkistusta ei tehdä minmax funktion sisällä vaan sen kutsunnan jälkeen) tai siirron arvo on 10000 (voittoarvo), pysäytetään silmukka.
Tämä jälkeen tulostetaan näkyviin tietoja siitä kauan aikaa suunnilleen siirron tekemiseen meni, mihin syvyyteen lopetettiin ja mikä siirto ja sen arvo on.

#### minmax
Funktio ottaa argumentteina pelilaudan, pelaajan numeron, edellisen pelaajan siirron, alpha- ja beta-arvon, sekä maksimisyvyyden rajan ja tämän hetkisen syvyyden ja välimuistin.
Funktio tarkistaa ensin löytyykö kyseinen pelitilanne välimuistista ja jos löytyy, siirtää silloisen parhaan siirron siirtolistassa ensimmäiseksi.
Funkti otarkistaa sitten, ettei edellisen pelaajan siirto johtanut voittoon tai häviöön ja jos johti niin palautetaan sen mukainen arvo.

Tämän jälkeen funktio hakee mahdolliset siirrot possible_columns funktiolla.
Funktio tarkistaa sitten että tämän hetkinen syvyys ei ole maksimisyvyys, ja että mahdollisia siirtoja on eli sarakelista ei ole tyhjä. Muutoin se hakee score_position funktiolla tämän hetkiselle pelitilanteelle arvon ja palauttaa sen edellisen siirron kanssa.

Jos vuorossa on # Max player, asetetaan "value" arvoksi -100000 ja best_move arvoksi None.
Sen jälkeen funktio käy läpi mahdolliset siirrot ja muuttaa suoraan siirron kohtaan pelilaudalla pelaajan merkin.
Sitten funktio hakee new_value muuttujalle rekursiivisesti minmax funktiolla arvon. Tämän jälkeen aiemmin tehty siirto perutaan/nollataan laudalla.
Jos saatu arvo on isompi kuin nykyinen "value", niin "new_value" asetetaan "value" muuttujan uudeksi arvoksi. Samalla best_move arvoksi asetetaan sarake johon siirto oli tehty.
Tämän lisäksi, alpha arvo on maksimi alpha arvosta (aluksi -inf) ja "value" arvosta. Jos tämä arvo on isompi kuin beta muuttujan arvo, lopetetaan siirtojen läpikäynti tähän. Lopuksi palautetaan paras siirto ja sen arvo.

Jos kyseessä on # Min player, asetetaan  "value" arvoksi 100000 ja best_move arvoksi None.
Sen jälkeen funktio käy läpi mahdolliset siirrot ja muuttaa suoraan siirron kohtaan pelilaudalla pelaajan merkin.
Sitten funktio hakee new_value muuttujalle rekursiivisesti minmax funktiolla arvon. Tämän jälkeen aiemmin tehty siirto perutaan/nollataan laudalla. Jos saatu arvo on pienempi kuin nykyinen "value", niin "new_value" asetetaan "value" muuttujan uudeksi arvoksi. Samalla best_move arvoksi asetetaan sarake johon siirto oli tehty.
Tämän lisäksi, beta arvo on minimi beta arvosta (aluksi inf) ja "value" arvosta. Jos tämä arvo on pienempi kuin alpha muuttujan arvo, lopetetaan siirtojen läpikäynti tähän. Lopuksi palautetaan paras siirto ja sen arvo.
