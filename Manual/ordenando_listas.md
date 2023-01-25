### Ordenando uma lista de forma permanente com o método sort()
O método **sort()** altera a ordem da lista de forma permanente.
O exemplo a seguir ordena a lista de carros em ordem alfabética inversa: 
~~~
cars = ['bmw', 'audi', 'toyota', 'subaru'] 
cars.sort(reverse=True)
['toyota', 'subaru', 'bmw', 'audi']
~~~

### Ordenando uma lista temporariamente com a função sorted()
Para preservar a ordem original de uma lista, mas apresentá-la de forma ordenada, podemos usar a função **sorted()**. 
~~~
print(sorted(cars))
~~~

### Exibindo uma lista em ordem inversa
Para inverter a ordem original de uma lista, podemos usar o método **reverse()**.
~~~
cars.reverse() print(cars)
['bmw', 'audi', 'toyota', 'subaru']
['subaru', 'toyota', 'audi', 'bmw']
~~~

### Descobrindo o tamanho de uma lista
Podemos rapidamente descobrir o tamanho de uma lista usando a função **len()**.
~~~
cars = ['bmw', 'audi', 'toyota', 'subaru']
len(cars)
~~~
