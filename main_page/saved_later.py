import tkinter as tk
from main_page.addons_function import delete_widget


def save_for_later(frame: tk.Frame):
    delete_widget(frame)
    print("takeaway clicked")