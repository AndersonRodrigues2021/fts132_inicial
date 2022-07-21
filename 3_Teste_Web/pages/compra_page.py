# 1 - Bibliotecas

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

# from pages.base_page import BasePage
# 2- Classe

class CompraPage():

    def inicio(self, driver):
        self.driver = driver
        self._entrar('https://www.petz.com.br')
        self.pesquisa = "search"
        self.nome_produto = "coleira azul"
        self.botao_pesquisa = ".custom-icon"

    def pesquisando_produto(self,locator):
        self.driver.find_element_by_id(self.pesquisa).click()
        self.driver.find_element_by_id(self.pesquisa).clear()
        self.driver.find_element_by_id(self.pesquisa).send_keys(self.nome_produto)
        self.driver.find_element_by_css_selectot(self.botao_pesquisa).click()