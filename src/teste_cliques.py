from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# Caminho para o chromedriver
service = Service(executable_path='./chromedriver.exe')

# Instancia do navegador
driver = webdriver.Chrome(service=service)

# Navegar para a página local do contador
driver.get('http://127.0.0.1:5500/contador-cliques/src/')  # ajuste para seu caminho real

# Encontrar o botão (id correto)
botao_contar = driver.find_element(By.ID, "botao-contar")

# Clicar 10 vezes
for i in range(10):
    botao_contar.click()
    WebDriverWait(driver, 5).until(
        lambda d: len(d.find_elements(By.CSS_SELECTOR, "#historico li")) == i + 1
    )

# Verificar se 10 números foram exibidos
lista_cliques = driver.find_elements(By.CSS_SELECTOR, "#historico li")
assert len(lista_cliques) == 10, "Quantidade de cliques não corresponde!"

# Verificar se os números estão corretos
for idx, li in enumerate(lista_cliques, start=1):
    esperado = f"Clique nº {idx}"
    assert li.text == esperado, f"Esperado '{esperado}', encontrado '{li.text}'"

print("✅ Teste passou com sucesso!")

input("Pressione Enter para fechar o navegador...")
driver.quit()
