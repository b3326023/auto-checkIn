from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

class AutoClockIn():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://eadm.ncku.edu.tw/welldoc/ncku/iftwd/signIn.php")

    def keyIn(self):
        myID = '10708048'
        myPSW = '3326023Ab'
        Account = self.driver.find_element_by_name('psnCode')
        Account.clear()
        Account.send_keys(myID)

        Password = self.driver.find_element_by_name('password')
        Password.clear()
        Password.send_keys(myPSW)

    def signIn(self):
        btn_signin = self.driver.find_element_by_xpath("//button[contains(.,'上班簽到')]")
        btn_signin.click()

    def signOut(self):
        btn_signout = self.driver.find_element_by_xpath("//button[contains(.,'下班簽退')]")
        btn_signout.click()

    def viewRecord(self):
        btn_signout = self.driver.find_element_by_xpath("//button[contains(.,'查看本日刷卡紀錄')]")
        btn_signout.click()
    
    def close(self):
        self.driver.close()
