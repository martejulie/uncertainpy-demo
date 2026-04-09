# Usikkerhetskvantifisering og sensitivitetsanalyse med Uncertainpy



## Installer nødvendige pakker med conda

Start med å klone repoet og navigér inn i det:

```bash 
git clone https://github.com/martejulie/uncertainpy-demo
cd uncertainpy-demo
```

Bruk ``environment.yaml`` til å lage et nytt miljø:

```bash
conda env create -f environment.yaml
```

Hvis dette ikke fungerer, forsøk denne kommandoen først:

```bash
conda config --set channel_priority disabled
```

Aktivér miljøet ved å kjøre: 

```bash
conda activate uncertainpy-env
```

Til slutt må du innstallere noe flere pakker på innsien av miljøet med pip:

```bash
pip install --no-deps -r requirements.txt
```

