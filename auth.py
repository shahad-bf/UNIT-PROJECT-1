import json

def get_users():
    try:
        file = open("users.json", "r")
        users = json.load(file)
        file.close()
        return users
    except:
        return {}

def check_login():
    users = get_users()
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in users:
        if users[username] == password:
            print(f"Welcome, {username}!")
            return username 
        else:
            print("Wrong password\n")
    else:
        print("Username not found\n")

    return None 


if __name__ == "__main__":
    user = check_login()
    if user:
        print(f"Login successful")
    else:
        print("Try again")
