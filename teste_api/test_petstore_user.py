import pytest
import requests

base_url = 'https://petstore.swagger.io/v2/user'
headers = {'Content-Type': 'application/json'}

def testar_criar_usuario():
    status_code_esperado = 200
    codigo_esperado = 200
    tipo_esperado = "unknown"
    mensagem_esperada = '1001'

    resposta = requests.post(
        url=base_url,
        data=open('C://Users//Anderson//PycharmProjects//fts132_inicial//2_Teste_API//db//user1.json', 'rb'),
        headers=headers
    )

    corpo_da_resposta = resposta.json()
    print(resposta)
    print(resposta.status_code)
    print(corpo_da_resposta)

    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['code'] == codigo_esperado
    assert corpo_da_resposta['type'] == tipo_esperado
    assert corpo_da_resposta['message'] == mensagem_esperada


def testar_consultar_usuario():
    status_code = 200
    id = 1001
    username = 'HerGra'
    firstName = 'Hermione'
    lastName = 'Granger'
    email = 'andersonanderson_@hotmail.com'
    password = 'Senha@123'
    phone = '11999999999'
    userStatus = 0

    resposta = requests.get(
        url=f'{base_url}/{username}',
        headers=headers
    )

    corpo_da_resposta = resposta.json()
    print(resposta)
    print(resposta.status_code)
    print(corpo_da_resposta)

    assert resposta.status_code == status_code
    assert corpo_da_resposta['id'] == 1001
    assert corpo_da_resposta['username'] == 'HerGra'
    assert corpo_da_resposta['email'] == 'andersonanderson_@hotmail.com'
    assert corpo_da_resposta['phone'] == '11999999999'


def testar_alterar_usuario():
    username = 1001
    status_code_esperado = 200
    codigo_esperado = 200
    tipo_esperado = "unknown"
    mensagem_esperada = '1001'

    resposta = requests.put(
        url=f'{base_url}/{username}',
        data=open('C://Users//Anderson//PycharmProjects//fts132_inicial//2_Teste_API//db//user2.json', 'rb'),
        headers=headers
    )
    corpo_da_resposta = resposta.json()
    print(resposta)
    print(resposta.status_code)
    print(corpo_da_resposta)

    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['code'] == codigo_esperado
    assert corpo_da_resposta['type'] == tipo_esperado
    assert corpo_da_resposta['message'] == mensagem_esperada


def testar_excluir_usuario():
    username = 'HerGra'
    status_code_esperado = 200
    codigo_esperado = 200
    tipo_esperado = "unknown"
    mensagem_esperada = 'HerGra'

    resposta = requests.delete(
        url=f'{base_url}/{username}',
        headers=headers
    )

    match resposta.status_code:
        case 200:  # Apagar um usuário que foi encontrado
            print('Usuário apagado')
            orpo_da_resposta = resposta.json()
            print(resposta)
            print(resposta.status_code)
            print(corpo_da_resposta)

            assert resposta.status_code == status_code_esperado
            assert corpo_da_resposta['code'] == codigo_esperado
            assert corpo_da_resposta['type'] == tipo_esperado
            assert corpo_da_resposta['message'] == mensagem_esperada

        case 400:
            print('username fornecido incorretamente')

        case 404:
            print('usuário não encontrado')


def testar_login_do_usuario():
    username = 'HerGra'
    password = 'Senha@123'
    status_code_esperado = 200
    codigo_esperado = 200
    tipo_esperado = 'unknown'
    inicio_mensagem_esperada = 'logged in user session:'

    resposta = requests.get(
        url=f'{base_url}/login?username={username}&password={password}',
        headers=headers
    )

    corpo_da_resposta = resposta.json()
    print(resposta)
    print(resposta.status_code)
    print(corpo_da_resposta)

    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['code'] == codigo_esperado
    assert corpo_da_resposta['type'] == tipo_esperado
    assert corpo_da_resposta['message'].find(inicio_mensagem_esperada)!= -1

    frase = 'Neste fim de ano planeje p seo sucesso'
    assert frase.find('sucesso') != -1

    mensagem_recebida = corpo_da_resposta['message']
    print(f'A mensagem recebida é: {mensagem_recebida}')
    token_usuario = mensagem_recebida[23:37]
    print(f'O token do usuario é:{token_usuario}')

