# Vaatimusmäärittely

## Sovelluksen tarkoitus

Käyttäjä voi lisätä sovellukseen tulonsa ja menonsa, ja näin määrittää itselleen kuukausittaisen budjetin. 


## Perusversio

### Ennen kirjautumista

- Käyttäjä voi luoda järjestelmään käyttäjätunnuksen
  - Käyttäjätunnuksen tulee olla uniikki ja vähintään 3 merkkiä pitkä
- Käyttäjä voi kirjautua järjestelmään
  - Kirjautuminen tapahtuu syöttämällä käyttäjätunnus ja salasana sovellukseen
  - Jos käyttäjänimeä ei löydy tai salasana on väärin, tulee virheilmoitus

### Kirjautumisen jälkeen

- Käyttäjä näkee tulonsa, menonsa ja kuukausibudjettinsa
- Käyttäjä voi lisätä uusia tuloja tai menoja
  - Negatiivisesta syötteestä virheilmoitus
  - Ilmoitus, mikäli käyttäjän menot menevät yli budjetin
- Käyttäjä voi kirjautua ulos

## Jatkomahdollisuuksia

Perusversion jälkeen järjestelmää täydennetään ajan salliessa esim. seuraavilla toiminnallisuuksilla:

- Olemassa olevien tulojen tai menojen poistaminen tai muokkaus
- Kategoriointi
  - Käyttäjä voi luoda menoilleen kategorioita ja nähdä esimerkiksi minkälaisiin asioihin rahaa kuluu eniten
- Jonkinlainen säästötavoite
