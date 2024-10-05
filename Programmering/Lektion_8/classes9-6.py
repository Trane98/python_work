class Restaurant:
    """A simple representation of a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant's name and type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Prints the restaurant's name and cuisine type."""
        print(f"The restaurant's name is {self.restaurant_name}.")
        print(f"They serve {self.cuisine_type} cuisine.")

class IceCreamStand(Restaurant):
    """A specific kind of restaurant that sells ice cream."""

    def __init__(self, restaurant_name, cuisine_type='Ice Cream'):
        """Initialize the ice cream stand with its flavors."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def add_flavors(self, *flavors):
        """Add flavors to the ice cream stand."""
        self.flavors.extend(flavors)

    def display_flavors(self):
        """Display the list of available ice cream flavors."""
        if self.flavors:
            print(f"The available flavors are: {', '.join(self.flavors)}")
        else:
            print("There are no flavors available at the moment.")

# Opret en instans af IceCreamStand
ice_cream_stand = IceCreamStand("Sweet Treats")

# Tilføj og vis smagsvarianter
ice_cream_stand.add_flavors("Vanilla", "Chocolate", "Strawberry")
ice_cream_stand.display_flavors()
