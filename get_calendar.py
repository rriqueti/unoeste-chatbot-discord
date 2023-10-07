
import os

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

load_dotenv()


class SeleniumMethod:
    def __init__(self):
        self.options = Options()
        # self.options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get('https://www.unoeste.br/Site/AVA/Default.aspx')
        self.MATRICULA = os.getenv('MATRICULA')
        self.SENHA_UNOESTE = os.getenv('SENHA_UNOESTE')
        self.thead = {'disciplina': [], 'destaque': [], 'periodo': []}
        self.login = self.login()
        self.filtrar_entregas = self.filtrar_entregas()

    def login(self):
        self.driver.find_element(By.ID, 'tbLogin').send_keys(self.MATRICULA)
        self.driver.find_element(
            By.ID, 'tbSenha').send_keys(self.SENHA_UNOESTE)
        self.driver.find_element(By.ID, 'bAutenticar').click()
        self.wait = WebDriverWait(self.driver, 10)
        self.wait.until(EC.element_to_be_clickable(
            (By.CLASS_NAME, 'destaque')))

    def filtrar_entregas(self):
        disciplina = self.driver.find_elements(
            By.CLASS_NAME, 'disciplina')
        destaque = self.driver.find_elements(
            By.CLASS_NAME, 'destaque')
        periodo = self.driver.find_elements(
            By.CLASS_NAME, 'periodo')

        for d in disciplina:
            self.thead['disciplina'].append(d.text)
        for d in destaque:
            self.thead['destaque'].append(d.text)
        for d in periodo:
            self.thead['periodo'].append(d.text)

    def mostrar_atividades(self):
        value = len(self.thead['disciplina']) - 1
        count = 0
        ata = []
        while count <= value:
            if 'Resumo' in self.thead['destaque']:
                continue
            valor = self.thead['disciplina'][count]+'\n'+self.thead[
                'destaque'][count]+'\n'+self.thead['periodo'][count]+'\n\n'
            ata.append(valor)
            msg_final = '\n'.join(ata)
            count += 1
        self.driver.quit()
        return msg_final
