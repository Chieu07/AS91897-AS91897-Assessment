from tkinter import *# This code to import tkinter,so we can make a GUI
main_window = Tk()

Label(main_window, text=" Hire Store", font=("Arial",25)).grid(row=0, column=1)


# Create a quit function
def quit ():
    main_window.destroy()
Button(main_window, text = "Quit",command= quit, width=6).grid(row=0, column=5)


#Set up buttons and Labels

def setup():
    
    Label(main_window,text="Customer Full Name").grid(column=0,row=2)
    entry_customers = Entry(main_window).grid(column=1,row=2)
    Label(main_window, text=" Item Hired").grid(column=0, row=3)
    entry_Item=Entry(main_window).grid(column=1,row=3)
    Label(main_window,text="Receipt Number").grid(column=3,row=2)
    entry_receipt= Entry(main_window).grid(column=4,row=2)
    Label(main_window,text="Number Hired").grid(column=3,row=3)
    entry_number=Entry(main_window).grid(column=4,row=3)
    Label(main_window,text="Only Type IF You Need To Return Items",wraplength=150).grid(column=1,row=4)
    Label(main_window,text="Row#").grid(column=0,row=5)
    entry_row=Entry(main_window).grid(column=1,row=5)
    Button(main_window,text="Update Details",width=10).grid(column=4,row=4,sticky=E)
    Button(main_window,text="Print Details",width=10).grid(column=4,row=5,sticky=E)
    Button(main_window,text="Delete",width=10).grid(column=1,row=6)
setup()
    
            
        
    
