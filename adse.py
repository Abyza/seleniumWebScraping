from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome("C://Users//paulo//Downloads//chromedriver_win32 (1)//chromedriver.exe")

driver.get('https://datadrivenenvirolab.github.io/urban-city-page/')


dropbox = driver.find_elements(by=By.TAG_NAME, value="Option")
# 0 america  - ChapelHill
#
# 2 asia
dropbox[2].click()


dropbox = driver.find_elements(by=By.TAG_NAME, value="Option")

CityName = []

CityArea = []
CityPopulation= []
GDPPerCapita = []
isUSD =[]
CityTier =[]
AirQuality=[]
UrbanHeatIsland=[]
ClimatePolicy =[]
CO2Emission = []
TreeCover= []
Water = []
PublicTransit=[]

startClick = False


for i in dropbox:
# cahnge this to corresponsing continent
    if i.text == "Bagcilar":
        startClick = True
    if i.text == "PM2.5":
        startClick = False
    if startClick == True:
        i.click()
        city = i.text
        print(city)
        CityName.append(city)
        target = driver.find_element(by = By.ID, value = "cityArea").text
        print(target)
        CityArea.append(target)

        target = driver.find_element(by=By.ID, value="population").text
        print(target)
        CityPopulation.append(target)

        target = driver.find_element(by=By.ID, value="income").text
        print(target)
        GDPPerCapita.append(target)

        target = driver.find_element(by=By.ID, value="tier").text
        print(target)
        isUSD.append(target)

        target = driver.find_element(by=By.ID, value="city_Tier").text
        print(target)
        CityTier.append(target)

        target = driver.find_element(by=By.ID, value="meanAir").text
        print(target)
        AirQuality.append(target)

        target = driver.find_element(by=By.ID, value="UHI").text
        print(target)
        UrbanHeatIsland.append(target)

        target = driver.find_element(by=By.ID, value="climPol").text
        print(target)
        ClimatePolicy.append(target)

        target = driver.find_element(by=By.ID, value="co2Emission").text
        print(target)
        CO2Emission.append(target)

        target = driver.find_element(by=By.ID, value="meanTree").text
        print(target)
        TreeCover.append(target)

        target = driver.find_element(by=By.ID, value="meanWater").text
        print(target)
        Water.append(target)

        target = driver.find_element(by=By.ID, value="meanTrans").text
        print(target)
        PublicTransit.append(target)



zipped = list(zip(CityName, CityArea, CityPopulation, GDPPerCapita,isUSD,CityTier, AirQuality,UrbanHeatIsland,ClimatePolicy, CO2Emission,TreeCover, Water,PublicTransit))

df = pd.DataFrame(zipped, columns=['CityName','CityArea', 'CityPopulation', 'GDPPerCapita','isUSD','CityTier', 'AirQuality','UrbanHeatIsland','ClimatePolicy', 'CO2Emission','TreeCover', 'Water','PublicTransit'])

print(df)
df.to_csv('/adseDataFrameOceanisdsdad.csv')


print("done")
sleep(10000)

#driver.quit()