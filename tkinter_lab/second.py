import tkinter as tk
from tkinter import ttk

root = tk.Tk()


main = ttk.Labelframe(root, text="some")
main.pack(side="left", fill="both", expand=True)
rect1 = ttk.Label(main, text="number1", background="green", foreground="white")
rect1.pack(ipadx=10, ipady=10, fill="both", expand=True)
rect2 = ttk.Label(main, text="number2", background="blue", foreground="white")
rect2.pack(ipadx=10, ipady=10)

root.mainloop()
