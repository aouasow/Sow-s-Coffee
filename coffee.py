"""
Author : Aoua Sow
Final Project : Sow's Coffee
Date : 07/12/2024
DESC: a GUI app python tkinter for coffee ordering system

"""

from os import W_OK
from tkinter import *

def clicked():
    value = myEntry.get(())
    myLabel.configure(text=value)

window = Tk()
window.title("Sow's Coffee" )
window.geometry("400x400")

myEntry = Entry(window, width=15)
myLabel = Label(window, text = "Menu")
myButton = Button(window, text= "Order Now", command=clicked)

checkSate = BooleanVar()
checkSate.set(True)
myCheck1 = Checkbutton(window, text="French Vanilla", var=checkSate)
myCheck2 = Checkbutton(window, text="Cappuccino")
myCheck3 = Checkbutton(window, text="House Blend")
myCheck4 = Checkbutton(window, text="Iced Coffee")

radioState = StringVar()
radioState.set("COD")
myRadio1 = Radiobutton(window, text="Debit Card", value="DC", variable= radioState)
myRadio2 = Radiobutton(window, text="Credit Card", value="CD", variable=radioState)
myRadio3 = Radiobutton(window, text="Cash on Delivery", value="COD", variable=radioState)

myLabel.grid(row=0, column=0)
myEntry.grid(row=1, column=0)
myButton.grid(row=10, column=0)
myCheck1.grid(row=3, column=0)
myCheck2.grid(row=4, column=0)
myCheck3.grid(row=5, column=0)
myCheck4.grid(row=6, column=0)
myRadio1.grid(row=7, column=0, sticky="w")
myRadio2.grid(row=8, column=0, sticky="w")
myRadio3.grid(row=9, column=0, sticky="w")

window.mainloop()
