import tkinter as tk
import time
from datetime import datetime

def update_time():
    """時刻を更新する"""
    current_time = datetime.now().strftime("%H:%M:%S")
    time_label.config(text=current_time)
    root.after(1000, update_time)  # 1秒後に再度更新

# ウィンドウ作成
root = tk.Tk()
root.title("GUI Digital Clock")
root.geometry("300x100")

# 時刻表示ラベル
time_label = tk.Label(root, font=("Helvetica", 48), bg="black", fg="white")
time_label.pack(expand=True, fill="both")

# 時刻更新開始
update_time()

# ウィンドウ実行
root.mainloop()
