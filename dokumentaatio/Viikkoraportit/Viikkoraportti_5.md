# Viikko 5

### Työtunnit: 4h 

Yhä kaksi samaa testiä kuin edllisellä viikolla jotka eivät mene läpi.

Poistettu score_positionista kokonaan diagonaalikatselu, tämän poistolla ei näyttänyt olevaan mitään vaikutusta testituloksiin. \
Minmaxista poistettu drop_piece käyttö ja deepcopy, korvattu check_top:illa ja sitten suoraan boardiin[rivi][sarake] tehtävällä muutoksella (ja muutoksen perumisella). \
drop_piece funktion voisi myös kokonaan korvata connect.py:ssä samalla tavalla. Tai en tiedä onko tällä edes merkitystä kummin tekee, kunhan deepcopyn pitää poissa.

Kokeilin jos testien ongelma ratkeaisi sillä että minmaxiin lisätään argumenttina minimisyvyys jota päivitettäisiin niin että value arvoa muutettaisiin \
jos nykyisen siirron voittoarvo on sama kuin jo olemassa oleva paras value arvo, mutta voitto saavutettaisiin vähemmällä määrällä siirtoja. \
Tällä ei kuitenkaan näyttänyt olevan vaikutusta testien läpimenoon tai sitten se oli implementoitu väärin, joten jätin päivityksestä kokonaan pois.


