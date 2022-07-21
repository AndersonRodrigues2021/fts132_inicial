import pytest

def somar_dois_numeros(num1, num2):
    return num1 + num2

def subtrair_dois_numeros(num1, num2):
    return num1 - num2

def multiplicar_dois_numeros(num1, num2):
    return num1 * num2

def dividir_dois_numeros(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return 'Não é possivel dividir por zero'

def elevar_um_numero_pelo_outro (num1, num2):
    return num1 ^ num2

def area_quadrado (num1):
    return num1 * num1

def area_retangulo (num1, num2):
    return num1 * num2

def area_triangulo (num1, num2):
    return num1 * num2 / 2

def calcular_area_do_circulo(raio):
    try:
        return 3.14 * raio ** 2
    except TypeError:
        return 'Falha no calculo - Raio não é um número'

def calcular_volume_do_paralelograma (largura, comprimento, altura):
    return largura * comprimento * altura


if __name__ == '__main__':
    #print_hi('Anderson')
    resultado = somar_dois_numeros(5,7)
    print(f'A soma é {resultado}')

    resultado = subtrair_dois_numeros(9,6)
    print(f'A subtração é {resultado}')

    resultado = multiplicar_dois_numeros(5,7)
    print(f'A multiplicação é {resultado}')

    resultado = dividir_dois_numeros(12,0)
    print(f'A divisão é {resultado}')

    resultado = elevar_um_numero_pelo_outro(2,3)
    print(f'A exponenciação é {resultado}')

    resultado = area_quadrado(8)
    print(f'A area do quadrado é {resultado}cm²')

    resultado = area_retangulo(8,3)
    print(f'A area do retangulo é {resultado}cm²')

    resultado = area_triangulo(8,6)
    print(f'A area do triangulo é {resultado}cm²')



'''
def testar_somar_dois_numeros():
    # 1 Etapa: Configuração/Prepara
    # Dados / Valores
    # Entrada / Input
    num1 = 8
    num2 = 9
    # Saida / Output
    resultado_esperado = 17

    # 2 Etapa: Executa
    resultado_atual = somar_dois_numeros(num1, num2)

    # 3 Etapa: Confirma / Check/ Valida
    assert resultado_atual == resultado_esperado
'''








