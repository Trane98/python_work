def describe_pet(pet_name, animal_type="hunden"):
    """Beskriver favorit dyr og navnet på dyret"""
    print(f"Mit ynglings dyr er {animal_type}")
    print(f"\nOg {animal_type} har navnet {pet_name.title()}")

describe_pet(pet_name="kalle")