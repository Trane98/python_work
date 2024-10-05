class Battery:
    """A model of a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go approximately {range} miles on a full charge.")

    def upgrade_battery(self):
        """Upgrade the battery if it isn't already 100 kWh."""
        if self.battery_size < 100:
            self.battery_size = 100
            print("The battery has been upgraded to 100 kWh.")

class ElectricCar:
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the car."""
        self.make = make
        self.model = model
        self.year = year
        self.battery = Battery()

    def describe_car(self):
        """Print a statement describing the car."""
        print(f"{self.year} {self.make} {self.model}")

# Opret en instans af ElectricCar
my_tesla = ElectricCar("Tesla", "Model S", 2024)

# Vis batteristørrelse og rækkevidde, opgrader batteriet og vis rækkevidde igen
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()
