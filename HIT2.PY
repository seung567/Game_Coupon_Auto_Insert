from ast import Pass
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import time

coupon_list = []

with open('coupon.txt','r') as file :
    text = file.readlines()



driver1 = webdriver.Chrome()
driver1.get('https://mcoupon.nexon.com/hit2')


name = '0R700ZD10C0CI'


def auto_input(account,coupon) :

    driver1.find_element(By.ID,"eRedeemNpaCode").send_keys(account)
    driver1.find_element(By.ID,"eRedeemCoupon").send_keys(coupon)
    driver1.find_element(By.XPATH,'//*[@id="tab2"]/div[1]/button').click()

    element = WebDriverWait(driver1, 20).until(EC.presence_of_element_located((By.ID,'popAlert')))
    time.sleep(2)
    
    driver1.find_element(By.XPATH,'//*[@id="popAlert"]/div/div[3]/button').click()

    try : 
        driver1.find_element(By.XPATH,'//*[@id="afterConfirm"]/ul/li/div/ul/li').click()
        time.sleep(2)
    
        driver1.find_element(By.XPATH,'//*[@id="popConfirm"]/div/div[3]/button[2]').click()
        time.sleep(2)
        driver1.find_element(By.XPATH,'//*[@id="popAlert"]/div/div[3]/button').click()
        time.sleep(2)
        driver1.refresh()
    except :
        print(f"{coupon} // 이미사용된 쿠폰 or 오류")
        driver1.refresh()
        Pass


result_count = 0

for i in text :
    i.strip()
    result_count += 1

    print(f'{i}//{result_count}')
    i.replace('\n','')
    auto_input(name,i)