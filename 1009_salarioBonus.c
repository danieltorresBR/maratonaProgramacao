#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(){
	
	char nome[1000];
	int numFuncionario;
	double valorHora, salario, horasTrabalhadas;
	
	scanf("%d", &numFuncionario);
	scanf("%lf", &horasTrabalhadas);
	scanf("%lf", &valorHora);
	
	salario  = horasTrabalhadas*valorHora;
	
	printf("NUMBER = %d\n", numFuncionario);
	printf("SALARY = U$ %.2lf\n", salario);

	return 0;
}
