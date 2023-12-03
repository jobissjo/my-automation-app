import tkinter as tk
from main_page.addons_function import delete_widget
from PIL import Image, ImageTk
from tkinter import ttk

book_data = [
    {"image": "G:\\Jobi Development\\My Own Projects\\Automation Daily Task\\img\\SLAA.jpeg", "title": "Title 1",
     "button_text": "Button 1"},
    {"image": "G:\\Jobi Development\\My Own Projects\\Automation Daily Task\\img\\TAGR.png", "title": "Title 2",
     "button_text": "Button 2"},
    {"image": "G:\\Jobi Development\\My Own Projects\\Automation Daily Task\\img\\TLAM.jpeg", "title": "Title 3",
     "button_text": "Button 3"},
    {"image": "G:\\Jobi Development\\My Own Projects\\Automation Daily Task\\img\\TLAM.jpeg", "title": "Title 3",
     "button_text": "Button 3"},
    {"image": "G:\\Jobi Development\\My Own Projects\\Automation Daily Task\\img\\SLAA.jpeg", "title": "Title 1",
     "button_text": "Button 1"},
    {"image": "G:\\Jobi Development\\My Own Projects\\Automation Daily Task\\img\\TAGR.png", "title": "Title 2",
     "button_text": "Button 2"},
    {"image": "G:\\Jobi Development\\My Own Projects\\Automation Daily Task\\img\\TLAM.jpeg", "title": "Title 3",
     "button_text": "Button 3"},
    {"image": "G:\\Jobi Development\\My Own Projects\\Automation Daily Task\\img\\TLAM.jpeg", "title": "Title 3",
     "button_text": "Button 3"},
    {"image": "G:\\Jobi Development\\My Own Projects\\Automation Daily Task\\img\\TLAM.jpeg", "title": "Title 3",
     "button_text": "Button 3"},
]


def reading_list(frame: tk.Frame):
    delete_widget(frame)

    app = BookList(frame, book_data)


class BookList:
    def __init__(self, master, data):
        self.master = master
        row_frame = ttk.Frame(self.master, padding=6)
        row_count = 0
        for i, item in enumerate(data):
            if i != 0 and i % 3 == 0:
                row_count = i // 3
                row_frame = ttk.Frame(self.master, padding=5)
            self.create_row(row_frame, item, i, row_count)

        self.master = master
        self.canvas = tk.Canvas(master)
        self.scrollbar = ttk.Scrollbar(master, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)

        self.row_count = 0
        for i, item in enumerate(data):
            if i != 0 and i % 3 == 0:
                self.row_count = i // 3
            self.create_row(self.scrollable_frame, item, i, self.row_count)

    def create_row(self, row_frame, item, column_count, row_count):
        # Frame to hold the row
        row_frame = ttk.Frame(row_frame, padding=5)
        row_frame.pack(fill=tk.X, pady=5)

        # Image
        image = Image.open(item["image"])
        img = ImageTk.PhotoImage(image)
        img_label = ttk.Label(row_frame, image=img)
        img_label.image = img
        img_label.grid(row=row_count, column=column_count, padx=20)

        # Title
        # title_label = ttk.Label(row_frame, text=item["title"])
        # title_label.grid(row=0, column=1, padx=5)

        # # Button
        # button = ttk.Button(row_frame, text=item["button_text"])
        # button.grid(row=0, column=2, padx=5)
