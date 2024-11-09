# Viikkoraportti 2

### Työtunnit 5h

- Korjattu minmax, nyt voittotarkistus joka kerta. Lisäksi nyt pidetään koko ajan yllä viimeisimmän siirron sarakkeen tietoa. 
(check_winner funktio joka tarvitsee rivitietoa, saa sen check_top funktiolla).
- Muutettu possible_colums funktiosta column_order lista minmax.py:hyn (ainoa paikka missä sitä käytetään).
- Vaihdettu kaikki inf arvot sopiviksi arvoiksi (alpha/beta kutsutaan aluksi -1000000/1000000, value alkuarvo -100000/100000 
ja voitto/häviö palautusarvoksi asetettu -10000/10000).

- Muokattu testejä niin, että ne pystytään ajamaan (10 testiä ei mene läpi syvyydellä 6,
näyttäisi että ongelma score_position/evaluate funktioissa, selkeät voittoliikkeet jää nyt tekemättä).
- Evaluate funktiosta poistettu turha voiton tarkistus.

Dokumentaatiosta ei vielä korjattu funktioiden selityksiä ajan tasalle 
(todennäköisesti toiminta vielä muuttuu osassa funktioita, niin turhaa työtä päivittää vielä).
