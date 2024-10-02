print("Welcome to Alex's plizza place")
toppings = []
while True:
    topping = input("\nWhat would you like to order? ")

    if topping == "quit":
        break
    else:
        toppings.append(toppings)
        print(f"\nYou have choosen to add {topping} to your pizza")
        print(toppings)