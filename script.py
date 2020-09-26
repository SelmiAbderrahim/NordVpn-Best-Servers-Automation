#Things we need to import
from selenium import webdriver
import platform
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.keys import Keys

#headless method to hide the browser's window (True)
op = Options()
op.headless = False

#The platform.system to define the system we use
what_os = platform.system()

#Use the right browser for each system
if what_os == "Linux":
    driver = webdriver.Firefox(executable_path="linux64/geckodriver", options=op)
elif what_os == "Windows":
    driver = webdriver.Firefox(executable_path="win64/geckodriver.exe", options=op)
elif what_os == "Darwin":
    driver = webdriver.Firefox(executable_path="macos/geckodriver", options=op)

#navigate the nordvpn tools page
url = "https://nordvpn.com/servers/tools/"
driver.get(url)

#where we will save the server names
file = open("best_servers", "a")

#loop over each country
for i in range(2, 60):
    #locate the dropdown menu
    dropdown = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@role='combobox']")))
    #open the dropdown menu
    ActionChains(driver).move_to_element(dropdown).click().perform()
    time.sleep(3)


    #scroll down
    ActionChains(driver).send_keys(Keys.ARROW_DOWN).perform()
    time.sleep(2)

    #locate each country element
    country = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@role='combobox']//div[@data-id='%d']" %i)))

    #click on each country
    ActionChains(driver).move_to_element(country).click().perform()
    time.sleep(3)

    #get the name of the server
    name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//p[@class='Text micro mb-7']")))


    #save server names ina file
    file.write(name.text+"\n")

file.close()
driver.close()
