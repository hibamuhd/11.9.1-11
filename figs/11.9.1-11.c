#include <stdio.h>

int main() {
    FILE *file;
    file = fopen("sequence_values.txt", "w");

    if (file == NULL) {
        printf("Error opening the file.\n");
        return 1;
    }

    int xn = 3;

    for (int n = 1; n <= 8; ++n) {
        fprintf(file, "%d\n", xn);
        xn = 3 * xn + 2;
    }

    fclose(file);

    return 0;
}

