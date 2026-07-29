#include <gtk/gtk.h>
#include <time.h>
#include <math.h>
#include <string.h>

#define CLOCK_SIZE 300
#define CENTER_X (CLOCK_SIZE / 2)
#define CENTER_Y (CLOCK_SIZE / 2)
#define RADIUS (CLOCK_SIZE / 2 - 20)

GtkWidget *drawing_area;

static gboolean draw_clock(GtkWidget *widget, cairo_t *cr, gpointer data) {
    time_t current_time;
    struct tm *time_info;
    int hour, minute, second;
    double hour_angle, minute_angle, second_angle;
    int hour_x, hour_y, minute_x, minute_y, second_x, second_y;

    // 現在時刻を取得
    time(&current_time);
    time_info = localtime(&current_time);
    hour = time_info->tm_hour % 12;
    minute = time_info->tm_min;
    second = time_info->tm_sec;

    // 画面をクリア
    cairo_set_source_rgb(cr, 1, 1, 1);  // 白で塗りつぶし
    cairo_paint(cr);

    // 時計の外枠
    cairo_set_source_rgb(cr, 0, 0, 0);  // 黒
    cairo_set_line_width(cr, 2);
    cairo_arc(cr, CENTER_X, CENTER_Y, RADIUS, 0, 2 * M_PI);
    cairo_stroke(cr);

    // 目盛りを描画
    for (int i = 0; i < 12; i++) {
        double angle = i * M_PI / 6 - M_PI / 2;  // 12時方向を0度とする
        int x1 = CENTER_X + (RADIUS - 10) * cos(angle);
        int y1 = CENTER_Y + (RADIUS - 10) * sin(angle);
        int x2 = CENTER_X + RADIUS * cos(angle);
        int y2 = CENTER_Y + RADIUS * sin(angle);

        cairo_set_line_width(cr, 2);
        cairo_move_to(cr, x1, y1);
        cairo_line_to(cr, x2, y2);
        cairo_stroke(cr);

        // 数字を描画
        char num_str[3];
        sprintf(num_str, "%d", i + 1);
        cairo_set_source_rgb(cr, 0, 0, 0);
        cairo_set_font_size(cr, 12);
        cairo_move_to(cr, CENTER_X + (RADIUS - 25) * cos(angle - M_PI/6),
                            CENTER_Y + (RADIUS - 25) * sin(angle - M_PI/6));
        cairo_show_text(cr, num_str);
    }

    // 時針
    hour_angle = (hour * 30 + minute * 0.5) * M_PI / 180 - M_PI / 2;
    hour_x = CENTER_X + RADIUS * 0.5 * cos(hour_angle);
    hour_y = CENTER_Y + RADIUS * 0.5 * sin(hour_angle);
    cairo_set_source_rgb(cr, 0, 0, 0);
    cairo_set_line_width(cr, 6);
    cairo_move_to(cr, CENTER_X, CENTER_Y);
    cairo_line_to(cr, hour_x, hour_y);
    cairo_stroke(cr);

    // 分針
    minute_angle = (minute * 6) * M_PI / 180 - M_PI / 2;
    minute_x = CENTER_X + RADIUS * 0.7 * cos(minute_angle);
    minute_y = CENTER_Y + RADIUS * 0.7 * sin(minute_angle);
    cairo_set_source_rgb(cr, 0, 0, 1);
    cairo_set_line_width(cr, 4);
    cairo_move_to(cr, CENTER_X, CENTER_Y);
    cairo_line_to(cr, minute_x, minute_y);
    cairo_stroke(cr);

    // 秒針
    second_angle = (second * 6) * M_PI / 180 - M_PI / 2;
    second_x = CENTER_X + RADIUS * 0.9 * cos(second_angle);
    second_y = CENTER_Y + RADIUS * 0.9 * sin(second_angle);
    cairo_set_source_rgb(cr, 1, 0, 0);
    cairo_set_line_width(cr, 2);
    cairo_move_to(cr, CENTER_X, CENTER_Y);
    cairo_line_to(cr, second_x, second_y);
    cairo_stroke(cr);

    // 中心の丸
    cairo_set_source_rgb(cr, 0, 0, 0);
    cairo_arc(cr, CENTER_X, CENTER_Y, 5, 0, 2 * M_PI);
    cairo_fill(cr);

    return TRUE;
}

static gboolean update_clock(gpointer user_data) {
    gtk_widget_queue_draw(drawing_area);
    return TRUE;
}

static void activate(GtkApplication *app, gpointer user_data) {
    GtkWidget *window;
    GtkWidget *box;

    // ウィンドウ作成
    window = gtk_application_window_new(app);
    gtk_window_set_title(GTK_WINDOW(window), "GUI Analog Clock");
    gtk_window_set_default_size(GTK_WINDOW(window), CLOCK_SIZE, CLOCK_SIZE);

    // ボックスレイアウト
    box = gtk_box_new(GTK_ORIENTATION_VERTICAL, 0);
    gtk_container_add(GTK_CONTAINER(window), box);

    // 描画領域
    drawing_area = gtk_drawing_area_new();
    gtk_widget_set_size_request(drawing_area, CLOCK_SIZE, CLOCK_SIZE);
    gtk_box_pack_start(GTK_BOX(box), drawing_area, TRUE, TRUE, 0);

    // 描画シグナル接続
    g_signal_connect(drawing_area, "draw", G_CALLBACK(draw_clock), NULL);

    // 時刻更新開始（1秒ごと）
    g_timeout_add_seconds(1, update_clock, NULL);

    // ウィンドウ表示
    gtk_widget_show_all(window);
}

int main(int argc, char **argv) {
    GtkApplication *app;
    int status;

    app = gtk_application_new("org.example.analogclock", G_APPLICATION_FLAGS_NONE);
    g_signal_connect(app, "activate", G_CALLBACK(activate), NULL);
    status = g_application_run(G_APPLICATION(app), argc, argv);
    g_object_unref(app);

    return status;
}
