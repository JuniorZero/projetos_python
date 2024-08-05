#Recebe o numero que vai ser multiplicado por outros em sequência
numero = input("Digita um numero a ser multiplicado: ")
quantidade = input('Multiplicar até que numero: ')

#Transforma string em inteiro(numero)
valor1 = int(numero)
valor2 = int(quantidade)

#começo da formação da sequência da multiplicação
for calculo in range(valor2):
    calculo += 1
    if valor1:
        resultado = calculo * valor1
        
        #Mensagem do resultado
        print(f'{numero} * {calculo} = {resultado}') 
    else:
        print('Tchau')
else:
    print('Fim')
