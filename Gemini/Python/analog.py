import math
import tkinter as tk
from datetime import datetime


class SmoothClockApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Smooth Analog Clock")
        self.root.geometry("420x440")

        # デザイン用のカラーパレット（ダークテーマ）
        self._bg_color = "#1C1C1E"  # 背景色
        self._clock_face_color = "#2C2C2E"  # 文字盤背景
        self._rim_color = "#48484A"  # 外枠
        self._tick_color = "#AEAEB2"  # 目盛り
        self._hour_hand_color = "#FFFFFF"  # 時針
        self._min_hand_color = "#D1D1D6"  # 分針
        self._sec_hand_color = "#FF453A"  # 秒針

        self.root.configure(bg=self._bg_color)

        # 描画用キャンバス（ダブルバッファリングは自動適用）
        self.canvas = tk.Canvas(
            root, bg=self._bg_color, highlightthickness=0
        )
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # 画面サイズ変更イベントのバインド
        self.canvas.bind("<Configure>", self.on_resize)

        # 初回の描画フラグ
        self.initialized = False

        # 60FPS相当 (16ms) でループタイマーを開始
        self.update_clock()

    def create_clock_elements(self, cx, cy, radius):
        """文字盤や目盛りなど、動かない静的な部品を1度だけ作成する"""
        self.canvas.delete("all")

        # 1. 文字盤の背景と外枠
        self.canvas.create_oval(
            cx - radius,
            cy - radius,
            cx + radius,
            cy + radius,
            fill=self._clock_face_color,
            outline=self._rim_color,
            width=4,
        )

        # 2. 目盛り（インデックス）の描画
        for i in range(60):
            angle = (i / 60.0) * 2.0 * math.pi - math.pi / 2.0
            outer = radius * 0.95
            inner = radius * 0.85 if i % 5 == 0 else radius * 0.90
            line_width = 3 if i % 5 == 0 else 1

            x1 = cx + math.cos(angle) * inner
            y1 = cy + math.sin(angle) * inner
            x2 = cx + math.cos(angle) * outer
            y2 = cy + math.sin(angle) * outer

            self.canvas.create_line(
                x1, y1, x2, y2, fill=self._tick_color, width=line_width
            )

        # 3. 針オブジェクトの先行作成（ダミー座標で作り、後で座標更新する）
        # tkinterは丸い先端（capstyle="round"）をサポートしています
        self.hour_hand = self.canvas.create_line(
            0,
            0,
            0,
            0,
            fill=self._hour_hand_color,
            width=6,
            capstyle="round",
        )
        self.min_hand = self.canvas.create_line(
            0,
            0,
            0,
            0,
            fill=self._min_hand_color,
            width=4,
            capstyle="round",
        )
        self.sec_hand = self.canvas.create_line(
            0, 0, 0, 0, fill=self._sec_hand_color, width=2, capstyle="round"
        )

        # 4. 中央のピン（キャップ）
        pin_radius = 5
        self.canvas.create_oval(
            cx - pin_radius,
            cy - pin_radius,
            cx + pin_radius,
            cy + pin_radius,
            fill=self._sec_hand_color,
            outline="",
        )

        inner_pin_radius = 2
        self.canvas.create_oval(
            cx - inner_pin_radius,
            cy - inner_pin_radius,
            cx + inner_pin_radius,
            cy + inner_pin_radius,
            fill=self._bg_color,
            outline="",
        )

        self.initialized = True

    def update_hand_position(
        self, hand_obj, value, max_val, length, cx, cy, offset=0.0
    ):
        """指定した針オブジェクトの座標を計算して更新する"""
        angle = (value / max_val) * 2.0 * math.pi - math.pi / 2.0

        # 中心から後ろに少し突き出るデザイン用の開始点計算
        start_x = cx - math.cos(angle) * offset
        start_y = cy - math.sin(angle) * offset
        target_x = cx + math.cos(angle) * length
        target_y = cy + math.sin(angle) * length

        # 既存のオブジェクトの座標だけを書き換える（超高速）
        self.canvas.coords(hand_obj, start_x, start_y, target_x, target_y)

    def update_clock(self):
        """16ミリ秒ごとに呼ばれるループ処理"""
        if self.initialized:
            w = self.canvas.winfo_width()
            h = self.canvas.winfo_height()
            radius = min(w, h) / 2.0 * 0.85
            cx = w / 2.0
            cy = h / 2.0

            # 時間の計算（ミリ秒を含めて滑らかに移動）
            now = datetime.now()
            ms = now.microsecond / 1000.0
            sec = now.second + (ms / 1000.0)
            minute = now.minute + (sec / 60.0)
            hour = (now.hour % 12) + (minute / 60.0)

            # 各針の座標を更新（秒針は後ろに15%突き出る）
            self.update_hand_position(
                self.hour_hand, hour, 12, radius * 0.50, cx, cy
            )
            self.update_hand_position(
                self.min_hand, minute, 60, radius * 0.75, cx, cy
            )
            self.update_hand_position(
                self.sec_hand, sec, 60, radius * 0.85, cx, cy, radius * 0.15
            )

        # 16ms後に再度このメソッドを実行
        self.root.after(16, self.update_clock)

    def on_resize(self, event):
        """ウィンドウサイズが変わった時に文字盤を再構成する"""
        w = event.width
        h = event.height
        radius = min(w, h) / 2.0 * 0.85
        cx = w / 2.0
        cy = h / 2.0
        self.create_clock_elements(cx, cy, radius)


if __name__ == "__main__":
    root = tk.Tk()
    app = SmoothClockApp(root)
    root.mainloop()
