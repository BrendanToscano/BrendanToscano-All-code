#include <stdio.h>

int main(int argc, char *argv[]){
	if(argc == 3){
		int num, n = 0;
		sscanf(argv[1], "%d", &num);
		while(n < num){
			printf("%s\n", argv[2]);
			n++;
		}
	}
	else
		printf("User Instruction: ./loop <num> <word>");
}
