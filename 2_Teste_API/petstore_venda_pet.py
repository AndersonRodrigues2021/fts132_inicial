import pytest
import requests

base_url = 'https://petstore.swagger.io/v2/store/order'
headers = {'Content-Type': 'application/json'}

def teste_venda_pet():
    status_code_esperado = 200
    id_pet = 10030
    status_venda = 'vendido'
    finalizado_venda = True

    resposta = requests.post(
        url=base_url,
        data=open('C://Users//Anderson//PycharmProjects//fts132_inicial//2_Teste_API//db//venda1.json', 'rb'),
        headers=headers
    )
    corpo_da_resposta = resposta.json()
    print(resposta)
    print(resposta.status_code)
    print(corpo_da_resposta)

    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['petId'] == id_pet
    assert corpo_da_resposta['status'] == status_venda
    assert corpo_da_resposta['complete'] == finalizado_venda
