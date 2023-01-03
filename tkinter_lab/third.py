import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


# root = tk.Tk()

# user_name = tk.StringVar()
# # Frame for input
# input_frame = ttk.LabelFrame(root, text="input", padding=(10, 15, 10, 15))
# input_frame.pack(fill="both", expand=True)

# input_label = ttk.Label(input_frame, text="name")
# input_label.pack(side="left", expand=True, fill="both", padx=10)
# input_label = ttk.Entry(input_frame, textvariable=user_name)
# input_label.pack(side="left", expand=True, fill="both")

# # buttons Frame

# buttons_frame = ttk.LabelFrame(root, text="buttons", padding=(10, 15))
# buttons_frame.pack(fill="both", expand=True)

# greet_button = ttk.Button(buttons_frame, text="greet")
# greet_button.pack(side="left", fill="both", expand=True)
# quit_button = ttk.Button(buttons_frame, text="quit")
# quit_button.pack(side="left", fill="both", expand=True)

# root.mainloop()


# using grid layout manager
root = tk.Tk()
root.geometry("250x150")
root.resizable(False, False)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

# adding image to label:
image = Image.open("tkinter_lab\images\strawberry.png").resize((15, 20))
photo = ImageTk.PhotoImage(image)


user_name = tk.StringVar()
# Frame for input
input_frame = ttk.LabelFrame(root, text="input", padding=(10, 15, 10, 15))
input_frame.grid(row=0, column=0, sticky="nsew")

input_frame.columnconfigure(0, weight=1)
input_frame.columnconfigure(1, weight=1)
input_frame.rowconfigure(0, weight=1)

input_label = ttk.Label(input_frame, text="name", image=photo, compound="left")
input_label.grid(row=0, column=0, padx=10, sticky="nsew")
input_label.config(font=("Arial", 10))
input_label = ttk.Entry(input_frame, textvariable=user_name)
input_label.grid(row=0, column=1, sticky="nsew")

# buttons Frame

buttons_frame = ttk.LabelFrame(root, text="buttons", padding=(10, 15))
buttons_frame.grid(row=1, column=0, sticky="nsew")

buttons_frame.columnconfigure(0, weight=1)
buttons_frame.columnconfigure(1, weight=1)
buttons_frame.rowconfigure(0, weight=1)


greet_button = ttk.Button(buttons_frame, text="greet")
greet_button.grid(row=0, column=0, padx=10, sticky="nsew")
quit_button = ttk.Button(buttons_frame, text="quit")
quit_button.grid(row=0, column=1, sticky="nsew")

root.mainloop()
