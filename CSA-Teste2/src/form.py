from abc import ABC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from time import sleep
import pandas as pd

class FormElement(ABC):
    def __init__(self, webdriver, url):
        self.webdriver = webdriver
        self.url = url
        
    def open(self):
        self.webdriver.get(self.url)

class Form(FormElement):
    nome = (By.NAME, 'your-name')
    empresa = (By.CLASS_NAME, 'empresa')
    telefone = (By.NAME, 'telefone')
    email = (By.NAME, 'your-email')
    website = (By.NAME, 'website')
    mensagem = (By.NAME, 'your-message')
    submit = (By.ID, 'contact-page-button-blue')
    blog = (By.LINK_TEXT, 'BLOG')

    def clickButton(self):
        lista_datas = []
        lista_titles = []
        lista_content = []
        lista_urls = []
        self.webdriver.find_element(*self.blog).click()
        element = self.webdriver.find_element_by_xpath('//*[@id="main"]/div[2]/div[1]/div/div[1]/div[1]/div[4]/div/a')

        link_b = element.is_displayed()
        try:
            
            while link_b != False:
                element.click()
                sleep(2)
                
                post_title = self.webdriver.find_elements_by_class_name('post-title')
                post_date = self.webdriver.find_elements_by_class_name('post-date')
                post_content = self.webdriver.find_elements_by_class_name('post-excerpt')
                url_image = self.webdriver.find_elements_by_class_name('attachment-post-thumbnail')

                for i in post_title:
                    lista_titles.append(i.text)
                for j in post_date:
                    lista_datas.append(j.text)
                for w in post_content:
                    lista_content.append(w.text)
                for v in url_image:
                    lista_urls.append(v.get_attribute('src'))
                    
        except StaleElementReferenceException:
            lista_final = []
            lista_final.append([lista_titles, lista_datas, lista_content, lista_urls])
            sleep(2)
            df = pd.DataFrame(lista_final, columns=['Titulos', 'Data', 'Conteudos', 'Links-Images'])
            df.to_excel('teste02csa.xlsx', index=False)

            contato = self.webdriver.find_element_by_class_name("icon-envelope-alt")
            contato.click()

    def create_form(self, nome, empresa, telefone, email, website, mensagem):

        self.webdriver.find_element(*self.nome).send_keys(nome)
        self.webdriver.find_element(*self.empresa).send_keys(empresa)
        self.webdriver.find_element(*self.telefone).send_keys(telefone)
        self.webdriver.find_element(*self.email).send_keys(email)
        self.webdriver.find_element(*self.website).send_keys(website)
        self.webdriver.find_element(*self.mensagem).send_keys(mensagem)
        
        self.webdriver.find_element(*self.submit).click()
        

