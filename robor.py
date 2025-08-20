from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep

# Configuração do navegador
chrome_options = Options()
chrome_options.binary_location = "/usr/bin/chromium"  # caminho correto no Ubuntu

driver = webdriver.Chrome(options=chrome_options)

def login_inpi(driver, usuario: str, senha: str):
    """Realiza o login no sistema do INPI"""
    driver.get("https://busca.inpi.gov.br/pePI/")
    sleep(3)

    login = driver.find_element(By.NAME, "T_Login")
    login.send_keys(usuario)
    sleep(1)

    senha_input = driver.find_element(By.NAME, "T_Senha")
    senha_input.send_keys(senha)
    sleep(1)

    botao = driver.find_element(By.XPATH, '//input[@value=" Continuar » "]')
    botao.click()

    print("✅ Login efetuado com sucesso.")


def navegar_pedidos(driver):
    """Navega até 'Meus Pedidos'"""
    botao = driver.find_element(By.XPATH, '/html/body/div/div/table/tbody/tr[4]/td/div/p/map/area[1]')
    botao.click()
    sleep(5)

    botao = driver.find_element(By.LINK_TEXT, "Meus Pedidos")
    botao.click()
    sleep(10)

    while not driver.find_elements(By.LINK_TEXT, "Início"):
        print("⏳ Aguardando página carregar...")
        sleep(1)

    print("🔗 Link 'Início' encontrado!")


def avancar_paginas(driver):
    """Avança pelas páginas enquanto houver botão 'Próxima»'"""
    while driver.find_elements(By.LINK_TEXT, "Próxima»"):
        botao = driver.find_element(By.LINK_TEXT, "Próxima»")
        botao.click()
        sleep(5)
        print("➡️ Avançando página")


def voltar_paginas(driver):
    """Volta pelas páginas enquanto houver botão '«Anterior-'"""
    while driver.find_elements(By.LINK_TEXT, "«Anterior-"):
        driver.back()
        print("⬅️ Voltou página")
        sleep(1)


if __name__ == "__main__":
    try:
        login_inpi(driver, usuario="pontocomr", senha="Registro12")
        navegar_pedidos(driver)
        avancar_paginas(driver)
        voltar_paginas(driver)

        input("✅ Finalizado! Pressione ENTER para sair...")

    finally:
        driver.quit()

