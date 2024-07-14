from tkinter import *
import pyshorteners
import pyshorteners.shorteners

root = Tk()
root.title("Python URL Shortener")
root.geometry("600x270+650+50")
root.configure(bg="brown")

#ButtonFunction
def short():
    url = entry1.get()
    s = pyshorteners.Shortener().tinyurl.short(url)

    entry2.insert(END,s)

#Label for entering user url
Label(root,text="Enter Your URL",font="impack 20 bold",bg="black",fg="brown").pack(fill="x")

#EntryBox
entry1 = Entry(root,font="10",bd=3,width=40)
entry1.pack(pady=30)

#Button
Button(root,text="Convert URL",font="impack 15 bold",bg="black",fg="grey",command=short).pack()

#Entry
entry2 = Entry(root,font="impack 15 bold",bg="brown",width=24,bd=0)
entry2.pack(pady=30)

mainloop()
