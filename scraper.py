from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from bs4 import BeautifulSoup
import pandas as pd
import time
import re
import requests



# Creating Instance
chrome_options = webdriver.ChromeOptions()

# Working with the 'add_argument' Method to modify Driver Default Notification
chrome_options.add_argument('--disable-notifications')

driver = webdriver.Chrome("C:/Users/Admin/Downloads/chrome-win64/chrome-win64", options= chrome_options)
driver.maximize_window()
wait = WebDriverWait(driver, 10)  # 10-second maximum wait time

driver.get('https://www.facebook.com/')

email = wait.until(EC.presence_of_element_located((By.NAME, "email")))
email.send_keys("dali.uchiha")

password = driver.find_element(By.NAME, "pass")
password.send_keys("sasukeJbari0000")

login_button = driver.find_element(By.XPATH, "//button[@name='login']")
login_button.click()

time.sleep(3)

first_time = 1
links = []
top = '603953925268682'
last_messaged = ''

while True:

    print("start")
    driver.get('https://www.facebook.com/marketplace/category/vehicles?sortBy=creation_time_descend&exact=false')



    """if first_time:
        first = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href^="/marketplace/item"]')))
        top = first.get_attribute('href').split("/")[-2]
        first_time = 0
        """
    repeat = 1

    while repeat:
        
        
        for _ in range(3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        matching_links = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a[href^="/marketplace/item"]')))
        
        time.sleep(1)

        i = 0
        
        for link in matching_links:
            i += 1
            href = link.get_attribute('href')
            
            link_href = link.get_attribute('href')
            links.append(link_href)
            if top == href.split("/")[-2] :
                print("Found the top link!")
                top = matching_links[0].get_attribute('href').split("/")[-2]
                print(top)
                repeat = 0
                break
            
    if repeat == 1:
        top = last_messaged

    for link in links[::-1]:
        
        if last_messaged != link.split("/")[-2] :
            #open new window 
            driver.execute_script("window.open('', '_blank');")
            driver.switch_to.window(driver.window_handles[1])
            print(link)
            driver.get(link)

            name = driver.find_element('tag name', 'h1').text
            print(name)

            with open('phrases.txt', 'r') as file:
                phrases = [line.strip() for line in file.readlines()]
        

            matching_phrases = [phrase for phrase in phrases if phrase in name]

            if not matching_phrases :
                wait = WebDriverWait(driver, 10)  # You can adjust the timeout as needed

                soup = BeautifulSoup(driver.page_source, 'html.parser')
                all_pc = soup.find_all('div', attrs={'id': re.compile("^mount_0_0_")})
                id_ = str(all_pc[0].get('id'))
                xpath = '//*[@id="' + id_ + '"]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/div/div[3]/div/div/span/div/div/span/div/div/div[1]/div'
                post = driver.find_element(By.XPATH, xpath)
                post.click()





                '''x_coordinate = 1350
                y_coordinate = 800
                

                # Use JavaScript to perform an action using the coordinates
                js_script = f"window.scrollTo({x_coordinate}, {600});"
                driver.execute_script(js_script)

                time.sleep(1)
                # Perform any desired action at the specified coordinates
                #  click at those coordinates
                action = ActionChains(driver)
                action.move_by_offset(x_coordinate, y_coordinate)
                action.context_click()
                action.perform()


                print('im here')'''
                time.sleep(5)



                '''
                #####################
                # send message here #
                #####################
                div_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[aria-label="Envoyer un message"]')))
                div_element.click()

                # Find the label element by aria-label and click it
                label_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'label[aria-label="Veuillez entrer votre message pour le vendeur"]')))
                label_element.click()

                # Locate the input field associated with the label and send keys
                input_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[aria-label="Veuillez entrer votre message pour le vendeur"]')))
                time.sleep(1)
                actions = ActionChains(driver)

                # Simulate typing in the input field
                actions.click(input_field)
                actions.send_keys("ahla, b9adeh ?")
                actions.send_keys(Keys.ENTER)  # Simulate pressing the Enter key
                actions.perform()'''

                
            

            last_messaged = link.split("/")[-2]


        
        

    

              
    time.sleep(60)    

    

        


    
            



