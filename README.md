# Usikkerhetskvantifisering og sensitivitetsanalyse med Uncertainpy

Dette repoet inneholder to eksempler på hvordan man kan bruke ``Uncertainpy`` fra Tennø et al. 2018 [1] til å gjøre usikkerhetskvantifisering og
sensitivitetsanalyse i Python. Begge eksemplene er gjort på PMRTD-modellen fra Børve 2021 [2] som predikerer rekkevidden til termiske sensorer. I eksemplene ser vi på termisk rekkevidde som funksjon av den
atmosfæriske ekstinksjonskoeffisienten og analyserer modellen når 
henholdsvis to og tre parametere er usikre. 

## Installér ``Uncertainpy`` med conda

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

Til slutt må du innstallere noe flere pakker på innsiden av miljøet med pip:

```bash
pip install --no-deps -r requirements.txt
```

## Kjør eksemplene

Programmene ``analysis_two_uncertain.py`` og ``analysis_three_uncertain.py`` kjører analysene og lager passende figurer. 

## Referanser

[1] Simen Tennøe, Geir Halnes, og Gaute T. Einevoll. "Uncertainpy: a python toolbox for uncertainty quantification and sensitivity analysis in computational neuroscience." *Frontiers in neuroinformatics* 12 (2018): 370145.

[2] Steinar Børve. "Therman sensor aquisition range estimation" *Forsvarets forskningsinstitutt* FFI-rapport 21/00388 (2021).
