#include<stdlib.h>
#include<stdio.h>
#include<unistd.h>


int main(int argc, char *argv[]){
    int rc = fork();
    if (rc == 0){
        float height = atof(argv[1]);
        float weight = atof(argv[2]);
        weight = weight*0.453592;
        height = height*height;
        printf("Your BMI is %.2f", weight/height);
    }
    else if(rc < 0){
        printf("No child process created");
    }
    else{
        wait(NULL);
        printf("This is parent process");
    }
    return 0;
}