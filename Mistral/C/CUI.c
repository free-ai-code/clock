#include <stdio.h>
#include <time.h>
#include <unistd.h>  // sleep()関数用
#include <stdlib.h>  // system()関数用

void clear_screen() {
    #ifdef _WIN32
        system("cls");
    #else
        system("clear");
    #endif
}

int main() {
    time_t current_time;
    struct tm *time_info;
    char time_str[9];  // HH:MM:SS + null terminator

    printf("=== CUI Digital Clock ===\n");
    printf("終了するには Ctrl+C を押してください\n");

    while (1) {
        // 現在時刻を取得
        time(&current_time);
        time_info = localtime(&current_time);
        strftime(time_str, sizeof(time_str), "%H:%M:%S", time_info);

        // 画面をクリアして時刻を表示
        clear_screen();
        printf("現在時刻: %s\n", time_str);

        // 1秒待機
        sleep(1);
    }

    return 0;
}
