#include <stdio.h>
#include <stdlib.h>
#include <pwd.h>
#include <sys/types.h>
#include <unistd.h>
#include <time.h>
#include <sys/stat.h>
#include <limits.h>

void print_file_content(char *file_path) {
    FILE *file = fopen(file_path, "r");
    if (file == NULL) {
        return;
    }

    char line[256];
    while (fgets(line, sizeof(line), file)) {
        printf("%s", line);
    }

    fclose(file);
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("Usage: %s <username>\n", argv[0]);
        return 1;
    }

    for (int i = 1; i < argc; i++) {
        char *username = argv[i];
        struct passwd *user_entry = getpwnam(username);

        if (user_entry == NULL) {
            printf("User '%s' not found.\n", username);
            continue;
        }

        printf("Username: %s\n", user_entry->pw_name);
        printf("Home directory: %s\n", user_entry->pw_dir);
        printf("Shell: %s\n", user_entry->pw_shell);
        printf("User ID: %d\n", user_entry->pw_uid);
        printf("Group ID: %d\n", user_entry->pw_gid);

        char bash_history_path[PATH_MAX];
        snprintf(bash_history_path, PATH_MAX, "%s/.bash_history", user_entry->pw_dir);
        struct stat file_stat;

        if (stat(bash_history_path, &file_stat) == 0) {
            char last_login_time[20];
            strftime(last_login_time, sizeof(last_login_time), "%Y-%m-%d %H:%M:%S", localtime(&file_stat.st_mtime));
            printf("Last login: %s\n", last_login_time);
        } else {
            printf("Last login: Never logged in\n");
        }

        char plan_path[PATH_MAX];
        snprintf(plan_path, PATH_MAX, "%s/.plan", user_entry->pw_dir);
        printf("Plan:\n");
        print_file_content(plan_path);

        printf("\n");
    }

    return 0;
}
