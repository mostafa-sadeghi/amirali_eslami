import tkinter as tk
from tkinter import ttk


def greet():
    print(user_name.get())


root = tk.Tk()
root.title("My app")
root.geometry("400x300")
user_name = tk.StringVar()

# my_label = ttk.Label(root, text="Hi", padding=(30, 15), background="cyan")
# my_label.pack(fill="both")

# greet_button = ttk.Button(root, text="Greet", command=greet)
# greet_button.pack(side="left", fill="both", expand=True)
# quit_button = ttk.Button(root, text="Quit", command=root.destroy)
# quit_button.pack(side="left", fill="both", expand=True)


my_label = ttk.Label(root, text="Name", padding=(30, 15), background="cyan")
my_label.pack(side="left", padx=(0, 10))

name_entry = ttk.Entry(root, width=15, textvariable=user_name)
name_entry.pack(side="left")
name_entry.focus()
greet_button = ttk.Button(root, text="Greet", command=greet)
greet_button.pack(side="left", fill="both", expand=True)
quit_button = ttk.Button(root, text="Quit", command=root.destroy)
quit_button.pack(side="left", fill="both", expand=True)
root.mainloop()
