#include <stdio.h>
#include <time.h>
#include <stdlib.h>

#ifdef _WIN32
  #include <windows.h>
  #define CLEAR_SCREEN() system("cls")
  #define SLEEP_SEC(sec) Sleep((sec) * 1000)
#else
  #include <unistd.h>
  #define CLEAR_SCREEN() system("clear")
  #define SLEEP_SEC(sec) sleep(sec)
#endif

int main(void) {
    time_t rawtime;
    struct tm *timeinfo;
    char date_buf[64];
    char time_buf[64];

    // 曜日名の定義（日本語環境用）
    const char *days[] = {"日", "月", "火", "水", "木", "金", "土"};

    while (1) {
        // 現在時刻を取得
        time(&rawtime);
        timeinfo = localtime(&rawtime);

        // 日付・時刻文字列の整形
        snprintf(date_buf, sizeof(date_buf), "%04d/%02d/%02d (%s)",
                 timeinfo->tm_year + 1900,
                 timeinfo->tm_mon + 1,
                 timeinfo->tm_mday,
                 days[timeinfo->tm_wday]);

        snprintf(time_buf, sizeof(time_buf), "%02d:%02d:%02d",
                 timeinfo->tm_hour,
                 timeinfo->tm_min,
                 timeinfo->tm_sec);

        // 画面をクリアして再描画
        CLEAR_SCREEN();
        printf("======================\n");
        printf("   %s\n", date_buf);
        printf("      %s\n", time_buf);
        printf("======================\n");
        printf(" (Ctrl+C で終了)\n");

        // 1秒待機
        SLEEP_SEC(1);
    }

    return 0;
}
