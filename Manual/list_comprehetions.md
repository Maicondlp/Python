# List comprehensions 

A abordagem descrita antes para gerar a lista squares usou três ou quatro linhas de código. 
Uma list comprehension (abrangência de lista) permite gerar essa mesma lista com apenas uma linha de código. 
Uma list comprehension combina o laço for e a criação de novos elementos em uma linha, e concatena cada novo elemento automaticamente. 
O exemplo a seguir cria a lista de quadrados perfeitos: 
~~~
squares = [value**2 for value in range(1,11)] 
print(squares) 
~~~
Para usar essa sintaxe, comece com um nome descritivo para a lista, por exemplo, squares. Em seguida, insira um colchete de abertura e defina a expressão para os valores que você quer armazenar na nova lista. 
Nesse exemplo, a expressão é value\*\*2, que eleva o valor ao quadrado. 
Então escreva um laço for para gerar os números que você quer fornecer à expressão e insira um colchete de fechamento. 
