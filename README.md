# ML Perusteet -harjoitustehtävät

## Projektin rakenne

Alla oleva hakemistolistaus kuvaa projektin rakennetta. Piilotetut hakemistot ja tiedostot ovat pois listauksesta. Listaus ei ole aakkosjärjestyksessä vaan järjestetty hahmottamista helpottavaan järjestykseen.

```
.
├── ▶test/                 # pytest testien määrittelyt - ÄLÄ KOSKE!
├── ▶data/                 # Säilö ladatuille dataseteille
├── src/
│   ├── ▶vastaukset/         # Opettajan vastaukset. Älä katso :D
│   ├── ▶scripts/            # Datasettien latausskriptit ja muut apuskriptit 
│   ├── ml/                 
│   │   ├── a.py
│   │   ├── b.py
│   │   ├── c.py
│   │   └── ▶a_module/
│   ├── sandbox/            # Git-hylätyt Notebook-kokeilut
│   │   ├── temp.ipynb
│   │   └── removeme.ipynb
│   └-- playground/         # Git-pidetyt Notebook-kokeilut
│       ├── lorem.ipynb
│       └── ipsum.ipynb
├── ml/
│   ├── some.py
│   ├── code.py
│   ├── here.py
│   ├── ▶modularize/
│   ├── ▶code/
│   ├── ▶into/
│   └── directories/
│      └── helpers.py
├── README.md
├── requirements.txt       # Python-paketit joita sinä tarvitset
├── requirements-test.txt  # Pytest - ÄLÄ KOSKE!
├── pytest.ini             # Pytest - ÄLÄ KOSKE!
├── tester.Dockerfile      # Pytest - ÄLÄ KOSKE!
└── docker-compose.yml     # Docker Compose Project
```

## Koodin suorittaminen

Tarvitset virtuaaliympäristön. Suosi Pythonin versiota 3.11.x.

```bash
# Luo virtuaaliympäristö
python -m venv --copies .venv

# Asenna tarvittavat paketit
pip install -r requirements.txt

# Asenna tämä paketti (ml/) paikallisesti
# -e tarkoittaa "editable", jolloin koodiin tehdyt muutokset näkyvät heti
#    ilman uutta installia.
pip install -e .
```

Paketti asennetaan, jotta se on käytettävissä mistä tahansa kansiosta. Tämä on hyödyllistä esimerkiksi `src/sandbox` -kansion Jupyter Notebook -tiedostojen kanssa. Voit käyttää `import ml` -komentoa missä tahansa kansiosta.

## Kuinka testata

Koodi on kirjoitettu siten, että osa koodista on paikoillaan `src/ml/`-kansion alaisuudessa, mutta osa koodista tulee kirjoittaa itse. Testit on kirjoitettu siten, että ne testaavat koodin tärkeimmän toiminnallisuuden. Siispä tyypillisen luennon jälkeen tehtäväsi on:

* Lue tehtävänanto (Moodle/Youtube/Muu)
* Käynnistä Allure (`docker compose up -d`)
    * Avaa selaimessa [Allure UI (localhost:5050)](http://localhost:5050/latest-report)
    * Etsi luentoon liittyvät testit
        * Suites => `Lesson n: ...`
    * Testit ovat sinulle TODO-lista
* Tee seuraavaa Game Loop -hengessä:
    * Lue testitulos
    * Muokkaa tai kirjoita koodia
        * Hox! Useimmissa skripteissä tunnistat muokattavat kohdat kommentista: `# IMPLEMENT ...`
    * Aja testit (`docker compose start tester`)
    * Toista kunnes kaikki testit menevät läpi
* Lopuksi sulje raportointipalvelin (`docker compose down`)

Muista dokumentoida työsi, kirjoittaa oppimispäiväkirjaa ja tehdä muut tehtävään liittyvät tehtävät. Ethän unohda myöskään versionhallintaa!

## Tarvittavat datasetit

Kurssin harjoituksiin käytetään datasettejä, jotka voi ladata joko käsin tai ajamalla `scripts/`-kansion `download_datasets.py`-tiedosto. Datasetit ladataan `./datasets/`-kansioon.

Alla katalogi näistä:

| Datasetti | Lähdetieto          | Lisenssi  |
| --------- | ------------------- | --------- |
| Set name  | Link to description | BY-NC 4.0 |