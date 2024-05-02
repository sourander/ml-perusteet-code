# ML Perusteet -harjoitustehtävät

## Projektin rakenne

Alla oleva hakemistolistaus kuvaa projektin rakennetta. Piilotetut hakemistot ja tiedostot ovat pois listauksesta. Listaus ei ole aakkosjärjestyksessä vaan järjestetty hahmottamista helpottavaan järjestykseen.

```
.
├── ▶tests/                  # Katsoa saa, mutta ÄLÄ KOSKE!
├── ▶data/                   # Datasetit (> 10 MB ei versionhallintaan!)
├── src/
│   ├── ▶scripts/            # Datasettien latausskriptit ja muut apuskriptit 
│   ├── ml/                 
│   │   ├── a.py
│   │   └── ▶utils/
│   ├── playground/          # (Optional) Git-hylkiöt
│   │   └── practice.ipynb
│   └-- sandbox/             # Git-pidetyt Jupyter Notebook -tiedostot
│       └── junk.ipynb
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
python -m venv .venv

# Asenna tarvittavat paketit
pip install -r requirements.txt

# Asenna tämä paketti (ml/) paikallisesti
# -e tarkoittaa "editable", jolloin koodiin tehdyt muutokset näkyvät heti
#    ilman uutta installia.
pip install -e .
```

Paketti asennetaan, jotta se on käytettävissä mistä tahansa kansiosta. Tämä on hyödyllistä esimerkiksi `src/sandbox` -kansion Jupyter Notebook -tiedostojen kanssa. Voit käyttää `import ml` -komentoa missä tahansa kansiosta.

Huomaa, että saat lisätä tarvitsemiasi paketteja `requirements.txt`-tiedostoon. Aja tällöin `pip install -r requirements.txt` uudelleen. Älä kuitenkaan lisää mitään `requirements-test.txt`-tiedostoon - testien tulisi pärjätä ilman numpyä, scikit learnia ja muita kirjastoja, sillä tarkoituksena on luoda Python-natiiveja ratkaisija *"from scratch"*.

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

Kurssin harjoituksiin käytetään datasettejä, jotka voi ladata joko käsin tai ajamalla `scripts/`-kansion `download_datasets.py`-tiedosto. Datasetit ladataan `./datasets/`-kansioon.

Alla katalogi näistä:

| Datasetti | Lähdetieto          | Lisenssi  |
| --------- | ------------------- | --------- |
| Set name  | Link to description | BY-NC 4.0 |