from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import database
import tkinter as tk
#object for db class
dbase=database()
class crud:
    def modifyframe(self):
        #title
        title=Label(self.frame1,text="ALUMINI MANAGEMENT SYSTEM",font=("Calibr",18,"bold"),)
        title.grid(row=0,columnspan=2,padx=10,pady=20)
        # Adding textboxes and labels for other attributes
        label1 = Label(self.frame1, text="NAME", font=("Calibri", 18, "bold"))
        label1.grid(row=1, column=0,padx=10,pady=20)
        textname = Entry(self.frame1, textvariable=self.name)
        textname.grid(row=1, column=1,pady=20,columnspan=2)

        label2 = Label(self.frame1, text="AGE", font=("Calibri", 18, "bold"))
        label2.grid(row=2, column=0,padx=10,pady=20)
        textage = Entry(self.frame1, textvariable=self.age)
        textage.grid(row=2, column=1,pady=20,columnspan=2)

        label3 = Label(self.frame1, text="GENDER", font=("Calibri", 18, "bold"))
        label3.grid(row=3, column=0)
        textgender = Entry(self.frame1, textvariable=self.gender)
        textgender.grid(row=3, column=1,pady=20)

        label4 = Label(self.frame1, text="EMAIL", font=("Calibri", 18, "bold"))
        label4.grid(row=2, column=2,padx=25,pady=20)
        textemail = Entry(self.frame1, textvariable=self.email)
        textemail.grid(row=2, column=3,padx=10,pady=20)

        label5 = Label(self.frame1, text="CONTACT", font=("Calibri", 18, "bold"))
        label5.grid(row=3, column=2,padx=25,pady=20)
        textcontact = Entry(self.frame1, textvariable=self.contact)
        textcontact.grid(row=3, column=3,padx=10,pady=20)

        label6 = Label(self.frame1, text="ADDRESS", font=("Calibri", 18, "bold"))
        label6.grid(row=5, column=0)
        self.textaddress = tk.Text(self.frame1,width=40,height=4)#for textwidget we use get()
        self.address = self.textaddress.get("1.0", tk.END)
        self.textaddress.grid(row=5, column=1,padx=10,pady=20)
        #buttons
        bframe=Frame(self.frame1)
        bframe.grid(row=6,column=0,columnspan=4,padx=10,pady=10)
        #adding button to bttonframe
        b1 = tk.Button(bframe, text="ADD", background="#34eb98", fg="white",width=15, command=self.add)
        #note if we use add() it executed when init is call to avoid we use self.add
        b2 = tk.Button(bframe, text="UPDATE", background="#34eb98", fg="white",width=15, command=self.update)
        b3 = tk.Button(bframe, text="DELETE", background="#34eb98", fg="white",width=15, command=self.delete)
        b4 = tk.Button(bframe, text="CLEAR", background="#34eb98", fg="white",width=15, command=self.clearall)

        b1.grid(row=0,column=1)
        b2.grid(row=0,column=2)
        b3.grid(row=0,column=3)
        b4.grid(row=0,column=4)
        #treeframe
        tree=Frame(self.frame1)
        tree.place(x=0,y=500,width=1000,height=500)
        self.tv=ttk.Treeview(tree,columns=(1,2,3,4,5,6,7))
        self.tv.heading("1",text="ID")
        self.tv.heading("2",text="NAME")
        self.tv.heading("3",text="AGE")
        self.tv.heading("4",text="GENDER")
        self.tv.heading("5",text="EMAIL")
        self.tv.heading("6",text="CONTACT")
        self.tv.heading("7",text="ADDRESS")
        #to show headings only
        self.tv['show']='headings'
        self.tv.bind("<ButtonRelease-1>",self.getdata)
        self.tv.pack(fill=X)
        self.displayall()
    # Function to get the value when the button is clicked
    def getvalue(self):
        # Access the values using self.name.get(), self.age.get(), etc.
        print("Name:", self.name.get())
        print("Age:", self.age.get())
        print("Gender:", self.gender.get())
        print("Email:", self.email.get())
        print("Contact:", self.contact.get())
        self.address=self.textaddress.get("1.0",tk.END)
        print("Address:", self.address)
    def displayall(self):
        self.tv.delete(*self.tv.get_children())
        #fetching data form db
        for row in dbase.fetch():
            self.tv.insert("",END,values=row)
    def clearall(self):
        print("clearall called")
        # Declare variables to hold dynamic updates
        self.name.set("")
        self.age.set("")
        self.gender.set("")
        self.email.set("")
        self.contact.set("")
        #for text we use delete funtion
        self.textaddress.delete("1.0",tk.END)
        self.address=self.textaddress.get("1.0",tk.END)
    def add(self):
        self.address = self.textaddress.get("1.0", tk.END)
        self.getvalue()#to update values before if
        if self.name.get()=="" or self.age.get()=="" or self.gender.get()==""  or self.email.get()=="" or self.contact.get()=="" or self.textaddress.get("1.0",tk.END)=="":#self.textaddress beacuse of what inside textbox

            messagebox.showerror("error in input","please fill all details")
            return
        dbase.insert(self.name.get(),self.age.get(),self.gender.get(),self.email.get(),self.contact.get(),self.address)
        messagebox.showinfo("SUCCESS","RECORD INSERTED")
        self.displayall()
        self.clearall()
        print("add done")
    def getdata(self, event):       
        selectedrow = self.tv.focus()
        data = self.tv.item(selectedrow)
        self.row = data["values"]
        self.uid.set(self.row[0]) 
        self.name.set(self.row[1])
        self.age.set(self.row[2])
        self.gender.set(self.row[3])
        self.email.set(self.row[4])
        self.contact.set(self.row[5])
        self.textaddress.delete("1.0", tk.END)
        self.textaddress.insert(tk.END, self.row[6])
        print("getdata done")
        
    def update(self):
        self.address = self.textaddress.get("1.0", tk.END)
        self.getvalue()#to update values before if
        if self.name.get()=="" or self.age.get()=="" or self.gender.get()==""  or self.email.get()=="" or self.contact.get()=="" or self.textaddress.get("1.0",tk.END)=="":#self.textaddress beacuse of what inside textbox
            messagebox.showerror("ERROR IN INPUT","PLEASE FILL ALL DETAILS")
            return
        dbase.update(self.name.get(),self.age.get(),self.gender.get(),self.email.get(),self.contact.get(),self.address,self.uid)
        print("update done")
        messagebox.showinfo("SUCCESS","RECORD UPDATED")
        self.displayall()
        self.clearall()
    def delete(self):
        dbase.delete(self.uid)
        messagebox.showinfo("SUCCESS","RECORD DELETED")
        self.displayall()
        self.clearall()
    def __init__(self, frame1):
        self.frame1 = frame1
        # Declare variables to hold dynamic updates
        self.name = tk.StringVar()
        self.age = tk.StringVar()
        self.gender = tk.StringVar()
        self.email = tk.StringVar()
        self.contact = tk.StringVar()
        self.address = tk.StringVar()
        self.uid = tk.StringVar()       
        #note only after declearing varible you call method, don't call before this line
        self.modifyframe()
        



    

    
