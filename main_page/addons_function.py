from tkinter import Frame


def delete_widget(frame: Frame):
    for widget in frame.winfo_children():
        widget.destroy()