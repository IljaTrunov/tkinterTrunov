from tkinter import *
k=0
def clicker(event):
    global k
    k+=1
    nupp.config(text=k)
def clicker_(event):
    global k
    k-=1
    nupp.config(text=k)
def txt_to_nicetext(event):
    text=txt.get()
    nicetext.configure(text=text)
    txt.delete(0,END)
def valimine():
    valik=var.get()
    nicetext.configure(text=valik)
aken=Tk()
aken.title("взлом пентагона")
aken.geometry("1920x1080")
nupp=Button(aken, text="взломать пентагон",font="Arial 16", width=40, fg="blue",bg="yellow",relief=RAISED)
#nupp.pack(side=centre)
nupp.place(relx=0.5, rely=0.5, anchor=CENTER)
nupp.bind("<Button-1>",clicker)
nupp.bind("<Button-3>",clicker_)
nicetext=Label(aken,text="Pentagon hack 3000",height=3, width=30,font="Arial 20", fg="blue",bg="yellow",relief="solid")
nicetext.pack()
txt=Entry(aken,width=30,font="Arial 20", fg="blue",bg="yellow",justify=CENTER)
txt.pack()
txt.bind("<Return>", txt_to_nicetext)
i1=PhotoImage(file="1.gif")
i2=PhotoImage(file="2.gif")
i3=PhotoImage(file="3.gif")
var=StringVar()
var.set("Üks")
r1=Radiobutton(aken,image=i1, variable=var,value="Üks",command=valimine(value))
r2=Radiobutton(aken,image=i2, variable=var,value="kaks",command=valimine(value))
r3=Radiobutton(aken,image=i3, variable=var,value="kolm",command=valimine(value))
r1.pack(side=LEFT)
r2.pack(side=LEFT)
r3.pack(side=LEFT)
aken.mainloop()
