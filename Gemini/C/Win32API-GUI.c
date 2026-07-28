#include <windows.h>
#include <stdio.h>

#define ID_TIMER 1

LRESULT CALLBACK WndProc(HWND hwnd, UINT msg, WPARAM wParam, LPARAM lParam) {
    static char date_str[64] = "";
    static char time_str[64] = "";

    switch (msg) {
        case WM_CREATE:
            // 1秒(1000ms)ごとにWM_TIMERイベントを発生させる
            SetTimer(hwnd, ID_TIMER, 1000, NULL);
            // 初回表示用に一度更新メッセージを送る
            SendMessage(hwnd, WM_TIMER, 0, 0);
            return 0;

        case WM_TIMER: {
            SYSTEMTIME st;
            GetLocalTime(&st);

            const char *days[] = {"日", "月", "火", "水", "木", "金", "土"};

            snprintf(date_str, sizeof(date_str), "%04d/%02d/%02d (%s)",
                     st.wYear, st.wMonth, st.wDay, days[st.wDayOfWeek]);
            snprintf(time_str, sizeof(time_str), "%02d:%02d:%02d",
                     st.wHour, st.wMinute, st.wSecond);

            // 画面の再描画を要求
            InvalidateRect(hwnd, NULL, TRUE);
            return 0;
        }

        case WM_PAINT: {
            PAINTSTRUCT ps;
            HDC hdc = BeginPaint(hwnd, &ps);

            // 背景描画（ダークモード風 #0D1117）
            HBRUSH hBrush = CreateSolidBrush(RGB(13, 17, 23));
            FillRect(hdc, &ps.rcPaint, hBrush);
            DeleteObject(hBrush);

            SetBkMode(hdc, TRANSPARENT);

            // 日付の描画
            HFONT hFontDate = CreateFontA(20, 0, 0, 0, FW_NORMAL, FALSE, FALSE, FALSE,
                                          DEFAULT_CHARSET, OUT_DEFAULT_PRECIS,
                                          CLIP_DEFAULT_PRECIS, DEFAULT_QUALITY,
                                          DEFAULT_PITCH | FF_DONTCARE, "Segoe UI");
            SelectObject(hdc, hFontDate);
            SetTextColor(hdc, RGB(139, 148, 158));
            TextOutA(hdc, 50, 25, date_str, strlen(date_str));
            DeleteObject(hFontDate);

            // 時間の描画（大きく表示）
            HFONT hFontTime = CreateFontA(48, 0, 0, 0, FW_BOLD, FALSE, FALSE, FALSE,
                                          DEFAULT_CHARSET, OUT_DEFAULT_PRECIS,
                                          CLIP_DEFAULT_PRECIS, DEFAULT_QUALITY,
                                          DEFAULT_PITCH | FF_DONTCARE, "Segoe UI");
            SelectObject(hdc, hFontTime);
            SetTextColor(hdc, RGB(88, 166, 255));
            TextOutA(hdc, 40, 55, time_str, strlen(time_str));
            DeleteObject(hFontTime);

            EndPaint(hwnd, &ps);
            return 0;
        }

        case WM_DESTROY:
            KillTimer(hwnd, ID_TIMER);
            PostQuitMessage(0);
            return 0;
    }
    return DefWindowProc(hwnd, msg, wParam, lParam);
}

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow) {
    const char CLASS_NAME[] = "ClockWindowClass";

    WNDCLASS wc = {0};
    wc.lpfnWndProc   = WndProc;
    wc.hInstance     = hInstance;
    wc.lpszClassName = CLASS_NAME;
    wc.hbrBackground = (HBRUSH)(COLOR_WINDOW + 1);
    wc.hCursor       = LoadCursor(NULL, IDC_ARROW);

    RegisterClass(&wc);

    HWND hwnd = CreateWindowEx(
        0, CLASS_NAME, "C Digital Clock",
        WS_OVERLAPPED | WS_CAPTION | WS_SYSMENU | WS_MINIMIZEBOX,
        CW_USEDEFAULT, CW_USEDEFAULT, 320, 160,
        NULL, NULL, hInstance, NULL
    );

    if (hwnd == NULL) return 0;

    ShowWindow(hwnd, nCmdShow);

    MSG msg = {0};
    while (GetMessage(&msg, NULL, 0, 0)) {
        TranslateMessage(&msg);
        DispatchMessage(&msg);
    }

    return 0;
}
