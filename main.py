import tkinter as tk
from main_page import starter
import btn_function

TITLE_FONT: tuple[str, int, str] = ("Arial", 18, "bold")
SIDE_LABEL_FONT: tuple[str, int] = ("Verdana", 14)

app = tk.Tk()
app.title("Automation App")
app.geometry("1000x850")
app.resizable(False, False)

label_frame = tk.Frame(app, bd=2, relief=tk.GROOVE, highlightbackground="red")
label_frame.place(x=0, y=0)

label = tk.Label(label_frame, text="Daily Automation Task", padx=10, pady=10, bg='lightblue', fg='black',
                 font=TITLE_FONT, width=70)
label.pack()

# Side Labels

# Pomodoro Button
pomodoro_button = tk.Button(app, text='Pomodoro', font=SIDE_LABEL_FONT, width=20, bg='sky blue', pady=2,
                            command=lambda: btn_function.pomodoro_clicked(main_frame, 'Whatever content'))
pomodoro_button.place(x=0, y=55)

# Vocabulary Learn Button
vocabulary_learn_button = tk.Button(app, text='English Vocabulary', font=SIDE_LABEL_FONT, width=20, bg='sky blue',
                                    pady=2, command=lambda: btn_function.dummy_click(main_frame))
vocabulary_learn_button.place(x=0, y=90)

# NoteTaking Button
note_taking_button = tk.Button(app, text='Note Taking', font=SIDE_LABEL_FONT, width=20, bg='sky blue',
                               pady=2, command=lambda: btn_function.dummy_click(main_frame))
note_taking_button.place(x=0, y=130)

# NoteTaking Button
todo_button = tk.Button(app, text='Todo', font=SIDE_LABEL_FONT, width=20, bg='sky blue',
                        pady=2, command=lambda: btn_function.dummy_click(main_frame))
todo_button.place(x=0, y=170)

# Download YouTube Video Button
video_downloader_button = tk.Button(app, text='Youtube Video', font=SIDE_LABEL_FONT, width=20, bg='sky blue',
                                    pady=2, command=lambda: btn_function.dummy_click(main_frame))
video_downloader_button.place(x=0, y=210)

# Track Progress Button
track_progress_button = tk.Button(app, text='Track Progress', font=SIDE_LABEL_FONT, width=20, bg='sky blue',
                                  pady=2, command=lambda: btn_function.dummy_click(main_frame))
track_progress_button.place(x=0, y=250)

# Book Reading List Button
book_reading_list_button = tk.Button(app, text='Book Reading List', font=SIDE_LABEL_FONT, width=20, bg='sky blue',
                                     pady=2, command=lambda: btn_function.dummy_click(main_frame))
book_reading_list_button.place(x=0, y=290)

# Movie Watchlist Button
movie_watchlist_button = tk.Button(app, text='Movie Watchlist', font=SIDE_LABEL_FONT, width=20, bg='sky blue',
                                   pady=2, command=lambda: btn_function.dummy_click(main_frame))
movie_watchlist_button.place(x=0, y=330)

# Journaling Button
journaling_button = tk.Button(app, text='Journaling', font=SIDE_LABEL_FONT, width=20, bg='sky blue',
                              pady=2, command=lambda: btn_function.dummy_click(main_frame))
journaling_button.place(x=0, y=370)

# Takeaways Button
takeaways_button = tk.Button(app, text='Takeaways', font=SIDE_LABEL_FONT, width=20, bg='sky blue',
                             pady=2, command=lambda: btn_function.dummy_click(main_frame))
takeaways_button.place(x=0, y=410)

# Saved Later Button
saved_later_button = tk.Button(app, text='Saved Later', font=SIDE_LABEL_FONT, width=20, bg='sky blue',
                               pady=2, command=lambda: btn_function.dummy_click(main_frame))
saved_later_button.place(x=0, y=450)

# Remainder Button
remainder_button = tk.Button(app, text='Remainder', font=SIDE_LABEL_FONT, width=20, bg='sky blue',
                             pady=2, command=lambda: btn_function.dummy_click(main_frame))
remainder_button.place(x=0, y=490)

# Build Something Button
build_something_button = tk.Button(app, text='Build Something', font=SIDE_LABEL_FONT, width=20, bg='sky blue',
                                   pady=2, command=lambda: btn_function.dummy_click(main_frame))
build_something_button.place(x=0, y=530)

# Learning New Button
learning_new_button = tk.Button(app, text='Learning New', font=SIDE_LABEL_FONT, width=20, bg='sky blue',
                                pady=2, command=lambda: btn_function.dummy_click(main_frame))
learning_new_button.place(x=0, y=570)

# Entertainment Button
entertainment_button = tk.Button(app, text='Entertainment', font=SIDE_LABEL_FONT, width=20, bg='sky blue',
                                 pady=2, command=lambda: btn_function.dummy_click(main_frame))
entertainment_button.place(x=0, y=570)

# Whatever 1 Button
whatever_1_button = tk.Button(app, text='Whatever 1', font=SIDE_LABEL_FONT, width=20, bg='sky blue',
                              pady=2, command=lambda: btn_function.dummy_click(main_frame))
whatever_1_button.place(x=0, y=610)

# Whatever 2 Button
whatever_2_button = tk.Button(app, text='Whatever 2', font=SIDE_LABEL_FONT, width=20, bg='sky blue',
                              pady=2, command=lambda: btn_function.dummy_click(main_frame))
whatever_2_button.place(x=0, y=650)

# Whatever 3 Button
whatever_3_button = tk.Button(app, text='Whatever 3', font=SIDE_LABEL_FONT, width=20, bg='sky blue',
                              pady=2, command=lambda: btn_function.dummy_click(main_frame))
whatever_3_button.place(x=0, y=690)

# Whatever 4 Button
whatever_4_button = tk.Button(app, text='Whatever 4', font=SIDE_LABEL_FONT, width=20, bg='sky blue',
                              pady=2, command=lambda: btn_function.dummy_click(main_frame))
whatever_4_button.place(x=0, y=730)

# Whatever 5 Button
whatever_5_button = tk.Button(app, text='Whatever 5', font=SIDE_LABEL_FONT, width=20, bg='sky blue',
                              pady=2, command=lambda: btn_function.dummy_click(main_frame))
whatever_5_button.place(x=0, y=770)

# Whatever 6 Button
whatever_6_button = tk.Button(app, text='Whatever 6', font=SIDE_LABEL_FONT, width=20, bg='sky blue',
                              pady=2, command=lambda: btn_function.dummy_click(canvas))
whatever_6_button.place(x=0, y=810)

# Staring Main Page

# canvas = tk.Canvas(app, width=750, height=800, bg='grey')
# canvas.place(x=250, y=55)

main_frame = tk.Frame(app, width=750, height=800, bg='grey')
main_frame.place(x=250, y=55)

# btn_function.update_canvas_content(canvas, "Initial content goes here")

app.mainloop()
