#include <stdio.h>

#define MAX_SIZE 1000

int main(void) {
    char string[MAX_SIZE];
    int n;
    int i;
    int j;
    fgets(string, MAX_SIZE, stdin);
    scanf("%d", &n);
    for (i=n-1; i >= 0; --i) {
        // nまでの最後の空白文字を改行に置き換えて出力
        if (string[i] == ' ' || string[i] == '\t') {
            string[i] = '\n';
            printf("%s", string);
            // むりやうごかへん 
            for (j=0; j < n-i; ++j) {
                string[j] = string[i+j+1];
            }
        }
    }
    return 0;
}