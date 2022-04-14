from ast import parse
from msilib.schema import SelfReg
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from time import sleep
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-a", "--days", required=True, type=int, help="days that you want to train")
parser.add_argument("-b", "--dhh", required=True, type=str, nargs='+', help="enter your training days as DHH (DAY HOURHOUR). IE: L07 = monday from 07:30 to 08:30")
args = vars(parser.parse_args())

x = int(args['days'])
days = list(args['dhh'])

print(f"quieres entrenar {x} dias y quieres entrenar estos dias: {days}")

class UPVBot():
    def __init__(self):
        s = Service('C:/chromedriver.exe')
        self.driver = webdriver.Chrome(service=s)
    
    def login(self):
        self.driver.get('https://intranet.upv.es/pls/soalu/est_intranet.ni_portal_n?P_IDIOMA=c')
        
        dni_in = self.driver.find_element(By.NAME, 'dni')
        # introduce dni
        dni_in.send_keys('')

        pin_in = self.driver.find_element(By.NAME, 'clau')
        # introduce access pin
        pin_in.send_keys('')
        sleep(1)

        lgin_btn = self.driver.find_element(By.CLASS_NAME, 'upv_btsubmit')
        lgin_btn.click()
        sleep(1)
        print("acaba login")

        intranet_btn = self.driver.find_element(By.XPATH, '//*[@id="intranet"]/a[2]')
        intranet_btn.click()
        sleep(1)

        facilities_btn = self.driver.find_element(By.XPATH, '//*[@id="elemento_1003"]/tbody/tr/td[1]/p/a')
        facilities_btn.click()
        sleep(1)

        # select "EN FORMA"
        programa = Select(self.driver.find_element(By.NAME, 'tipoact'))
        programa.select_by_value('6358')

        # select "MUSCULACION"
        actividad = Select(self.driver.find_element(By.NAME, 'acti'))
        actividad.select_by_value('20435')
        sleep(1)
    
    def reservar_gimnasio(self, off):

        buttons = self.driver.find_elements(By.CLASS_NAME, "upv_enlacelista")
        numero_botones = len(buttons)+off
        día_1_arg = numero_botones
        dia1 = buttons[día_1_arg]
        dia1.click()
    
def dias_a_reservar(diahora):
    dia = diahora[0]
    hora = str(diahora[1:3])

    offset_dia = 0
    offset_hora = 0

    if dia == 'L':
        offset_dia = -5
    elif dia == 'M':
        offset_dia = -4
    elif dia == 'X':
        offset_dia = -3
    elif dia == 'J':
        offset_dia = -2
    elif dia == 'V':
        offset_dia = -1

    if hora == '07' :
        offset_hora = -65
    elif hora == '08' :
        offset_hora = -60
    elif hora == '09' :
        offset_hora = -55
    elif hora == '11' :
        offset_hora = -50
    elif hora == '12' :
        offset_hora = -45
    elif hora == '13' :
        offset_hora = -40
    elif hora == '14' :
        offset_hora = -35
    elif hora == '15' :
        offset_hora = -30
    elif hora == '16' :
        offset_hora = -25
    elif hora == '17' :
        offset_hora = -20
    elif hora == '18' :
        offset_hora = -15
    elif hora == '19' :
        offset_hora = -10
    elif hora == '20' :
        offset_hora = -5
    elif hora == '21' :
        offset_hora = 0
    
    return offset_dia + offset_hora

bot = UPVBot()
bot.login()

for i in range(x):
    d = days[i]
    offset = dias_a_reservar(d)
    bot.reservar_gimnasio(offset)