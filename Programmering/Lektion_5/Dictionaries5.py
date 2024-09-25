#Lave en måling med personer og deres ynglings kodesprog
poll = { "jen" : "python",
        "lucas" : "JavaScript",
        "mia" : "ruby",
        "oliver" : "java",
        "sofie" : "c++",
        "Emil" : "swift",
        "freja" : "kotlin"}

#Takke dem der deltog i testen
for name in sorted(poll.keys()):
    if name in poll:
        print(f"{name.title()}, Thanks you for taking the poll")

#Hvis ikke erin er i poll print        
if "erin" not in poll.keys():
    print("Please take the poll Erin")