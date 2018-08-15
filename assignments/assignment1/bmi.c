#include<stdlib.h>
#include<stdio.h>
#include<unistd.h>


int main(int argc, char *argv[]){
    float height = atof(argv[1]);
    float weight = atof(argv[2]);
    weight = weight*0.453592;
    height = height*height;
    printf("Your BMI is %.2f", weight/height);
    return 0;
}