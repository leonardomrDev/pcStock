from tkinter import *

# Hook the Tk.Buttons to this function commands
def migrate_list():
    print('Migrate')
#------------------------
def add():
    print('Add Item')
#------------------------
def remove():
    print('Remove Item')
#------------------------
def edit():
    print('Edit Item')
# App Window -----------------------------------------------
app = Tk()
app.title("PCStock: Inventory Manager for Computer Parts")
app.geometry("800x400")
#-----------------------------------------------------------

# Item Insert Labels ----------------------------------------------------
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

price_text = StringVar()
price_label = Label(app, text='Item Price', font=("bold", 12), pady= 10, padx=20)
price_label.grid(row= 2, column= 0, sticky=W)
price_entry = Entry(app, textvariable=price_text)
price_entry.grid(row= 2, column= 1, sticky=W)
#----------------------------------------------------------------------------

# List of Items on Inventory ------------------------------------------------
item_list = Listbox(app, height= 10, width= 60, border= 0)
item_list.grid(row= 3, column= 0, columnspan= 3, rowspan= 6, pady= 20, padx= 20)
#----------------------------------------------------------------------------

# Scrollbar for the List of Items in Inventory-------------------------------
scrollbar = Scrollbar(app).grid(row=3, column=3)
# Connects the Scrollbar to the list
"""
item_list.configure(yscrollcommand= scrollbar.set)
scrollbar.configure(command=item_list.yview)
#-----------------------------------------------------------------------------
"""

#------------------------------------------------------------------------------
Button(app, text="Add", width= 12, command=add, font=("bold", 12)).grid(row=10, column=0, sticky=W, padx=20)
Button(app, text="Edit", width= 12, command=edit, font=("bold", 12)).grid(row=10, column=1, sticky=W, padx=20)
Button(app, text="Delete", width= 12, command=remove, font=("bold", 12)).grid(row=10, column=2, sticky=W, padx=20)
#------------------------------------------------------------------------------

# Migrate our Data
migrate_list()
# Command to Run the App -------------------
app.mainloop()
#--------------------------------------------


