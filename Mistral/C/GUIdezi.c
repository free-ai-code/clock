#include <gtk/gtk.h>
#include <time.h>
#include <string.h>

GtkWidget *time_label;

static gboolean update_time(gpointer user_data) {
    time_t current_time;
    struct tm *time_info;
    char time_str[9];  // HH:MM:SS + null terminator

    time(&current_time);
    time_info = localtime(&current_time);
    strftime(time_str, sizeof(time_str), "%H:%M:%S", time_info);

    gtk_label_set_text(GTK_LABEL(time_label), time_str);
    return TRUE;  // 繰り返し実行する
}

static void activate(GtkApplication *app, gpointer user_data) {
    GtkWidget *window;
    GtkWidget *box;

    // ウィンドウ作成
    window = gtk_application_window_new(app);
    gtk_window_set_title(GTK_WINDOW(window), "GUI Digital Clock");
    gtk_window_set_default_size(GTK_WINDOW(window), 300, 100);

    // ボックスレイアウト
    box = gtk_box_new(GTK_ORIENTATION_VERTICAL, 0);
    gtk_container_add(GTK_CONTAINER(window), box);

    // 時刻表示ラベル
    time_label = gtk_label_new("");
    gtk_widget_set_name(time_label, "time_label");
    gtk_label_set_justify(GTK_LABEL(time_label), GTK_JUSTIFY_CENTER);
    gtk_box_pack_start(GTK_BOX(box), time_label, TRUE, TRUE, 0);

    // スタイル設定
    GtkCssProvider *provider = gtk_css_provider_new();
    gtk_css_provider_load_from_data(provider,
        "#time_label { font-size: 48px; font-weight: bold; }", -1, NULL);
    gtk_style_context_add_provider_for_screen(
        gdk_screen_get_default(),
        GTK_STYLE_PROVIDER(provider),
        GTK_STYLE_PROVIDER_PRIORITY_APPLICATION);

    // 時刻更新開始（1秒ごと）
    g_timeout_add_seconds(1, update_time, NULL);

    // ウィンドウ表示
    gtk_widget_show_all(window);
}

int main(int argc, char **argv) {
    GtkApplication *app;
    int status;

    app = gtk_application_new("org.example.digitalclock", G_APPLICATION_FLAGS_NONE);
    g_signal_connect(app, "activate", G_CALLBACK(activate), NULL);
    status = g_application_run(G_APPLICATION(app), argc, argv);
    g_object_unref(app);

    return status;
}
