#Først laver vi variablerne og de tilføjes så til et dictionari
def build_character(first_name, last_name, age, skin_color, hair_color, gender):
    character = f"{first_name, last_name, age, skin_color, hair_color, gender}"
    return character

#Der gives en variabel til character i reference til build_character, som bliver retuneret
character = build_character("Alexander", "Trendholm", 26, "Hvid", "Blond", "Mand")

print(character)