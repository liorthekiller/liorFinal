import tkinter as tk
import socket
import chess
import chess.svg
import threading
import random

from board import TimerApp_for_white

from clientOOP import clientOOP


def update_time(number):
    print(number)
    root = tk.Tk()
    app = TimerApp_for_white(root,number)
    root.mainloop()


def open_new_window():
    # root.destroy()

    # Create a new window
    new_window = tk.Tk()
    new_window.title("New Window")

    # Add a label to the new window
    label = tk.Label(new_window, text="This is the new window")
    label.pack()

    # Start the event loop for the new window
    new_window.mainloop()


def open_window(root, window_type):
    root.title(window_type)
    if window_type == "main":
        button = tk.Button(root, text="start game!", command=open_new_window)
        button.pack()
        time1 = tk.Button(root, text="5 minutes", command=lambda: update_time(5))
        time1.pack()

        time2 = tk.Button(root, text="10 minutes", command=lambda: update_time(10))
        time2.pack()
        time3 = tk.Button(root, text="15 minutes", command=lambda: update_time(15))
        time3.pack()
        time4 = tk.Button(root, text="infinity ∞", command=lambda: update_time(0))
        time4.pack()



        root.mainloop()

def main():
    root = tk.Tk()
    thread = threading.Thread(target=clientOOP)
    thread.start()
    open_window(root,"main")

main()