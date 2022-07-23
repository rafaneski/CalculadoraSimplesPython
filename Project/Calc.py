import os

def linha():
    print('='*19)

def linhaLonga():
    print('='*50)

def somar():
    num1 = int(input('Escolha o 1º numero: '))
    num2 = int(input('Escolha o 2º numero: '))
    print(f'O resultado da soma entre {num1} e {num2} é igual a: {num1 + num2}')

def subtrair():
    num1 = int(input('Escolha o 1º numero: '))
    num2 = int(input('Escolha o 2º numero: '))
    print(f'O resultado da subtração entre {num1} e {num2} é igual a: {num1 - num2}')

def mult():
    num1 = int(input('Escolha o 1º numero: '))
    num2 = int(input('Escolha o 2º numero: '))
    print(f'O resultado da multiplicação entre {num1} e {num2} é igual a: {num1 * num2}')

def div():
    num1 = int(input('Escolha o 1º numero: '))
    num2 = int(input('Escolha o 2º numero: '))
    if num2 != 0: 
        print(f'O resultado da divisão entre {num1} e {num2} é igual a: {num1 / num2}')
    else:
        linhaLonga()
        print('Não é possível dividir um numero por 0, tente novamente')
        linhaLonga()

linha()
print('Calculadora Simples')
linha()

escolheuSair = False

while escolheuSair == False:
    try:
        print('[1] - Somar\n[2] - Subtrair\n[3] - Multiplicar\n[4] - Dividir\n[5] - Sair')
        opcao = int(input('Escolha: '))
    except ValueError as e:
        linhaLonga()
        print(f'{e} Error\nOpção Inválida, escolha um numero!')
        linhaLonga()
        input('Aperte qualquer tecla para voltar...')
        os.system("cls")
        continue
    linhaLonga()
    if opcao == 1:
        somar()

    elif opcao == 2:
        subtrair()

    elif opcao == 3:
        mult()

    elif opcao == 4:
        div()

    elif opcao == 5:
        escolheuSair == True
        print('Obrigado por utilizar a Calculadora simples!!!')
        linhaLonga()
        break

    else:
        print('Opção inválida!')

    linhaLonga()
    input('Aperte qualquer tecla para voltar...')
    os.system("cls")
