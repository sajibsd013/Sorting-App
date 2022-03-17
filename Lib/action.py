from tkinter.messagebox import askyesno, showinfo, showerror
from database import db
from GUI import extention
from app import main



def update_ext(new_ext, folder, root):
    if folder == "Select":
        Error = showerror(
            "File Sorting App",
            "Please Select Folder "
        )
    elif len(new_ext) > 0:
        ext_arr = new_ext.split(' ')
        count = db.update_extention(ext_arr, folder)

        Message = showinfo(
            "File Sorting App",
            f"{count} Extentions Added  "
        )

        root.destroy()
        main()
    else:
        Error = showerror(
            "File Sorting App",
            "Please Enter Extentions "
        )


def remove_ext(new_ext, folder, root):
    if len(new_ext) > 0:
        confirm = askyesno("Confirmation", "Are You sure?")
        if(confirm):
            ext_arr = new_ext.split(' ')
            db.remove_ext_arr(ext_arr, folder)

            Message = showinfo(
                "File Sorting App",
                "Extentions Removed Successfully "
            )

            root.destroy()
            main()
    else:
        Error = showerror(
            "File Sorting App",
            "Please Enter Extentions "
        )


def add_folder(new_ext, new_folder, root):
    try:
        folders = db.get_folders()
        check = False
        for folder in folders:
            if new_folder == folder:
                check = True
                break

        if check:
            Error = showerror(
                "File Sorting App",
                "Folder ALready Exists!"
            )

        elif len(folders) < 6:
            ext_arr = new_ext.split(' ')
            db.update_extention(ext_arr, new_folder)
            Message = showinfo(
                "File Sorting App",
                "Folder Added Successfully "
            )
            root.destroy()
            main()
        else:
            Error = showerror(
                "File Sorting App",
                "You can add max 6 folder!"
            )

    except:
        Error = showerror(
            "File Sorting App",
            "Error Found!"
        )


def remove_folder(folder, root):
    if folder == "Select":
        Error = showerror(
            "File Sorting App",
            "Please Select Folder "
        )
    else:
        confirm = askyesno("Confirmation", "Are You sure?")
        if(confirm):
            db.remove_folder(folder)

            Message = showinfo(
                "File Sorting App",
                "Folder Deleted Successfully "
            )
            root.destroy()
            main()


def clear(var1, var2):
    var1.set('')
    var2.set('')
