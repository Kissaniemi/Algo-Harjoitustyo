# Viikko 6

### Työtunnit: 8h

#### Edit 10.12.24:  Voitontarkitusfunktiota paranneltu, nyt kaikki testit menevät läpi


Voittajan tunnistusfunktiossa oli sittenkin vielä ainakin yksi virhe (alaspäin menevien diagonaalien tarkistus meni rivin verran yli laudan), nyt korjattu.

En saanut edellisten viikkojen parin testin läpimenemättömyyttä ratkaistua sellaisenaan, joten siirryin ottamaan iteeratiivisen syvenemisen käyttöön, joka ratkaisikin kyseiset testiongelmat.
Testien läpimenotulokset vaihtelevat nyt sen mukaan mikä asetettu maksimisyvyys tai aikaraja. Mutta esimerkkinä max_depth 43(menee 42 asti, mikä pitäisi olla maksimi mahdollinen syvyys neljänsuora laudalle) ja aikaraja 2, niin läpimenemättä jää välillä 1 testi (ei aina ilmeisesti ehdi ajaa samalla lailla ennen aikakatkaisua). 

Muokkasin yhtä testiä joka testasi että ei tehtäisi häviöön johtavaa liikettä, mutta häviö oli pakosti edessä viiden siirron jälkeen tehtiin mikä siirto tahansa jos vastustaja pelaa ideaalisti.

Pitänee vielä yrittää saada nopeutettua algoritmia että saisi kaikki testit menenmään läpi koko ajan.
