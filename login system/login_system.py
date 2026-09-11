def login():
    username = "admin"
    password = "python123"

    attempts = 0

    while attempts < 3:
        user = input("Enter username: ")
        pwd = input("Enter password: ")

        if user == username and pwd == password:
            print("Login successful!")
            return
        else:
            attempts += 1
            print("Incorrect username or password.")
            print("Attempts remaining:", 3 - attempts)

    print("Account locked!")


login()