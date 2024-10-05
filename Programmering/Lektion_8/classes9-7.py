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

class Admin(User):
    """A special kind of user with administrative privileges."""

    def __init__(self, first_name, last_name, age, email):
        """Initialize the admin with the same attributes as a user."""
        super().__init__(first_name, last_name, age, email)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        """Display the privileges the admin has."""
        print(f"Admin privileges: {', '.join(self.privileges)}")

# Opret en instans af Admin
admin_user = Admin("Alice", "Wonder", 35, "alice@example.com")

# Kald metoden for at vise privilegier
admin_user.show_privileges()
