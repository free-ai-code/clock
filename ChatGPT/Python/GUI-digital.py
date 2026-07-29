import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("デジタル時計")
root.geometry("400x150")

label = tk.Label(
    root,
    font=("Consolas", 40),
    bg="black",
    fg="lime"
)
label.pack(expand=True, fill="both")

def update_time():
    label.config(text=strftime("%Y-%m-%d\n%H:%M:%S"))
    label.after(1000, update_time)

update_time()
root.mainloop()
