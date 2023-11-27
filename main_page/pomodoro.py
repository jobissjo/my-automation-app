import tkinter as tk
from datetime import timedelta
import os


def pomodoro_func(frame, content: str = 'Whatever content',
                  title_font: tuple[str, int, str] = ("Arial", 18, "bold")):
    PomodoroTimerApp(frame)


class PomodoroTimerApp:
    def __init__(self, master):
        self.master = master
        # master.title("Pomodoro Timer")

        # print(os.path.abspath('img/tomato.jpg'))
        # Load an image (replace 'path/to/your/image.png' with the actual path)
        print("image loaded")

        self.image = tk.PhotoImage(name='./../img/tomato.jpg')
        print("image loaded")
        # Create a Canvas
        self.canvas = tk.Canvas(master, width=200, height=300)
        self.canvas.pack()

        # Display the image on the Canvas
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image)

        # Initialize timer duration
        self.timer_duration = timedelta(minutes=25)

        # Create a label to display the timer
        self.timer_label = tk.Label(master, text=self.format_time(self.timer_duration), font=("Helvetica", 24))
        self.timer_label.pack()

        # Create Start and Reset buttons
        self.start_button = tk.Button(master, text="Start", command=self.start_timer)
        self.start_button.pack(side=tk.LEFT, padx=10)
        self.reset_button = tk.Button(master, text="Reset", command=self.reset_timer)
        self.reset_button.pack(side=tk.RIGHT, padx=10)

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
