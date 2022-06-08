from tkinter import *# This code to import tkinter,so we can make a GUI
main_window = Tk()

Label(main_window, text=" Hire Store", font="Times 30 italic bold",bg="Yellow").grid(row=0, column=3)


# Create a quit function
def quit ():
    main_window.destroy()
Button(main_window, text = "Quit",command= quit, fg = "black", width=7, highlightbackground="yellow").grid(row=0, column=5,sticky=N)


#Set up buttons and Labels

def setup_window():
    main_window.title("Hire Store")
    main_window.configure(bg="sky blue")
    Label(main_window,text=" Full Name",bg="sky blue").grid(column=0,row=2)
    entry_customers = Entry(main_window).grid(column=1,row=2)
    Label(main_window, text=" Item Hired",bg="Sky Blue").grid(column=0, row=3)
    entry_Item=Entry(main_window).grid(column=1,row=3)
    Label(main_window,text="Receipt Number",bg="Sky Blue").grid(column=3,row=2)
    entry_receipt= Entry(main_window).grid(column=4,row=2)
    Label(main_window,text="Number Hired",bg="Sky Blue").grid(column=3,row=3)
    entry_number=Entry(main_window).grid(column=4,row=3)
    Label(main_window,text="Only type row number if you need return Items",bg="Sky Blue",fg="red",).grid(column=1,row=4,sticky=S)
    Label(main_window,text="Row#",bg="Sky Blue").grid(column=0,row=5)
    entry_row=Entry(main_window).grid(column=1,row=5)
    Button(main_window,text="Update Details",width=10, fg="red",bg="blue",pady=5).grid(column=4,row=4,sticky=E)
    Button(main_window,text="Print Details",width=10,fg="red",bg="blue",pady=5).grid(column=4,row=5,sticky=E)
    Button(main_window,text="Delete",width=10,fg="red",bg="blue",pady=5).grid(column=1,row=6)
setup_window()
    
            
        
