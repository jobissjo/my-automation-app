import tkinter as tk


def take_notes(frame: tk.Frame, title_font: tuple[str, int, str] = ("Arial", 18, "bold")):
    label = tk.Label(frame, text="This is not taking content", font=title_font, bg='black', fg='white')
    label.place(x=260, y=80)

    button = tk.Button(frame, text="Click Me", command=lambda: print("Button clicked"))
    button.place(x=260, y=100)