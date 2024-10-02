#For at definere funktioner, så kan de opbygges således
def greet_user(username):
    """Display a simple greeting."""#Dette kaldes en docstring, som forklarer hvad funktionen gør. 
    print(f"Hello {username.title()}")

#Her kaldes funktionen hvilket skriver Hello Alex
greet_user("alex")
