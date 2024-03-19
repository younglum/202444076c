#include <stdio.h>
#include <stdlib.h>

int main(void){

    int cnt;

    printf("알파벳  소문자가 출력됩니다.\n");

    for (cnt= 97; cnt <=122; cnt++)
    {
        printf("%c", cnt);
    }

    return 0;
    
}
