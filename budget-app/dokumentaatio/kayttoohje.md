
# Ohjelman käynnistäminen

Ennen ohjelman käynnistämistä, asenna riippuvuudet komennolla:

```bash
poetry install
```

Käynnistä ohjelma komennolla:

```
poetry run invoke start
```

# Ohjelman käyttö

##Talletuksen lisääminen
Kirjoita tekstikenttään haluamasi summa ja sen kuvaus muodossa "summa kuvaus", esimerkiksi
```bash
1000 gift
```
ja klikkaa "Add deposit"

##Noston lisääminen
Kirjoita tekstikenttään haluamasi summa ja sen kuvaus muodossa "summa kuvaus", esimerkiksi
```bash
10 food
```
ja klikkaa "Add withdrawal"

##Budjetin tarkastelu
Klikkaamalla "View budget" näet senhetkisen budjettisi.

##Kirjanpidon tarkastelu
Klikkaamalla "View ledger" näet senhetkisen kirjanpitosi eli listan kaikista tekemistäsi toimeksiannoista.

##Kirjanpidon alustaminen
Klikkaamalla "Reset ledger" saat poistettua kaikki toimeksiantosi.
