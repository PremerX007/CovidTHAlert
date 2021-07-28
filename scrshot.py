from selenium import webdriver
from Screenshot import Screenshot_Clipping
import time

def screenshot_data():
    ss = Screenshot_Clipping.Screenshot()
    driver = webdriver.Edge(executable_path=r'C:\Users\banna\Downloads\edgedriver_win64\msedgedriver.exe')
    url = "https://dvis3.ddc.moph.go.th/t/sat-covid/views/SATCOVIDDashboard/1-dash-tiles?:embed=y&:showVizHome=no&:host_url=https%3A%2F%2Fdvis3.ddc.moph.go.th%2F&:embed_code_version=3&:tabs=no&:toolbar=no&:isGuestRedirectFromVizportal=y&:display_spinner=no&:loadOrderID=0"
    driver.get(url)
    time.sleep(15)
    ss.full_Screenshot(driver, save_path=r'D:\dir\pictotext' , image_name='name.png')
    driver.close()
    driver.quit()
    return
