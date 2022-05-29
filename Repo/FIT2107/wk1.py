#list of allowed users
user1 = "Jack"
user2 = "Jill"

access = False

while not access:
    username = input("Login: >> ")
    if username == user1:
        print("Access granted")
        access = True
    elif username == user2:
        print("Welcome to FIT2107")
        access = True
    else:
        print("Access denied")
        access = False