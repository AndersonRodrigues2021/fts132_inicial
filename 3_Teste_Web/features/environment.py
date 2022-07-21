from selenium import webdriver

# Inicio
def before_all (context):
    # Declarar o Selenium, instanciar como o navegador e apontar o driver
    context.driver = webdriver.Chrome('C://Users//Anderson//PycharmProjects//fts132_inicial//3_Teste_Web//drivers//chromedriver.exe')

    #Maximizar a janela do navegador
    context.driver.maximize_window()

    print('Passo A - Antes de Tudo')

def after_all(context):
    context.driver.quit()

    print('Passo Z - Depois de Tudo')

def after_step(context, step):
    print()
