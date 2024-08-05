
import string
from secrets import SystemRandom


while True:
    #Mensagem de erro no casso do usuario colocar uma String
    def entrada_um_invalida():
        if quantidade != int:
            print('{:^100}'.format('Não é numero. Entrada Invalida!'))
        return entrada_um_invalida
    
    def entrada_dois_invalida():
        if opcao != str:
            print('{:^100}'.format('Entrada Invalida!'))
        return entrada_dois_invalida
    
    #Gerar a combinação dos numeros,letras e caracteristicos
    def gerador(): 
        senha = ''.join(SystemRandom().choices(string.ascii_letters + string.digits + string.punctuation, k= numero))
        return senha 

    quantidade = input('Quantos digitos a senha deve ter ? ')

    # verificar se foi digitado numero
    if quantidade.isdigit(): 
        numero = int(quantidade)
        print('{:^100}'.format(f'Senha Gerada: {gerador()}'))
    else:
        entrada_um_invalida()
        
    #Opção em continuar ou parar
    opcao = input('Deseja continuar sim ou não ? ')
    if opcao == 'sim':
        continue
    elif opcao == 'não' or 'nao':
        break
    else:
        entrada_dois_invalida()
        break
