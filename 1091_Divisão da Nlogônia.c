#include <stdio.h>
#include <stdlib.h>
		
int main(){
	
	unsigned int k;
	int i, m, n, x, y;
    
    while(1) {
		scanf("%u", &k);
		if (k!=0){
			scanf("%d %d", &m, &n);
			for(i=0; i<k; i++){
				scanf("%d %d", &x, &y);			
				if((x==m) || (y==n)){
					printf("divisa\n");
				}
				else if((x>m) && (y>n)){
					printf("NE\n");
				}
				else if((x<m) && (y<n)){
					printf("SO\n");
				}
				else if((x<m) && (y>n)){
					printf("NO\n");
				}
				else if((x>m) && (y<n)){
					printf("SE\n");
				}
			}
		} else{
			return 0;
		}
	}
	return 0;
}
