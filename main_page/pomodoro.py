import tkinter as tk
from datetime import timedelta
from PIL import ImageTk, Image
from main_page.addons_function import delete_widget
import os


def pomodoro_func(frame, content: str = 'Whatever content',
                  title_font: tuple[str, int, str] = ("Arial", 18, "bold")):
    delete_widget(frame)
    PomodoroTimerApp(frame)


class PomodoroTimerApp:
    def __init__(self, master):
        self.master: tk.Frame = master
        self.master.configure(bg='white',width=750, height=800)

        temp_path = 'G:/Jobi Development/My Own Projects/Automation Daily Task/img/tomato.jpg'
        image = Image.open(temp_path)
        self.image = ImageTk.PhotoImage(image)

        # Create a Canvas
        self.canvas = tk.Canvas(master, width=612, height=612)
        self.canvas.pack()

        # Display the image on the Canvas
        self.canvas.create_image(50, 50, anchor=tk.NW, image=self.image)

        title_text = "Pomodoro"
        self.canvas.create_text(350, 350, text=title_text, font=("Helvetica", 24, 'bold'), fill="white")

        # Initialize timer duration
        self.timer_duration = timedelta(minutes=25)

        # Create a label to display the timer
        self.timer_label = tk.Label(master, text=self.format_time(self.timer_duration), font=("Helvetica", 24),
                                    pady=10, padx=5, bg="#CD0508", fg="black")
        self.timer_label.config(highlightthickness=0, highlightbackground="white")
        # self.timer_label.pack()
        self.timer_label_window = self.canvas.create_window(350, 400,anchor=tk.N, window=self.timer_label)

        # Create Start and Reset buttons
        # self.start_button = tk.Button(master, text="Start", command=self.start_timer, padx=10, pady=5,
        #                               bg='light green',font=("Helvetica", 18))
        # self.start_button.place(x=50, y=700)
        # self.reset_button = tk.Button(master, text="Reset", command=self.reset_timer, padx=10, pady=5, bg='sky blue',
        #                               font=("Helvetica", 18))
        # self.reset_button.place(x=515, y=500)

        # self.start_button = tk.Button(self.canvas, text="Start", command=self.start_timer, padx=10, pady=5,
        #                               bg='light green', font=("Helvetica", 18))
        # self.canvas.create_window(50, 700, anchor=tk.NW, window=self.start_button)
        #
        # self.reset_button = tk.Button(self.canvas, text="Reset", command=self.reset_timer, padx=10, pady=5,
        #                               bg='sky blue', font=("Helvetica", 18))
        # self.canvas.create_window(515, 500, anchor=tk.NW, window=self.reset_button)

        self.start_button = tk.Button(master, text="Start", command=self.start_timer, padx=10, pady=5,
                                      bg='light green', font=("Helvetica", 18))
        self.start_button.place(x=50, y=650)
        self.reset_button = tk.Button(master, text="Reset", command=self.reset_timer, padx=10, pady=5, bg='sky blue',
                                      font=("Helvetica", 18))
        self.reset_button.pack()

        # Initialize timer state
        self.timer_running = False
        self.update_timer()

    def start_timer(self):
        self.timer_running = not self.timer_running
        if self.timer_running:
            self.start_button.config(text="Pause")
            self.master.after(1000, self.update_timer)
        else:
            self.start_button.config(text="Resume")

    def reset_timer(self):
        self.timer_running = False
        self.start_button.config(text="Start")
        self.timer_duration = timedelta(minutes=25)
        self.update_timer()

    def update_timer(self):
        if self.timer_running and self.timer_duration.total_seconds() > 0:
            self.timer_duration -= timedelta(seconds=1)
            self.timer_label.config(text=self.format_time(self.timer_duration))
            self.master.after(1000, self.update_timer)
        elif self.timer_running:
            self.timer_running = False
            self.start_button.config(text="Start")

    @staticmethod
    def format_time(duration):
        seconds = duration.total_seconds()
        minutes, seconds = divmod(seconds, 60)
        return f"{int(minutes):02d}:{int(seconds):02d}"
