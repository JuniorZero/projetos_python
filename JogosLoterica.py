from random import randint as rr
from time import sleep
from tkinter import *

#Armazenar o resultado final
MegaSena1 = list()
MegaSena2 = list()
LotoFacil1 = list()
LotoFacil2 = list()
Quina1 = list()
Quina2 = list()
LotoMania1 = list()
LotoMania2 = list()
DuplaSena1 = list()
DuplaSena2 = list()
#Design e separador entre os resultados
print('*' * 40)
print('{:^40}'.format('Testa sua sorte'))
print('*' * 40)
#Unico local de inserir dados pelo usuario 
quantidade = int(input('Quantos jogos você deseja obter? '))

#MegaSena
Senatotal = 1
while Senatotal <= quantidade:
    Senacontagem = 0
    while True:
        # loop de 1 ate 60
        Meganumero = rr(1,60)
        # verificar se nao ha repetição entre os numeros na lista
        if Meganumero not in MegaSena1: 
            # adicionando numero
            MegaSena1.append(Meganumero)
            # adiciona o numero e acrescenta o proximo numero e nao entrar no loop 
            Senacontagem += 1
        if Senacontagem >= 6:
            break
    # organizar em ordem numerica(menor para o maior)
    MegaSena1.sort() 
    # armazenar o resultado da lista1(uma copia)
    MegaSena2.append(MegaSena1[:])
    # apagar lista 
    MegaSena1.clear() 
    Senatotal += 1
print('{:^12}'.format('~=' * 25,'~=' * 25))
#mostrar a lista, um abaixo do outro em um loop, i = listagem
for i, l in enumerate(MegaSena2): 
    print(f'MegaSena Jogo {i + 1}: {l}')
    sleep(1)
print('{:^12}'.format('~=' * 25,'~=' * 25))

#LotoFacil
Faciltotal = 1
while Faciltotal <= quantidade:
    Facilcontagem = 0
    while True:
        Lotonumero = rr(1,25)  
        if Lotonumero not in LotoFacil1: 
            LotoFacil1.append(Lotonumero)
            Facilcontagem += 1 
        if Facilcontagem >= 15:
            break
    LotoFacil1.sort() 
    LotoFacil2.append(LotoFacil1[:]) 
    LotoFacil1.clear() 
    Faciltotal += 1
print('{:^12}'.format('~=' * 25,'~=' * 25))
for i, l in enumerate(LotoFacil2): 
    print('{:^12}'.format(f'LotoFácil Jogo {i + 1}: {l}\n'))
    sleep(1)
print('{:^12}'.format('~=' * 25,'~=' * 25))

#Quina
Quinatotal = 1
while Quinatotal <= quantidade:
    Quinacontagem = 0
    while True:
        Quinanumero = rr(1,80)  
        if Quinanumero not in Quina1: 
            Quina1.append(Quinanumero)
            Quinacontagem += 1 
        if Quinacontagem >= 5:
            break
    Quina1.sort() 
    Quina2.append(Quina1[:]) 
    Quina1.clear() 
    Quinatotal += 1
print('{:^12}'.format('~=' * 25,'~=' * 25))
for i, l in enumerate(Quina2): 
    print('{:^12}'.format(f'Quina Jogo {i + 1}: {l}'))
    sleep(1)
print('{:^12}'.format('~=' * 25,'~=' * 25))

#LotoMania
LotoManiatotal = 1
while LotoManiatotal <= quantidade:
    LotoManiacontagem = 0
    while True:
        LotoManianumero = rr(0,99)  
        if LotoManianumero not in LotoMania1: 
            LotoMania1.append(LotoManianumero)
            LotoManiacontagem += 1 
        if LotoManiacontagem >= 50:
            break
    LotoMania1.sort() 
    LotoMania2.append(LotoMania1[:]) 
    LotoMania1.clear() 
    LotoManiatotal += 1
print('{:^12}'.format('~=' * 25,'~=' * 25))
for i, l in enumerate(LotoMania2): 
    print('{:^12}'.format(f'LotoMania Jogo {i + 1}: {l}\n'))
    sleep(1)
print('{:^12}'.format('~=' * 25,'~=' * 25))

#DuplaSena
DuplaSenatotal = 1
while DuplaSenatotal <= quantidade:
    DuplaSenacontagem = 0
    while True:
        DuplaSenanumero = rr(1,50)  
        if DuplaSenanumero not in DuplaSena1: 
            DuplaSena1.append(DuplaSenanumero)
            DuplaSenacontagem += 1 
        if DuplaSenacontagem >= 6:
            break
    DuplaSena1.sort() 
    DuplaSena2.append(DuplaSena1[:]) 
    DuplaSena1.clear() 
    DuplaSenatotal += 1
print('{:^12}'.format('~=' * 25,'~=' * 25))
for i, l in enumerate(DuplaSena2): 
    print('{:^12}'.format(f'DuplaSena Jogo {i + 1}: {l}'))
    sleep(1)
print('{:^12}'.format('~=' * 25,'~=' * 25))
