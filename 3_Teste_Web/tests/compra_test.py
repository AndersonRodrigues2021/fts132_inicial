import os

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.compra_page import CompraPage

@pytest.fixture
def driver(request):

    def test_inicio(request):
        _chromedriver = 'drivers/chromedriver.exe'

        if os.path.isfile(_chromedriver):
            driver_ = webdriver.Chrome(_chromedriver)
        else:
            driver_ = webdriver.Chrome()
        ComprarPage = ComprarPage(driver_)
        def quit():
            driver_.quit()

        # sinalizando o fim da execução para o ambiente
        request.addfinalizer(quit)
        return driver_

    def test_pesquisando_produto (driver):
        driver.get('https://www.petz.com.br')
        driver.find_element(By.ID, "search").click()
        driver.find_element(By.ID, "search").clear()
        driver.find_element(By.ID, "search").send_keys("coleira azul")
        driver.find_element(By.CSS_SELECTOR, ".custom-icon").click()
    return ComprarPage
