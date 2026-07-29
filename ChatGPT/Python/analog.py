import tkinter as tk
import math
from time import localtime

root = tk.Tk()
root.title("アナログ時計")
root.resizable(False, False)

W, H = 400, 400
CX, CY = W // 2, H // 2
R = 180

canvas = tk.Canvas(root, width=W, height=H, bg="white")
canvas.pack()

def draw_clock_face():
    canvas.delete("all")
    canvas.create_oval(CX-R, CY-R, CX+R, CY+R, width=3)

    for i in range(60):
        angle = math.radians(i * 6 - 90)
        outer_x = CX + R * math.cos(angle)
        outer_y = CY + R * math.sin(angle)
        inner_r = R - 15 if i % 5 == 0 else R - 8
        inner_x = CX + inner_r * math.cos(angle)
        inner_y = CY + inner_r * math.sin(angle)
        canvas.create_line(inner_x, inner_y, outer_x, outer_y, width=3 if i % 5 == 0 else 1)

    for n in range(1, 13):
        angle = math.radians(n * 30 - 90)
        tx = CX + (R - 35) * math.cos(angle)
        ty = CY + (R - 35) * math.sin(angle)
        canvas.create_text(tx, ty, text=str(n), font=("Arial", 14, "bold"))

def draw_hand(angle_deg, length, width, color):
    angle = math.radians(angle_deg - 90)
    x = CX + length * math.cos(angle)
    y = CY + length * math.sin(angle)
    canvas.create_line(CX, CY, x, y, width=width, fill=color)

def update_clock():
    draw_clock_face()

    t = localtime()
    sec = t.tm_sec
    minute = t.tm_min + sec / 60
    hour = (t.tm_hour % 12) + minute / 60

    # 針
    draw_hand(hour * 30, R * 0.5, 6, "black")
    draw_hand(minute * 6, R * 0.7, 4, "blue")
    draw_hand(sec * 6, R * 0.8, 2, "red")

    canvas.create_oval(CX-6, CY-6, CX+6, CY+6, fill="black")
    root.after(1000, update_clock)

update_clock()
root.mainloop()
