def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

# Call the function with your first name, last name, and three other key-value pairs
user_profile = build_profile('John', 'Doe', location='Denmark', field='Software Development', hobby='Cycling')

print(user_profile)
