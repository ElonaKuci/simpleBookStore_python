from tkinter import *
import backend


def get_selected_row(event):
  try:
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])
  except IndexError:
        pass



def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row )

def search_command():
    list1.delete(0,END)
    for row in backend.search(title_value.get(),author_value.get(),year_value.get(),isbn_value.get()):
        list1.insert(END,row)

def insert_command():
    backend.insert(title_value.get(),author_value.get(),year_value.get(),isbn_value.get())
    list1.delete(0,END)
    list1.insert(END,(title_value.get(),author_value.get(),year_value.get(),isbn_value.get()))

def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    backend.update(selected_tuple[0],title_value.get(),author_value.get(),year_value.get(),isbn_value.get())


window= Tk()


l1=Label(window,text="Title:")
l1.grid(row=0,column=0)

title_value=StringVar()
e1=Entry(window, textvariable=title_value)
e1.grid(row=0,column=1)

l2=Label(window,text="Author:")
l2.grid(row=0,column=2)
author_value=StringVar()
e2=Entry(window, textvariable=author_value)
e2.grid(row=0,column=3)

l1=Label(window,text="Year:")
l1.grid(row=1,column=0)
year_value=StringVar()
e3=Entry(window, textvariable=year_value)
e3.grid(row=1,column=1)

l1=Label(window,text="ISBN:")
l1.grid(row=1,column=2)
isbn_value=StringVar()
e4=Entry(window, textvariable=isbn_value)
e4.grid(row=1,column=3)


b1=Button(window,text="View All",command=view_command,width="15")
b1.grid(row=3,column=3)

b2=Button(window,text="Search Entry",command=search_command,width="15")
b2.grid(row=4,column=3)

b3=Button(window,text="Add Entry",command=insert_command,width="15")
b3.grid(row=5,column=3)

b4=Button(window,text="Update Selected",command=update_command,width="15")
b4.grid(row=6,column=3)

b5=Button(window,text="Delete Selected",command=delete_command,width=15)
b5.grid(row=7,column=3)

b6=Button(window,text="Close",command=window.destroy,width=15)
b6.grid(row=8,column=3)

list1= Listbox(window,height=6,width=35)
list1.grid(row=2,column=0,columnspan=2,rowspan=6)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)
#list1.configure(yscrollcommand=sb1.set)
#sb1.configure(command=list1.yview)
list1.bind('<<ListboxSelect>>',get_selected_row)
window.wm_title("BookStore")
window.mainloop()
