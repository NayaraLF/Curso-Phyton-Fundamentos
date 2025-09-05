#Nessa aula, vamos aprender operações com String no Python. As principais operações que vamos aprender são o Fatiamento de String, Análise com len(), count(), find(), transformações com replace(), upper(), lower(), capitalize(), title(), strip(), junção com join().
#

frase = 'Curso em video Phyton'

###Fatiamento###
print(frase[9])

print(frase[9:14]) #o ultimo valor nao entra na contagem

frase[9:21:2] #vai pulando de 2 em 2

frase[:5] # inicia no 0

frase[15:] #do 15 até o final

frase[9::3] #vai comecar no 9 e vai ate o final, pulando de 3 em 3

###Análise###

len(frase)  #quantos caracteres que tem

frase.count('o')  #contar quantas vezes aparece a letra o

frase.count('o', 0, 13)  #quantas vezes aparece a letra o do caracter 0 até o 13

frase.find('deo') # quantas vezes encontrou deo

frase.find('Android')   #o que não existe ele retorna o valor -1

###Transformacao###

frase.replace('Phyton', 'Android') #substituir

frase.upper() #troca tudo para maiusculo

frase.lower() #troca tudo para minusculo

frase.capitalize() #muda a primeira letra da frase pra maiusculo

frase.title() #muda todas as palavras separadas em maiusculo

frase.strip() #remove os espaços no inicio e no final

frase.rstrip() #remove somente os ultimos espaços (direita)

frase.lstrip() #remove somente os espaços iniciais (esquerda)

###Divisao###

frase.split() #divisao considerando os espacos, transforma em uma lista

###Juncao###

'-'.join(frase)


###outros###
#para imprimir textos grandes
print(""" Para receber bônus e materiais exclusivos (que não serão compartilhados em nenhum outro canal), participe do nosso Grupo Silencioso de WhatsApp! """)









