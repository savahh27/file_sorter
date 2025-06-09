import os
import shutil
from tkinter import *
from tkinter import messagebox

def organize_files_by_extension(directory):
    try:
        os.chdir(directory)

        for file in os.listdir():
            if os.path.isfile(file):
                name, ext = os.path.splitext(file)
                ext = ext[1:].upper() or "NO_EXTENSION"
                target_dir = os.path.join(directory, f"{ext}_Files")

                if not os.path.exists(target_dir):
                    os.mkdir(target_dir)

                shutil.move(file, os.path.join(target_dir, file))

    except Exception as e:
        messagebox.showwarning("Error", str(e) + "!")

root = Tk()

root.title("File Sorter")
root.iconbitmap(r"C:\Users\Korisnik\Desktop\sort downloads\generic-sorting-32.ico")

e = Entry(root, width=40, font=('Helvetica', 14), bg="#9ce1cf")
e.insert(0, "Enter Directory Location")
e.grid(row=0, column=0, rowspan=2, pady=10, padx=5)

def clear_entry(event):
    if e.get() == "Enter Directory Location":
        e.delete(0, END)

e.bind("<FocusIn>", clear_entry)

btn = Button(root, text="Sort It!", command=lambda: organize_files_by_extension(e.get()), font=("Helvetica", 12), 
              activebackground="#c3f7ea", activeforeground="#b9c69c", bd=3, cursor="hand2", bg="#9ce1cf", fg="#6a705d")
btn.grid(row=2, column=0, pady=10)

root.mainloop()
