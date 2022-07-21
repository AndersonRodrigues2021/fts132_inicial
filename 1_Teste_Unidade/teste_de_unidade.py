import pytest

def calcular_racao_cao (tamanho, peso):
    print(f'peso {peso}')
    if tamanho == 'P':
        num1 = int(10)
        return int(peso) * int(10)
    elif tamanho == 'M':
        return int(peso) * int(20)
    elif tamanho ==  'G':
        return int(peso) * int(30)
    else:
        print ('A medida inserida é invalida' )
        print ('Por gentileza, digitar uma medida valida.')

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        peso =str(input(msg))
        if peso.isnumeric():
                valor = int(peso)
                ok = True
        else:
            print ('\033[0;31m Você digitou peso errado.\033[m')
        if ok:
            break
    return valor



if __name__ == '__main__':
    print ('Calculando a quantidade de ração para o cachorro')

    peso = leiaInt('Digite o peso do cachorro: ')
    tamanho = input("Digite o tamanho do cachorro (P, M, G): ")
       # peso = input("Digite o peso do cachorro: ")



    resultado = calcular_racao_cao(tamanho,peso)
    print(f'A quantidade de ração é {resultado}')