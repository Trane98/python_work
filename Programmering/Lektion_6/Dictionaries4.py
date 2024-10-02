#Hvordan man kører et loop igennem og får begge to med samt tilhørende stort forbogstav
rivers={"nilen":"egypt",
        "amazonasfloden":"Brasilien",
        "Mississippi-floden":"USA",
        "Yangtze-floden":"Kina",
        "Donau":"Tyskland"}

for river, country in rivers.items():
    print(f"{river.title()} befinder sig i {country.title()}.")