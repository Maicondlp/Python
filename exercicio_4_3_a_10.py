""" 
4.3 – Contando até vinte: Use um laço for para exibir os números de 1 a 20, incluindo-os.

numeros = range(1,21)
for numero in numeros:
        print(numero)


4.4 – Um milhão: Crie uma lista de números de um a um milhão e, então, use um laço for para exibir os números. 
(Se a saída estiver demorando demais, interrompa pressionando CTRL-C ou feche a janela de saída.)

numeros = range(1,1000001)
for numero in numeros:
        print(numero)

4.5 – Somando um milhão: Crie uma lista de números de um a um milhão e, em seguida, use min() e max() para garantir que sua 
lista realmente começa em um e termina em um milhão. Além disso, utilize a função sum() para ver a rapidez com que Python é 
capaz de somar um milhão de números.
"""
numeros = range(1,10000001)
print(min(numeros))
print(max(numeros))
print(sum(numeros))

"""
4.6 – Números ímpares: Use o terceiro argumento da função range() para criar uma lista de números ímpares de 1 a 20. 
Utilize um laço for para exibir todos os números.
"""
numeros_impares = list(range(1,21,2))
print(numeros_impares)

"""
4.7– Três: Crie uma lista de múltiplos de 3, de 3 a 30. Use um laço for para exibir os números de sua lista.
"""
multiplos_de_3 = list(range(1,11))
for multiplo in multiplos_de_3:
    multiplo = 3 * multiplo
    print(multiplo)
"""
4.8 – Cubos: Um número elevado à terceira potência é chamado de cubo. Por exemplo, o cubo de 2 é escrito como 2**3 em Python.
 Crie uma lista dos dez primeiros cubos (isto é, o cubo de cada inteiro de 1 a 10), e utilize um laço for para exibir o valor
    de cada cubo.
"""
cubos = list(range (1,11))
for cubo in cubos:
    print(cubo**3)

"""
4.9 – Comprehension de cubos: Use uma list comprehension para gerar uma lista dos dez primeiros cubos.
"""
cubos = [cubo**3 for cubo in range(1,11)]
print(cubos)