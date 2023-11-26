import tkinter as tk


def pomodoro_func(frame, content: str = 'Whatever content',
                  title_font: tuple[str, int, str] = ("Arial", 18, "bold")):

    label = tk.Label(frame, text=content, font=title_font, bg='black', fg='white')
    label.place(x=260, y=80)

    button = tk.Button(frame, text="Click Me", command=lambda: print("Button clicked"))
    button.place(x=260, y=100)
