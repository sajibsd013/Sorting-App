import sqlite3
from tkinter.messagebox import askyesno, showerror, showinfo


def execute_sql(sql):
    # =======Connect Database======
    with sqlite3.connect('sorting_app.db') as conn:
        conn = sqlite3.connect('sorting_app.db')
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
    return cursor.fetchall()


def get_folders():
    sql_folder = "SELECT DISTINCT  FolderName FROM Extentions "
    folders_db = execute_sql(sql_folder)
    folders = [folder[0] for folder in folders_db]
    return folders


def get_extention(folder):
    sql_ext = f"SELECT extention FROM Extentions WHERE FolderName = '{folder}'"
    ext_db = execute_sql(sql_ext)
    ext = [e[0] for e in ext_db]
    return ext


def insert_extension(ext, folder):
    INSERT_VALUSE = f"INSERT INTO Extentions VALUES('{ext}','{folder}')"
    execute_sql(INSERT_VALUSE)


def remove_ext(ext, folder):
    REMOVE_EXT = f"DELETE FROM Extentions WHERE extention ='{ext}' AND  FolderName = '{folder}'"
    execute_sql(REMOVE_EXT)


def remove_folder(folder):
    REMOVE_FOLDER = f"DELETE FROM Extentions WHERE FolderName ='{folder}'"
    execute_sql(REMOVE_FOLDER)


def update_extention(ext_arr, folder):
    count = 0
    for ext in ext_arr:
        if ext.startswith('.'):
            try:
                insert_extension(ext, folder)
                count += 1
            except:
                Message = showinfo(
                    "File Sorting App",
                    f"{ext} Already Exist!"
                )
    return count


def remove_ext_arr(ext_arr, folder):
    for ext in ext_arr:
        if ext.startswith('.'):
            remove_ext(ext, folder)
