from tkinter import Tk, Frame, Menu, Text
from PIL import Image, ImageTk
from tkinter import Button, LEFT, X, FLAT, TOP

class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        
        self.initUI()
        
    
    def initUI(self):
      
        self.parent.title("Notes on Alignment- NoA")

        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        filemenu = Menu(self.parent)
        filemenu.add_command(label= "Exit", command = self.onExit)
        menubar.add_cascade(label="File", menu= filemenu)

        editmenu = Menu(self.parent)
        editmenu.add_command(label= "Select Note")
        menubar.add_cascade(label="Edit", menu = editmenu)

        viewmenu = Menu(self.parent)
        viewmenu.add_command(label = "Notes")
        viewmenu.add_command(label = "Tags")
        viewmenu.add_command(label = "Categories")
        menubar.add_cascade(label = "View", menu = viewmenu)

        helpmenu = Menu(self.parent)
        helpmenu.add_command(label="About")
        helpmenu.add_command(label="Submit Report")
        helpmenu.add_command(label="FAQ")
        helpmenu.add_command(label="Check For Updates")
        menubar.add_cascade(label="Help", menu = helpmenu)

        addNote = Frame(self.parent, bd=1,)
        self.img = Image.open("ink.png")
        eimg = ImageTk.PhotoImage(self.img)

        addButton = Button(addNote, image=eimg)
        addButton.grid(row=0, column=1)
        addButton.image = eimg
        addButton.pack(side=LEFT)

        addNote.pack(side=TOP, fill=X)
        self.pack()
        

        
        

    def onExit(self):
        self.quit()

def main():
  
    root = Tk()
    root.geometry("600x650+400+400")
    app = Example(root)
    root.mainloop()  


if __name__ == '__main__':
    main()
