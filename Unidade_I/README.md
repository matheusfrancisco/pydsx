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
É o modelo mais simples de listas, por ser simplesmente encadeada ela pode ser percorrida em apenas um sentido da lista. O seu início pode ser ou naõ por uma celula vazia auxiliar que chamamos de cabeça, ela é usada para aumentar a facilidade na construçaõ do algoritmo.

```c
struct celula {
int x; // Dado que cada célula armazena, nesse caso é um numero inteiro;
struct celula * prox;
};

typedef celula Celula;
```

Nossa lista sera' composta por vaŕias células, uma ligada na outra, a diferença da lista com ou sem cabeça vai na hora de criar a célula e realizar as operações de adiçaõ, remoçaõ e busca.


### Lista Duplamente encadeada  <a name="listad"></a>


### Lista Circular  <a name="listac"></a>




