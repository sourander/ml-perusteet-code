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
export PACKAGE_NAME=vastaukset 

# Docker
docker compose up -d

# Repeat this
docker compose start tester
```

Testitulokset löytyvät samasta palvelimesta, oli kummat tahansa testit ajettu.: http://localhost:5050/latest-report

### Ympäristömuuttujan vaihtuessa

Pelkkä `docker compose start tester` ei riitä, koska ympäristömuuttujaa ei ole päivitetty. Täytyy ajaa `docker compose up -d` uudelleen.

```bash
# If need to check the student templates
# Or go back to the teacher's answers
unset PACKAGE_NAME            # This
export PACKAGE_NAME=student   # or this

# And then
docker compose up -d
```

### Tuloksien poisto

```bash
# To clean up results
docker compose down --volumes
docker compose up
```

