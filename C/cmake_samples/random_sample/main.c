#include <stdlib.h>
#include <stdio.h>
#include "random.h"

#define NUM_RAND 10


int main(){
	int i;
	double rands[NUM_RAND];
	for(i=0; i<NUM_RAND; i++){
		rands[i] = 1.0 + 0.5*random_normal();
		printf("%f\n", rands[i]);
	}
	return 0;
}
