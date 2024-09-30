def describe_pet(animal_type, pet_name):
    """Beskriver favorit dyr og navnet på dyret"""
    print(f"Mit ynglings dyr er {animal_type}")
    print(f"\nOg {animal_type} har navnet {pet_name.title()}")

describe_pet(animal_type="hunden", pet_name="kalle")