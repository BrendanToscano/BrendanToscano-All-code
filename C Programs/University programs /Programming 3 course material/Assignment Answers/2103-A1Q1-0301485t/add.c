#include <stdio.h>

int main(int argc, char *argv[]){
	if(argc == 3){
    	int num1, num2;
		sscanf(argv[1], "%d" , &num1);
		sscanf(argv[2], "%d" , &num2);
		printf("%d\n", num1 + num2);
	}
	else
		printf("User Instruction: ./add <num1> <num2>\n");
}

