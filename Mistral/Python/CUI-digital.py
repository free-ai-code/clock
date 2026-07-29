import time
import os
import sys

def clear_screen():
    """コンソール画面をクリアする"""
    os.system('cls' if os.name == 'nt' else 'clear')

def digital_clock_cui():
    try:
        while True:
            # 現在時刻を取得
            current_time = time.strftime("%H:%M:%S")

            # 画面をクリアして時刻を表示
            clear_screen()
            print("=== CUI Digital Clock ===")
            print(f"現在時刻: {current_time}")
            print("\n終了するには Ctrl+C を押してください")

            # 1秒待機
            time.sleep(1)

    except KeyboardInterrupt:
        print("\n時計を終了します")
        sys.exit(0)

if __name__ == "__main__":
    digital_clock_cui()
