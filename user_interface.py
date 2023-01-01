import tkinter as tk
from tkinter import ttk
import tkinter.font as font

import web


def update(my_list, all_data):
    for index, data in enumerate(all_data):
        my_list.insert("end", f"{data['id']}. {data['question']}")
        my_list.grid(row=0, column=0)


def crawling(my_list):
    web.crawl()
    all_data = web.show_all_data("QA")
    update(my_list, all_data)


root = tk.Tk()
font.nametofont('TkDefaultFont').configure(family="Arial", size=15)
root.columnconfigure(0, weight=1)

all_data = web.show_all_data("QA")
scrollbar = ttk.Scrollbar(root, orient="vertical")
my_list = tk.Listbox(root, width=800, height=25, yscrollcommand=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky="ns")
update(my_list, all_data)

# scrollbar.config(command=my_list.yview)
scrollbar["command"] = my_list.yview

button = ttk.Button(root, text="Crawl",
                    command=lambda: crawling(my_list))
button.grid(row=1, column=0, columnspan=2)


root.mainloop()
