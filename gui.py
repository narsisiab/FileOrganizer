import tkinter as tk
from tkinter import filedialog

from organizer import (
    organize_files,
    is_valid_folder
)


def choose_folder():

    folder_path = filedialog.askdirectory()

    if not folder_path:
        return

    if not is_valid_folder(folder_path):

        result_label.config(
            text="Invalid folder"
        )

        return

    try:

        count = organize_files(
            folder_path
        )

        result_label.config(
            text=f"Moved {count} files"
        )

    except Exception as e:

        result_label.config(
            text=f"Error: {e}"
        )


root = tk.Tk()

root.title(
    "File Organizer"
)

root.geometry(
    "500x250"
)

button = tk.Button(
    root,
    text="Choose Folder",
    command=choose_folder
)

button.pack(pady=20)

result_label = tk.Label(
    root,
    text=""
)

result_label.pack()

root.mainloop()