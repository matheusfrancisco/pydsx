# Data Struct in C ~~(Estrutura de Dados em C)~~



# Conteúdo 
1. [Introduação](#introduction)
2. [Unidade I](#unidade1)
    1. [Lista simplesmente encadeada](#listas)
    	1. [Lista  com cabeça](#ccabeca)
    	2. [Lista sem cabeça](#scabeca)
    2. [Lista duplamente encadeada](#listasd)
    3. [Lista circular](#listac)



## Introdução <a name="introduction"></a>
Este repositório tem a função de compartilhar listas de exercícios  utilizando inicialmente a linguagem de programação C. Qualquer código aqui postando pode ser utilizado e editado por qualquer usúario.



## Unidade I <a name="unidade1"></a>
Nesta unidade será postado exemplos utilizando a estrutra de lista encadeadas.
Segue abaixo as listas contida na unidade

### Lista Simplesmente encadeada <a name="listas"></a>
É o modelo mais simples de listas, por ser simplesmente encadeada ela pode ser percorrida em apenas um sentido da lista. O seu início pode ser ou não por uma celula vazia auxiliar que chamamos de cabeça, ela é usada para aumentar a facilidade na construção do algoritmo.

```c
struct celula {
int x; // Dado que cada célula armazena, nesse caso é um numero inteiro;
struct celula * prox;
};

typedef celula Celula;
```

Nossa lista será composta por vaŕias células, uma ligada na outra, a diferença da lista com ou sem cabeça vai na hora de criar a célula e realizar as operações de adição, remoçaõ e busca.


[exemplo_de_lista_s_encadeada_c_cabeca](https://github.com/matheusfrancisco/Estrutura-de-Dados/blob/master/Unidade_I/Listas_simplesmente_encadeada/linkedList-Head.c)<br>
Link para uma explicação bem mais detalhada de lista simplemente encadeada , [clique aqui](https://matheusfrancisco.github.io/como-criar-lista-encadeadas-em-c/)


### Lista Duplamente encadeada  <a name="listad"></a>

As listas duplamente encadeadas são estruturas de dados semelhantes às listas simplesmente encadeadas. A alocação da memória é feita durante a execução. No entanto, em comparação com as listas simplesmente encadeadas a conexão entre os elementos é feita através de dois ponteiros (um que aponta para o elemento anterior, e o outro, para o seguinte). 
O ponteiro anterior ao primeiro elemento deve apontar para NULL (o início da lista). 
O ponteiro seguinte ao último elemento deve apontar para NULL (o fim da lista). 

Para acessar um elemento, a lista pode ser percorrida pelos dois lados: 

```c
struct celula {
int x; // Dado que cada célula armazena, nesse caso é um numero inteiro;
struct celula * prox;
struct celula * ant; //ponteiro que aponta para a lista anterior;
};

typedef celula Celula;
```
Como na lista simplesmente encadeada podemos utilizar uma celula no inicio vazia que chamamos de cabeça, e também podemos utilizar uma celula no final no qual podemos chamar de calda.

### Lista Circular  <a name="listac"></a>





