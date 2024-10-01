toppings = []
while True:
    user_input_for_toppings = input("Select one topping of your liking ")
    if user_input_for_toppings.lower() == "quit":
        break
    else:
        toppings.append(user_input_for_toppings)
        print(f"You have selected {user_input_for_toppings} it will be added to your pizza")

for topping in toppings:
    print(f"You have selected the following {toppings} for your pizza")
