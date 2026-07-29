import tkinter as tk
import time
import math
from datetime import datetime

class AnalogClock:
    def __init__(self, root):
        self.root = root
        self.root.title("GUI Analog Clock")
        self.root.geometry("400x400")

        # キャンバス作成
        self.canvas = tk.Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack()

        # 時計の目盛りを描画
        self.draw_clock_face()

        # 時刻更新
        self.update_clock()

    def draw_clock_face(self):
        """時計の目盛りを描画"""
        self.canvas.create_oval(50, 50, 350, 350, width=2)  # 時計の外枠

        # 目盛りを描画
        for i in range(12):
            angle = math.radians(i * 30 - 90)  # 12時方向を0度とする
            x1 = 200 + 150 * math.cos(angle)
            y1 = 200 + 150 * math.sin(angle)
            x2 = 200 + 170 * math.cos(angle)
            y2 = 200 + 170 * math.sin(angle)
            self.canvas.create_line(x1, y1, x2, y2, width=2)

            # 数字を描画
            num_angle = math.radians(i * 30 - 60)
            num_x = 200 + 130 * math.cos(num_angle)
            num_y = 200 + 130 * math.sin(num_angle)
            self.canvas.create_text(num_x, num_y, text=str(i+1), font=("Helvetica", 12))

    def update_clock(self):
        """時計の針を更新"""
        self.canvas.delete("hands")  # 既存の針を消去

        now = datetime.now()
        hour = now.hour % 12
        minute = now.minute
        second = now.second

        # 時針
        hour_angle = math.radians((hour * 30) + (minute * 0.5) - 90)
        hour_x = 200 + 60 * math.cos(hour_angle)
        hour_y = 200 + 60 * math.sin(hour_angle)
        self.canvas.create_line(200, 200, hour_x, hour_y, width=6, fill="black", tags="hands")

        # 分針
        minute_angle = math.radians((minute * 6) - 90)
        minute_x = 200 + 90 * math.cos(minute_angle)
        minute_y = 200 + 90 * math.sin(minute_angle)
        self.canvas.create_line(200, 200, minute_x, minute_y, width=4, fill="blue", tags="hands")

        # 秒針
        second_angle = math.radians((second * 6) - 90)
        second_x = 200 + 120 * math.cos(second_angle)
        second_y = 200 + 120 * math.sin(second_angle)
        self.canvas.create_line(200, 200, second_x, second_y, width=2, fill="red", tags="hands")

        # 中心の丸
        self.canvas.create_oval(195, 195, 205, 205, fill="black", tags="hands")

        # 1秒後に再度更新
        self.root.after(1000, self.update_clock)

# ウィンドウ作成
root = tk.Tk()
clock = AnalogClock(root)
root.mainloop()
