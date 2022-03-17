from tkinter import *
from tkinter import ttk
from database import db

class extention_gui:
    def __init__(self, root):

        self.root = root
        self.screenWidth = self.root.winfo_screenwidth()
        self.screenHeight = self.root.winfo_screenheight()

        lbl_support_ext = Label(
            self.root,
            text='Supported Extentions',
            font=('times new roman', 18),
            bg='white'
        ).place(x=50, y=130)

    def extentions(self, count_dict, folders_len, folders):
        x = 55
        w = (self.screenWidth-100)/folders_len
        h = self.screenHeight/100

        frame_pos = 180

        for folder in folders:
            frame1 = Frame(
                self.root, 
                bd=2, 
                # bg='white', 
                relief=RIDGE
            )
            frame1.place(x=x, y=frame_pos, width=w-10, height=h*18)
            extentions = db.get_extention(folder)
            extentions.insert(0, folder)

            self.combo_box = ttk.Combobox(
                values=extentions,
                state='readonly',
                justify=CENTER,
                font=('times new roman', 16)
            )
            self.combo_box.place(x=x, y=frame_pos, width=w-10, height=40)
            self.combo_box.current(0)

            lbl_ext_count = Label(
                self.root,
                text=f'{count_dict.get(folder)}',
                font=('Agency FB', 34),
   

            ).place(x=x+2, y=frame_pos+h*7, width=w-14)

            x = x+w

