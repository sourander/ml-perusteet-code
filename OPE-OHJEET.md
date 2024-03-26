# Opettajan ohjeet

## Testien pohjustus

Testit voi ajaa siten, että ne ajetaan "vastaukset"-kansiosta, joka sijaitsee aivan muualla Filesystemissä, ja on tuotuna src/ kansion sisään symbolisena linkkinä.

Huomaa, että testit kuitenkin importtaavat `ml`-moduulista eivätkä noudata `PACKAGE_NAME`-ympäristömuuttujaa. Siispä **testit on pakko ajaa Dockerilla**, kun testaa opettajan vastauksia.

```bash
# Luo absoluuttinen polku vastauksiin
VASTAUSPATH="$(realpath ..)/ml-perusteet-vastaukset/src/vastaukset"

# Poista vanha symbolinen linkki ja luo uusi
rm src/vastaukset
ln -s "$VASTAUSPATH" src/vastaukset
```

## Testien ajaminen

Tiedostossa `docker-compose.yml` on määritelty palvelu `tester`, joka ajaa testit. Yllä pohjustettu kansio on mahdollista syöttää Docker-palvelulle ympäristömuuttujana `VASTAUSPATH`. Katso `.yml`-tiedostosta tarkemmin toteutus.

```bash
# Aseta ympäristömuuttuja
PACKAGE_NAME=vastaukset 

# Docker 
docker compose up

# Repeat this 
docker compose up tester
```