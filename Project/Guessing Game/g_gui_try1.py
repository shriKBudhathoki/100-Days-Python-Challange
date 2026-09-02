import hashlib
import random
import os
import tkinter as tk
from tkinter import ttk, messagebox

# ---------------- GLOBAL USER DATA ---------------- #
users = {}
USER_FILE = "users.txt"


def load_users():
    """Reads users.txt and populates the users dictionary."""
    if not os.path.exists(USER_FILE):
        return

    with open(USER_FILE, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            try:
                name, username, email, hashed_password = line.split(",")
                users[email.strip().lower()] = {
                    "name": name.strip(),
                    "username": username.strip(),
                    "password": hashed_password.strip(),
                }
            except ValueError:
                continue


def generate_username(name):
    """Generates a unique username using the user's name and a random 4-digit number."""
    clean_name = name.replace(" ", "")
    while True:
        number = random.randint(1000, 9999)
        username = clean_name + str(number)
        if not any(
            u["username"] == username for u in users.values()
        ):
            return username


# ---------------- GUI APPLICATION ---------------- #
class GameAuthApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Game Authentication Portal")
        self.root.geometry("420x480")
        self.root.resizable(False, False)

        # Apply standard visual theme
        self.style = ttk.Style()
        self.style.theme_use("clam")

        # Create Tabbed Layout
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)

        self.login_tab = ttk.Frame(self.notebook)
        self.signup_tab = ttk.Frame(self.notebook)

        self.notebook.add(self.login_tab, text="  Login  ")
        self.notebook.add(self.signup_tab, text="  Sign Up  ")

        self.build_login_ui()
        self.build_signup_ui()

    # ---------------- LOGIN TAB UI ---------------- #
    def build_login_ui(self):
        container = ttk.Frame(self.login_tab, padding=20)
        container.pack(fill="both", expand=True)

        ttk.Label(
            container, text="Welcome Back!", font=("Helvetica", 16, "bold")
        ).pack(pady=(10, 20))

        ttk.Label(container, text="Email Address:").pack(
            anchor="w", pady=(5, 0)
        )
        self.login_email_entry = ttk.Entry(container, width=35)
        self.login_email_entry.pack(fill="x", pady=(0, 15))

        ttk.Label(container, text="Password:").pack(
            anchor="w", pady=(5, 0)
        )
        self.login_password_entry = ttk.Entry(
            container, width=35, show="*"
        )
        self.login_password_entry.pack(fill="x", pady=(0, 20))

        login_btn = ttk.Button(
            container, text="Login", command=self.handle_login
        )
        login_btn.pack(fill="x", ipady=5)

    def handle_login(self):
        email = self.login_email_entry.get().strip().lower()
        password = self.login_password_entry.get()

        if not email or not password:
            messagebox.showwarning(
                "Input Error", "Please enter both email and password."
            )
            return

        if email not in users:
            messagebox.showerror(
                "Login Failed", f"No account found with email: {email}"
            )
            return

        hashed_input = hashlib.sha256(password.encode()).hexdigest()

        if users[email]["password"] == hashed_input:
            user_info = users[email]
            messagebox.showinfo(
                "Success",
                f"Login Successful!\n\nWelcome, {user_info['name']}!\nUsername: {user_info['username']}",
            )
            self.login_email_entry.delete(0, tk.END)
            self.login_password_entry.delete(0, tk.END)
        else:
            messagebox.showerror(
                "Login Failed", "Incorrect password. Try again."
            )

    # ---------------- SIGNUP TAB UI ---------------- #
    def build_signup_ui(self):
        container = ttk.Frame(self.signup_tab, padding=20)
        container.pack(fill="both", expand=True)

        ttk.Label(
            container, text="Create Account", font=("Helvetica", 16, "bold")
        ).pack(pady=(5, 15))

        ttk.Label(container, text="Full Name:").pack(
            anchor="w", pady=(2, 0)
        )
        self.signup_name_entry = ttk.Entry(container, width=35)
        self.signup_name_entry.pack(fill="x", pady=(0, 10))

        ttk.Label(container, text="Email Address:").pack(
            anchor="w", pady=(2, 0)
        )
        self.signup_email_entry = ttk.Entry(container, width=35)
        self.signup_email_entry.pack(fill="x", pady=(0, 10))

        ttk.Label(container, text="Password (min. 8 chars):").pack(
            anchor="w", pady=(2, 0)
        )
        self.signup_pass_entry = ttk.Entry(container, width=35, show="*")
        self.signup_pass_entry.pack(fill="x", pady=(0, 10))

        ttk.Label(container, text="Confirm Password:").pack(
            anchor="w", pady=(2, 0)
        )
        self.signup_confirm_entry = ttk.Entry(
            container, width=35, show="*"
        )
        self.signup_confirm_entry.pack(fill="x", pady=(0, 15))

        signup_btn = ttk.Button(
            container, text="Sign Up", command=self.handle_signup
        )
        signup_btn.pack(fill="x", ipady=5)

    def handle_signup(self):
        name = self.signup_name_entry.get().strip()
        email = self.signup_email_entry.get().strip().lower()
        password = self.signup_pass_entry.get()
        confirm_password = self.signup_confirm_entry.get()

        if not name or not email or not password or not confirm_password:
            messagebox.showwarning(
                "Input Error", "All fields are required."
            )
            return

        if email in users:
            messagebox.showerror(
                "Error", "An account with this email already exists."
            )
            return

        if len(password) < 8:
            messagebox.showwarning(
                "Weak Password",
                "Password must be at least 8 characters long.",
            )
            return

        if password != confirm_password:
            messagebox.showerror(
                "Mismatch", "Passwords do not match. Please re-enter."
            )
            return

        username = generate_username(name)
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # Save to file
        with open(USER_FILE, "a") as file:
            file.write(
                f"{name},{username},{email},{hashed_password}\n"
            )

        # Save to in-memory state
        users[email] = {
            "name": name,
            "username": username,
            "password": hashed_password,
        }

        messagebox.showinfo(
            "Account Created",
            f"Account created successfully!\n\nYour assigned Username: {username}",
        )

        # Clear fields and redirect to Login tab
        self.signup_name_entry.delete(0, tk.END)
        self.signup_email_entry.delete(0, tk.END)
        self.signup_pass_entry.delete(0, tk.END)
        self.signup_confirm_entry.delete(0, tk.END)

        self.login_email_entry.insert(0, email)
        self.notebook.select(self.login_tab)


# ---------------- PROGRAM START ---------------- #
if __name__ == "__main__":
    load_users()
    root = tk.Tk()
    app = GameAuthApp(root)
    root.mainloop()