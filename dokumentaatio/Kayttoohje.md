
## Käyttöohje

Koodin käyttöliittymä on merkkipohjainen. Pelaaminen on mahdollista toista manuaalista vastustajaa vastaan tai tekoälyä vastaan. Kahden tekoälyn välistä pelaamista ei ole mahdollistettu. 

### Koodin riippuvuuksien ajaminen:

Kun koodin repositorio on ladattu, aja koodin juurihakemistossa komento

```bash
poetry shell
```
Lataa projektin riippuvuudet komennolla

```bash
poetry install 
```

### Koodin käynnistys

Aja komento 

```bash
python3 src/app.py
```

Peli alkaa valinnalla haluatko pelata AI:ta vastaan vai ei. Hyväksyttäviä vastauksia ovat "yes" tai "no", sekä missä tahansa vaiheessa peliä kohdissa joissa kysytään syötettä, voit poistua ohjelmasta kirjoittamalla "exit".
Muut syötteet johtavat kysymyksen toistumiseen, kunnes hyväksytty vastaus on saatu. Vastaus pitää kirjoittaa ilman isoja kirjaimia.

Kun on vastaus on "no", peli alkaa pelaajan 1 vuorosta ja pelipohja tulostuu. Valittavissa on seitsemän eri saraketta johon pelimerkin voi tiputtaa.
Sarakkeiden numerot on kirjoitettu pelilautaan näkyviin. Syöte hyväksyy vain numerot välillä 1-7, muut syötteet johtavat sarakekysymyksen toistumiseen.
Kun hyväksytty syöte on annettu, vuoro siirtyy pelaajalle 2. Sama sarakekysymys toistuu ja vuorovaihtuu samalla lailla. 
Peli jatkuu kunnes toinen pelaajista on saanut 4 pelimerkkiä riviin tai kunnes pelipohja on täysi. 
Tämän jälkeen koodi alkaa alusta kysymällä haluatko pelata tekoälyä vastaan vai et.

Jos syöte on "yes", saat kysymyksen haluatko aloittaa ensimmäisenä vai toisena vuorosi. 
Hyväksyttäviä vastauksia ovat "1" tai "2", muut syötteet toistavat alun kysymyksen haluatko pelata AI:ta vastaan.
Jos vastaus on "1", aloitat vuorosi ensin, jos "2" niin AI aloittaa. AI aloitta vuoronsa automaattisesti ja vuorosi jatkuu heti, kun AI on tehnyt siirron.
Peli jatkuu kunnes jompikumpi on voittanut tai pelipohja on täynnä. Tämän jälkeen koodi alkaa taas alusta kysymyksellä jaluatko pelata AI:ta vastaan.

Pelaajan 1 pelimerkkiä pelipohjalla vastaa "○" ja pelaajan 2 ja tekoälyn pelimerkkiä "●".

