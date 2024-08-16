'''
Automação com python

1 - Navergar até o site https://xxxxxxxxxxxxxxxxxxxx
2 - Inserir login
3 - Inserir senha
4 - Clicar em OK
5 - Selecionar a opção do menu 'xxxxxxx' - (Abre uma combo/lista)
6 - Selecionar a opção 'xxxxxxx'
7 - Informar a data anterior ao dia atual, no campo 'xxxxxxx', com dia, mês e ano xx/xx/xxxx
8 - Selecionar botão 'Buscar manifestações'
	a) O processo deve ser realizado todos os dias, uma vez ao dia, às 05h00.
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
from time import sleep
import schedule
import time

def realizar_automacao():

# Configurar opções do Chrome
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument('--ignore-certificate-errors') # Ignorar erros de navegador
	chrome_options.add_argument('--ignore-ssl-errors') # Ignorar erros de navegador
	chrome_options.add_argument('--disable-web-security')  # Ignorar erros de navegador - Não recomendado em produção

# Inicializar o driver do Chrome com as opções
	driver = webdriver.Chrome(options=chrome_options)

# 1 - Navegar até o site
	driver.get('https://xxxxxxxxxx')
	sleep(5)

# 2 - Inserir login
	login = driver.find_element(By.XPATH, "//input[@name='j_id108:j_id111']") # Sempre observar se as aspas de dentro e de fora estão diferentes - Se estiverem iguais ocorre erro
	sleep(2)
	login.send_keys('inserir usuário')
	sleep(1)

# 3 - Inserir senha
	senha = driver.find_element(By.XPATH, "//input[@name='j_id108:j_id114']") # Sempre observar se as aspas de dentro e de fora estão diferentes - Se estiverem iguais ocorre erro
	sleep(2)
	senha.send_keys('inserir senha')
	sleep(1)

# 4 - Clicar em OK
	botao_ok = driver.find_element(By.XPATH, "//input[@name='j_id108:j_id117']") # Sempre observar se as aspas de dentro e de fora estão diferentes - Se estiverem iguais ocorre erro
	sleep(2)
	botao_ok.click()
	sleep(5)

# 5 - Selecionar a opção do menu 'Integrações Externas' - (Abre uma combo/lista)
	menu_integracoes_externas = WebDriverWait(driver, 10).until(
    	EC.element_to_be_clickable((By.XPATH, "//div[@id='j_id20:j_id24']"))
)
	menu_integracoes_externas.click()

# 6 - Selecionar a opção do menu 'Buscar Manifestações'
	menu_buscarmanifestacoes = WebDriverWait(driver, 10).until(
    	EC.element_to_be_clickable((By.XPATH, "//span[@id='j_id20:j_id25:icon']"))
)
	menu_buscarmanifestacoes.click()

# 7 - Selecionar o campo 'Buscar Manifestações'
	campo_data = WebDriverWait(driver, 10).until(
    	EC.presence_of_element_located((By.XPATH, "//input[@id='j_id110:j_id115InputDate']")) 
)
	campo_data.click()

# 8 - Informar a data anterior ao dia atual
	data_anterior = (datetime.now() - timedelta(1)).strftime('%d/%m/%Y')
	campo_data.send_keys(data_anterior)

# 9 - Clicar em Buscar Manifestações
	botao_buscar = driver.find_element(By.XPATH, "//input[@id='j_id110:j_id116']") # Sempre observar se as aspas de dentro e de fora estão diferentes - Se estiverem iguais ocorre erro
	sleep(2)
	botao_buscar.click()

# Pausa para observar o resultado
	sleep(5)

# Fechar o navegador
	driver.quit()

# Agendar a execução diária às 06h00
schedule.every().day.at("06:00").do(realizar_automacao)

while True:
    schedule.run_pending()
    time.sleep(60)  # Aguarda 60 segundos entre as verificações de agendamento
'''
Usar driver.find_element(By.XPATH): Se você tiver certeza de que o elemento já está carregado e pronto no momento da interação.
Usar WebDriverWait com EC.element_to_be_clickable: Quando você estiver lidando com elementos que podem não estar prontos imediatamente, como em casos de carregamento dinâmico de conteúdo, animações ou scripts que modificam a página após o carregamento inicial.
Usando WebDriverWait com EC.element_to_be_clickable, você cria uma automação mais resiliente, capaz de lidar melhor com as variações de carregamento da página.
'''
'''
Esse código também funciona, basta completa-lo. Está mais simples.

from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
from time import sleep
import schedule

#def buscar_manifestacoes():
# Configurar opções do Chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')
chrome_options.add_argument('--disable-web-security')  # Não recomendado em produção

# Inicializar o driver do Chrome com as opções
driver = webdriver.Chrome(options=chrome_options)

# 1 - Navegar até o site https://xxxxxxxx
driver.get('https://xxxxxxxx')
sleep(5)

# Utilizar o XPATH para localização dos elementos que serão utilizados na automação (campos, botões e etc) = tag[@atributo='valor']

# 2 - Inserir login
login = driver.find_element(By.XPATH,"//input[@name='j_id108:j_id111']") # Sempre observar se as aspas de dentro e de fora estão diferentes - Se estiverem iguais ocorre erro
sleep(2)
login.send_keys('login')
sleep(1)

# 3 - Inserir senha
senha = driver.find_element(By.XPATH,"//input[@name='j_id108:j_id114']") # Sempre observar se as aspas de dentro e de fora estão diferentes - Se estiverem iguais ocorre erro
sleep(2)
senha.send_keys('senha')
sleep(1)

# 4 - Clicar em OK
botao_ok = driver.find_element(By.XPATH,"//input[@name='j_id108:j_id117']") # Sempre observar se as aspas de dentro e de fora estão diferentes - Se estiverem iguais ocorre erro
sleep(2)
botao_ok.click()
sleep(5)

# 5 - Selecionar a opção do menu 'Integrações Externas' - (Abre uma combo/lista)
menu_integracoes_externas = driver.find_element(By.XPATH, "//div[@id='j_id20:j_id24']") # ou //div[@id='j_id20:j_id24_span']
sleep(1)
menu_integracoes_externas.click()

# 6 - Selecionar a opção 'Buscar Manifestações'
menu_buscarmanifestacoes = driver.find_element(By.XPATH, "//span[@id='j_id20:j_id25:icon']") # ou //span[@id='j_id20:j_id25:anchor']
sleep(1)
menu_buscarmanifestacoes.click()
sleep(5)
'''
