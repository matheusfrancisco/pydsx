/*Uma lista simplesmente encadeada com cabeça utilizada no blog matheusfrancisco.github.io
criada por matheus francisco, este código pode ser copiado por qualquer usuario.
*/
#include <stdio.h>
#include <stdlib.h>

struct test{
	int valor;
	struct test *seg;
};
typedef struct test celula; /*nomeando como célula*/


void insereInicio(int x, celula *p)
{
   	celula *nova;
   	nova = malloc(sizeof (celula));
   	nova->valor = x;
	nova->seg = p->seg;
   	p->seg = nova;
}


void imprime(celula *lst)
{
    celula*aux;
    aux = lst->seg;
    
    while(aux != NULL){
        printf("%i", aux->valor);
        aux = aux->seg;
    }
}

int main()
{
	celula c;
	celula*lst;
 	c.seg = NULL;
 	lst = &c; 

	insereInicio(2, lst);
	insereInicio(3, lst);
	insereInicio(4, lst);
	insereInicio(5, lst);

	imprime(lst);	

}

