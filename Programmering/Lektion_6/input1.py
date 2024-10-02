#Lave simple inputs fx som navn
name=input("Hvad er dit navn:")

print(f"\nHello, {name}")

#Lidt mere komplicerede inputs kan være:
promt = "Hvis du vil være så venlig at indsætte dit navn, så vi kan registere dig."
promt += "\nHvad er dit fornavn? {name}"

name = input(promt)
print(f"\nHello, {name}!")