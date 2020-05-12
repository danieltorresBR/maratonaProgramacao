#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(){
	
	int a, b, x;
	
	double area, n=3.14159, raio;
	
	scanf("%lf", &raio);

	area = n * pow(raio, 2);
	
	printf("A=%.4lf\n", area);
	
	return 0;

}

