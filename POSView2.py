# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 12:30:00 2016

@author: Carlos
"""

import POSController 
import tkinter as tk
from tkinter import Menu
from tkinter import ttk
from tkinter import messagebox
from matplotlib import pyplot as plt

"""
Desc: Print the message to the user, this was made to encapsulate the print command,
    so controller can call this function without caring how actually the print is done
Param: Info Message to be printed
Return: 
"""
def PrintToUser(Msg):
    messagebox.showinfo(title="Info",message=Msg)
    
"""
Commands for subwindows (pop-ups)
"""

"""
Visualize AddSale
"""   
def winSale():
    # create child window
    win = tk.Toplevel()
    win.grab_set()
    win.title("Sales per customer")
    win.geometry("200x200")
    # display message
    message = "Sales per customer"
    ttk.Label(win, text=message).grid()
    # quit child window and return to root window
    ttk.Button(win, text='OK', command=win.destroy).grid()  

"""
Function for storing SKUs
Does some checks on the view
Calls CheckSKUCommand for checks on info stored
Returns success or failure to display message on screen
"""   
def storeSKU(entries):
   error=0 
   newSKU=[]
   for entry in entries:
      text  = entry.get()
      newSKU.append(text)
      if not entry.get():        #If either ID or Customer empty
          messagebox.showerror(title="Error",message="Some fields are empty, please fill and retry")
          error=1
   
   if error !=1:      
      print(newSKU)
      message=POSController.CheckSKUCommand(newSKU)
      print(message)

"""
Function for storing customers
Does some checks on the view
Calls CheckCustomerCommand for checks on info stored
Returns success or failure to display message on screen
"""   
def storeC(entries):
   error=0 
   newC=[]
   for entry in entries:
      text  = entry.get()
      newC.append(text)
      if not entry.get():        #If either ID or Customer empty
          messagebox.showerror(title="Error",message="Some fields are empty, please fill and retry")
          error=1
   
   if error !=1:      
      print(newC)
      message=POSController.CheckCustomerCommand(newC)
      print(message)
"""
Function for creating SKU and customer text fields
Inputs: window it comes from, fields to fill in
Output: entries of the fields
""" 

def dinamicform(window, fields):
   entries = []
   for field in fields:
      row = ttk.Frame(window)
      lab = ttk.Label(row, width=15, text=field, anchor='w')
      ent = ttk.Entry(row)
      row.pack()
      lab.pack()
      ent.pack()
      entries.append(ent)
   return entries

"""
Visualize AddSale
"""      
def winAddSKU():
    # create child window
    fields="Item name","ID"    
    win = tk.Toplevel()
    ents = dinamicform(win, fields)
#    radio1=tk.Radiobutton(win,variable=radVar,command=radCall)
    win.bind('<Return>', (lambda event, e=ents: storeC(e)))   
    b1 = ttk.Button(win, text='Store or press ENTER',command=(lambda e=ents: storeC(e)))
    b1.pack()
    b2 = ttk.Button(win, text='Quit', command=win.destroy)
    b2.pack()

"""
Visualize AddCustomer
"""      
def winAddCust():
    # create child window
    fields="Customer", "ID (9 digits)"    
    win = tk.Toplevel()
    win.geometry("200x200")
    ents = dinamicform(win, fields)
    win.bind('<Return>', (lambda event, e=ents: storeC(e)))   
    b1 = ttk.Button(win, text='Store or press ENTER',command=(lambda e=ents: storeC(e)))
    b1.pack()
    b2 = ttk.Button(win, text='Quit', command=win.destroy)
    b2.pack()
    
"""
Close of sales prompt
"""
def _mCloseSales():
    outcome=messagebox.askyesno(title="Close Sales", message="are you sure?")
    if outcome>0:
        POSController.CloseSalesDay()
        return

"""
Exit
""" 
def _quit():
    outcome=messagebox.askyesno(title="Exit program", message="are you sure?")
    if outcome>0:
        win_root.quit()
        win_root.destroy()
        exit()
        
"""
Visualize report
"""      
def winReport():
    data=POSController.PrepareReport()
    print(data)    
    n=range(len(data))
    print(n)  
    y=[num for (pay,num) in data ]
    labels=[pay for (pay,num) in data ]
    width=1
    plt.bar(n,y,width,color="red")
    plt.xticks(n,labels)
    plt.show()

"""
Visualize CRM
"""   
def winCRM():
    # create child window
    data=POSController.PrepareCRM()
    print(data)    
    n=range(len(data))
    print(n)  
    y=data.values()
    labels=data.keys()
    width=1
    plt.bar(n,y,width,color="red")
    plt.xticks(n,labels)
    plt.show()


"""
Main window starts here
"""
#Main window
win_root=tk.Tk()
win_root.title("El Corte Ingles POS")
background_image=tk.PhotoImage(file="files/eci.gif")
background_label = tk.Label(win_root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
win_root.geometry("400x400")

menuBar = Menu(win_root)
win_root.config(menu=menuBar)


"""
Submenus
"""
#cascade for file
fileMenu=Menu(menuBar,tearoff=0)
menuBar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Backup")
fileMenu.add_command(label="Restore Backup")
fileMenu.add_separator()
fileMenu.add_command(label="Close Day",command=_mCloseSales)
fileMenu.add_command(label="Exit",command=_quit)

#cascade for sales
saleMenu=Menu(menuBar,tearoff=0)
menuBar.add_cascade(label="Sales", menu=saleMenu)
saleMenu.add_command(label="New Sale")
saleMenu.add_command(label="Edit Sale")

#cascade for customers
customerMenu=Menu(menuBar,tearoff=0)
menuBar.add_cascade(label="Customer", menu=customerMenu)
customerMenu.add_command(label="New Customer", command=winAddCust)
customerMenu.add_command(label="Show Customers")

#cascade for SKUs
SKUMenu=Menu(menuBar,tearoff=0)
menuBar.add_cascade(label="SKU", menu=SKUMenu)
SKUMenu.add_command(label="New SKU",command=winAddSKU)
SKUMenu.add_command(label="Show SKUs")

#cascade for reports
reportMenu=Menu(menuBar,tearoff=0)
menuBar.add_cascade(label="Reports", menu=reportMenu)
reportMenu.add_command(label="Sales per customer", command=winCRM)
reportMenu.add_command(label="Sales per payment type", command=winReport)
reportMenu.add_command(label="Sales per day")


"""
Start GUI
"""

#start main GUI loop
def main():
    win_root.mainloop()