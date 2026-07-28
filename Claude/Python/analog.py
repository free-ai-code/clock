import tkinter as tk
import time
import math

class AnalogClockGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("アナログ時計")
        self.root.geometry("500x550")
        self.root.configure(bg="#f0f0f0")
        
        # キャンバスの作成
        self.canvas = tk.Canvas(
            root,
            width=500,
            height=500,
            bg="white",
            highlightthickness=2
        )
        self.canvas.pack(pady=10)
        
        # 時刻表示ラベル
        self.time_label = tk.Label(
            root,
            font=("Arial", 16),
            foreground="#333333"
        )
        self.time_label.pack()
        
        # 時計の中心
        self.center_x = 250
        self.center_y = 250
        self.radius = 180
        
        self.draw_clock()
        self.update_clock()
    
    def draw_clock(self):
        """時計の枠組みを描画"""
        # 時計の外枠（円）
        self.canvas.create_oval(
            self.center_x - self.radius,
            self.center_y - self.radius,
            self.center_x + self.radius,
            self.center_y + self.radius,
            outline="black",
            width=3
        )
        
        # 時間マーク
        for i in range(12):
            angle = math.radians(i * 30 - 90)
            x1 = self.center_x + (self.radius - 15) * math.cos(angle)
            y1 = self.center_y + (self.radius - 15) * math.sin(angle)
            x2 = self.center_x + (self.radius - 5) * math.cos(angle)
            y2 = self.center_y + (self.radius - 5) * math.sin(angle)
            
            self.canvas.create_line(x1, y1, x2, y2, width=3)
            
            # 数字
            number = i if i != 0 else 12
            text_x = self.center_x + (self.radius - 35) * math.cos(angle)
            text_y = self.center_y + (self.radius - 35) * math.sin(angle)
            self.canvas.create_text(text_x, text_y, text=str(number), font=("Arial", 14, "bold"))
        
        # 中心の点
        self.canvas.create_oval(
            self.center_x - 8,
            self.center_y - 8,
            self.center_x + 8,
            self.center_y + 8,
            fill="black"
        )
    
    def draw_hand(self, angle, length, width, color, tag):
        """針を描画"""
        rad = math.radians(angle - 90)
        x = self.center_x + length * math.cos(rad)
        y = self.center_y + length * math.sin(rad)
        
        self.canvas.create_line(
            self.center_x, self.center_y,
            x, y,
            width=width,
            fill=color,
            capstyle=tk.ROUND,
            tag=tag
        )
    
    def update_clock(self):
        """時計を更新"""
        # 既存の針を削除
        self.canvas.delete("hands")
        
        # 現在時刻を取得
        current_time = time.localtime()
        hours = current_time.tm_hour % 12
        minutes = current_time.tm_min
        seconds = current_time.tm_sec
        
        # 時間を角度に変換
        second_angle = seconds * 6  # 60秒で360度
        minute_angle = minutes * 6 + seconds * 0.1  # 60分で360度
        hour_angle = hours * 30 + minutes * 0.5  # 12時間で360度
        
        # 針を描画
        self.draw_hand(hour_angle, 80, 8, "#333333", "hands")  # 時針
        self.draw_hand(minute_angle, 120, 6, "#666666", "hands")  # 分針
        self.draw_hand(second_angle, 140, 2, "#ff0000", "hands")  # 秒針
        
        # デジタル時刻表示
        digital_time = time.strftime("%H:%M:%S")
        self.time_label.config(text=digital_time)
        
        # 50ミリ秒後に再度実行
        self.root.after(50, self.update_clock)

if __name__ == "__main__":
    root = tk.Tk()
    clock = AnalogClockGUI(root)
    root.mainloop()
