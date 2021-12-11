from tkinter import *
from tkinter import filedialog
from tkinter.font import BOLD, ITALIC

class GUI :

    def __init__(self):

        self.gui = Tk()
        self.gui.title("Notepad")
        self.gui.geometry("350x250")

        self.text = Text(self.gui, wrap = WORD, font=("Arial", 14, ITALIC, BOLD))
        self.text.pack(padx = 10, pady = 10, expand = TRUE, fill = BOTH)
        
        self.mymenu = Menu()
        File = Menu()
        File.add_command(label="New", accelerator= "CTRL + N", command = self.new_file )
        File.add_command(label="Open file", accelerator="CTRL + O", command= self.open_file)
        File.add_command(label="Save As", command = self.save_as)
        File.add_command(label="Save", accelerator="CTRL + S", command = self.save_file)
        File.add_command(label="Copy", accelerator="CTRL + C", command = self.Copy)
        File.add_command(label="Paste", accelerator="CTRL + V", command = self.Paste)
        File.add_command(label="Cut", accelerator="CTRL + X", command = self.Cut )
        self.mymenu.add_cascade(label = "File", menu = File)

        self.gui.config(menu = self.mymenu)
        self.gui.mainloop()

    def new_file(self):

        self.text.delete(1.0, END)

    
    def open_file(self):

        f = filedialog.askopenfile(mode = 'r')
        data = f.read()
        self.text.delete(1.0,END)
        self.text.insert(1.0,data)
    
    def save_file(self):
        # Some other logic required
        fileName = "Untitled.txt"
        data = self.text.get(1.0, END)
        f = open(fileName,'w')
        f.write(data)
 
    def save_as(self):

        f = filedialog.asksaveasfile(mode = "w", defaultextension=".txt")
        data = self.text.get(1.0, END)
        f.write(data)
    
    def Copy(self):
        self.text.clipboard_clear()
        self.text.clipboard_append(self.text.selection_get())
    
    def Paste(self):
        self.text.insert(INSERT, self.text.clipboard_get())

    def Cut(self):
        self.Copy()
        self.text.delete('sel.first','sel.last')

text_editor = GUI()
