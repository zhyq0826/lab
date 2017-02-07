/* Welcome to the Interactive C Tutorial.
 * Start by choosing a chapter and
 * write your code in this window. */

#include <stdio.h>

int main() {
    int foo = 10;
    int numbers[10];
    for(int i = 0;i < 10; i++){
            numbers[i] = 0;
    }
    char values[] = {'a', 'b', 'c'};
    char vowels[][5] = {
        {'A', 'E', 'I', 'O', 'U'},
        {'a', 'e', 'i', 'o', 'u'}
    };
    printf("Hello, World!");
    printf("%d", foo);

    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 5; j++) {
            printf("Address of vowels[%d][%d]: %p\n", i, j, &vowels[i][j]);
        }
        printf("\n");
    }
    return 0;
}
    
