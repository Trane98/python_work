def make_car(manufacturer, model, **car_info):
    """Build a dictionary containing information about a car."""
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model
    for key, value in car_info.items():
        car[key] = value
    return car

# Call the function with manufacturer, model, and additional keyword arguments
car = make_car('subaru', 'outback', color='blue', tow_package=True)

# Print the car dictionary
print(car)
