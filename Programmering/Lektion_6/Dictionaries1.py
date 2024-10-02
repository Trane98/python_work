#Lave dictionaries med store fortegn
person_0={"first_name":"mads","last_name":"nørregaard","lives_in":"aalborg","age":31}
print(person_0["first_name"].title())
print(person_0["last_name"].title())
print(person_0["lives_in"].title())
print(person_0["age"])


person_1={"first_name":"dina", "last_name":"raabjerg","age":55, "favorite_number":7}
person_2={"first_name":"bjarne", "last_name":"raabjerg","age":58,"favorite_number":4}

#Tilføje til en liste. Her tilføjer vi til person_0
person_0={"favorite_number":12}

#Forevisning med linjeskift
print(f"\n{person_0['favorite_number']}")
print(person_1["favorite_number"])
print(person_2["favorite_number"])

#Forklaringer til forskellige udtryk i python
python_udtryk={"lister":"Lister kan være inde i en variabel","integers":"Integers betyder heltal i kodesprog","floats":"Floats det er decimaltal i kodesprog","strings":"Strings det er tekst i kodesprog","variabler":"Variabler kan indeholde tal, lister og strings"}

#Print af de forskellige udtryk og deres tilhørende meninger
print(python_udtryk["lister"])
print(python_udtryk["floats"])
print(python_udtryk["strings"])
print(python_udtryk["variabler"])
print(python_udtryk["integers"])