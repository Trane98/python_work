class Restaurant:
    """A simple representation of a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant's name and type of cuisine."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Prints the restaurant's name and cuisine type."""
        print(f"The restaurant's name is {self.restaurant_name}.")
        print(f"They serve {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        """Print a message indicating that the restaurant is open."""
        print(f"{self.restaurant_name} is now open!")

# Opret en instans af klassen
restaurant = Restaurant("Alex's Kebabhus", "Grill")

# Print attributterne og kald metoderne
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()


##############################################Opgave 9-2##############################################
# Brug klassen fra 9-1
restaurant_1 = Restaurant("Mama Mia", "Italian")
restaurant_2 = Restaurant("Sushi King", "Japanese")
restaurant_3 = Restaurant("Curry Palace", "Indian")

# Kald metoden describe_restaurant for hver instans
restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()


##############################################Opgave 9-3##############################################
class User:
    """A simple model of a user."""

    def __init__(self, first_name, last_name, age, email):
        """Initialize the user with first name, last name, and other details."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email

    def describe_user(self):
        """Print a summary of the user's information."""
        print(f"User: {self.first_name} {self.last_name}, Age: {self.age}, Email: {self.email}")

    def greet_user(self):
        """Print a personalized greeting to the user."""
        print(f"Hello {self.first_name} {self.last_name}, welcome back!")

# Opret flere instanser af User
user_1 = User("John", "Doe", 30, "john.doe@example.com")
user_2 = User("Jane", "Smith", 25, "jane.smith@example.com")
user_3 = User("Max", "Mustermann", 40, "max.mustermann@example.com")

# Kald metoderne for hver bruger
user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()

user_3.describe_user()
user_3.greet_user()
