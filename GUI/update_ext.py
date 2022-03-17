from tkinter import *
from tkinter import ttk
from database import db
from tkinter.messagebox import askyesno, showinfo, showerror
from Lib import action


class update_ext_gui:
    def __init__(self, root):
        self.root = root
        self.screenWidth = self.root.winfo_screenwidth()
        self.screenHeight = self.root.winfo_screenheight()

        self.del_icon = PhotoImage(file="images/delete.png")
        self.add_icon = PhotoImage(file="images/add.png")

        self.var_folder = StringVar()
        self.var_ext = StringVar()

        self.folders = db.get_folders()
        self.folders.insert(0, "Select")

        w = self.screenWidth/108
        h = self.screenHeight/100
        frame_pos = self.screenHeight-h*42-50



        self.frame = Frame(self.root, bd=2, relief=RIDGE)
        self.frame.place(x=50, y=frame_pos, width=w*35, height=h*25)

        lbl_update_ext = Label(
            self.root,
            text='Update Extentions',
            font=('impact', 16),
            bg='#023548',
            fg="white"
        ).place(x=50, y=frame_pos, width=w*35, height=40)

        lbl_select_folder = Label(
            self.root,
            text='Select Folder',
            font=('times new roman', 13),
        ).place(x=50+w*3, y=frame_pos+h*7)

        self.combo_box = ttk.Combobox(
            values=self.folders,
            state='readonly',
            justify=CENTER,
            font=('times new roman', 12),
            textvariable=self.var_folder,
        )
        self.combo_box.place(
            x=50+w*16, y=frame_pos+h*7, height=30, width=w*15)
        self.combo_box.current(0)

        lbl_add_folder_ext = Label(
            self.root,
            text='Enter Extentions ',
            font=('times new roman', 13),
        ).place(x=50+w*3, y=frame_pos+h*12)

        self.entry_new_ext = Entry(
            self.root,
            font=('times new roman', 12),
            bg='white',
            justify=CENTER,
            textvariable=self.var_ext
        ).place(x=50+w*16, y=frame_pos+h*12, height=30, width=w*15)

        self.update_ext = Button(
            self.root,
            text="Update",
            font=('times new roman', 10, 'bold'),
            bg='white',
            fg='black',
            command=lambda: action.update_ext(
                self.var_ext.get(), self.var_folder.get(), root
            ),
            activebackground='white',
            activeforeground='black',
            cursor='hand2',
            compound=LEFT,
            padx='5px',
            image=self.add_icon
        ).place(x=50+w*5, y=frame_pos+h*18, height=35, width=w*10)

        self.remove_ext = Button(
            self.root,
            text="Remove",
            font=('times new roman', 10, 'bold'),
            bg='white',
            fg='black',
            command=lambda: action.remove_ext(
                self.var_ext.get(), self.var_folder.get(), root
            ),
            activebackground='white',
            activeforeground='black',
            cursor='hand2',
            compound=LEFT,
            padx='5px',
            image=self.del_icon
        ).place(x=50+w*20, y=frame_pos+h*18, height=35, width=w*10)
