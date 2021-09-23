from tkinter import * 

# App Window -----------------------------------------------
app = Tk()
app.title("PCStock: Inventory Manager for Computer Parts")
app.geometry("800x400")
#-----------------------------------------------------------

# Item Insert Labels ----------------------------------------------------
item_text = StringVar()
item_label = Label(app, text='Item Name', font=("bold", 12), pady= 10, padx=20)
item_label.grid(row= 0, column= 0, sticky=W)
item_entry = Entry(app, textvariable=item_text)
item_entry.grid(row= 0, column= 1, sticky=W)

item_text = StringVar()
item_label = Label(app, text='Item Brand', font=("bold", 12), pady= 10, padx=20)
item_label.grid(row= 1, column= 0, sticky=W)
item_entry = Entry(app, textvariable=item_text)
item_entry.grid(row= 1, column= 1, sticky=W)

item_text = StringVar()
item_label = Label(app, text='Item Price', font=("bold", 12), pady= 10, padx=20)
item_label.grid(row= 2, column= 0, sticky=W)
item_entry = Entry(app, textvariable=item_text)
item_entry.grid(row= 2, column= 1, sticky=W)
#----------------------------------------------------------------------------

# List of Items on Inventory ------------------------------------------------
item_list = Listbox(app, height= 10, width= 60, border= 0)
item_list.grid(row= 3, column= 0, columnspan= 3, rowspan= 6, pady= 20, padx= 20)
#----------------------------------------------------------------------------

# Scrollbar for the List of Items in Inventory-------------------------------
Scrollbar(app).grid(row=4, column=3)
# Connects the Scrollbar to the list
"""
item_list.configure(yscrollcommand= scrollbar.set)
scrollbar.configure(command=item_list.yview)
#-----------------------------------------------------------------------------
"""

#------------------------------------------------------------------------------
Button(app, text="Add", font=("bold", 12)).grid(row=10, column=0, sticky=W, padx=20)
Button(app, text="Edit", font=("bold", 12)).grid(row=10, column=2, sticky=W, padx=20)
Button(app, text="Delete", font=("bold", 12)).grid(row=10, column=4, sticky=W, padx=20)
#------------------------------------------------------------------------------

# Command to Run the App -------------------
app.mainloop()
#--------------------------------------------


