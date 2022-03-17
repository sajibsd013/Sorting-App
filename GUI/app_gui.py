from tkinter import *
from GUI import header_footer, add_folder, update_ext, delete_folder

class sorting_app:
    def __init__(self, root):
        self.root = root
        self.root.title("FILE SORTING APP | Developed By Sajib")
        self.screenWidth = self.root.winfo_screenwidth()
        self.screenHeight = self.root.winfo_screenheight()
        self.root.geometry(f'{self.screenWidth}x{self.screenHeight}+0+0')
        self.root.config(bg='white')
        self.root.minsize(self.screenWidth, self.screenHeight)
        self.root.state('zoomed')

  
        # ================ Header secton ================
        header_footer_sec = header_footer.header_footer_gui(self.root)

        # ================ Add FOlder secton ================
        add_folder_sec = add_folder.add_folder_gui(self.root)

        # ================ Extention Update secton ================
        update_ext_sec = update_ext.update_ext_gui(self.root)

        # ================ Extention Update secton ================
        delete_folder_sec = delete_folder.delete_folder_gui(self.root)
    

 

        

