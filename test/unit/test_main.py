import csv
import pytest
from main import somar_dois_numeros, calcular_area_do_circulo, calcular_volume_do_paralelograma

def testar_somar_dois_numeros():
    # 1 Etapa: Configuração/Prepara
    # Dados / Valores
    # Entrada / Input
    num1 = 8
    num2 = 9
    # Saida / Output
    resultado_esperado = 8
    # 2 Etapa: Executa
    resultado_atual = somar_dois_numeros(num1, num2)
    # 3 Etapa: Confirma / Check/ Valida
    assert resultado_atual == resultado_esperado

def testar_calcular_area_do_circulo():
    # 1 - Configura
    raio = 1
    resultado_esperado = 3.14
    # 2 - Executa
    resultado_atual = calcular_area_do_circulo(raio)
    # 3 - Valida
    assert resultado_atual == resultado_esperado

def ler_dados_csv():
    dados_csv = []                                                                                   # criaçao de uma lista vazia
    nome_arquivo = 'C:/Users/Anderson/PycharmProjects/fts132_inicial/test/db/massa_caixa.csv'        # local e nome do arquivo de massa
    try:
        with open(nome_arquivo, newline='') as csvfile:                                              # repetir a leitura ate o fim do arquivo
            campos = csv.reader(csvfile, delimiter=',')
            next(campos)
            for linha in campos:
                dados_csv.append(linha)
        return dados_csv
    except FileNotFoundError:
        print(f'Arquivo não encontrado: {nome_arquivo}')
    except Exception as fail:
        print(f'Falha imprevista: {fail}')
@pytest.mark.parametrize('id,largura,comprimento,altura,resultado_esperado', ler_dados_csv())

def testar_calcular_volume_do_paralelograma(id, largura,comprimento, altura,resultado_esperado):
    #1 - Configura
    largura = 5
    comprimento = 10
    altura = 2
    resultado_esperado = 100
    #2 - Executa
    resultado_atual = calcular_volume_do_paralelograma(int(largura), int(comprimento), int(altura))
    #3 - Valida
    assert resultado_atual == int(resultado_esperado)
