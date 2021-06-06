import time

from selenium import webdriver
driver = webdriver.Chrome(executable_path="D:\\Curs Software tester\\Softuri\\chromedriver.exe")

class Radio():

    def RadioGuru99(self):
        driver.get("http://demo.guru99.com/test/radio.html")
        radio = driver.find_elements_by_xpath("//input[@type='radio']")

        for button in radio:
            if button.is_selected():
                print("Button " + button.get_attribute("value") + " is selected")
            else:
                button.click()
                print("Button " + button.get_attribute("value") + " is selected")
                time.sleep(5)


        # radio[0].click()
        # print("Button 1 is selected")
        # time.sleep(5)
        # radio[1].click()
        # time.sleep(5)
        # print("Button 2 is selected")
        # radio[2].click()
        # print("Button 3 is selected")
        # time.sleep(5)

    def Checkbox(self):
        driver.get("http://demo.guru99.com/test/radio.html")
        box = driver.find_elements_by_xpath("//input[@type='checkbox']")

        for checkbox in box:
            if checkbox.is_selected():
                print("Button " + checkbox.get_attribute("value") + " is selected")
            else:
                checkbox.click()
                print("Button " + checkbox.get_attribute("value") + " is selected")
                time.sleep(5)





select = Radio()
select.RadioGuru99()
select.Checkbox()
driver.quit()