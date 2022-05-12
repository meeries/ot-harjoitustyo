# Budget-App
Sovelluksen avulla käyttäjä voi nähdä esimerkiksi kuukauden budjettinsa lisäämällä sovellukseen tulonsa ja menonsa. Sovellus laskee käyttäjälle budjetin sekä pitää kirjaa lisätyistä ja poistetuista rahoista.

## Dokumentaatio

- [Vaatimusmäärittely](https://github.com/meeries/ot-harjoitustyo/blob/master/budget-app/dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](https://github.com/meeries/ot-harjoitustyo/blob/master/budget-app/dokumentaatio/ty%C3%B6aikakirjanpito.md)
- [Changelog](https://github.com/meeries/ot-harjoitustyo/blob/master/budget-app/dokumentaatio/changelog.md)
- [Käyttöohje](https://github.com/meeries/ot-harjoitustyo/blob/master/budget-app/dokumentaatio/kayttoohje.md)
- [Testausdokumentti](https://github.com/meeries/ot-harjoitustyo/blob/master/budget-app/dokumentaatio/testausdokumentti.md)
- [Arkkitehtuurikuvaus](https://github.com/meeries/ot-harjoitustyo/blob/master/budget-app/dokumentaatio/arkkitehtuuri.md)

## Release
[Loppupalautus](https://github.com/meeries/ot-harjoitustyo/releases/tag/loppupalautus)

## Asennus
1. Komento:
```bash
poetry install
```
asentaa riippuvuudet

2. Komento:
```bash
poetry run invoke start
```
käynnistää sovelluksen

## Komentirivitoiminnot
Komento:
```bash
poetry run invoke start
```
suorittaa ohjelman

Komento:
```bash
poetry run invoke test
```
suorittaa testit

Komento:
```bash
poetry run invoke coverage-report
```
luo testikattavuusraportin

Komento:

```bash
poetry run invoke lint
```
suorittaa pylint tarkastukset
