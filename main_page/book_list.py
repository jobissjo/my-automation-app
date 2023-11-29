import tkinter as tk
from main_page.addons_function import delete_widget


def reading_list(frame: tk.Frame):
    delete_widget(frame)
    book_data = [
        {"bookname": "Book 1", "readed": False},
        {"bookname": "Book 2", "readed": True},
        {"bookname": "Book 3", "readed": False},
    ]

    app = BookApp(frame, book_data)


import tkinter as tk
from tkinter import messagebox


class BookApp:
    def __init__(self, master, books_data):
        self.master = master
        # self.master.title("Book List App")

        # Initial book data
        self.book_data = books_data

        # Lists to store books
        self.reading_list = []
        self.read_list = []

        # Create widgets
        self.reading_frame = tk.Frame(master)
        self.reading_frame.pack(side=tk.LEFT, padx=10, pady=10)

        self.read_frame = tk.Frame(master)
        self.read_frame.pack(side=tk.RIGHT, padx=10, pady=10)

        self.create_book_lists()
        self.create_buttons()

    def create_book_lists(self):
        # Display reading list
        tk.Label(self.reading_frame, text="Reading List", font=("Helvetica", 16)).pack()
        self.reading_listbox = tk.Listbox(self.reading_frame, selectmode=tk.SINGLE)
        self.reading_listbox.pack()

        # Display read list
        tk.Label(self.read_frame, text="Read List", font=("Helvetica", 16)).pack()
        self.read_listbox = tk.Listbox(self.read_frame, selectmode=tk.SINGLE)
        self.read_listbox.pack()

        # Populate initial book data
        for book in self.book_data:
            book_name = book['bookname']
            read_status = book['readed']

            if read_status:
                self.read_list.append(book_name)
                self.read_listbox.insert(tk.END, book_name)
            else:
                self.reading_list.append(book_name)
                self.reading_listbox.insert(tk.END, book_name)

    def create_buttons(self):
        # Button to move a book to the read list
        self.read_button = tk.Button(self.reading_frame, text="Read", command=self.move_to_read)
        self.read_button.pack(pady=10)

        # Button to display details of the selected book
        self.details_button = tk.Button(self.master, text="Book Details", command=self.show_book_details)
        self.details_button.pack()

    def move_to_read(self):
        selected_index = self.reading_listbox.curselection()

        if selected_index:
            book_name = self.reading_list.pop(selected_index[0])
            self.read_list.append(book_name)

            # Update listboxes
            self.reading_listbox.delete(0, tk.END)
            self.read_listbox.delete(0, tk.END)

            for book in self.reading_list:
                self.reading_listbox.insert(tk.END, book)

            for book in self.read_list:
                self.read_listbox.insert(tk.END, book)

    def show_book_details(self):
        selected_index = self.reading_listbox.curselection()

        if selected_index:
            book_name = self.reading_list[selected_index[0]]
            messagebox.showinfo("Book Details", f"Book Name: {book_name}")



