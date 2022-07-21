import time

from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@given(u'acesso o site PETZ')
def step_impl(context):
    context.driver.get('https://www.petz.com.br')
    print('Passo 1 - Acessou o site Petz')
    time.sleep(1)

@when(u'consulto um produto "coleira azul"')
def step_impl(context):
    context.driver.find_element(By.ID, "search").click()
    context.driver.find_element(By.ID, "search").clear()
    context.driver.find_element(By.ID, "search").send_keys("coleira azul")
    print('Passo 2 - Consultou um produto chamado coleira')
    time.sleep(2)

@when(u'clico na lupa Pesquisa')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".custom-icon").click()
    print('Passo 3 - Clicou na Lupa')

@when(u'seleciono a coleira Ferplast')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".liProduct:nth-child(2) > #produto-href .product-img").click()
    print('Passo 4 - Selecionado a coleira "Coleira Ferplast Dayton Fantasy Azul para Cães"')

@when(u'comparo o nome produto "Coleira Ferplast Dayton Fantasy Azul para Cães"')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "h1").text == 'Coleira Ferplast Dayton Fantasy Azul para Cães'
    print('Passo 5 - Comparando o nome do produto')

@when(u'comparo o valor produto "R$ 79,99"')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".current-price-left > strong").text == 'R$ 79,99'
    print('Passo 6 - Comparando o preço do produto')
    time.sleep(1)

@when(u'clico na lupa "Adicionar Carrinho"')
def step_impl(context):
    context.driver.find_element(By.ID, "adicionarAoCarrinho").click()
    print('Passo 7 - Clicou na Lupa para adicionar ao carrinho')

@when(u'comparo o nome do produto carrinho')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".cart-item-detail > div:nth-child(2)").text == 'Coleira Ferplast Dayton Fantasy Azul para Cães'
    print('Passo 8 - Comparando o nome do produto')

@then(u'comparo o preco do produto carrinho')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".cont-start").text == '79,99'
    print('Passo 9 - Comparando o preço do produto')
