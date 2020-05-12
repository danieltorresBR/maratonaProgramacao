#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(){
	
	unsigned int entradaHum, entradaDois;
	
	while(scanf("%u %u", &entradaHum, &entradaDois)  != EOF ){
		printf("%u\n", entradaHum ^ entradaDois);
	}

	return 0;
}

