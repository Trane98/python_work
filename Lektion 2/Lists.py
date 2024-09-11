#Definere en liste
friends=["mads","Mikkel","Thomas","Tobias","Torben"]
print(friends)#printe hele listen

#Printe individuelle del af listen
print(friends[0])
print(friends[1])
print(friends[2])
print(friends[3])
print(friends[4])

#Kan også gøres med minus således her
print(friends[-1])
#Den vil altså sige Torben 2 gange lige efter hinanden


#Nu definere vi en besked, og sætter den sammen med en af vennerne.

message="Hej"

greeting=f"{message} {friends[0].title()}"#Jeg har tilføjet at det skal gøres med title, så vi får et stort forbogstav

print(greeting)

#Det er også muligt at ungå at definere 2 ting og kombinere dem således her
greeting=f"Hej med dig {friends[0].title()}"
print(greeting)

