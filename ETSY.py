#wt-grid__item-xs-6
from selenium import webdriver
import sys, os
import time
import os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import threading
from selenium.webdriver.common.by import By
import os


def func(req):
    Map_coordinates = dict({
        "latitude": 41.8781,
        "longitude": -87.6298,
        "accuracy": 100
        })
    chrome_locale = 'locale-of-choice'
    chrome_options = Options()
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.execute_cdp_cmd("Emulation.setGeolocationOverride", Map_coordinates)

    pageH='<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><link rel="stylesheet" href="styles.css"><script src="https://kit.fontawesome.com/cabc5ad2fa.js" crossorigin="anonymous"></script><title>Hoster</title></head><body><div id="container">'
    mid=''
    pageF='</div><script src="./script.js"></script></body></html>'
    for j in range(1,2):
        link ="https://www.etsy.com/search?q="+req+f"&page={j}&geo=US"
        driver.get(link)
        
        items=driver.find_elements(by=By.CLASS_NAME, value='wt-list-unstyled')
        for i in range(len(items)):
            if("Populaire" in items[i].get_attribute('innerHTML')):
                mid=mid+"<div class='item'>"+items[i].get_attribute('innerHTML')+"</div>"
            
            
        with open('index.html','w') as f:
            f.write(pageH+mid+pageF)
req=input()
request=req.split()
req=request[0]
for i in range(1,len(request)):
    req=req+"%20"+request[i]
func(req)