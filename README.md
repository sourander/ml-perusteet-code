# ML Perusteet -harjoitustehtävät

## Projektin rakenne

Alla oleva hakemistolistaus kuvaa projektin rakennetta. Piilotetut hakemistot ja tiedostot ovat pois listauksesta. Listaus ei ole aakkosjärjestyksessä vaan järjestetty hahmottamista helpottavaan järjestykseen.

```
.
├── ▶allure-results/       # pytest kirjoittaa tänne raportit
├── ▶allure-reports/       # Allure API luo raportit tänne
├── ▶test/                 # pytest testien määrittelyt - ÄLÄ KOSKE!
├── src/
│   ├── ▶vastaukset/         # Opettajan vastaukset. Älä katso :D
│   ├── ml/                 
│   │   ├── a.py
│   │   ├── b.py
│   │   ├── c.py
│   │   └── ▶a_module/
│   └-- playground/
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
├── requirements-test.txt  # Pytestin tarvitsemat paketit
├── tester.Dockerfile      # Dockerfile pytestiä varten
└── docker-compose.yml     # Docker-compose tiedosto (tester ja Allure API)
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
    * Aja testit (`docker compose up tester`)
    * Toista kunnes kaikki testit menevät läpi
* Lopuksi sulje raportointipalvelin (`docker compose down`)

Muista myös dokumentoida työsi, kirjoittaa oppimispäiväkirjaa ja tehdä muut tehtävään liittyvät tehtävät. Ethän unohda myöskään versionhallintaa!

Huomaathan, että testitulokset (allure-reports/ ja allure-results/) eivät ole versionhallinnassa. Mikäli haluat ne sinne, muokkaa .gitignore-tiedostoa.