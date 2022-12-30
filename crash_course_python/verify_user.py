import json


def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        answer = input(f"Are you {username}? y/n: ").lower()
        if answer in ['y', 'yes']:
            print(f"\n\tWelcome Back, {username}!")
        else:
            username = get_new_username()
            print("\n\tWe'll remember you when you come back, "
                  f"{username}!")
    else:
        username = get_new_username()
        print(f"\n\tWe'll remember you when you come back, {username}!")


greet_user()
