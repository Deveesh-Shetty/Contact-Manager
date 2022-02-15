from tkinter import *

i=1
def save():
    global i
    print("Saved")
    with open("Contacts.txt","a") as f:
        f.write(f"{i}. Name: {name_value.get()} \nMobile Number: {contact_value.get()}\n\n")
        i += 1
    name_value.set("")
    contact_value.set("")

root = Tk()
root.title("Contact Manager")
root.geometry("400x500")
root.minsize(400,500)
root.maxsize(400,500)
root.config(bg="Navy Blue")

lb = Label(text="Contact Manager",bg="Navy Blue", fg="white", font="Montserrat 30 bold")
lb.pack(pady=20)
fr1 = Frame(root, bg="Navy Blue")
fr1.pack(anchor="n",pady=15)
lb = Label(fr1, text="Name",bg="Navy Blue", fg="white", font="Montserrat 12 bold")
lb.pack(pady=10, anchor ="nw")
fr2 = Frame(root, bg="Navy Blue")
fr2.pack(anchor="n")
lb = Label(fr2, text="Mobile Number",bg="Navy Blue", fg="white", font="Montserrat 12 bold")
lb.pack(pady=10, anchor="nw")

name_value = StringVar()
contact_value = StringVar()

name_entry = Entry(fr1,textvariable=name_value,width=30)
name_entry.pack(side=RIGHT, anchor="ne")
contact_entry = Entry(fr2,textvariable=contact_value,width=30)
contact_entry.pack(side=RIGHT, anchor="ne")

fr = Frame(root,bg="Navy Blue")
fr.pack(pady=30)
b = Button(fr, text="Save",command=save,width=10, bg="Light Grey",relief=GROOVE)
b.pack()

root.mainloop()