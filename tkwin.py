from tkinter import *
me = Tk()
me.geometry("1000x1000")
me.title("NOTEPAD")


menu = Menu(me)
me.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
def __New1():
    me1=Tk()
    me1.title("NEWW")
    newwd=Toplevel(me)
    me1.mainloop()
bt=Button(me,text="jump",command=__New1)
bt.place()
filemenu.add_command(label='Open...')
filemenu.add_separator()


filemenu.add_command(label='Save...')
filemenu.add_command(label='Saveas...')
filemenu.add_command(label='Exit', command=me.quit)
from tkinter import scrolledtext
txt = scrolledtext.ScrolledText(me,width=40,height=10)


def __cut(self):
    self.__thisTextArea.event_generate("Cut")


def __copy(self):
    self.__thisTextArea.event_generate("Copy")


def __paste(self):
    self.__thisTextArea.event_generate("Paste")


def __delete(self):
    self.__thisTextArea.event_generate("delete")


def __undo(self):
    self.__thisTextArea.event_generate("undo")


def __selectall(self):
    self.__thisTextArea.event_generate("selectall")

helpmenu = Menu(menu)
editmenu=Menu(menu)
formatmenu=Menu(menu)
viewmenu=Menu(menu)
menu.add_cascade(label='Edit', menu=editmenu)
editmenu.add_command(label='Undo')
editmenu.add_command(label='Cut')
editmenu.add_command(label='Copy')
editmenu.add_command(label='Paste')
editmenu.add_command(label='Delete')
editmenu.add_command(label='Selectall')
editmenu.add_command(label='Time/Date')


menu.add_cascade(label='Format', menu=formatmenu)
formatmenu.add_command(label='font')
master =""
w = Spinbox(master, from_ = 0, to = 10)
w.pack()

menu.add_cascade(label='View', menu=viewmenu)
viewmenu.add_command(label='Status bar')

menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About')

me.mainloop()
