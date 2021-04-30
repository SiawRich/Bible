import requests
import json
from tkinter import *                                                                                              
from tkinter import ttk
from tkinter import messagebox


root = Tk()
root.title("The Holy Bible")
root.resizable(0,0)

icon = PhotoImage(file='C:/Users/OWNER/OneDrive/Desktop/Bible/bible.png')
root.iconphoto(False,icon)

url = "https://bible-api.com/"

messagebox.showinfo("The Holy Bible","Welcome to My Bible App\nPlease consider the following tips:\n" +
                   "\n1. The book field is not case sensitive, you can also use the correct abbreviated forms of the books.\n "+
                   "\n2. You can also search for two or more verses. Example(John 3:16-18). There should be no spaces between the verses just separate them with a hyphen.\n "+
                   "\n3. The field displaying your bible quotation is scrollable. Thus, you can scroll till the end.\n "+
                   "\nClick Ok or the Close button on top of the window to access The Holy Bible.\n "+
                   "\n                               Happy Reading!!!!"
                   )


def bibleV():
    try:
        books = book.get()
        chapters = chapter.get()
        verses = verse.get()
        versions  = opt.get()

        if(len(books) > 1):
            url_response = url + books + chapters +":" + verses + "?translation=" + versions
            response = requests.get(url_response).json()
            mainVerse ="\n" + response["text"] + "\n" + "Bible Version: "+versions
            
            display.delete(1.0,END)
            display.config(fg="#ffffff")
            display.insert(END, mainVerse)

        else:
            book.config(fg='red')
            bookValue.set('please enter book')
        
        
   
    except KeyError:
        book.config(fg='red')
        bookValue.set('incorrect book name')

HeadLabel = Label(root, text="THE HOLY BIBLE",font=("Comic Sans MS", 30,"bold")).pack() 

#Input Entry
bookLabel = Label(root, text="Enter Book",font=("Comic Sans MS", 15,"bold")).pack()
bookValue = StringVar()
bookValue.set("GENESIS")
book = Entry(root,textvariable=bookValue,bg="white",font=("Comic Sans MS", 15))
book.pack()

chapterLabel = Label(root, text="Enter Chapter",font=("Comic Sans MS", 15,"bold")).pack()
chapterValue = StringVar()
chapterValue.set("1")
chapter = Entry(root,textvariable=chapterValue,bg="white",font=("Comic Sans MS", 15))
chapter.pack()

verseLabel = Label(root, text="Enter Verse",font=("Comic Sans MS", 15,"bold")).pack()
verseValue = StringVar()
verseValue.set("1")
verse = Entry(root,textvariable=verseValue,bg="white",font=("Comic Sans MS", 15))
verse.pack()

versionLabel = Label(root, text="Select the Version",font=("Comic Sans MS", 15,"bold")).pack()
choice = ["kjv","web"]
opt = ttk.Combobox(root,values=choice)
opt.set(choice[0])
opt.pack()

space = Label(root,text="", font=("Comic Sans MS",10,"bold"))
space.pack()                                                                     

#Button
Button(root,text="Search",bg="blue",fg="white",cursor="hand2",font=("Comic Sans MS", 15),command=bibleV).pack()

space = Label(root,text="", font=("Comic Sans MS",10,"bold"))
space.pack()

#Output
display = Text(root,fg="#ffffff",relief=FLAT,bg="grey",width=40,height=8, font=("Comic Sans MS", 15))
display.pack()

root.mainloop()
