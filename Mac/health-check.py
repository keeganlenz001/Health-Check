import os
import time
from webbrowser import get
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

login_info = []

def login():
    file_path = 'data.txt'
    if os.stat(file_path).st_size == 0:
        input_username = input('Enter your username: ')
        input_password = input('Enter your password: ')
        infile = open("data.txt", "a")
        infile.write(input_username)
        infile.write("\n")
        infile.write(input_password)
        infile.close()

    login_info = []
    with open('data.txt') as infile:
            for line in infile:
                login_info.append(line)
    infile.close()


    global PATH
    PATH = os.getcwd()
    global driver
    driver = webdriver.Chrome(PATH + "/chromedriver")
    driver.get("https://myclu.callutheran.edu/health-check/?_=1")


    username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="frmLogin_UserName"]')))
    password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="frmLogin_Password"]')))
    submit = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="btnLogin"]')))

    username.send_keys(login_info[0])
    time.sleep(1)
    password.send_keys(login_info[1])
    submit.click()


def health_check():
    login()

    try:
        campus_status = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div[3]/div[3]/div[2]/fieldset/div[2]/div[1]/button')))
    except:
        driver.quit()
        print('Username or password is incorrect')
        data = open("data.txt", "w")
        data.close()
        health_check()
        

    campus_status.click()

    driver.implicitly_wait(10)
    vacc_status1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div[3]/div[4]/div[2]/fieldset[1]/div[2]/button[1]')))
    vacc_status2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div[3]/div[4]/div[2]/fieldset[2]/div[2]/button[3]')))
    vacc_status3 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div[3]/div[4]/div[2]/fieldset[3]/div[2]/button[3]')))
    vacc_status4 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div[3]/div[4]/div[2]/fieldset[4]/div[2]/button[3]')))

    vacc_status1.click()
    vacc_status2.click()
    vacc_status3.click()
    vacc_status4.click()

    box1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="confirm_mask"]')))
    box2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="confirm"]')))

    box1.click()
    box2.click()

    fname = driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div[5]/div[2]/div[3]/div[1]/label').text
    lname = driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div[5]/div[2]/div[3]/div[2]/label').text

    fbox = driver.find_element_by_xpath('//*[@id="signature_first_name"]')
    lbox = driver.find_element_by_xpath('//*[@id="signature_last_name"]')

    fbox.send_keys(fname)
    lbox.send_keys(lname)

    check = driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div[7]/button')
    check.click()
    driver.quit()

if __name__ == '__main__':
    health_check()