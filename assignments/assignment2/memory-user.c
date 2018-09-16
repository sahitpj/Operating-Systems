#include <stdlib.h>
#include <stdio.h>
#include <time.h>

int main(int argc, char * argv[]){
    clock_t start, end;
    int mem = atoi(argv[1]);
    int t = atoi(argv[2]);
    int flag = atoi(argv[3]);
    int mem_bit = mem * 1024 * 1024;
    int *arr = (int*)malloc(mem_bit);
    int i, count;
    start = clock();
    for( i = 0; i < mem_bit; i = i+sizeof(int)){
        printf("%d ", ++count);
        end = clock();
        if(((int)(end-start)) == t && flag == 1){
            break;
        } 
    }
    return 0;
} 