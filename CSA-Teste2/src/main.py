from form import *

diretório = 'D:/anaconda/chromedriver.exe'
driver = webdriver.Chrome(diretório)

url = 'http://www.csa-ma.com.br'

page = Form(driver, url)
page.open()
page.clickButton()
page.create_form(
    'Fylip',
    'luizempresateste3',
    '999222333',
    'luiz@luiz.com',
    'luiz.com',
    'testando Padrao page object'
)