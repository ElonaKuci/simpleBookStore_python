from tkinter import *

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


b1=Button(window,text="View All",command="",width="15")
b1.grid(row=3,column=3)

b2=Button(window,text="Search Entry",command="",width="15")
b2.grid(row=4,column=3)

b3=Button(window,text="Add Entry",command="",width="15")
b3.grid(row=5,column=3)

b4=Button(window,text="Update Selected",command="",width="15")
b4.grid(row=6,column=3)

b5=Button(window,text="Delete Selected",command="",width=15)
b5.grid(row=7,column=3)

b6=Button(window,text="Close",command="",width=15)
b6.grid(row=8,column=3)

list1= Listbox(window,height=6,width=35)
list1.grid(row=2,column=0,columnspan=2,rowspan=6)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)
#list1.configure(yscrollcommand=sb1.set)
#sb1.configure(command=list1.yview)

window.mainloop()
