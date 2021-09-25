from tkinter import *
from tkinter import messagebox
from db import Database

db = Database('App.db')

# CRUD

# Hook the Tk.Buttons to this function commands ---------------------------------
def migrate():
    item_list.delete(0, END)
    for row in db.get():
        item_list.insert(END, row)
#---------------------------------------------------------------------------------
def select(event):
    global selectedItem
    index = item_list.curselection()[0]
    selectedItem = item_list.get(index)
    print(selectedItem)

    itemname_entry.delete(0, END)
    itemname_entry.insert(END, selectedItem[1])
    
    itembrand_entry.delete(0, END)
    itembrand_entry.insert(END, selectedItem[2])

    itemprice_entry.delete(0, END)
    itemprice_entry.insert(END, selectedItem[3])
#------------------------------------------------------------------------------------
def add():
    if item_text.get() == "" or brand_text.get() == "" or itemprice_text.get() == "":
        messagebox.showerror('Required Fields', "Please, fill all the fields! ")
        return
    db.add(item_text.get(), brand_text.get(), itemprice_text.get())
    item_list.delete(0, END)
    item_list.insert(END, (item_text.get(), brand_text.get(), itemprice_text.get()))
    migrate()
#-------------------------------------------------------------------------------------
def remove():
    db.remove(selectedItem[0])
    migrate()
#------------------------------------------------------------------------------------
def edit():
    db.edit(selectedItem[0], item_text.get(), brand_text.get(), itemprice_text.get())
    migrate()
# App Window ------------------------------------------------------------------------
app = Tk()
app.title("PCStock: Inventory Manager for Computer Parts")
app.geometry("800x400")
#-------------------------------------------------------------------------------------

# Item Insert Labels -----------------------------------------------------------------
item_text = StringVar()
itemname_label = Label(app, text='Item Name', font=("bold", 12), pady= 10, padx=20)
itemname_label.grid(row= 0, column= 0, sticky=W)
itemname_entry = Entry(app, textvariable=item_text)
itemname_entry.grid(row= 0, column= 1, sticky=W)

brand_text = StringVar()
itembrand_label = Label(app, text='Item Brand', font=("bold", 12), pady= 10, padx=20)
itembrand_label.grid(row= 1, column= 0, sticky=W)
itembrand_entry = Entry(app, textvariable=brand_text)
itembrand_entry.grid(row= 1, column= 1, sticky=W)

itemprice_text = StringVar()
itemprice_label = Label(app, text='Item Price', font=("bold", 12), pady= 10, padx=20)
itemprice_label.grid(row= 2, column= 0, sticky=W)
itemprice_entry = Entry(app, textvariable=itemprice_text)
itemprice_entry.grid(row= 2, column= 1, sticky=W)
#---------------------------------------------------------------------------------------

# List of Items on Inventory ----------------------------------------------------
item_list = Listbox(app, height= 10, width= 60, border= 0)
item_list.grid(row= 3, column= 0, columnspan= 3, rowspan= 6, pady= 20, padx= 20)
item_list.bind('<<ListboxSelect>>', select)
#---------------------------------------------------------------------------------

# Scrollbar for the List of Items in Inventory----
scrollbar = Scrollbar(app).grid(row=3, column=3)
#-----------------------------------------------------------------------------------------------------------------
addb = PhotoImage(file = 'addbutton.png')
Button(app, image=addb, border=0, command=add, font=("bold", 12)).grid(row=10, column=0, sticky=W, padx=20)
editb = PhotoImage(file = 'editbutton.png')
Button(app, image=editb, border=0, command=edit, font=("bold", 12)).grid(row=10, column=2, sticky=W, padx=20)
removeb = PhotoImage(file = 'removebutton.png')
Button(app, image=removeb, border=0, command=remove, font=("bold", 12)).grid(row=10, column=1, sticky=W, padx=20)
#------------------------------------------------------------------------------------------------------------------

migrate()

# Command to Run the App --------------------
app.mainloop()
#--------------------------------------------


