#Her udtrykkes der en liste med 5 udtryk og deres tilhørende forklaringer
python_udtryk={"lister":"Lister kan være inde i en variabel",
               "integers":"Integers betyder heltal i kodesprog",
               "floats":"Floats det er decimaltal i kodesprog",
               "strings":"Strings det er tekst i kodesprog",
               "variabler":"Variabler kan indeholde tal, lister og strings"}

#Så køres de i et loop, hvor der først startes med den ene også den anden
for python in python_udtryk:
    print(f"{python}:{python_udtryk[python]}")

#Der tilføjes til dictionariet
python_udtryk={"loops":"får det hele til at køre i ring det antal gange man definere"}

#Vi kører printet igen, men den her gang er der et ekstra udtryk med. 
for python in python_udtryk:
    print(f"{python}:{python_udtryk[python]}")