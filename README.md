# ML Perusteet -harjoitustehtävät

## Projektin rakenne

Alla oleva hakemistolistaus kuvaa projektin rakennetta. Piilotetut hakemistot ja tiedostot ovat pois listauksesta. Listaus ei ole aakkosjärjestyksessä vaan järjestetty hahmottamista helpottavaan järjestykseen.

```
.
├── ▶tests/                  # Katsoa saa, mutta ÄLÄ KOSKE!
├── ▶data/                   # Datasetit (> 10 MB ei versionhallintaan!)
├── src/
│   ├── ml/                  # Koodi, jota sinun tulee täydentää (IMPLEMENT)
│   │   ├── a.py
│   │   └── ▶utils/
│   ├── playground/          # Versionhallitut harjoitustiedostot.
│   │   └── practice.ipynb
│   └-- sandbox/             # (Optional) Git-hylkiöt
│       └── junk.ipynb
├── README.md
├── pyproject.toml         # Projektin riippuvuudet - ÄLÄ KOSKE KÄSIN!
├── tester.Dockerfile      # Pytest - ÄLÄ KOSKE!
└── docker-compose.yml     # Docker Compose Project
```

## Koodin suorittaminen

Jos/kun haluat ajaa `ml`-paketin koodia lokaalisti, tarvitset `uv`-työkalun, joka luo sinulle virtuaaliympäristön. Kunhan `uv` on asennettu, on kirjaston käyttäminen helppoa.

```bash
# Luo virtuaaliympäristö
uv sync
```

Voit käyttää pakettia vain ja ainoastaan siten, että käytät `uv`-työkalun luomaa virtuaaliympäristöä. Tämä tarkoittaa, että sinun tulee aina käyttää `uv`-komentoa, kun haluat ajaa koodia. Esimerkiksi REPL toimisi näin:

```console
$ uv run python
>>> from ml.vector import Vector
>>> v = Vector(1, 2, 3)
>>> v
Vector(1, 2, 3)
>>> v + 2
Vector(3, 4, 5)
```

Jos tarvitset lisäpaketteja, asenna ne `uv add <paketinnimi>` -komennolla. Muista, että `uv` luo sinulle virtuaaliympäristön, joten pakettien asennus tapahtuu vain siihen ympäristöön.

## Kuinka testata

Koodi on kirjoitettu siten, että osa koodista on paikoillaan `src/ml/`-kansion alaisuudessa, mutta osa koodista tulee kirjoittaa itse. Kyseiset kohdat esitellään oppitunnilla, ja lisäksi tunnistat ne yleisesti koodista iskusanan `IMPLEMENT` läsnäolosta. Mikäli olet epävarma, mitä sinun tulee tehdä, kysy!

Tee siis näin:

```bash
# Käynnistä Allure
# ja navigoi: http://localhost:5050/latest-report
# ja etsi luentoon liittyvät testit (Lesson N: ...)
docker compose up -d

# Tee muutoksia koodiin ja aja testit.
# Toista tarvittaessa.
docker compose start tester

# Lopuksi sulje Allure
docker compose down
```

Muista dokumentoida työsi, kirjoittaa oppimispäiväkirjaa ja tehdä muut tehtävään liittyvät tehtävät. Ethän unohda myöskään versionhallintaa!

## Tarvittavat datasetit

Kurssin harjoituksiin käytetään datasettejä, joista osa tulee ladata itse, osa on saatavilla tämän projektin `data/`-kansiossa.

Alla katalogi `data/`-kansion dataseteistä. Huomaa, että jos lataat datasetteja itse, tulee ne ladata `data/`-kansioon. Muut kansiot kuin alla listatut eivät päädy versionhallintaan (ks. `.gitignore`-tiedosto).

| Datasetti   | Lähdetieto                                                                                  | Lisenssi  |
| ----------- | ------------------------------------------------------------------------------------------- | --------- |
| bike_or_not | Manually generated random data.                                                             | Public    |
| clustering  | Scikit-generated blob data.                                                                 | Public    |
| y_skills    | [Data in Brief Vol 54](https://www.sciencedirect.com/science/article/pii/S2352340924003652) | BY-NC 4.0 |