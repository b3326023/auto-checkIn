from selenium import webdriver
import time

acc = 'B0701221'
psw = 'Irene520'

driver = webdriver.Chrome()

driver.get('http://elearning.cnu.edu.tw/mooc/index.php')
time.sleep(2)

while True:
    btn_signin = driver.find_element_by_xpath('/html/body/div/header/div/div/div[3]/div/ul[1]/li[1]/a')
    btn_signin.click()
    time.sleep(1)

    account = driver.find_element_by_xpath('//*[@id="username"]')
    account.clear()
    account.send_keys(acc)

    password = driver.find_element_by_xpath('//*[@id="password"]')
    password.clear()
    password.send_keys(psw)

    btn_signin1 = driver.find_element_by_xpath('//*[@id="btnSignIn"]')
    btn_signin1.click()
    time.sleep(2)

    try:
        driver.switch_to_window(driver.window_handles[1])
        driver.close()
        driver.switch_to_window(driver.window_handles[0])
    except IndexError:
        print('No other windows.')
    

    driver.switch_to.frame('s_sysbar')
    btn_signout = driver.find_element_by_xpath('/html/body/div/header/div/div/div[4]/div/ul/li[3]/a')
    btn_signout.click()
    time.sleep(1)
