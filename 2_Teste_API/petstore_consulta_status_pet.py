import pytest
import requests

base_url = 'https://petstore.swagger.io/v2/pet'
headers = {'Content-Type': 'application/json'}

def teste_consulta_status_pet():
    status_code_esperado = 200
    id_pet = 10030
    name_pet = 'Bichento'
    tp_status = 'available'

    resposta = requests.get(
        url=f'{base_url}/{id_pet}',
        headers=headers
    )

    corpo_da_resposta = resposta.json()
    print(resposta)
    print(resposta.status_code)
    print(corpo_da_resposta)

    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['id'] == 10030
    assert corpo_da_resposta['name'] == name_pet
    assert corpo_da_resposta['status'] == tp_status
