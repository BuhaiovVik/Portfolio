import unittest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
import AllureReports
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException as WDE
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service
from selenium.webdriver.chrome.options import Options
from faker import Faker
import random
import pickle
import helper as H

fake = Faker()


class Chrome(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def test1_fept_001_max(self):
        driver = self.driver
        driver.get("https://internxt.com/temporary-email")
        wait = WebDriverWait(driver, 50)

        # Get email
        time.sleep(2)
        driver.find_element(By.XPATH, "//p[contains(text(),'Copy email')]").click()

        # Prada registration part 1
        driver.switch_to.new_window('tab')
        driver.get("https://www.prada.com/us/en.html")
        driver.find_element(By.XPATH, "//div[@class='banner_cta cta_accept'][contains(.,'ACCEPT ALL')]").click()
        driver.find_element(By.XPATH, "//span[contains(@class,'utils__icon pr-icon-new-login')]").click()
        wait.until(EC.visibility_of_element_located((By.ID, "gigya-textbox-100719189608483120")))
        driver.find_element(By.ID, "gigya-textbox-100719189608483120").send_keys(Keys.CONTROL + "v")
        driver.find_element(By.XPATH, "//input[contains(@value,'Next')]").click()
        time.sleep(10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Resend')]")))

        # Get verification code
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(10)
        driver.refresh()
        mail = driver.find_element(By.XPATH, H.mail_scroll)
        driver.execute_script("arguments[0].scrollIntoView(true)", mail)
        wait.until(EC.element_to_be_clickable((By.XPATH, H.mail_confirm)))
        driver.find_element(By.XPATH, H.mail_confirm).click()
        time.sleep(1)
        code = driver.find_element(By.XPATH, "//tbody/tr[3]/td[1]").text
        print("User received mail with verification code")

        # Prada registration part 2
        driver.switch_to.window(driver.window_handles[1])
        driver.find_element(By.XPATH, '//*[@placeholder="Verification code*"]').send_keys(code)
        driver.find_element(By.XPATH, H.drop_down).click()
        driver.find_element(By.ID, "gigya-textbox-105760616358098000").send_keys(H.f_name)
        driver.find_element(By.ID, "gigya-textbox-21007040083017830").send_keys(H.l_name)
        driver.find_element(By.ID, "gigya-textbox-74329674452397740").send_keys(H.mm_dd)
        driver.find_element(By.ID, "gigya-password-60262223393983710").send_keys(H.password)
        driver.find_element(By.ID, "visibleTextMarketing").click()
        driver.find_element(By.XPATH, "//input[@value='Register']").click()
        print("Verification code was correct")

        # Registration validation
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(@class,'utils__icon pr-icon-new-bag')]")))
        try:
            title_check = driver.title == "Prada Official Website | Thinking fashion since 1913 | PRADA"
            print("Title is correct!")
        except WDE:
            print("Incorrect title!")
        print("Account was successful created")

        # Opening the address form menu
        driver.find_element(By.XPATH, H.log_icon).click()
        driver.find_element(By.XPATH, H.address_dd).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Personal information')]")))
        try:
            title_check = driver.title == H.address_title
            print("Title is correct!")
        except WDE:
            print("Incorrect title!")
        driver.find_element(By.XPATH, '//*[contains(text(),"Add new shipping address")]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h3[contains(text(),'Shipping address')]")))
        driver.find_element(By.XPATH, "//input[contains(@id,'first_name_')]").send_keys(H.f_name)
        driver.find_element(By.XPATH, "//input[contains(@id,'last_name_')]").send_keys(H.l_name)
        driver.find_element(By.XPATH, "//input[contains(@id,'company_')]").send_keys(H.company)
        time.sleep(3)
        driver.find_element(By.XPATH, H.address_1).send_keys(H.add)
        driver.find_element(By.XPATH, "//input[contains(@id,'city_')]").send_keys(H.city)
        driver.find_element(By.XPATH, H.state_dd).click()
        scroll_to_state = driver.find_element(By.XPATH, H.state_city)
        driver.execute_script("arguments[0].scrollIntoView(true)", scroll_to_state)
        time.sleep(1)
        driver.find_element(By.XPATH, H.state_city).click()
        driver.find_element(By.XPATH, "//input[contains(@id,'zip_code_')]").send_keys(H.zip_code)
        driver.find_element(By.XPATH, "//input[contains(@id,'phone_')]").send_keys(H.phone)
        driver.find_element(By.XPATH, H.check_box).click()
        driver.find_element(By.XPATH, H.confirm).click()
        time.sleep(1)
        driver.find_element(By.XPATH, H.confirm_2).click()

        time.sleep(3)
        # Shipping and billing addresses verification
        shipp = driver.find_element(By.XPATH, H.ship_address).text
        bill = driver.find_element(By.XPATH, H.bill_address).text
        try:
            address_check = shipp == bill
            print("Shipping and billing addresses are correct!")
        except WDE:
            print("Shipping and billing addresses are incorrect!")
        print("Address was successful created")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(AllureReports)
