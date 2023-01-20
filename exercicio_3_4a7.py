"""
3.4 – Lista de convidados: Se pudesse convidar alguém, vivo ou morto, para
o jantar, quem você convidaria? Crie uma lista que inclua pelo menos três
pessoas que você gostaria de convidar para jantar. Em seguida, utilize sua
lista para exibir uma mensagem para cada pessoa, convidando-a para jantar.
"""
convidadas = ["Kate Beckinsale","Kristen Bell","Sofia Bush"]
for convidada in convidadas:
	print("Olá " +  convidada + ", gostaria de jantar comigo hj?")


"""
3.5 – Alterando a lista de convidados: Você acabou de saber que um de seus
convidados não poderá comparecer ao jantar, portanto será necessário enviar
um novo conjunto de convites. Você deverá pensar em outra pessoa para
convidar. 
• Comece com seu programa do Exercício 3.4. Acrescente uma instrução print
no final de seu programa, especificando o nome do convidado que não poderá
comparecer. 
• Modifique sua lista, substituindo o nome do convidado que não poderá 
comparecer pelo nome da nova pessoa que você está convidando. 
• Exiba um segundo conjunto de mensagens com o convite, uma para cada pessoa
que continua presente em sua lista.
"""
print("Sofia Bush não poderá comparecer")

convidadas.pop()

convidadas.append("Kaley Cuoco")

for convidada in convidadas:
        print("Olá " +  convidada + ", gostaria de jantar comigo hj?")

"""
3.6 – Mais convidados: Você acabou de encontrar uma mesa de jantar maior,
portanto agora tem mais espaço disponível. Pense em mais três convidados
para o jantar. 
• Comece com seu programa do Exercício 3.4 ou do Exercício 3.5. Acrescente
 uma instrução print no final de seu programa informando às pessoas que você
 encontrou uma mesa de jantar maior. 
• Utilize insert() para adicionar um novo convidado no início de sua lista. 
• Utilize insert() para adicionar um novo convidado no meio de sua lista. 
• Utilize append() para adicionar um novo convidado no final de sua lista. 
• Exiba um novo conjunto de mensagens de convite, uma para cada pessoa que
 está em sua lista.
"""
for convidada in convidadas:
	print ("Ola " + convidada + ", encontrei uma mesa maior e agora conseguirei levar mais 3 pessoas")

convidadas.insert(0,"Cleo Pires")
convidadas.insert(2,"Thayla Ayla")
convidadas.append("Anita")

for convidada in convidadas:
        print("Olá " +  convidada + ", gostaria de jantar comigo hj?")

print("Só vou poder levar duas convidas")
"""
3.7 – Reduzindo a lista de convidados: Você acabou de descobrir que sua nova
 mesa de jantar não chegará a tempo para o jantar e tem espaço para somente
 dois convidados. 
• Comece com seu programa do Exercício 3.6. Acrescente uma nova linha que
 mostre uma mensagem informando que você pode convidar apenas duas pessoas
 para o jantar.
• Utilize pop() para remover os convidados de sua lista, um de cada vez,
 até que apenas dois nomes permaneçam em sua lista. Sempre que remover um
 nome de sua lista, mostre uma mensagem a essa pessoa, permitindo que ela
 saiba que você sente muito por não poder convidá-la para o jantar. 
• Apresente uma mensagem para cada uma das duas pessoas que continuam na
 lista, permitindo que elas saibam que ainda estão convidadas. 
• Utilize del para remover os dois últimos nomes de sua lista, de modo que
 você tenha uma lista vazia. Mostre sua lista para garantir que 
você realmente tem uma lista vazia no final de seu programa.
"""
tamanho_da_lista = len(convidadas)

while tamanho_da_lista > 2:
	desconvidada = convidadas.pop()
	print("Desculpe " + desconvidada + ", o jantar foi cancelado")
	tamanho_da_lista = tamanho_da_lista - 1

print (convidadas)

while tamanho_da_lista > 0:
	del convidadas[-1]
	tamanho_da_lista = tamanho_da_lista - 1

print (convidadas)
