from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import schedule
import time


def health_check():
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)

    driver.get("https://myclu.callutheran.edu/health-check/?_=1")


    username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="frmLogin_UserName"]')))
    password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="frmLogin_Password"]')))
    submit = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="btnLogin"]')))

    username.send_keys('username')
    password.send_keys('password')

    driver.implicitly_wait(100)
    submit.click()


    campus_status = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div[3]/div[3]/div[2]/fieldset/div[2]/div[1]/button')))
    campus_status.click()

    driver.implicitly_wait(10)

    vacc_status1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div[3]/div[4]/div[2]/fieldset[1]/div[2]/div[1]/button')))
    vacc_status2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div[3]/div[4]/div[2]/fieldset[2]/div[2]/div[2]/button')))
    vacc_status3 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div[3]/div[4]/div[2]/fieldset[3]/div[2]/div[2]/button')))

    vacc_status1.click()
    vacc_status2.click()
    vacc_status3.click()

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


# Runs Automatic Health Check Program every day at 1:00 AM
schedule.every().day.at('1:00').do(health_check)
while True:
    schedule.run_pending()
    time.sleep(1)