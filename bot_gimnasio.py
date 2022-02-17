from msilib.schema import SelfReg
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from time import sleep


class UPVBot():
    def __init__(self):
        s = Service('C:/chromedriver.exe')
        self.driver = webdriver.Chrome(service=s)
    
    def login(self):
        self.driver.get('https://intranet.upv.es/pls/soalu/est_intranet.ni_portal_n?P_IDIOMA=c')
        
        dni_in = self.driver.find_element(By.NAME, 'dni')
        # introducir dni sin letra
        dni_in.send_keys('')

        pin_in = self.driver.find_element(By.NAME, 'clau')
        # introducir clave de acceso a la upv
        pin_in.send_keys('')
        sleep(1)

        lgin_btn = self.driver.find_element(By.CLASS_NAME, 'upv_btsubmit')
        lgin_btn.click()
        sleep(2)
        print("acaba login")
    
    def reservar_gimnasio(self):
        # busca boton de la intranet
        intranet_btn = self.driver.find_element(By.XPATH, '//*[@id="intranet"]/a[2]')
        intranet_btn.click()
        sleep(2)

        facilities_btn = self.driver.find_element(By.XPATH, '//*[@id="elemento_1003"]/tbody/tr/td[1]/p/a')
        facilities_btn.click()
        sleep(2)

        # despliego el menu de programas
        programa = Select(self.driver.find_element(By.NAME, 'tipoact'))
        programa.select_by_value('6358')

        # despliego el menu de actividades
        actividad = Select(self.driver.find_element(By.NAME, 'acti'))
        actividad.select_by_value('20435')
        sleep(2)

        # creo una matriz con los huecos libres que hay
        # leer readme
        buttons = self.driver.find_elements(By.CLASS_NAME, "upv_enlacelista")

        dia1 = buttons[5]
        dia1.click()
        buttons = self.driver.find_elements(By.CLASS_NAME, "upv_enlacelista")

        dia2 = buttons[15]
        dia2.click()
        buttons = self.driver.find_elements(By.CLASS_NAME, "upv_enlacelista")

        dia3 = buttons[25]
        dia3.click()

bot = UPVBot()
bot.login()
bot.reservar_gimnasio()
