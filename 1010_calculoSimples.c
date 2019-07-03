#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(){
	
	int codPeca, qtdPecas, contador=0;
	float valorPeca, valorPagar=0;
	
	do{
		scanf("%d", &codPeca);
		scanf("%d", &qtdPecas);
		scanf("%f", &valorPeca);
		
		valorPagar  = (qtdPecas*valorPeca)+valorPagar;
		
		contador++;
		
	}while(contador<2);
	
	printf("VALOR A PAGAR: R$ %.2f\n", valorPagar);

	return 0;
}
