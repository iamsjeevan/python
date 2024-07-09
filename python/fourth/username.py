def print_all_items(d):
    print("Items in the dictionary:")
    for key, value in d.items():
        print(f"{key}: {value}")

def print_all_keys(d):
    print("Keys in the dictionary:")
    for key in d.keys():
        print(key)

def print_all_values(d):
    print("Values in the dictionary:")
    for value in d.values():
        print(value)

def get_password(d, username):
    if username in d:
        return d[username]
    else:
        return None

def change_password(d, username, new_password):
    if username in d:
        d[username] = new_password
        print(f"Password for '{username}' changed to '{new_password}'")
    else:
        print(f"Username '{username}' not found in the dictionary")

def main():
    # Initialize the dictionary of usernames and passwords
    passwd = {'rahul': 'genius', 'kumar': 'smart', 'ankita': 'intelligent'}

    # Print all items in the dictionary
    print_all_items(passwd)

    # Print all keys in the dictionary
    print_all_keys(passwd)

    # Print all values in the dictionary
    print_all_values(passwd)

    # Get passwords of users
    username = 'rahul'
    print(f"Password for '{username}': {get_password(passwd, username)}")

    # Change password of a particular user
    username = 'ankita'
    new_password = 'brilliant'
    change_password(passwd, username, new_password)

if __name__ == "__main__":
    main()
