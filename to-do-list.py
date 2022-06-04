from tkinter import *
import pickle

root = Tk()
root.title('To Do List App')
root.geometry("500x500")

# Create frame
my_frame = Frame(root)
my_frame.pack(pady=10)

# Create listbox
my_list = Listbox(my_frame,
            width=80,
            height=22,
            bg="SystemButtonFace",
            bd=0,
            fg="#464646",
            highlightthickness=0,
            selectbackground="#a6a6a6",
            activestyle="none")
my_list.pack(side=LEFT, fill=BOTH)

# stuff = ["Walk The Dog", "Buy Groceries", "Take A Nap", "Learn Tkinter", "Rule The World"]
# for item in stuff:
# 	my_list.insert(END, item)

# Create Scrollbar
my_scrollbar = Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT, fill=BOTH)

# Add scrollbar
my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)

# Create entry box
my_entry = Entry(root, width=30)
my_entry.pack(pady=20)

# Create a button frame
button_frame = Frame(root)
button_frame.pack(pady=20)

# Functions
def add_item():
    my_list.insert(END, my_entry.get())
    my_entry.delete(0, END)

def delete_item():
    my_list.delete(ANCHOR) # delete highlighed items

def cross_item():
    my_list.itemconfig(my_list.curselection(), fg="#dedede")
    
    my_list.select_clear(0, END)
def uncross_item():
    my_list.itemconfig(my_list.curselection(), fg="#464646")
    my_list.select_clear(0, END)

def delete_crossed():
    count = 0
    while count < my_list.size():
        if my_list.itemcget(count, "fg")  == "#dedede":
            my_list.delete(my_list.index(count))
        else:
            count += 1

# Add buttons
add_button = Button(button_frame, text="Add", command=add_item)
delete_button = Button(button_frame, text="Delete", command=delete_item)
cross_button = Button(button_frame, text="Cross", command=cross_item)
uncross_button = Button(button_frame, text="Uncross", command=uncross_item)
delete_crossed_button = Button(button_frame, text="Delete Crossed", command=delete_crossed)

add_button.grid(row=0, column=1, padx=20)
delete_button.grid(row=0, column=0)
cross_button.grid(row=0, column=2)
uncross_button.grid(row=0, column=3, padx=20)
delete_crossed_button.grid(row=0, column=4)

root.mainloop()