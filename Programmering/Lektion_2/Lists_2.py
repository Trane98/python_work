#Vi starter med at definere en masse biler

biler=["VW","audi","mercedes","toyota","land rover","zeat"]

#Vi definere så en masse beskeder og printer dem ud fra listen af biler
message=f"Jeg vil gerne have en {biler[0].title()}"
print(message)

message=f"Jeg vil helst ikke have en {biler[1].title()}"
print (message)

message=f"Det ville være mega fedt at eje en {biler[2].title()}"
print(message)

message=f"En nederen bil er en {biler[3].title()}"
print(message)

message=f"En virkelig fed bil er en {biler[-2].title()}"
print(message)

message=f"En forfærdelig bil er en {biler[-1].title()}"
print(message)

#Nu erstartter vi elementer i listen som fx en ny første vil, som er 0.
biler[0]="Ferrari"

print(biler)#Vi får nu i stedet for Vw så får vi en Ferrari.

#Vi kan også bare tilføje til listens bagende, hvilket kan gøres med .append
biler.append("VW")#Vi tilføjer VW igen

print(biler)

