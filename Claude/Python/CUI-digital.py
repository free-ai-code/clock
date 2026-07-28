import time
import os

def cui_digital_clock():
    """ターミナルに表示するデジタル時計"""
    try:
        while True:
            # 画面をクリア
            os.system('clear' if os.name == 'posix' else 'cls')
            
            # 現在時刻を取得
            current_time = time.strftime("%H:%M:%S")
            current_date = time.strftime("%Y-%m-%d")
            
            # 表示
            print("\n" * 3)
            print("=" * 40)
            print(f"         {current_date}")
            print(f"         {current_time}")
            print("=" * 40)
            print("\n(終了: Ctrl+C)")
            
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\n時計を終了しました")

if __name__ == "__main__":
    cui_digital_clock()
