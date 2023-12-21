import tkinter as tk
import threading
import time

class TimerApp_for_white :
    def __init__(self, root, duration):
        self.root = root
        self.root.title("Stopwatch App")

        self.duration = duration*60
        self.remaining_time = self.duration
        self.is_running = False

        self.timer_label = tk.Label(root, text=self.format_time(self.remaining_time), font=("Helvetica", 24))
        self.timer_label.pack(padx=20, pady=10)

        self.start_button = tk.Button(root, text="Start", command=self.start_timer)
        self.start_button.pack(padx=20, pady=5)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_timer, state=tk.DISABLED)
        self.stop_button.pack(padx=20, pady=5)

    def update_timer(self):
        while self.is_running and self.remaining_time > 0:
            self.timer_label.config(text=self.format_time(self.remaining_time))
            time.sleep(1)
            self.remaining_time -= 1

        if self.remaining_time <= 0:
            self.timer_label.config(text="Time's up!")
            self.is_running = False
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)

    def start_timer(self):
        if not self.is_running:
            self.is_running = True
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            self.thread = threading.Thread(target=self.update_timer)
            self.thread.start()

    def stop_timer(self):
        if self.is_running:
            self.is_running = False
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)

    @staticmethod
    def format_time(seconds):
        hours = int(seconds / 3600)
        minutes = int((seconds % 3600) / 60)
        seconds = int(seconds % 60)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
