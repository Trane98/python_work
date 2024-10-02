print("Welcome to the movie theater")

prices = []

while True:
    age = int(input("Insert age to get price of one ticket "))
    if age < 3:
        price = 0
    
    elif age < 12:
        price = 10
    
    elif age > 12:
        price = 15
    
    prices.append(price)
    
    print(f"A price with that age costs {price}$")

    stopping = input("Insert quit when done with age control else type continue ")
    if stopping == "quit":
        break

total_price = sum(prices)
print(f"All ticket prices {prices}")
print(f"The total cost for all tickets is: {total_price}$")