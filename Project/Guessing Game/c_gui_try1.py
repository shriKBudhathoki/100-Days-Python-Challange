import random
import hashlib
import tkinter as tk
from tkinter import messagebox


# =========================================================
# USERS
# =========================================================

users = {}

# =========================================================
# LOAD USERS FROM FILE
# =========================================================

try:

    with open("users.txt", "r") as file:

        for line in file:

            line = line.strip()

            if not line:
                continue

            try:

                name, username, email, hashed_password = line.split(",")

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


# =========================================================
# MAIN WINDOW
# =========================================================

root = tk.Tk()

root.title("Guessing Game")
root.geometry("500x400")


# =========================================================
# CLEAR WINDOW
# =========================================================

def clear_window():

    for widget in root.winfo_children():

        widget.destroy()


# =========================================================
# GAME INTERFACE
# =========================================================

def game_interface():

    clear_window()

    title = tk.Label(
        root,
        text="Welcome to our game..!",
        font=("Arial", 22)
    )

    title.pack(pady=40)


    signup_button = tk.Button(
        root,
        text="Create Account",
        width=20,
        command=Create_account
    )

    signup_button.pack(pady=10)


    login_button = tk.Button(
        root,
        text="Login",
        width=20,
        command=User_login
    )

    login_button.pack(pady=10)


# =========================================================
# GENERATE USERNAME
# =========================================================

def generate_username(name):

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


# =========================================================
# CREATE ACCOUNT
# =========================================================

def Create_account():

    clear_window()


    title = tk.Label(
        root,
        text="Create Account",
        font=("Arial", 22)
    )

    title.pack(pady=20)


    # ---------------- NAME ----------------

    name_label = tk.Label(
        root,
        text="Enter your name:"
    )

    name_label.pack()

    name_entry = tk.Entry(root, width=35)

    name_entry.pack(pady=5)


    # ---------------- EMAIL ----------------

    email_label = tk.Label(
        root,
        text="Enter your email:"
    )

    email_label.pack()

    email_entry = tk.Entry(root, width=35)

    email_entry.pack(pady=5)


    # ---------------- PASSWORD ----------------

    password_label = tk.Label(
        root,
        text="Enter your password:"
    )

    password_label.pack()

    password_entry = tk.Entry(
        root,
        width=35,
        show="*"
    )

    password_entry.pack(pady=5)


    # ---------------- CONFIRM PASSWORD ----------------

    confirm_label = tk.Label(
        root,
        text="Re-enter your password:"
    )

    confirm_label.pack()

    confirm_entry = tk.Entry(
        root,
        width=35,
        show="*"
    )

    confirm_entry.pack(pady=5)


    # =====================================================
    # CREATE ACCOUNT FUNCTION
    # =====================================================

    def create_user():

        name = name_entry.get().strip()

        email = email_entry.get().strip().lower()

        password = password_entry.get()

        confirm_password = confirm_entry.get()


        # ---------------- CHECK NAME ----------------

        if not name:

            messagebox.showerror(
                "Error",
                "Please enter your name."
            )

            return


        # ---------------- CHECK EMAIL ----------------

        if not email:

            messagebox.showerror(
                "Error",
                "Please enter your email."
            )

            return


        if email in users:

            messagebox.showerror(
                "Error",
                "An account with this email already exists!"
            )

            return


        # ---------------- CHECK PASSWORD ----------------

        if len(password) < 8:

            messagebox.showerror(
                "Error",
                "Password must be at least 8 characters!"
            )

            return


        # ---------------- CONFIRM PASSWORD ----------------

        if password != confirm_password:

            messagebox.showerror(
                "Error",
                "Passwords do not match!"
            )

            return


        # ---------------- USERNAME ----------------

        username = generate_username(name)


        # ---------------- HASH PASSWORD ----------------

        hashed_password = hashlib.sha256(
            password.encode()
        ).hexdigest()


        # ---------------- SAVE TO FILE ----------------

        with open("users.txt", "a") as file:

            file.write(
                name + "," +
                username + "," +
                email + "," +
                hashed_password + "\n"
            )


        # ---------------- SAVE TO DICTIONARY ----------------

        users[email] = {

            "name": name,
            "username": username,
            "password": hashed_password

        }


        messagebox.showinfo(
            "Success",
            f"Account created successfully!\n\n"
            f"Your username is:\n{username}"
        )


        # Go to login page

        User_login()


    # =====================================================
    # CREATE BUTTON
    # =====================================================

    create_button = tk.Button(
        root,
        text="Create Account",
        width=20,
        command=create_user
    )

    create_button.pack(pady=15)


    # =====================================================
    # BACK BUTTON
    # =====================================================

    back_button = tk.Button(
        root,
        text="Back",
        width=20,
        command=game_interface
    )

    back_button.pack()


# =========================================================
# LOGIN
# =========================================================

def User_login():

    clear_window()


    title = tk.Label(
        root,
        text="Login",
        font=("Arial", 22)
    )

    title.pack(pady=30)


    # ---------------- EMAIL ----------------

    email_label = tk.Label(
        root,
        text="Enter your email:"
    )

    email_label.pack()

    email_entry = tk.Entry(
        root,
        width=35
    )

    email_entry.pack(pady=5)


    # ---------------- PASSWORD ----------------

    password_label = tk.Label(
        root,
        text="Enter your password:"
    )

    password_label.pack()

    password_entry = tk.Entry(
        root,
        width=35,
        show="*"
    )

    password_entry.pack(pady=5)


    # =====================================================
    # LOGIN FUNCTION
    # =====================================================

    def login_user():

        email = email_entry.get().strip().lower()

        password = password_entry.get()


        # ---------------- CHECK EMAIL ----------------

        if email not in users:

            messagebox.showerror(
                "Login Failed",
                "Email doesn't exist!"
            )

            return


        # ---------------- HASH PASSWORD ----------------

        hashed_password = hashlib.sha256(
            password.encode()
        ).hexdigest()


        # ---------------- CHECK PASSWORD ----------------

        if users[email]["password"] == hashed_password:

            messagebox.showinfo(
                "Login Successful",
                f"Welcome {users[email]['name']}!"
            )

            # You can call your actual game here later.

        else:

            messagebox.showerror(
                "Login Failed",
                "Incorrect password!"
            )


    # =====================================================
    # LOGIN BUTTON
    # =====================================================

    login_button = tk.Button(
        root,
        text="Login",
        width=20,
        command=login_user
    )

    login_button.pack(pady=15)


    # =====================================================
    # BACK BUTTON
    # =====================================================

    back_button = tk.Button(
        root,
        text="Back",
        width=20,
        command=game_interface
    )

    back_button.pack()


# =========================================================
# START GUI
# =========================================================

game_interface()

root.mainloop()

