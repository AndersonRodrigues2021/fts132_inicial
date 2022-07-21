import pytest
import requests

base_url = 'https://petstore.swagger.io/v2/pet'
headers = {'Content-Type': 'application/json'}

def testar_criar_pet():
    status_code_esperado = 200
    nome_pet_esperado = 'Bichento'
    tag_esperada = 'vacinado'

    resposta = requests.post(
        url=base_url,
        data=open('C://Users//Anderson//PycharmProjects//fts132_inicial//2_Teste_API//db//pet1.json', 'rb'),
        headers=headers
    )
    corpo_da_resposta = resposta.json()
    print(resposta)
    print(resposta.status_code)
    print(corpo_da_resposta)

    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['name'] == nome_pet_esperado
    #assert corpo_da_resposta['tags.name'] == tag_esperada
