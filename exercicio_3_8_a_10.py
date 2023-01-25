"""3.8 – Conhecendo o mundo: Pense em pelo menos cinco lugares do mundo que você gostaria de visitar. 
• Armazene as localidades em uma lista. Certifique-se de que a lista não esteja em ordem alfabética.
"""
lugares = ["Nova York","Dublin","Paris","Yushuaia","Londres"]

"""
• Exiba sua lista na ordem original. Não se preocupe em exibir a lista de forma elegante; basta exibi-la como uma lista
 Python pura. 
"""
print(lugares)
"""
• Utilize sorted() para exibir sua lista em ordem alfabética, sem modificar a lista propriamente dita.
"""
print(sorted(lugares))
"""
• Mostre que sua lista manteve sua ordem original exibindo-a. 
"""
print(lugares)
"""
• Utilize sorted() para exibir sua lista em ordem alfabética inversa sem alterar a ordem da lista original. 
"""
print(sorted(lugares,reverse=True))
"""
• Mostre que sua lista manteve sua ordem original exibindo-a novamente. 
"""
print(lugares)
"""
• Utilize reverse() para mudar a ordem de sua lista. Exiba a lista para mostrar que sua ordem mudou. 
"""
lugares.reverse()
print(lugares)
"""
• Utilize reverse() para mudar a ordem de sua lista novamente. Exiba a lista para mostrar que ela voltou à sua ordem original. 
"""
lugares.reverse()
print(lugares)
"""
• Utilize sort() para mudar sua lista de modo que ela seja armazenada em ordem alfabética. 
 Exiba a lista para mostrar que sua ordem mudou. 
"""
lugares.sort()
print(lugares)
"""
• Utilize sort() para mudar sua lista de modo que ela seja armazenada em ordem alfabética inversa. 
 Exiba a lista para mostrar que sua ordem mudou.
"""
lugares.sort(reverse=True)
print(lugares)

"""
3.9 – Convidados para o jantar: Trabalhando com um dos programas dos Exercícios de 3.4 a 3.7 (páginas 80 e 81), use len()
 para exibir uma mensagem informando o número de pessoas que você está convidando para o jantar. 
"""
convidadas = ["Kate Beckinsale","Kristen Bell","Sofia Bush"]

for convidada in convidadas:
	print("Olá " +  convidada + ", gostaria de jantar comigo hj?")

print(len(convidadas))
"""
3.10 – Todas as funções: Pensa em algo que você poderia armazenar em uma lista. Por exemplo, você poderia criar uma lista de
 montanhas, rios, países, cidades, idiomas ou qualquer outro item que quiser. Escreva um programa que crie uma lista contendo
 esses itens e então utilize cada função apresentada neste capítulo pelo menos uma vez.
"""
times_cariocas = ["flamengo","botafogo","fluminense","vasco"]
print(sorted(times_cariocas))
print(sorted(times_cariocas,reverse=True))
print(times_cariocas)
times_cariocas.sort()
print(times_cariocas)


