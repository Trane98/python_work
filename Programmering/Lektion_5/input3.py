print("(Welcome til Alex's dinner)")

people = int(input("How many are you in your group "))

print(f"\nYou have selected that you are {people} people in your group")

if people >=8:
    print("\nWe do not have the space right now, you will have to wait")
else:
    print("\nWe have space for you at table 10")