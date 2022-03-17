from tkinter import *
from tkinter import ttk
from database import db
from tkinter.messagebox import askyesno, showinfo, showerror
from Lib import action


class delete_folder_gui:
    def __init__(self, root):
        self.root = root
        self.screenWidth = self.root.winfo_screenwidth()
        self.screenHeight = self.root.winfo_screenheight()

        self.del_icon = PhotoImage(file="images/delete.png")

        self.var_folder = StringVar()
        self.var_ext = StringVar()

        self.folders = db.get_folders()
        not_removeable = ['audios','videos','documents','images']

        for folder in not_removeable:
            self.folders.remove(folder)
            
        self.folders.insert(0, "Select")


        w = self.screenWidth/100
        h = self.screenHeight/100

        frame_pos = self.screenHeight-h*42-50

        self.frame = Frame(self.root, bd=2, relief=RIDGE)
        self.frame.place(
            x=w*38, y=frame_pos, width=w*24, height=h*25
        )

        lbl_update_ext = Label(
            self.root,
            text='Delete Folder ',
            font=('impact', 16),
            bg='#023548',
            fg="white"
        ).place(x=w*38, y=frame_pos, width=w*24, height=40)

        lbl_select_folder = Label(
            self.root,
            text='Select Folder',
            font=('times new roman', 13),
        ).place(x=w*39, y=frame_pos+h*8)

        self.combo_box = ttk.Combobox(
            values=self.folders,
            state='readonly',
            justify=CENTER,
            font=('times new roman', 12),
            textvariable=self.var_folder,
        )
        self.combo_box.place(
            x=w*50, y=frame_pos+h*8, height=30, width=w*10
        )
        self.combo_box.current(0)

        self.delete_folder = Button(
            self.root,
            text="Delete",
            font=('times new roman', 10, 'bold'),
            bg='white',
            fg='black',
            command=lambda: action.remove_folder(
                self.var_folder.get(), root
            ),
            activebackground='white',
            activeforeground='black',
            cursor='hand2',
            compound=LEFT,
            padx='5px',
            image=self.del_icon
        ).place(x=w*45, y=frame_pos+h*15, height=35, width=w*11)
