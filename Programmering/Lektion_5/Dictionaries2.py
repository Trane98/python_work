#Loops for dictionaries
favorite_languages = {
    "jen":"python",
    "sarah":"c",
    "edward":"rust",
    "phil":"python",
    }
#Her loopes der igennem alle navne og deres ynglings kodesprog
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

#Man kan også gøre det samme med keys ved at sige

for name in favorite_languages.keys():
    print(name.title())