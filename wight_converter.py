import tkinter as tk 

#Create a GUI Window

window = tk.Tk()
window.title("Weight Converter")
window.geometry("620x400+0+0")
window.resizable(False,False)

#textvariable
wt =tk.StringVar()


#function Convert Weight KG to Gram,Pound and Ounce.

def convert_kg():
    #Convert KG to gram
    gram = float(wt.get())*1000

    #Convert KG to Pounds
    pounds = float(wt.get())*2.20462

    #Convert KG to Ounce
    ounce = float(wt.get())*35.274

    gram_entry.delete(0,tk.END)
    gram_entry.insert(tk.END,gram)

    pound_entry.delete(0,tk.END)
    pound_entry.insert(tk.END,pounds)

    ounce_entry.delete(0,tk.END)
    ounce_entry.insert(tk.END,ounce)


#Clear function used for clear all the Entry Widgets
def clear():
    kg_entry.delete(0,tk.END)
    gram_entry.delete(0,tk.END)
    pound_entry.delete(0,tk.END)
    ounce_entry.delete(0,tk.END)

#---------------------Create the Label Widgets------------------------

weight_label= tk.Label(window,text="Enter the weight in Kg")
gram_label= tk.Label(window,text="gram")
pound_label= tk.Label(window,text="Pounds")
ounce_label= tk.Label(window,text="Ounce")

#---------------------Grid methods used for placeing the widgets at respective positions--------
weight_label.grid(row=0,column=0,padx=10,pady=10)
gram_label.grid(row=1,column=0,pady=10)
pound_label.grid(row=1,column=1,pady=10)
ounce_label.grid(row=1,column=2,pady=10)

#---------------------Create the Entry Widgets----------------------------------------
kg_entry= tk.Entry(window,width=30,textvariable=wt)
gram_entry= tk.Entry(window,width=30)
pound_entry= tk.Entry(window,width=30)
ounce_entry= tk.Entry(window,width=30)
kg_entry.focus()

# ------------------------------Entry Placeing at respective Positons--------------------------
kg_entry.grid(row=0,column=1,padx=10,pady=10)
gram_entry.grid(row=2,column=0,padx=10)
pound_entry.grid(row=2,column=1,padx=10)
ounce_entry.grid(row=2,column=2,padx=10)

#---------------------------------Create Buttons------------------------------------------------
convert_button = tk.Button(window,text="convert",command=convert_kg)
clear_button = tk.Button(window,width=25,text="Clear",command=clear)

#--------------------------------Buttons Positions----------------------------------------------
convert_button.grid(row=0,column=2,padx=10,pady=10)
clear_button.grid(row=3,column=1,pady=10)

window.mainloop()