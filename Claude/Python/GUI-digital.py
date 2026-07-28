import tkinter as tk
import time

class DigitalClockGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("デジタル時計")
        self.root.geometry("400x150")
        self.root.configure(bg="#1a1a1a")
        
        # 日付ラベル
        self.date_label = tk.Label(
            root,
            font=("Arial", 24),
            background="#1a1a1a",
            foreground="#00ff00"
        )
        self.date_label.pack(pady=10)
        
        # 時刻ラベル
        self.time_label = tk.Label(
            root,
            font=("Arial", 80, "bold"),
            background="#1a1a1a",
            foreground="#00ff00"
        )
        self.time_label.pack(pady=20)
        
        self.update_time()
    
    def update_time(self):
        """時刻を更新"""
        current_time = time.strftime("%H:%M:%S")
        current_date = time.strftime("%Y年%m月%d日 (%A)")
        
        self.time_label.config(text=current_time)
        self.date_label.config(text=current_date)
        
        # 1000ミリ秒後に再度実行
        self.root.after(1000, self.update_time)

if __name__ == "__main__":
    root = tk.Tk()
    clock = DigitalClockGUI(root)
    root.mainloop()
