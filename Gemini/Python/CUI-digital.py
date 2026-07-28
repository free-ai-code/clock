import time
import os

try:
    while True:
        # 画面をクリア（Windowsなら 'cls', Mac/Linuxなら 'clear'）
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # 現在時刻を取得して表示
        now = time.strftime("%Y-%m-%d %H:%M:%S")
        print("====================")
        print(f"   {now}   ")
        print("====================")
        print(" (Ctrl+C で終了)")
        
        time.sleep(1)
except KeyboardInterrupt:
    print("\n時計を終了しました。")
