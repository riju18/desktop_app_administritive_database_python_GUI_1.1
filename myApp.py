from tkinter import *
import backend
import os

window = Tk()

rootDirectory = os.path.dirname(os.path.abspath(__file__))
window.iconbitmap(os.path.join(rootDirectory, 'safety-code.ico'))
window.title('employers information')

def get_row(event):
    global get_tuple_val
    index = list1.curselection()[0]
    get_tuple_val = list1.get(index)
    name_entry.delete(0, END)
    name_entry.insert(END, get_tuple_val[1])

    age_entry.delete(0, END)
    age_entry.insert(END, get_tuple_val[2])
    
    pro_entry.delete(0, END)
    pro_entry.insert(END, get_tuple_val[3])

    uid_entry.delete(0, END)
    uid_entry.insert(END, get_tuple_val[4])

def viewall():
    list1.delete(0, END)
    for values in backend.viewAll():
        list1.insert(END, values)


def addEntry():
    getName = name_entry.get()
    getAge = age_entry.get()
    getPro = pro_entry.get()
    getUId = uid_entry.get()

    backend.insert(getName, getAge, getPro, getUId)
    list1.delete(0, END)
    list1.insert(END, (getName, getAge, getPro, getUId))

def searchEntry():
    list1.delete(0, END)
    for values in backend.searchParticular(name_entry.get(),age_entry.get(),pro_entry.get(),uid_entry.get()):
        list1.insert(END, values)

def deleteEntry():
    backend.delete(get_tuple_val[0])


def update_entry():
    backend.update(get_tuple_val[0],name_entry.get(),age_entry.get(),pro_entry.get(),uid_entry.get())

window.geometry('500x300')
window.configure(background='#0F2027')

name = Label(window, text='Name:')
name.grid(row=0, column=0)

age = Label(window, text='Age:')
age.grid(row=0, column=2, padx=15, pady=10)

profession = Label(window, text='Profession:')
profession.grid(row=1, column=0)

user_id = Label(window, text='Id:')
user_id.grid(row=1, column=2)

name_entry = Entry(window, textvariable=StringVar())
name_entry.grid(row=0, column=1)

age_entry = Entry(window, textvariable=StringVar())
age_entry.grid(row=0, column=3)

pro_entry = Entry(window, textvariable=StringVar())
pro_entry.grid(row=1, column=1)

uid_entry = Entry(window, textvariable=StringVar())
uid_entry.grid(row=1, column=3)

list1 = Listbox(window, height=10, width=45)
list1.grid(row=2, column=0, rowspan=6, columnspan=2, pady=10, padx=7)


list1.bind('<<ListboxSelect>>', get_row)


sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.xview)

view_btn = Button(window, text='view all', command=viewall)
view_btn.grid(row=2, column=3, pady=10)

search_btn = Button(window, text='search', command=searchEntry)
search_btn.grid(row=3, column=3, pady=6)

add_btn = Button(window, text='add entry', command=addEntry)
add_btn.grid(row=4, column=3, pady=6)

up_btn = Button(window, text='update entry', command=update_entry)
up_btn.grid(row=5, column=3, pady=6)

del_btn = Button(window, text='delete entry', command=deleteEntry)
del_btn.grid(row=6, column=3, pady=6)

cls_btn = Button(window, text='close')
cls_btn.grid(row=7, column=3)

window.mainloop()
