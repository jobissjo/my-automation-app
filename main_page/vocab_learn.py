import tkinter as tk


def vocabulary_words(frame, content: str = 'whatever content',
                     title_font: tuple[str, int, str] = ("Arial", 18, "bold")):
    label = tk.Label(frame, text=content, font=title_font, bg='black', fg='white')
    label.place(x=260, y=80)

    button = tk.Button(frame, text="Click Me", command=lambda: print("Button clicked"))
    button.place(x=260, y=100)
