import time
from re import split
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd


df = pd.read_excel(r'Automação Acesso Questor Zen.xlsx')
dff = df[['CNPJ/CEI','EMPRESAS','ANALISTA FISCAL NOVO','USUÁRIO QUESTOR ZEN','GRUPO QUESTOR ZEN']]

lista_grupos = list(dff['GRUPO QUESTOR ZEN'])
lista_cnpj = list(dff['CNPJ/CEI'])

lista_grupos_nrepetidos = []
lista_cnpj_nrepetidos = []
for element in lista_grupos:
    if element not in lista_grupos_nrepetidos:
        lista_grupos_nrepetidos.append(element)
for element in lista_cnpj:
    if element not in lista_cnpj_nrepetidos:
        lista_cnpj_nrepetidos.append(element)        
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
navegador.get('https://jrcontabilidade.app.questorpublico.com.br')
navegador.find_element('xpath', '//*[@id="UserName"]').send_keys('julio@jrcontabiltr.com.br')
time.sleep(1)
navegador.find_element('xpath', '//*[@id="Password"]').send_keys('Jm146614127')
time.sleep(1)
navegador.find_element('xpath', '//*[@id="login-button"]').click()
time.sleep(1)
navegador.find_element('xpath', '//*[@id="user-menu"]/li[4]/a/i').click()
time.sleep(1)
navegador.find_element('xpath', '//*[@id="user-menu"]/li[4]/ul/li[8]/a').click()
time.sleep(1)
navegador.find_element('xpath', '/html/body/div/div/div[2]/div[1]/div/div/ul/li[2]/a').click()
# time.sleep(1)
# navegador.find_element('xpath', '//*[@id="search-name-direct"]//div[2]').click()
for item in lista_grupos_nrepetidos:
    str(item).strip()
    str(item).replace(".", " -",2)
dff.set_index('GRUPO QUESTOR ZEN')
for item in lista_grupos_nrepetidos:
    lista_cnpjj = []
    dfff = 0
    print(item)
    print(lista_grupos_nrepetidos)
    if item != '-':
        dfff = dff.loc[dff['GRUPO QUESTOR ZEN']==item]
        print(dfff.tail(10))
        time.sleep(2)
        navegador.find_element('xpath', '//*[@id="search-name-direct"]').send_keys(str(item))
        time.sleep(2)
        navegador.find_element('xpath', '//*[@id="def-table"]/tbody/tr/td[2]/a[1]/span').click()
        time.sleep(5)
        navegador.find_element('xpath', '/html/body/div[1]/div/div[2]/div[1]/div[1]/div[1]/div[3]/div[2]/div[4]/div/div/form/div[2]/div/div[1]/div[1]/div/label/select/option[9]').click()
        time.sleep(2)
        for i in range(0,2):
            lista_somente_cnpj = []
            if i != 0:  
                navegador.find_element('xpath', '//*[@id="clientLote_wrapper"]/div[2]/div/div/ul/li[5]/a').click()
                time.sleep(3)
            elements = navegador.find_elements(By.TAG_NAME, 'small')
            elementss = navegador.find_elements(By.XPATH, '//*[@id="clientLote"]/tbody/tr/td[3]/span')
            
            #//*[@id="clientLote"]/tbody/tr[242]/td[2]/small[1]
            for e in range(0,len(elements)):
                lista_cnpjj.append(elements[e].text)
                if len(lista_cnpjj) % 2 == 0:
                    lista_somente_cnpj.append(lista_cnpjj[-1])
                    if len(lista_somente_cnpj) != 0:
                        if lista_somente_cnpj[-1] in list(dfff['CNPJ/CEI']):
                            index = int(len(lista_somente_cnpj))
                            if elementss[index-1].text == 'Ativo':
                                checkbox = navegador.find_element('xpath', f'/html/body/div[1]/div/div[2]/div[1]/div[1]/div[1]/div[3]/div[2]/div[4]/div/div/form/div[2]/div/table/tbody/tr[{index}]/td[1]/input')
                                checagem = checkbox.is_selected()
                                if checagem == False:
                                    checkbox.click()
                                    
                        elif lista_somente_cnpj[-1] not in list(dfff['CNPJ/CEI']):
                            index = int(len(lista_somente_cnpj))
                            if elementss[index-1].text == 'Ativo':
                                checkbox = navegador.find_element('xpath', f'/html/body/div[1]/div/div[2]/div[1]/div[1]/div[1]/div[3]/div[2]/div[4]/div/div/form/div[2]/div/table/tbody/tr[{index}]/td[1]/input')
                                checagem = checkbox.is_selected()
                                if checagem == True:
                                    checkbox.click()
                            else:
                                checkbox = navegador.find_element('xpath', f'/html/body/div[1]/div/div[2]/div[1]/div[1]/div[1]/div[3]/div[2]/div[4]/div/div/form/div[2]/div/table/tbody/tr[{index}]/td[1]/input')
                                checagem = checkbox.is_selected()
                                if checagem == True:
                                    checkbox.click()                     
        navegador.find_element('xpath', f'/html/body/div[1]/div/div[2]/div[1]/div[1]/div[1]/div[3]/div[2]/div[4]/div/div/form/div[3]/input').click()  
        time.sleep(23)                    
    time.sleep(1)
    #navegador.find_element('xpath', '//*[@id="form-groupLote"]/div[1]/button').click()
    time.sleep(1)
    navegador.find_element('xpath', '//*[@id="search-name-direct"]').clear()
time.sleep(5)
#/html/body/div[1]/div/div[2]/div[1]/div[1]/div[1]/div[3]/div[2]/div[4]/div/div/form/div[3]/input
#posicao = pyautogui.position()
#Point(x=1577, y=541) sobe
#Point(x=1601, y=694) desce
#print(posicao)