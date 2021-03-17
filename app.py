from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys 

argument = sys.argv[1]

def Config(name):
    description = input("enter the description:")

    driver = webdriver.Firefox("D:\\Programing\\Python\\Automation\\GitHub_Automation")
    driver.get("https://github.com/")

    driver.find_element_by_xpath("/html/body/div[1]/header/div/div[2]/div[2]/a[1]").click()


    input1 = driver.find_element_by_xpath("//*[@id=\"login_field\"]")
    input1.send_keys("snehashish090")

    input2 = driver.find_element_by_id("password")
    input2.send_keys("snehashish08036")

    button1 = driver.find_element_by_xpath("/html/body/div[3]/main/div/div[4]/form/div/input[12]").click()

    button2 = driver.find_element_by_xpath("/html/body/div[4]/div/aside[1]/div[2]/div[2]/div/h2/a").click()

    input3 = driver.find_element_by_xpath("//*[@id=\"repository_name\"]")
    input3.send_keys(name)

    input4 = driver.find_element_by_xpath("//*[@id=\"repository_description\"]")
    input4.send_keys(description)

    input5 = driver.find_element_by_xpath("//*[@id=\"repository_auto_init\"]").click()

    driver.find_element_by_xpath("/html/body/div[4]/main/div/form/div[4]/button").click()

    driver.find_element_by_xpath("/html/body/div[4]/main/div/form/div[4]/button").click()

    
Config(argument) 
 


