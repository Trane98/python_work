def make_sandwich(*items):
    """Accepts a list of items and prints a summary of the sandwich being ordered."""
    print("\nMaking a sandwich with the following ingredients:")
    for item in items:
        print(f"- {item}")

# Call the function three times with a different number of ingredients
make_sandwich("ham", "cheese", "lettuce")
make_sandwich("turkey", "bacon", "avocado", "tomato")
make_sandwich("peanut butter", "jelly")
