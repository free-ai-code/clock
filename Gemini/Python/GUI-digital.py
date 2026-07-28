import tkinter as tk
import time

def update_clock():
    # 現在の時刻と日付を取得
    current_time = time.strftime("%H:%M:%S")
    current_date = time.strftime("%Y/%m/%d (%a)")
    
    # ラベルの文字を更新
    time_label.config(text=current_time)
    date_label.config(text=current_date)
    
    # 1000ミリ秒（1秒）後に再度この関数を実行
    root.after(1000, update_clock)

# ウィンドウの設定
root = tk.Tk()
root.title("Digital Clock")
root.geometry("350x150")
root.configure(bg="#0d1117")  # ダークモード風背景
root.resizable(False, False)  # サイズ変更を固定

# 日付表示用ラベル
date_label = tk.Label(
    root, 
    font=("Segoe UI", 14), 
    bg="#0d1117", 
    fg="#8b949e"
)
date_label.pack(pady=(20, 0))

# 時刻表示用ラベル（大きく表示）
time_label = tk.Label(
    root, 
    font=("Segoe UI", 40, "bold"), 
    bg="#0d1117", 
    fg="#58a6ff"
)
time_label.pack(pady=(0, 20))

# 時計の更新処理をスタート
update_clock()

# アプリを実行
root.mainloop()
