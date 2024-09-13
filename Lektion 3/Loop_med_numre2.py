# Vi laver en liste med tal, hvor at vi kan se max og min værdien i printet samt summen af talle tallene sammen
numbers=list(range(1,1000001))

print(f"Min værdien af numrende {min(numbers)}") #Min værdi
print(f"Max værdien af numrende {max(numbers)}") #Max værdi

print(f"Summen af tallene {sum(numbers)}") #Summen af værdierne





#Nu laver vi det, så at den kun tager hvert tredje tal fra 3 til 30
uneven_numbers=list(range(3,33, 3))
print(uneven_numbers)



squares=[value**3 for value in range(1,11)]
print(squares)




