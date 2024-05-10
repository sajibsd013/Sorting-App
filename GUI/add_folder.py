from tkinter import *
from tkinter.messagebox import askyesno, showerror, showinfo

from database import db
from Lib import action


class add_folder_gui:
    def __init__(self, root):
        self.root = root
        self.screenWidth = self.root.winfo_screenwidth()
        self.screenHeight = self.root.winfo_screenheight()

        w = self.screenWidth/108
        h = self.screenHeight/100
        frame_pos = self.screenHeight-h*42-50

        self.del_icon = PhotoImage(file="images/delete.png")
        self.add_icon = PhotoImage(file="images/add.png")

        self.var_new_folderName = StringVar()
        self.var_new_folder_ext = StringVar()

        self.frame = Frame(self.root, bd=2, relief=RIDGE)
        self.frame.place(x=self.screenWidth-w*35-50,
                         y=frame_pos, width=w*35, height=h*25)
        box_start = self.screenWidth-w*35-50
        lbl_add_ext = Label(
            self.root,
            text='Add New Folder ',
            font=('impact', 16),
            bg='#023548',
            fg="white"
        ).place(x=box_start, y=frame_pos, width=w*35, height=40)

        lbl_add_new_folder = Label(
            self.root,
            text='Folder Name  ',
            font=('times new roman', 13),
        ).place(x=box_start+w*3, y=frame_pos+h*7)

        self.entry_new_folder = Entry(
            self.root,
            font=('times new roman', 13),
            bg='white',
            textvariable=self.var_new_folderName,
            justify=CENTER,
        ).place(x=box_start+w*16, y=frame_pos+h*7, height=30, width=w*15)

        lbl_add_folder_ext = Label(
            self.root,
            text='Enter Extentions ',
            font=('times new roman', 13),
        ).place(x=box_start+w*3, y=frame_pos+h*12)

        self.entry_new_ext = Entry(
            self.root,
            font=('times new roman', 13),
            bg='white',
            justify=CENTER,
            textvariable=self.var_new_folder_ext
        ).place(x=box_start+w*16, y=frame_pos+h*12, height=30, width=w*15)

        self.Add_Folder = Button(
            self.root,
            text="ADD",
            font=('times new roman', 10, 'bold'),
            bg='white',
            fg='black',
            command=lambda: action.add_folder(
                self.var_new_folder_ext.get(), self.var_new_folderName.get(), root
            ),
            activebackground='white',
            activeforeground='black',
            cursor='hand2',
            compound=LEFT,
            padx='5px',
            image=self.add_icon
        ).place(x=box_start+w*5, y=frame_pos+h*18, height=35, width=w*10)

        self.clear_Folder = Button(
            self.root,
            text="CLEAR",
            font=('times new roman', 10, 'bold'),
            bg='white',
            fg='black',
            command=lambda: action.clear(
                self.var_new_folder_ext, self.var_new_folderName
            ),
            activebackground='white',
            activeforeground='black',
            cursor='hand2',
            compound=LEFT,
            padx='5px',
            image=self.del_icon
        ).place(x=box_start+w*20, y=frame_pos+h*18, height=35, width=w*10)
