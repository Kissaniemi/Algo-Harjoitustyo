# Testausdokumentti

## Testien ajo

Testit voidaan ajaa terminaalista ensin menemällä projektin juurikansioon ja ajamalla komento 

```bash
poetry shell
```
ja sen jälkeen komento 

```bash
pytest src
```

Testikattavuuden saa ajamalla komennon

```bash
coverage run --branch -m pytest src
```

ja komennon 
```bash
coverage report -m
```

## Ulkopuolelle jätetyt testit ja testikattavuus

ui_start ja playing_stage funktioita ei ole testattu näiden hoitaessa käyttöliittymää. Myöskään print_board funktiota ei ole yksikkötestattu.

Kun minmax funktion syvyydeksi on asetettu 2, se läpäisee kaikki paitsi yhden testin, kun syvyys on 4 se läpäisee kaikki paitsi 2 ja jos 6 se läpäisee kaikki paitsi kolme testiä. Suuremmilla syvyyksillä koodi toimii hitaasti. Virheet johtuvat puutteellisesta heuristiikasta.

Esimerkki heuristiikan puutteeista on se ettei connect.py:n testeissä evaluate funktio läpäise kahta sille asetettua testiä, jotka ihanne tilanteessa antaisivat eri arvot, eivätkä samaa.

Testikattavuus on laskettu syvyydellä 4.

![alt text](image.png)


## Testien yksityiskohtainen selitys


### connect.py testit


### minmax.py testit




