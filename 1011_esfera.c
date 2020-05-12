#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(){
	
	double a, b, c, pi = 3.14159, areaTriangulo, areaCirculo, areaTrapezio, areaQuadrado, areaRetangulo;

	scanf("%lf", &a);
	scanf("%lf", &b);
	scanf("%lf", &c);
	
	areaTriangulo = (a * c)/2;
	areaCirculo = pi * (pow(c, 2));
	areaTrapezio = (((a+b)*c)/2);
	areaQuadrado = pow(b,2);
	areaRetangulo = a * b;
	
	printf("TRIANGULO: %.3lf\n", areaTriangulo);
	printf("CIRCULO: %.3lf\n", areaCirculo);
	printf("TRAPEZIO: %.3lf\n", areaTrapezio);
	printf("QUADRADO: %.3lf\n", areaQuadrado);
	printf("RETANGULO: %.3lf\n", areaRetangulo);
	
	return 0;
}
