import tkinter as tk
from tkinter import simpledialog

class CustomLoginDialog(simpledialog.Dialog):
    def body(self, master):
        tk.Label(master, text="Username:").grid(row=0)
        tk.Label(master, text="Password:").grid(row=1)

        self.username_entry = tk.Entry(master)
        self.password_entry = tk.Entry(master, show="*")

        self.username_entry.grid(row=0, column=1)
        self.password_entry.grid(row=1, column=1)
        return self.username_entry

    def apply(self):
        self.username = self.username_entry.get()
        self.password = self.password_entry.get()

def show_login_popup():
    root = tk.Tk()
    root.withdraw() 
    login_dialog = CustomLoginDialog(root)
    root.destroy()

    print("Username:", login_dialog.username)
    print("Password:", login_dialog.password)

show_login_popup()