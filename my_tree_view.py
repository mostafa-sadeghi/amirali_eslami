from tkinter import ttk, END
import tkinter as tk


def add_record():
    global count
    my_tree.insert(parent='', index='end', iid=count, text="",
                   values=(name_box.get(), id_box.get(), food_box.get()))
    count += 1
    name_box.delete(0, END)
    id_box.delete(0, END)
    food_box.delete(0, END)


root = tk.Tk()
# create treeview
my_tree = ttk.Treeview(root)
my_tree['columns'] = ("Name", "ID", "Food")
# format our columns
my_tree.column("#0", width=0, stretch="no")
my_tree.column("Name", anchor="w", width=120)
my_tree.column("ID", anchor="center", width=80)
my_tree.column("Food", anchor="w", width=120)
# create headings:
my_tree.heading("#0", text="", anchor="w")
my_tree.heading("Name", text="Name", anchor="w")
my_tree.heading("ID", text="Id", anchor="w")
my_tree.heading("Food", text="Food", anchor="w")

# add data
# my_tree.insert(parent='', index='end', iid=0, text="",
#                values=("nikan", 1, "hamburger"))
# my_tree.insert(parent='', index='end', iid=1, text="",
#                values=("vihan", 2, "pizza"))

# # adding child
# my_tree.insert(parent='0', index='end', iid=2, text="",
#                values=("rozhman", 2, "cheese"))


# Adding data
data = [
    ["nima", 1, "pepperoni"],
    ["reza", 2, "hamburger"],
    ["ali", 3, "pepperoni"],
    ["sima", 4, "pizza"],
]

count = 0
for i, record in enumerate(data):
    my_tree.insert(parent='', index='end', iid=count, text="",
                   values=(record[0], record[1], record[2]))
    count += 1

my_tree.pack(pady=20)

add_frame = ttk.Frame(root)
add_frame.pack(pady=20)

# adding Labels

nl = ttk.Label(add_frame, text="Name")
nl.grid(row=0, column=0)
il = ttk.Label(add_frame, text="Id")
il.grid(row=0, column=1)
fl = ttk.Label(add_frame, text="food")
fl.grid(row=0, column=2)

# adding entru boxes:
name_box = ttk.Entry(add_frame)
name_box.grid(row=1, column=0)
id_box = ttk.Entry(add_frame)
id_box.grid(row=1, column=1)
food_box = ttk.Entry(add_frame)
food_box.grid(row=1, column=2)
# adding Buttons
add_record = ttk.Button(root, text="Add record", command=add_record)
add_record.pack(pady=20)

# todo removing all items/ removing one item/removing manay items/ Adding Scrollbar to our treeview


root.mainloop()
