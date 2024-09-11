#Her skal vi prøve at sortere i lister

#Vi laver en liste, med 5 steder vi gerne vil besøge

ferie_lokalitioner=["Rom","Albanien","Buddapest","Tyrkiet","USA"]
#Vi tester listen
print(ferie_lokalitioner)

#Vi vil gerne have dem sorteret alphabetisk, hvilket kan gøres på følgende måde
ferie_lokalitioner.sort()
print(ferie_lokalitioner)

#Vi kan også gøre det omvendt ved at sætte et argument ind i funktionen således her med (reverse=True)
ferie_lokalitioner.sort(reverse=True)

print(ferie_lokalitioner)

#Vi kan også altid få et totalt antal af vores liste, ved at tilføje en len i en print
print(len(ferie_lokalitioner))