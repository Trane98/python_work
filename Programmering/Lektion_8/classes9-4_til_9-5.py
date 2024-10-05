##############################################Opgave 9-4##############################################
class Restaurant:
    """A simple representation of a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant's name, type, and the number of customers served."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  # Default value

    def describe_restaurant(self):
        """Prints the restaurant's name and cuisine type."""
        print(f"The restaurant's name is {self.restaurant_name}.")
        print(f"They serve {self.cuisine_type} cuisine.")
        print(f"Customers served: {self.number_served}")

    def open_restaurant(self):
        """Print a message indicating that the restaurant is open."""
        print(f"{self.restaurant_name} is now open!")

    def set_number_served(self, number):
        """Set the number of customers served."""
        self.number_served = number

    def increment_number_served(self, number):
        """Increment the number of customers served by the given number."""
        self.number_served += number

# Opret en instans af klassen
restaurant = Restaurant("Alex's Kebabhus", "Grill")

# Print antal kunder og derefter opdater værdien
print(f"Number served: {restaurant.number_served}")
restaurant.set_number_served(100)
print(f"Number served after setting: {restaurant.number_served}")
restaurant.increment_number_served(50)
print(f"Number served after incrementing: {restaurant.number_served}")

##############################################Opgave 9-5##############################################
class User:
    """A simple model of a user."""

    def __init__(self, first_name, last_name, age, email):
        """Initialize the user with first name, last name, and other details."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.login_attempts = 0  # Default value

    def describe_user(self):
        """Print a summary of the user's information."""
        print(f"User: {self.first_name} {self.last_name}, Age: {self.age}, Email: {self.email}")

    def greet_user(self):
        """Print a personalized greeting to the user."""
        print(f"Hello {self.first_name} {self.last_name}, welcome back!")

    def increment_login_attempts(self):
        """Increment the number of login attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the login attempts to 0."""
        self.login_attempts = 0

# Opret en instans af User-klassen
user = User("John", "Doe", 30, "john.doe@example.com")

# Øg loginforsøgene og print værdien
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(f"Login attempts: {user.login_attempts}")

# Nulstil loginforsøg og print værdien igen
user.reset_login_attempts()
print(f"Login attempts after reset: {user.login_attempts}")
