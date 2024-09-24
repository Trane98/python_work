#Invitationsliste

invitations_liste=["dina","bjarne","jens","ulla","kathrina","morten"]

invitation=f"Hej jeg vil gerne invitere dig {invitations_liste[0].title()} til min fødselsdagsfest D. 16-06-2025"
print(invitation)

invitation=f"Hej jeg vil gerne invitere dig {invitations_liste[1].title()} til min fødselsdagsfest D. 16-06-2025"
print(invitation)

invitation=f"Hej jeg vil gerne invitere dig {invitations_liste[2].title()} til min fødselsdagsfest D. 16-06-2025"
print(invitation)

invitation=f"Hej jeg vil gerne invitere dig {invitations_liste[3].title()} til min fødselsdagsfest D. 16-06-2025"
print(invitation)

invitation=f"Hej jeg vil gerne invitere dig {invitations_liste[4].title()} til min fødselsdagsfest D. 16-06-2025"
print(invitation)

invitation=f"Hej jeg vil gerne invitere dig {invitations_liste[5].title()} til min fødselsdagsfest D. 16-06-2025"
print(invitation)


#Vi får nu at vide, at Morten og Katharina ikke kan komme, vi ændrer derfor i listen.
invitations_liste[4]="caroline"
invitations_liste[5]="Mads"

#Vi tester den nye og opdaterede liste
print(invitations_liste)

#Vi ser det virker, og kan nu gentage tidligere koder med en ny og opdateret invitationsliste
invitation=f"Hej jeg vil gerne invitere dig {invitations_liste[0].title()} til min fødselsdagsfest D. 16-06-2025"
print(invitation)

invitation=f"Hej jeg vil gerne invitere dig {invitations_liste[1].title()} til min fødselsdagsfest D. 16-06-2025"
print(invitation)

invitation=f"Hej jeg vil gerne invitere dig {invitations_liste[2].title()} til min fødselsdagsfest D. 16-06-2025"
print(invitation)

invitation=f"Hej jeg vil gerne invitere dig {invitations_liste[3].title()} til min fødselsdagsfest D. 16-06-2025"
print(invitation)

invitation=f"Hej jeg vil gerne invitere dig {invitations_liste[4].title()} til min fødselsdagsfest D. 16-06-2025"
print(invitation)

invitation=f"Hej jeg vil gerne invitere dig {invitations_liste[5].title()} til min fødselsdagsfest D. 16-06-2025"
print(invitation)

#Vi tilføjer nu flere til listen med mennesker
invitations_liste.insert(0,"David")
invitations_liste.insert(3,"Sofie")
invitations_liste.append("Thomas")

print(invitations_liste)

#Desværre kan der kun komme 2, så nu fjerner vi slavisk indtil der kun er 2 tilbage. 

fjernet_personer=invitations_liste.pop()
fjernet_personer=invitations_liste.pop()
fjernet_personer=invitations_liste.pop()
fjernet_personer=invitations_liste.pop()
fjernet_personer=invitations_liste.pop()
fjernet_personer=invitations_liste.pop()
fjernet_personer=invitations_liste.pop()

#Vi printer hver liste, hvor der nu kun er 2 tilbage på den ene og 7 på den anden.
print(fjernet_personer)
print(invitations_liste)

#Så kan vi lave en besked til de fjernede personer og beholde en besked til invitationslisten

afvisningsbesked_1="Jeg beklager, men grundet bordændringer, kan jeg ikke invitere"
afvisningsbesked_2="til min fødselsdagsfest alligevel"

afvisning_færdig=f"{afvisningsbesked_1} {fjernet_personer[0]} {afvisningsbesked_2}"
print(afvisning_færdig)
#Gentag denne og vi kan skrive en afvisning til alle på den afviste liste.