def soma(x,y):
    return (x+y)

def multiplicacao(x,y):
    return (x*y)

def substracao(x,y):
    return (x-y)

def divisao(x,y):
    return (x/y)

def imprimirNome(nome,vezes):
    for n in range(1,vezes):
        print(nome)

loop = True

while loop:
    print('----------- Menu ------------')
    print('Escolha sua opcao:')
    print('1 - soma')
    print('2 - multiplicacao')
    print('3 - substracao')
    print('4 - divisao')
    print('5 - imprimirNome')
    print('0 - sair')

    opcao = int(input("Opção:"))

    if(opcao == 0):
        loop = False
        continue
    elif(opcao == 5):
        nome = input("Digite seu nome:")
        vezes = int(input("Digite quantas vezes repetir:"))
        imprimirNome(nome, vezes)
        continue    

    x = int(input("Digite valor para x:"))
    y = int(input("Digite valor para y:"))

    value = 0

    if(opcao == 1):
       value = soma(x,y)
    elif(opcao == 2):
       value = multiplicacao(x,y)
    elif(opcao == 3):
       value = substracao(x,y)
    elif(opcao == 4):
       value = divisao(x,y)
    elif(opcao == 4):
       value = divisao(x,y)
    
    print(value)