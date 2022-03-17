from tkinter import *
from Lib import sort
from database import db
from tkinter import ttk
from GUI import extention


class header_footer_gui:
    def __init__(self, root):
        self.root = root
        self.screenWidth = self.root.winfo_screenwidth()
        self.screenHeight = self.root.winfo_screenheight()

        self.start_icon = PhotoImage(file="images/start.png")
        self.del_icon = PhotoImage(file="images/delete.png")
        self.add_folder_icon = PhotoImage(file="images/add_folder.png")
        self.var_folderName = StringVar()

        # ===============hearder sec=============

        title = Label(
            self.root,
            text="FILE SORTING APPLICATION",
            padx='10',
            font=("impact", 25),
            bg="#023548",
            fg="white",
        ).place(x=0, y=0, relwidth=1)

        lbl_select_folder = Label(
            self.root,
            text='Select Folder',
            font=('times new roman', 20),
            bg='white'
        ).place(x=50, y=60)

        txt_folder_name = Entry(
            self.root,
            font=('times new roman', 13),
            state='readonly',
            textvariable=self.var_folderName,
        ).place(x=220, y=65, height=30, width=self.screenWidth-450)

        self.btn_browse = Button(
            self.root,
            text="BROWSE",
            font=('times new roman', 12, 'bold'),
            bg='white',
            fg='black',
            command=lambda: sort.browse_function(
                self.var_folderName,
                self.lbl_status_total,
                self.lbl_status_move,
                self.lbl_status_left,
                self.count_dict,
                count_func
            ),
            activebackground='#262626',
            activeforeground='white',
            cursor='hand2',
            compound=LEFT,
            padx='5px',
            image=self.add_folder_icon
        ).place(x=self.screenWidth-180, y=60, height=35, width=130)

        hr = Label(
            self.root,
            bg="lightgray"
        ).place(x=50, y=105, height=2, width=self.screenWidth-100)

        # ============footer sec==========
        wf = self.screenWidth/100*12

        hr3 = Label(
            bg="lightgray"
        ).place(x=50, y=self.screenHeight-120, height=2, width=self.screenWidth-100)

        lbl_status = Label(
            text=f'STATUS',
            font=('times new roman', 20),
            bg='white'
        ).place(x=50, y=self.screenHeight-110)

        self.lbl_status_total = Label(
            text='TOTAL: 0',
            font=('times new roman', 17),
            fg='green',
            bg='white'
        )
        self.lbl_status_total.place(x=50+wf, y=self.screenHeight-110)

        self.lbl_status_move = Label(
            text='MOVE: 0',
            font=('times new roman', 17),
            fg='blue',
            bg='white'
        )
        self.lbl_status_move.place(x=50+2*wf, y=self.screenHeight-110)

        self.lbl_status_left = Label(
            text='LEFT: 0',
            font=('times new roman', 17),
            fg='orange',
            bg='white'
        )
        self.lbl_status_left.place(x=50+3*wf, y=self.screenHeight-110)

        def lbl_config(count, length):
            self.lbl_status_move.config(
                text=f'MOVE: {count}'
            )
            self.lbl_status_left.config(
                text=f'LEFT: {length-count}'
            )

        self.Start = Button(
            text="START",
            font=('times new roman', 12, 'bold'),
            bg='white',
            fg='Black',
            command=lambda: sort.start_function(
                self.var_folderName.get(),
                lbl_config
            ),
            activebackground='white',
            activeforeground='black',
            cursor='hand2',
            compound=LEFT,
            padx='10px',
            image=self.start_icon
        ).place(x=self.screenWidth-200, y=self.screenHeight-113, height=40, width=150)

        self.clear_all = Button(
            text="CLEAR ALL",
            font=('times new roman', 12, 'bold'),
            bg='white',
            fg='Black',
            command=lambda: sort.clear_function(
                self.var_folderName,
                self.lbl_status_total,
                self.lbl_status_move,
                self.lbl_status_left,
            ),
            activebackground='white',
            activeforeground='black',
            cursor='hand2',
            compound=LEFT,
            padx='5px',
            image=self.del_icon
        ).place(x=self.screenWidth-360, y=self.screenHeight-113, height=40, width=150)

        lbl_add_ext_demo = Label(
            self.root,
            text='Note: Extentions must be separate using space (demo: .png .jpg .jpeg) ',
            font=('times new roman', 12),
            bg='white',
            fg='#17a2b8'
        ).place(x=50, y=self.screenHeight-146)

        # ================= Extention sec===========
        extention_sec = extention.extention_gui(
            self.root
        )
        self.folders = db.get_folders()
        self.folders.append("others")
        self.count_dict = {}
        for f in self.folders:
            self.count_dict.update({f: 0})

        def count_func(count_dict):
            extention_sec.extentions(
                count_dict, len(self.folders), self.folders
            )

        count_func(self.count_dict)
