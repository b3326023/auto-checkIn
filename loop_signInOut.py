from selenium import webdriver
import time

acc = 'B0701221'
psw = 'Irene520'

driver = webdriver.Chrome()

#連至嘉南藥理大學網路大學網頁
driver.get('http://elearning.cnu.edu.tw/mooc/index.php')
time.sleep(2)

i = 0
while True:
<<<<<<< Updated upstream
    i += 1
=======

>>>>>>> Stashed changes
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


    #因此網站會有彈出視窗問題，故需切換視窗後繼續動作
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
<<<<<<< Updated upstream

    #一定次數後，重啟瀏覽器
    if i == 50:
        driver.close()
        driver = webdriver.Chrome()
        driver.get('http://elearning.cnu.edu.tw/mooc/index.php')
        time.sleep(2)
        i = 0

        
=======
    i += 1
    if i == 389:
        break
>>>>>>> Stashed changes
