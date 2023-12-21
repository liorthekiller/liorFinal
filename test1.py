import tkinter as tk


def open_new_window():
    text = entry.get()

    new_window = tk.Toplevel(root)
    label = tk.Label(new_window, text="Entered Text:")
    label.pack()

    text_label = tk.Label(new_window, text=text)
    text_label.pack()


root = tk.Tk()
root.title("Text Entry Window")

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Submit", command=open_new_window)
button.pack()

root.mainloop()
