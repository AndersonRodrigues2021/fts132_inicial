import pytest
import requests

base_url = 'https://petstore.swagger.io/v2/store/order'
headers = {'Content-Type': 'application/json'}

def teste_consulta_status_pet():
    status_code_esperado = 200
    id_order = 1
    id_pet = 10030
    tp_status = 'vendido'

    resposta = requests.get(
        url=f'{base_url}/{id_order}',
        headers=headers
    )

    corpo_da_resposta = resposta.json()
    print(resposta)
    print(resposta.status_code)
    print(corpo_da_resposta)

    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['id'] == id_order
    assert corpo_da_resposta['petId'] == id_pet
    assert corpo_da_resposta['status'] == tp_status
