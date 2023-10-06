'''from PIL import Image, ImageTk
from tkinter import Tk, Label, BOTH
from tkinter.ttk import Frame, Style

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.initUI()
    def initUI(self):
        self.parent.title("Absolute positioning")
        self.pack(fill=BOTH, expand=1)
        Style().configure("TFrame", background="#333")
        bard = Image.open("E:\\Courses\\Python\\bardejov.jpg")
        bard=bard.resize((100,100),Image.ANTIALIAS)
        bardejov = ImageTk.PhotoImage(bard)
        label1 = Label(self, image=bardejov)
        label1.image = bardejov
        label1.place(x=20, y=20)
        rot = Image.open("E:\\Courses\\Python\\rotunda.jpg")
        rot=rot.resize((100,100),Image.ANTIALIAS)
        rotunda = ImageTk.PhotoImage(rot)
        label2 = Label(self, image=rotunda)
        label2.image = rotunda
        label2.place(x=40, y=160)
        minc = Image.open("E:\\Courses\\Python\\mincol.jpg")
        minc=minc.resize((100,100),Image.ANTIALIAS)
        mincol = ImageTk.PhotoImage(minc)
        label3 = Label(self, image=mincol)
        label3.image = mincol
        label3.place(x=170, y=50)
root = Tk()
root.geometry("300x280+300+300")
app = Example(root)
root.mainloop()'''

'''from tkinter import Tk, RIGHT, BOTH, RAISED
from tkinter.ttk import Frame, Button, Style

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Button")
        self.style = Style()
        self.style.theme_use("default")
        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill=BOTH, expand=True)
        self.pack(fill=BOTH, expand=True)
        closeButton = Button(self, text="Close")
        closeButton.pack(side=RIGHT, padx=5, pady=5)
        okButton = Button(self, text="OK")
        okButton.pack(side=RIGHT)
root = Tk()
root.geometry("300x200+300+300")
app = Example(root)
root.mainloop()'''

'''from tkinter import Tk, Text, TOP, BOTH, X, N, LEFT
from tkinter.ttk import Frame, Label, Entry

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Review")
        self.pack(fill=BOTH, expand=True)
        frame1 = Frame(self)
        frame1.pack(fill=X)
        lbl1 = Label(frame1, text="Title", width=6)
        lbl1.pack(side=LEFT, padx=5, pady=5)
        entry1 = Entry(frame1)
        entry1.pack(fill=X, padx=5, expand=True)
        frame2 = Frame(self)
        frame2.pack(fill=X)
        lbl2 = Label(frame2, text="Author", width=6)
        lbl2.pack(side=LEFT, padx=5, pady=5)
        entry2 = Entry(frame2)
        entry2.pack(fill=X, padx=5, expand=True)

        frame3 = Frame(self)
        frame3.pack(fill=BOTH, expand=True)

        lbl3 = Label(frame3, text="Review", width=6)
        lbl3.pack(side=LEFT, anchor=N, padx=5, pady=5)

        txt = Text(frame3)
        txt.pack(fill=BOTH, pady=5, padx=5, expand=True)

root = Tk()
root.geometry("300x300+300+300")
app = Example(root)
root.mainloop()'''

'''from tkinter import Tk, W, E
from tkinter.ttk import Frame, Button, Style
from tkinter.ttk import Entry

class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.initUI()

    def initUI(self):

        self.parent.title("Calculator")

        Style().configure("TButton", padding=(0, 5, 0, 5), font='serif 10')

        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)
        self.columnconfigure(2, pad=3)
        self.columnconfigure(3, pad=3)

        self.rowconfigure(0, pad=3)
        self.rowconfigure(1, pad=3)
        self.rowconfigure(2, pad=3)
        self.rowconfigure(3, pad=3)
        self.rowconfigure(4, pad=3)

        entry = Entry(self)
        entry.grid(row=0, columnspan=4, sticky=W+E)
        cls = Button(self, text="Cls")
        cls.grid(row=1, column=0)
        bck = Button(self, text="Back")
        bck.grid(row=1, column=1)
        lbl = Button(self)
        lbl.grid(row=1, column=2)
        clo = Button(self, text="Close")
        clo.grid(row=1, column=3)
        sev = Button(self, text="7")
        sev.grid(row=2, column=0)
        eig = Button(self, text="8")
        eig.grid(row=2, column=1)
        nin = Button(self, text="9")
        nin.grid(row=2, column=2)
        div = Button(self, text="/")
        div.grid(row=2, column=3)
        fou = Button(self, text="4")
        fou.grid(row=3, column=0)
        fiv = Button(self, text="5")
        fiv.grid(row=3, column=1)
        six = Button(self, text="6")
        six.grid(row=3, column=2)
        mul = Button(self, text="*")
        mul.grid(row=3, column=3)

        one = Button(self, text="1")
        one.grid(row=4, column=0)
        two = Button(self, text="2")
        two.grid(row=4, column=1)
        thr = Button(self, text="3")
        thr.grid(row=4, column=2)
        mns = Button(self, text="-")
        mns.grid(row=4, column=3)
        zer = Button(self, text="0")
        zer.grid(row=5, column=0)
        dot = Button(self, text=".")
        dot.grid(row=5, column=1)
        equ = Button(self, text="=")
        equ.grid(row=5, column=2)
        pls = Button(self, text="+")
        pls.grid(row=5, column=3)
        self.pack()

root = Tk()
app = Example(root)
root.mainloop()'''


'''from tkinter import Tk, Frame, Checkbutton
from tkinter import BooleanVar, BOTH

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
    def initUI(self):
        self.parent.title("Checkbutton")
        self.pack(fill=BOTH, expand=True)
        self.var = BooleanVar()
        cb = Checkbutton(self, text="Show Title", variable=self.var, command=self.onClick)
        cb.select()
        cb.place(x=50, y=50)
    def onClick(self):
        if self.var.get() == True:
            self.master.title("Checkbutton")
        else:
            self.master.title("")
root = Tk()
root.geometry("250x150+300+300")
app = Example(root)
root.mainloop()'''


'''from PIL import Image, ImageTk
from tkinter import Tk, Frame, Label

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
    def initUI(self):
        self.parent.title("Label")
        self.img = Image.open("E:\\Courses\\Python\\rotunda.jpg")
        rotunda = ImageTk.PhotoImage(self.img)
        label = Label(self, image=rotunda)
        label.image = rotunda
        label.pack()
        self.pack()
    def setGeometry(self):
        w, h = self.img.size
        self.parent.geometry(("%dx%d+300+300") % (w, h))
root = Tk()
ex = Example(root)
ex.setGeometry()
root.mainloop()'''

'''from tkinter import Tk, BOTH, IntVar, LEFT
from tkinter.ttk import Frame, Label, Scale, Style

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
    def initUI(self):
        self.parent.title("Scale")
        self.style = Style()
        self.style.theme_use("default")
        self.pack(fill=BOTH, expand=1)
        scale = Scale(self, from_=0, to=100, command=self.onScale)
        scale.pack(side=LEFT, padx=15)
        self.var = IntVar()
        self.label = Label(self, text=0, textvariable=self.var)
        self.label.pack(side=LEFT)
    def onScale(self, val):
        v = int(float(val))
        self.var.set(v)
root = Tk()
ex = Example(root)
root.geometry("250x100+300+300")
root.mainloop()'''


'''from tkinter.ttk import Frame, Label
from tkinter import Tk, BOTH, Listbox, StringVar, END

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
    def initUI(self):
        self.parent.title("Listbox")
        self.pack(fill=BOTH, expand=1)
        acts = ["Scarlet Johansson", "Rachel Weiss", "Natalie Portman", "Jessica Alba"]
        lb = Listbox(self)
        for i in acts:
            lb.insert(END, i)
        lb.bind("<<ListboxSelect>>", self.onSelect)
        lb.pack(pady=15)
        self.var = StringVar()
        self.label = Label(self, text=0, textvariable=self.var)
        self.label.pack()
    def onSelect(self, val):
        sender = val.widget
        idx = sender.curselection()
        value = sender.get(idx)
        self.var.set(value)
root = Tk()
ex = Example(root)
root.geometry("300x250+300+300")
root.mainloop()'''


'''from tkinter import Frame, Tk, Menu

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
    def initUI(self):
        self.parent.title("Simple Menu")
        menuBar = Menu(self.parent)
        self.parent.config(menu=menuBar)
        fileMenu = Menu(menuBar)
        fileMenu.add_command(label="Exit", command=self.onExit)
        menuBar.add_cascade(label="File", menu=fileMenu)
    def onExit(self):
        self.quit()
root = Tk()
root.geometry("250x150+300+300")
app = Example(root)
root.mainloop()'''

'''from tkinter import Tk, Frame, Menu

class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
    def initUI(self):
        self.parent.title("Submenu")
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)
        fileMenu = Menu(menubar)
        submenu = Menu(fileMenu)
        submenu.add_command(label="New feed")
        submenu.add_command(label="Bookmarks")
        submenu.add_command(label="Mail")
        fileMenu.add_cascade(label='Import', menu=submenu)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=self.onExit)
        menubar.add_cascade(label="File", menu=fileMenu)
    def onExit(self):
        self.quit()
root = Tk()
root.geometry("250x150+300+300")
app = Example(root)
root.mainloop()'''

'''from tkinter import Tk, Frame, Menu

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
    def initUI(self):
        self.parent.title("Popup menu")
        self.menu = Menu(self.parent, tearoff=0)
        self.menu.add_command(label="Beep", command=self.bell())
        self.menu.add_command(label="Exit", command=self.onExit)
        self.parent.bind("<Button-3>", self.showMenu)
        self.pack()
    def showMenu(self, e):
        self.menu.post(e.x_root, e.y_root)
    def onExit(self):
        self.quit()
root = Tk()
root.geometry("250x150+300+300")
app = Example(root)
root.mainloop()'''


'''from tkinter.ttk import Frame, Button
from tkinter import Tk, BOTH
import tkinter.messagebox as mbox

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
    def initUI(self):
        self.parent.title("Message Boxes")
        self.pack()
        error = Button(self, text="Error", command=self.onError)
        error.grid(padx=5, pady=5)
        warning = Button(self, text="Warning", command=self.onWarn)
        warning.grid(row=1, column=0)
        question = Button(self, text="Question", command=self.onQuest)
        question.grid(row=0, column=1)
        inform = Button(self, text="Information", command=self.onInfo)
        inform.grid(row=1, column=1)
    def onError(self):
        mbox.showerror("Error", "Could not open file")
    def onWarn(self):
        mbox.showwarning("Warning", "Deprecated function call")
    def onQuest(self):
        mbox.askquestion("Question", "Are you sure to quit?")
    def onInfo(self):
        mbox.showinfo("Information", "Download completed")
root = Tk()
ex = Example(root)
root.geometry("300x150+300+300")
root.mainloop()'''


'''from tkinter import Tk, Frame, Button, BOTH, SUNKEN
from tkinter.colorchooser import askcolor

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
    def initUI(self):
        self.parent.title("Color chooser")
        self.pack(fill=BOTH, expand=1)
        self.btn = Button(self, text="Choose Color", command=self.onChoose)
        self.btn.place(x=30, y=30)
        self.frame = Frame(self, border=1, relief=SUNKEN, width=100, height=100)
        self.frame.place(x=160, y=30)
    def onChoose(self):
        (rgb, hx) = askcolor()
        self.frame.config(bg=hx)
root = Tk()
ex = Example(root)
root.geometry("300x150+300+300")
root.mainloop()'''


'''from tkinter import Frame, Tk, BOTH, Text, Menu, END
from tkinter.filedialog import Open

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
    def initUI(self):
        self.parent.title("File dialog")
        self.pack(fill=BOTH, expand=1)
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)
        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Open", command=self.onOpen)
        menubar.add_cascade(label="File", menu=fileMenu)
        self.txt = Text(self)
        self.txt.pack(fill=BOTH, expand=1)
    def onOpen(self):
        ftypes = [('Python files', '*.py'), ('All files', '*')]
        dlg = Open(self, filetypes = ftypes)
        fl = dlg.show()
        if fl != '':
            text = self.readFile(fl)
            self.txt.insert(END, text)
    def readFile(self, filename):
        f = open(filename, "r")
        text = f.read()
        return text
root = Tk()
ex = Example(root)
root.geometry("300x250+300+300")
root.mainloop()'''
