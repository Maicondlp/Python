# Fatiando uma lista

Para criar uma fatia, especifique o índice do primeiro e do último elemento com os quais você quer trabalhar.

Para exibir os três primeiros elementos de uma lista, solicite os índices de 0 a 3; os elementos 0, 1 e 2 serão devolvidos.
~~~
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

Saída: ['charles', 'martina', 'michael']
~~~

Por exemplo, se quiser o segundo, o terceiro e o quarto itens de uma lista, comece a fatia no índice 1 e termine no índice 4: 
~~~
players = ['charles', 'martina', 'michael', 'florence', 'eli'] 
print(players[1:4]) 

Saída: ['martina', 'michael', 'florence']
~~~
Sem um índice de início, Python usa o início da lista. Exemplo: [:5]
Sem um índice de final, Python usa o final da lista. Exemplo: [5:]

Um índice negativo devolve um elemento a uma determinada distância do final de uma lista; 
~~~
players = ['charles', 'martina', 'michael', 'florence', 'eli'] 
print(players[-3:])

Saída: ['michael', 'florence', 'eli'] 
~~~
