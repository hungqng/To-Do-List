from fileinput import filename
from tkinter import *
from tkinter import filedialog
import pickle
import smartsheet

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

# test = ["Morning walk", "Exercise", "Check email", "Read the news", "Study"]
# for item in test:
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

def save_list():
    file_name = filedialog.asksaveasfilename(
                                            initialdir="D:\School\Programming\Python\To Do List",
                                            title="Save File",
                                            filetypes=(
                                                        ("Text Files", "*.txt"),
                                                        #("Excel Files", "*.xls"),
                                                        # ("Dat Files", "*.dat"),
                                                        ("All Files", "*.*"))
    )
    if file_name:
        if file_name.endswith(".txt"):
            pass
        else:
            file_name = f'{file_name}.txt'
        count = 0
        while count < my_list.size():
            if my_list.itemcget(count, "fg") == "#dedede":
                my_list.delete(my_list.index(count))
            else:
                count += 1
        
        stuff = my_list.get(0, END)

        # Open the file
        output_file = open(file_name, 'wb')

        # Add items to the file
        pickle.dump(stuff, output_file)

    
def open_list():
    file_name = filedialog.askopenfilename(
                                            initialdir="D:\School\Programming\Python\To Do List",
                                            title="Open File",
                                            filetypes=(
                                                        ("Text Files", "*.txt"),
                                                        #("Excel Files", "*.xls"),
                                                        # ("Dat Files", "*.dat"),
                                                        ("All Files", "*.*"))
    )
    if file_name:
        # Delete current list
        my_list.delete(0, END)

        # Open the file
        input_file = open(file_name, 'rb')

        # Load the file
        stuff = pickle.load(input_file)

        # Display the content
        for item in stuff:
            my_list.insert(END, item)

def delete_list():
    my_list.delete(0, END)

# Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Add items to the menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)

# Add dropdown
file_menu.add_command(label="Save List", command=save_list)
file_menu.add_command(label="Open List", command=open_list)
file_menu.add_separator
file_menu.add_command(label="Clear List", command=delete_list)

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