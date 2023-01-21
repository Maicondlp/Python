<div align="center">

![Estudando python](https://miro.medium.com/max/1400/1*ycIMlwgwicqlO6PcFRA-Iw.png | width=50)

</div>

# Estudando Python
## Lista ou array
### Alterar, acrescentar e remover elementos

Para alterar um elemento, use o nome da lista seguido do índice do elemento que você quer modificar e, então, forneça o novo valor que você quer que esse item tenha.
~~~ 
motorcycles = ['honda', 'yamaha', 'suzuki'] 
~~~
~~~
motorcycles[0] = 'ducati'
~~~

### Concatenar elementos no final de uma lista
O método **append()** acrescenta um elemento no final da lista sem afetar qualquer outro elemento.
~~~
motorcycles.append('suzuki')
~~~

### Inserir elementos em uma lista
Você pode adicionar um novo elemento em qualquer posição de sua lista usando o método **insert()**.
~~~
motorcycles.insert(0, 'ducati')
~~~

### Remover um item usando a instrução del
Se a posição do item que você quer remover de uma lista for conhecida, a instrução **del** poderá ser usada.
~~~
del motorcycles[0]
~~~

### Remover um item usando o método pop
O método **pop()** remove o último item de uma lista, mas permite que você trabalhe com esse item depois da remoção.
~~~
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
~~~
Na verdade, você pode usar pop() para remover um item de qualquer posição em uma lista se incluir o índice do item que você deseja remover entre parênteses.

### Remover um item de acordo com o valor
Se conhecer apenas o valor do item que deseja remover, o método **remove()** poderá ser usado.
~~~
motorcycles.remove('ducati') 
print(motorcycles)
~~~
