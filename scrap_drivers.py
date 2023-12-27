import pandas as pd
import time
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import datetime

scrap_start = datetime.now()

#opciones de chrome
options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

#Buscar sitio web
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
driver = webdriver.Chrome(options=options)
driver.get('https://formula1.lne.es/')

#Aceptar cookies
time.sleep(1)
button_cookies = driver.find_element(by=By.XPATH,value='/html/body/div[1]/div/div/div/div/div/div[2]/button[2]')
button_cookies.click()

#PESTAÑA PILOTOS
def drivers_page():
    time.sleep(1)
    drivers_page = driver.find_element(by=By.XPATH,value='/html/body/header/nav/div/div[2]/ul/li[5]/a')
    drivers_page.click()
drivers_page()

#TABLA DATOS PILOTOS
name = []
car_number = []
nationality = []
birth_day = []
birth_place = []
championship = []

#George Russell
time.sleep(1)
russell_page = driver.find_element(by='xpath',value='//*[@id="pilotos"]/div[1]/div[1]/div/div/div[1]/a').click()
profile_russell = driver.find_elements(by='xpath', value='//*[@id="ficha_piloto"]/dl[1]/..')
for info in profile_russell:
    name.append(info.find_element(by='xpath',value='./dl[1]/dd').text)
    car_number.append(info.find_element(by='xpath',value='./dl[2]/dd').text)
    nationality.append(info.find_element(by='xpath',value='./dl[3]/dd').text)
    birth_day.append(info.find_element(by='xpath',value='./dl[4]/dd').text)
    birth_place.append(info.find_element(by='xpath',value='./dl[5]/dd').text)
    championship.append(info.find_element(by='xpath',value='./dl[6]/dd').text)
time.sleep(1)
drivers_page()

#Lewis Hamilton
time.sleep(1)
hamilton_page = driver.find_element(by='xpath',value='//*[@id="pilotos"]/div[1]/div[2]/div/div/div[1]/a').click()
profile_hamilton = driver.find_elements(by='xpath', value='//*[@id="ficha_piloto"]/dl[1]/..')
for info in profile_hamilton:
    name.append(info.find_element(by='xpath',value='./dl[1]/dd').text)
    car_number.append(info.find_element(by='xpath',value='./dl[2]/dd').text)
    nationality.append(info.find_element(by='xpath',value='./dl[3]/dd').text)
    birth_day.append(info.find_element(by='xpath',value='./dl[4]/dd').text)
    birth_place.append(info.find_element(by='xpath',value='./dl[5]/dd').text)
    championship.append(info.find_element(by='xpath',value='./dl[6]/dd').text)
time.sleep(1)
drivers_page()

#Pierre Gasly
time.sleep(1)
gasly_page = driver.find_element(by='xpath',value='//*[@id="pilotos"]/div[1]/div[5]/div/div/div[1]/a').click()
profile_gasly = driver.find_elements(by='xpath', value='//*[@id="ficha_piloto"]/dl[1]/..')
for info in profile_gasly:
    name.append(info.find_element(by='xpath',value='./dl[1]/dd').text)
    car_number.append(info.find_element(by='xpath',value='./dl[2]/dd').text)
    nationality.append(info.find_element(by='xpath',value='./dl[3]/dd').text)
    birth_day.append(info.find_element(by='xpath',value='./dl[4]/dd').text)
    birth_place.append(info.find_element(by='xpath',value='./dl[5]/dd').text)
    championship.append(info.find_element(by='xpath',value='./dl[6]/dd').text)
time.sleep(1)
drivers_page()

#Esteban Ocon
time.sleep(1)
ocon_page = driver.find_element(by='xpath',value='//*[@id="pilotos"]/div[1]/div[6]/div/div/div[1]/a').click()
profile_ocon = driver.find_elements(by='xpath', value='//*[@id="ficha_piloto"]/dl[1]/..')
for info in profile_ocon:
    name.append(info.find_element(by='xpath',value='./dl[1]/dd').text)
    car_number.append(info.find_element(by='xpath',value='./dl[2]/dd').text)
    nationality.append(info.find_element(by='xpath',value='./dl[3]/dd').text)
    birth_day.append(info.find_element(by='xpath',value='./dl[4]/dd').text)
    birth_place.append(info.find_element(by='xpath',value='./dl[5]/dd').text)
    championship.append(info.find_element(by='xpath',value='./dl[6]/dd').text)
time.sleep(1)
drivers_page()

#Nico Hulk
time.sleep(1)
hulk_page = driver.find_element(by='xpath',value='//*[@id="pilotos"]/div[1]/div[8]/div/div/div[1]/a').click()
profile_hulk = driver.find_elements(by='xpath', value='//*[@id="ficha_piloto"]/dl[1]/..')
for info in profile_hulk:
    name.append(info.find_element(by='xpath',value='./dl[1]/dd').text)
    car_number.append(info.find_element(by='xpath',value='./dl[2]/dd').text)
    nationality.append(info.find_element(by='xpath',value='./dl[3]/dd').text)
    birth_day.append(info.find_element(by='xpath',value='./dl[4]/dd').text)
    birth_place.append(info.find_element(by='xpath',value='./dl[5]/dd').text)
    championship.append(info.find_element(by='xpath',value='./dl[6]/dd').text)
time.sleep(1)
drivers_page()

#Kevin Magnussen
time.sleep(1)
magnus_page = driver.find_element(by='xpath',value='//*[@id="pilotos"]/div[1]/div[9]/div/div/div[1]/a').click()
profile_magnus = driver.find_elements(by='xpath', value='//*[@id="ficha_piloto"]/dl[1]/..')
for info in profile_magnus:
    name.append(info.find_element(by='xpath',value='./dl[1]/dd').text)
    car_number.append(info.find_element(by='xpath',value='./dl[2]/dd').text)
    nationality.append(info.find_element(by='xpath',value='./dl[3]/dd').text)
    birth_day.append(info.find_element(by='xpath',value='./dl[4]/dd').text)
    birth_place.append(info.find_element(by='xpath',value='./dl[5]/dd').text)
    championship.append(info.find_element(by='xpath',value='./dl[6]/dd').text)
time.sleep(1)
drivers_page()

#Oscar Piastri
time.sleep(1)
piastri_page = driver.find_element(by='xpath',value='//*[@id="pilotos"]/div[1]/div[12]/div/div/div[1]/a').click()
profile_piastri = driver.find_elements(by='xpath', value='//*[@id="ficha_piloto"]/dl[1]/..')
for info in profile_piastri:
    name.append(info.find_element(by='xpath',value='./dl[1]/dd').text)
    car_number.append(info.find_element(by='xpath',value='./dl[2]/dd').text)
    nationality.append(info.find_element(by='xpath',value='./dl[3]/dd').text)
    birth_day.append(info.find_element(by='xpath',value='./dl[4]/dd').text)
    birth_place.append(info.find_element(by='xpath',value='./dl[5]/dd').text)
    championship.append(info.find_element(by='xpath',value='./dl[6]/dd').text)
time.sleep(1)
drivers_page()

#Lando Norris
time.sleep(1)
norris_page = driver.find_element(by='xpath',value='//*[@id="pilotos"]/div[1]/div[13]/div/div/div[1]/a').click()
profile_norris = driver.find_elements(by='xpath', value='//*[@id="ficha_piloto"]/dl[1]/..')
for info in profile_norris:
    name.append(info.find_element(by='xpath',value='./dl[1]/dd').text)
    car_number.append(info.find_element(by='xpath',value='./dl[2]/dd').text)
    nationality.append(info.find_element(by='xpath',value='./dl[3]/dd').text)
    birth_day.append(info.find_element(by='xpath',value='./dl[4]/dd').text)
    birth_place.append(info.find_element(by='xpath',value='./dl[5]/dd').text)
    championship.append(info.find_element(by='xpath',value='./dl[6]/dd').text)
time.sleep(1)
drivers_page()

#Sergio Perez
time.sleep(1)
perez_page = driver.find_element(by='xpath',value='//*[@id="pilotos"]/div[1]/div[15]/div/div/div[1]/a').click()
profile_perez = driver.find_elements(by='xpath', value='//*[@id="ficha_piloto"]/dl[1]/..')
for info in profile_perez:
    name.append(info.find_element(by='xpath',value='./dl[1]/dd').text)
    car_number.append(info.find_element(by='xpath',value='./dl[2]/dd').text)
    nationality.append(info.find_element(by='xpath',value='./dl[3]/dd').text)
    birth_day.append(info.find_element(by='xpath',value='./dl[4]/dd').text)
    birth_place.append(info.find_element(by='xpath',value='./dl[5]/dd').text)
    championship.append(info.find_element(by='xpath',value='./dl[6]/dd').text)
time.sleep(1)
drivers_page()

#Max Verstappen
time.sleep(1)
vers_page = driver.find_element(by='xpath',value='//*[@id="pilotos"]/div[1]/div[16]/div/div/div[1]/a').click()
profile_vers = driver.find_elements(by='xpath', value='//*[@id="ficha_piloto"]/dl[1]/..')
for info in profile_vers:
    name.append(info.find_element(by='xpath',value='./dl[1]/dd').text)
    car_number.append(info.find_element(by='xpath',value='./dl[2]/dd').text)
    nationality.append(info.find_element(by='xpath',value='./dl[3]/dd').text)
    birth_day.append(info.find_element(by='xpath',value='./dl[4]/dd').text)
    birth_place.append(info.find_element(by='xpath',value='./dl[5]/dd').text)
    championship.append(info.find_element(by='xpath',value='./dl[6]/dd').text)
time.sleep(1)
drivers_page()

#Fernando Alonso
time.sleep(1)
alonso_page = driver.find_element(by='xpath',value='//*[@id="pilotos"]/div[1]/div[18]/div/div/div[1]/a').click()
profile_alonso = driver.find_elements(by='xpath', value='//*[@id="ficha_piloto"]/dl[1]/..')
for info in profile_alonso:
    name.append(info.find_element(by='xpath',value='./dl[1]/dd').text)
    car_number.append(info.find_element(by='xpath',value='./dl[2]/dd').text)
    nationality.append(info.find_element(by='xpath',value='./dl[3]/dd').text)
    birth_day.append(info.find_element(by='xpath',value='./dl[4]/dd').text)
    birth_place.append(info.find_element(by='xpath',value='./dl[5]/dd').text)
    championship.append(info.find_element(by='xpath',value='./dl[6]/dd').text)
time.sleep(1)
drivers_page()

#Lance Stroll
time.sleep(1)
stroll_page = driver.find_element(by='xpath',value='//*[@id="pilotos"]/div[1]/div[19]/div/div/div[1]/a').click()
profile_stroll = driver.find_elements(by='xpath', value='//*[@id="ficha_piloto"]/dl[1]/..')
for info in profile_stroll:
    name.append(info.find_element(by='xpath',value='./dl[1]/dd').text)
    car_number.append(info.find_element(by='xpath',value='./dl[2]/dd').text)
    nationality.append(info.find_element(by='xpath',value='./dl[3]/dd').text)
    birth_day.append(info.find_element(by='xpath',value='./dl[4]/dd').text)
    birth_place.append(info.find_element(by='xpath',value='./dl[5]/dd').text)
    championship.append(info.find_element(by='xpath',value='./dl[6]/dd').text)
time.sleep(1)
drivers_page()

#Nyck De Vries
time.sleep(1)
vries_page = driver.find_element(by='xpath',value='//*[@id="pilotos"]/div[1]/div[21]/div/div/div[1]/a').click()
profile_vries = driver.find_elements(by='xpath', value='//*[@id="ficha_piloto"]/dl[1]/..')
for info in profile_vries:
    name.append(info.find_element(by='xpath',value='./dl[1]/dd').text)
    car_number.append(info.find_element(by='xpath',value='./dl[2]/dd').text)
    nationality.append(info.find_element(by='xpath',value='./dl[3]/dd').text)
    birth_day.append(info.find_element(by='xpath',value='./dl[4]/dd').text)
    birth_place.append(info.find_element(by='xpath',value='./dl[5]/dd').text)
    championship.append(info.find_element(by='xpath',value='./dl[6]/dd').text)
time.sleep(1)
drivers_page()

#Yuki Tsunoda
time.sleep(1)
yuki_page = driver.find_element(by='xpath',value='//*[@id="pilotos"]/div[1]/div[22]/div/div/div[1]/a').click()
profile_yuki = driver.find_elements(by='xpath', value='//*[@id="ficha_piloto"]/dl[1]/..')
for info in profile_yuki:
    name.append(info.find_element(by='xpath',value='./dl[1]/dd').text)
    car_number.append(info.find_element(by='xpath',value='./dl[2]/dd').text)
    nationality.append(info.find_element(by='xpath',value='./dl[3]/dd').text)
    birth_day.append(info.find_element(by='xpath',value='./dl[4]/dd').text)
    birth_place.append(info.find_element(by='xpath',value='./dl[5]/dd').text)
    championship.append(info.find_element(by='xpath',value='./dl[6]/dd').text)
time.sleep(1)
drivers_page()

#Carlos Sainz
time.sleep(1)
sainz_page = driver.find_element(by='xpath',value='//*[@id="pilotos"]/div[1]/div[24]/div/div/div[1]/a').click()
profile_sainz = driver.find_elements(by='xpath', value='//*[@id="ficha_piloto"]/dl[1]/..')
for info in profile_sainz:
    name.append(info.find_element(by='xpath',value='./dl[1]/dd').text)
    car_number.append(info.find_element(by='xpath',value='./dl[2]/dd').text)
    nationality.append(info.find_element(by='xpath',value='./dl[3]/dd').text)
    birth_day.append(info.find_element(by='xpath',value='./dl[4]/dd').text)
    birth_place.append(info.find_element(by='xpath',value='./dl[5]/dd').text)
    championship.append(info.find_element(by='xpath',value='./dl[6]/dd').text)
time.sleep(1)
drivers_page()

#Charles Leclerc
time.sleep(1)
leclerl_page = driver.find_element(by='xpath',value='//*[@id="pilotos"]/div[1]/div[25]/div/div/div[1]/a').click()
profile_leclerl = driver.find_elements(by='xpath', value='//*[@id="ficha_piloto"]/dl[1]/..')
for info in profile_leclerl:
    name.append(info.find_element(by='xpath',value='./dl[1]/dd').text)
    car_number.append(info.find_element(by='xpath',value='./dl[2]/dd').text)
    nationality.append(info.find_element(by='xpath',value='./dl[3]/dd').text)
    birth_day.append(info.find_element(by='xpath',value='./dl[4]/dd').text)
    birth_place.append(info.find_element(by='xpath',value='./dl[5]/dd').text)
    championship.append(info.find_element(by='xpath',value='./dl[6]/dd').text)
time.sleep(1)
drivers_page()

#Valtteri Bottas
time.sleep(1)
bottas_page = driver.find_element(by='xpath',value='//*[@id="pilotos"]/div[1]/div[27]/div/div/div[1]/a').click()
profile_bottas = driver.find_elements(by='xpath', value='//*[@id="ficha_piloto"]/dl[1]/..')
for info in profile_bottas:
    name.append(info.find_element(by='xpath',value='./dl[1]/dd').text)
    car_number.append(info.find_element(by='xpath',value='./dl[2]/dd').text)
    nationality.append(info.find_element(by='xpath',value='./dl[3]/dd').text)
    birth_day.append(info.find_element(by='xpath',value='./dl[4]/dd').text)
    birth_place.append(info.find_element(by='xpath',value='./dl[5]/dd').text)
    championship.append(info.find_element(by='xpath',value='./dl[6]/dd').text)
time.sleep(1)
drivers_page()

#Ganyu Zhou
time.sleep(1)
zhou_page = driver.find_element(by='xpath',value='//*[@id="pilotos"]/div[1]/div[28]/div/div/div[1]/a').click()
profile_zhou = driver.find_elements(by='xpath', value='//*[@id="ficha_piloto"]/dl[1]/..')
for info in profile_zhou:
    name.append(info.find_element(by='xpath',value='./dl[1]/dd').text)
    car_number.append(info.find_element(by='xpath',value='./dl[2]/dd').text)
    nationality.append(info.find_element(by='xpath',value='./dl[3]/dd').text)
    birth_day.append(info.find_element(by='xpath',value='./dl[4]/dd').text)
    birth_place.append(info.find_element(by='xpath',value='./dl[5]/dd').text)
    championship.append(info.find_element(by='xpath',value='./dl[6]/dd').text)
time.sleep(1)
drivers_page()

#Logan Seargent
time.sleep(1)
logan_page = driver.find_element(by='xpath',value='//*[@id="pilotos"]/div[1]/div[30]/div/div/div[1]/a').click()
profile_logan = driver.find_elements(by='xpath', value='//*[@id="ficha_piloto"]/dl[1]/..')
for info in profile_logan:
    name.append(info.find_element(by='xpath',value='./dl[1]/dd').text)
    car_number.append(info.find_element(by='xpath',value='./dl[2]/dd').text)
    nationality.append(info.find_element(by='xpath',value='./dl[3]/dd').text)
    birth_day.append(info.find_element(by='xpath',value='./dl[4]/dd').text)
    birth_place.append(info.find_element(by='xpath',value='./dl[5]/dd').text)
    championship.append(info.find_element(by='xpath',value='./dl[6]/dd').text)
time.sleep(1)
drivers_page()

#Alexander Albon
time.sleep(1)
albon_page = driver.find_element(by='xpath',value='//*[@id="pilotos"]/div[1]/div[31]/div/div/div[1]/a').click()
profile_albon = driver.find_elements(by='xpath', value='//*[@id="ficha_piloto"]/dl[1]/..')
for info in profile_albon:
    name.append(info.find_element(by='xpath',value='./dl[1]/dd').text)
    car_number.append(info.find_element(by='xpath',value='./dl[2]/dd').text)
    nationality.append(info.find_element(by='xpath',value='./dl[3]/dd').text)
    birth_day.append(info.find_element(by='xpath',value='./dl[4]/dd').text)
    birth_place.append(info.find_element(by='xpath',value='./dl[5]/dd').text)
    championship.append(info.find_element(by='xpath',value='./dl[6]/dd').text)
time.sleep(1)
drivers_page()

dict_drivers = {'Nombre':name,
                'Numero de Coche': car_number,
                'Nacionalidad': nationality,
                'Fecha de Nacimiento':birth_day,
                'Lugar de Nacimiento':birth_place,
                'Campeonatos':championship}
df_drivers = pd.DataFrame(dict_drivers)
time.sleep(2)
df_drivers.to_csv('Pilotos.csv', mode='w+', index=False)

scrap_end = datetime.now()
time_scrap = scrap_end - scrap_start
tiempo_scrap_seconds = time_scrap.seconds
print(f'Web scrapping demoró {tiempo_scrap_seconds} segundos')

#cerrar navegador
time.sleep(2)
driver.quit()
