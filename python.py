# Listas podem guardar várias informações e são formadas com "[]"
Lista = [item1, item2, item3, item4]

# Listas são mutáveis!
# Aseguir exemplos de alterações que podemos fazer em uma lista:


#pop() - Remove um item da lista de acordo com sua posição no índice inscrita no "()"
Nuemeros = [1, 2, 3, 2, 4]
Numeros.pop(2) 
print(Numeros) 
#Resultado: [1, 2, 2, 4]

#remove() - Remove o item da lista que estiver especificado dentro do "()"
amigos = ['Evandro', 'Miguel', 'Eduardo', 'Daniel']
amigos.remove('Daniel')
print(amigos)
#Resultado: ['Evandro', 'Miguel', 'Eduardo']

#append() - Adiciona o item que estiver dentro do "()" na ultima posição da lista
numeros = [1, 2, 3, 4, 5]
numeros.append(2)
print(numeros)
#Resultado: [1, 2, 3, 4, 5, 2]

#extend() - adicionar os itens de uma lista dentro da lista na ultima posição
numeros = [1, 2, 3, 4, 5]
novos = [6, 7, 8]
numeros.extend(novos)
print(numeros)
#Resultado: [1, 2, 3, 4, 5, 6, 7, 8]

#insert() - Adiciona o item especificado dentro do "()" na posição do index, também especificadio dentro do "()"
amigoS = ['Evandro', 'Miguel', 'Eduardo', 'Daniel']
amigoS.insert(2, 'Guilherme')
print(amigoS)
#Resultado: ['Evandro', 'Miguel', 'Guilherme', 'Eduardo', 'Daniel']

#sort() - Organiza a lista em ordem crescente
Aleatorio = [3, 2, 5, 6, 8, 7]
Aleatorio.sort()
print(Aleatorio)
#Resultado: [2, 3, 5, 6, 7, 8]

#reverse() - Organiza a lista em ordem decrescente
Aleatorio = [3, 2, 5, 6, 8, 7]
Aleatorio.reverse()
print(Aleatorio)
#Resultado: [7, 8, 6, 5, 2, 3]


# É possível buscar por informações dentro das listas como a seguir

#index() - Busca pela posição no index do item especificado dentro do "()"
frutas = ['maçã', 'banana', 'pera', 'maracujá', 'uva']
indice_pera = frutas.index('pera')
print(f"O índice do item procurado é {indice_pera}")
#Resultado: O índice do item procurado é 2

#count() - Busca pela quantidade do item especificado dentro do "()" na lista
cores = ['rosa', 'preto', 'rosa', 'rosa', 'amarelo', 'laranja', 'vermelho']
quantidade_rosa = cores.count('rosa')
print(f"A quantidade de cores rosa na lista é {quantidade_rosa}")
#Resultado: A quantidade de cores rosa na lista é 3

#len() - Mostra o tamanho da lista
nomes = ['Felipe', 'Júlia', 'Eduardo', 'Carlos']
Tamanho_nomes = len(nomes)
print(f'A lista possui {Tamanho_nomes} pessoas')
#Resultado: A lista possui 4 pessoas