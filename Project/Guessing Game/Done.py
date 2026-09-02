
import random
import hashlib

users = {}


# ---------------- LOAD USERS FROM FILE ---------------- #

try:
    with open("users.txt", "r") as file:

        for line in file:

            line = line.strip()

            # Ignore empty lines
            if not line:
                continue

            try:
                name, username, email, hashed_password = line.split(",")

                # Clean stored data
                name = name.strip()
                username = username.strip()
                email = email.strip().lower()
                hashed_password = hashed_password.strip()

                users[email] = {
                    "name": name,
                    "username": username,
                    "password": hashed_password
                }

            except ValueError:
                print("Invalid line in users.txt:")
                print(line)


except FileNotFoundError:
    pass


# ---------------- GAME INTERFACE ---------------- #

def game_interface():

    print("Welcome to our game..!")

    game_page()


# ---------------- GAME PAGE ---------------- #

def game_page():

    print("Game page Loading.....")

    try:

        choice = int(input(
            "\nEnter 1 to create an account"
            "\nEnter 0 to login"
            "\nYour Choice : "
        ))

    except ValueError:

        print("Please enter 0 or 1.")
        return

    if choice == 1:

        Create_account()

    elif choice == 0:

        User_login()

    else:

        print("Invalid Choice...!")


# ---------------- GENERATE USERNAME ---------------- #

def generate_username(name):

    # Remove spaces
    clean_name = name.replace(" ", "")

    while True:

        number = random.randint(1000, 9999)

        username = clean_name + str(number)

        username_exist = False

        for user_data in users.values():

            if user_data["username"] == username:

                username_exist = True
                break

        if not username_exist:

            return username


# ---------------- CREATE ACCOUNT ---------------- #

def Create_account():

    print("\nSignup page....")

    name = input("Enter your name : ").strip()

    email = input("Enter your email : ").strip().lower()

    # Check email
    if email in users:

        print("An account with this email already exists..!")
        return

    # Generate username
    username = generate_username(name)

    print(f"Your username is: {username}")

    # ---------------- PASSWORD ---------------- #

    while True:

        password = input("Enter a password : ")

        if len(password) < 8:

            print("Password must be at least 8 characters..!")
            continue

        confirm_password = input("Re-enter your password : ")

        if password != confirm_password:

            print("Passwords do not match. Try again.")
            continue

        break

    # ---------------- HASH PASSWORD ---------------- #

    hashed_password = hashlib.sha256(
        password.encode()
    ).hexdigest()

    # ---------------- STORE IN FILE ---------------- #

    with open("users.txt", "a") as file:

        file.write(
            name + "," +
            username + "," +
            email + "," +
            hashed_password + "\n"
        )

    # ---------------- STORE IN DICTIONARY ---------------- #

    users[email] = {
        "name": name,
        "username": username,
        "password": hashed_password
    }

    print("\nPassword Set Successfully")
    print("Account created successfully!")

    print("Loading Environment...")

    User_login()


# ---------------- LOGIN ---------------- #

def User_login():

    print("\nLogin page...")

    email = input("Enter your email id : ").strip().lower()

    # Check email
    if email not in users:

        print(f"Email doesn't exist: {email}")
        return

    password = input("Enter your password : ")

    # Hash entered password
    hashed_password = hashlib.sha256(
        password.encode()
    ).hexdigest()

    # Compare password
    if users[email]["password"] == hashed_password:

        print("\nLogin successfully...!")
        print(f"Welcome {users[email]['name']}!")
        print(f"Username: {users[email]['username']}")
        game()
    else:

        print("Incorrect Password...!")


# ---------------- START PROGRAM ---------------- #
def game():

    print("Let's play a game:")

    score = random.randint(1, 62)

    try:
         # Fetch the hiscore
        with open("Hi-score.txt", "r") as f:
            hiscore = f.read()

            if hiscore != "":
                hiscore = int(hiscore)
            else:
                hiscore = 0
    except FileNotFoundError:
        hiscore=0

    print(f"Your Score is : {score}")

    if score > hiscore:
        with open("Hi-score.txt", "w") as f:
            f.write(str(score))
        print(f"New high score!, {score}")
    else:
        print(f"You did not beat the high score, {hiscore}")

    return score


game_interface()

