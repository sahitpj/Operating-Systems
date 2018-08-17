#include<stdlib.h>
#include<stdio.h>
#include<unistd.h>
#include<time.h>
void delay(unsigned int mseconds)
{
    clock_t goal = mseconds + clock();
    while (goal > clock());
}

int main(){
    int i;
    for (i = 0; i < 100; i++){
        delay(1000000);
        int rc = fork();
        if (rc < 0){
            printf("No child process was created \n");
        }
        if (rc == 0){
            printf("Child process was created with pid %d and loop counter is %d \n", getpid(), i+1);
            break;
        }
        if (rc > 0){
            printf("Parent process with pid %d \n", getpid());
            wait(NULL);    
        }
    }
    return 0;
}