from tkinter import ttk, filedialog
import os
import shutil
from database import db
from tkinter.messagebox import askyesno, showinfo, showerror


def file_count(all_files, count_dict, count_func):
    folders = get_folders_dict()
    for f in folders:
        count_dict.update({f: 0})

    count = 0
    for i in all_files:
        ext = i.split('.')[-1]
        for folder in folders:
            if '.'+ext in folders[folder]:
                count_dict[folder] = count_dict.get(folder)+1
                count += 1
    count_dict["others"] = len(all_files)-count
    count_func(count_dict)


def browse_function(var_folderName, lbl_status_total, lbl_status_move, lbl_status_left, count_dict, count_func):
    try:
        op = filedialog.askdirectory(title="SELECT FOLDER FOR SORTING")
        if op != None:
            var_folderName.set(str(op))
            directory = var_folderName.get()
            all_files_list = os.listdir(directory)
            all_files = [file for file in all_files_list if os.path.isfile(os.path.join(directory, file))]

            file_count(all_files, count_dict, count_func)
            length = len(all_files)
            lbl_status_total.config(text=f'TOTAL: {length}')
            lbl_status_move.config(text=f'MOVE: 0')
            lbl_status_left.config(text=f'LEFT: 0')

    except:
        print("An exception occurred")


def rename_folder(directory):
    try:
        for folder in os.listdir(directory):
            if os.path.isdir(os.path.join(directory, folder)) == True:
                os.rename(
                    os.path.join(directory, folder),
                    os.path.join(directory, folder.lower())
                )
    except:
        Error = showerror(
            "File Sorting App",
            "An exception occurred"
        )


def get_ext(folder):
    ext = db.get_extention(folder)

    ext_list = []
    for i in ext:
        ext_list.append(i)
    return ext_list


def get_folders_dict():
    folders_list = db.get_folders()
    folders = {}
    for folder in folders_list:
        ext_list = get_ext(folder)
        folders.update({folder: ext_list})

    return folders


def create_move(directory, ext, file_name, other_name):
    try:
        find_check = False

        folders = get_folders_dict()

        for folder_name in folders:
            if '.'+ext in folders[folder_name]:
                if folder_name not in os.listdir(directory):
                    os.mkdir(os.path.join(directory, folder_name))
                shutil.move(
                    os.path.join(directory, file_name),
                    os.path.join(directory, folder_name)
                )
                find_check = True
                break
        if find_check != True:
            if other_name not in os.listdir(directory):
                os.mkdir(os.path.join(directory, other_name))
            shutil.move(
                os.path.join(directory, file_name),
                os.path.join(directory, other_name)
            )
    except:
        Error = showerror(
            "File Sorting App",
            "An exception occurred"
        )


def start_function(directory, lbl_config):

    try:
        other_name = "others"
        rename_folder(directory)
        all_files_list = os.listdir(directory)
        all_files = [file for file in all_files_list if os.path.isfile(
            os.path.join(directory, file))]
        length = len(all_files)
        count = 0

        for i in all_files:
            if os.path.isfile(os.path.join(directory, i)) == True:
                create_move(directory, i.split('.')[-1], i, other_name)
                count += 1
                lbl_config(count, length)

        Message = showinfo(
            "File Sorting App",
            f"{count} File Successfully Sorted!"
        )

    except:
        Error = showerror(
            "File Sorting App",
            "Error Found"
        )


def clear_function(var_folderName, lbl_status_total, lbl_status_move, lbl_status_left):
    var_folderName.set('')
    lbl_status_total.config(text='TOTAL: 0')
    lbl_status_move.config(text='MOVE: 0')
    lbl_status_left.config(text='LEFT: 0')
