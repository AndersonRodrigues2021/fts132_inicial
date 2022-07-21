


class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def _entrar(self, url):
        self.driver.get(url)

    def _encontrar(self, locator):
        self.driver.find_element(locator['by'],locator['value'])

    def _clicar(self,locator):
        self._encontrar(locator).click()

    def _escrever(self, locator, text):
        self._encontrar(locator.send_keys(text))

    def _aparece(self, locator, timeout=1):