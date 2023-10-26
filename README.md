# Oblig 3 Emir Nukic

## Beskrivelse:

I denne oppgaven skal vi sette opp GitHub Actions på vårt GitHub-repo med koden vi lagde i Oblig 2. Målet er å kjøre testene vi har laget automatisk hver gang en ny commit blir pushet til vår GitHub-repo.


## Handlinger utført:

### 1. Opprettelse av GitHub Repository 

Her har jeg da opprettet et nytt GitHub-repo og lagt inn filene/kodene fra Oblig 2. 
<img width="893" alt="image" src="https://github.com/PrimeRime/testing_leap/assets/117373652/f92a5cc9-da51-4a98-affb-a63c675b0b2a">


### 2. Konfigurasjon av GitHub Actions

* For å konfigurere GitHub Actions så lagde jeg først en .GitHub Directory og inni der en Workflows Dircetory.
<img width="772" alt="image" src="https://github.com/PrimeRime/testing_leap/assets/117373652/5596081b-d8a0-4e8a-93bf-ad854814db55">

* Deretter opprettet jeg en yml (python-app.yml) fil i GitHub som jeg da implementere inn i Repositoryet etterhvert under Workflows.
```
name: Testing leap year

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

permissions:
  contents: read

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3
    - name: Set up Python 3.10
      uses: actions/setup-python@v3
      with:
        python-version: "3.10"
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install flake8 pytest
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
    - name: Test with pytest
      run: |
        echo " now testing all tests from the ${{ github.testing_leap }} repository"
        pytest test/test_leap_year.py

```

### 3. Verifisere at testene kjører automatisk

* Jeg prøver å endre på name i python-app.yml fra Python Application til Testing leap year.
* Sjekker om testen fungerte ved å gå til Actions i GitHub, og der kom det opp at det fungerte.
```
name: Python Application
```
Til:
```
name: Testing leap year
```
* Her kan vi se at testene gikk gjennom:
<img width="1118" alt="image" src="https://github.com/PrimeRime/testing_leap/assets/117373652/4d0a4dd3-ad5c-4203-913b-bb3ac6d36491">


### 4. Dokumentering av oppgaven

Opprettet en README.md-fil der jeg forklarer kort om hvordan jeg gjennomførte denne oppgaven og hva som ble gjort. 
