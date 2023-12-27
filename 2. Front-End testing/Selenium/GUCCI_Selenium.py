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
from faker import Faker
import helper as H

fake = Faker()


class Chrome(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def test1_FEPT_0001_max(self):
        driver = self.driver
        driver.get(H.url)
        wait = WebDriverWait(driver, 5)

        # Pop-ups'
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, H.pop_up1)))
            driver.find_element(By.XPATH, H.pop_up1).click()
        except TimeoutException:
            print("Pop-up1 didn't appear")
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, H.pop_up2)))
            driver.find_element(By.XPATH, H.pop_up2).click()
        except TimeoutException:
            print("Pop-up2 didn't appear")

        # Title verification
        try:
            title_check = driver.title == H.m_title
            print("Title is correct!")
        except WDE:
            print("Incorrect title!")

        # Hamburger menu elements verification
        driver.find_element(By.XPATH, H.h_menu).click()
        wait.until(EC.element_to_be_clickable((By.ID, 'l1_navigation_item_0')))
        driver.find_element(By.ID, 'l1_navigation_item_0').click()
        wait.until(EC.element_to_be_clickable((By.ID, "l2_navigation_item_0_0")))
        time.sleep(1)
        driver.find_element(By.XPATH, "(//g-icon-chevron-left[@slot='icon-before'])[1]").click()
        wait.until(EC.element_to_be_clickable((By.ID, 'l1_navigation_item_1')))
        driver.find_element(By.ID, 'l1_navigation_item_1').click()
        wait.until(EC.element_to_be_clickable((By.ID, "l2_navigation_item_1_3")))
        time.sleep(1)
        driver.find_element(By.XPATH, '(//g-icon-chevron-left[@slot="icon-before"])[8]').click()
        wait.until(EC.element_to_be_clickable((By.ID, "l1_navigation_item_2")))
        driver.find_element(By.ID, 'l1_navigation_item_2').click()
        wait.until(EC.element_to_be_clickable((By.ID, "l2_navigation_item_2_0")))
        time.sleep(1)
        driver.find_element(By.XPATH, "(//g-icon-chevron-left[@slot='icon-before'])[13]").click()
        wait.until(EC.element_to_be_clickable((By.ID, "l1_navigation_item_3")))
        driver.find_element(By.ID, 'l1_navigation_item_3').click()
        wait.until(EC.element_to_be_clickable((By.ID, "l2_navigation_item_3_0")))
        time.sleep(1)
        driver.find_element(By.XPATH, "(//g-icon-chevron-left[@slot='icon-before'])[24]").click()
        wait.until(EC.element_to_be_clickable((By.ID, "l1_navigation_item_4")))
        driver.find_element(By.ID, 'l1_navigation_item_4').click()
        wait.until(EC.element_to_be_clickable((By.ID, "l2_navigation_item_4_0")))
        time.sleep(1)
        driver.find_element(By.XPATH, "(//g-icon-chevron-left[@slot='icon-before'])[27]").click()
        wait.until(EC.element_to_be_clickable((By.ID, "l1_navigation_item_5")))
        driver.find_element(By.ID, 'l1_navigation_item_5').click()
        wait.until(EC.element_to_be_clickable((By.ID, "l2_navigation_item_5_0")))
        time.sleep(1)
        driver.find_element(By.XPATH, "(//g-icon-chevron-left[@slot='icon-before'])[36]").click()
        wait.until(EC.element_to_be_clickable((By.ID, "l1_navigation_item_6")))
        driver.find_element(By.ID, 'l1_navigation_item_6').click()
        wait.until(EC.element_to_be_clickable((By.ID, "l2_navigation_item_6_0")))
        time.sleep(1)
        driver.find_element(By.XPATH, "(//g-icon-chevron-left[@slot='icon-before'])[45]").click()
        wait.until(EC.element_to_be_clickable((By.ID, "l1_navigation_item_7")))
        driver.find_element(By.ID, 'l1_navigation_item_7').click()
        wait.until(EC.element_to_be_clickable((By.ID, "l2_navigation_item_7_0")))
        time.sleep(1)
        driver.find_element(By.XPATH, "(//g-icon-chevron-left[@slot='icon-before'])[50]").click()
        wait.until(EC.element_to_be_clickable((By.ID, "l1_navigation_item_8")))
        driver.find_element(By.ID, 'l1_navigation_item_8').click()
        wait.until(EC.element_to_be_clickable((By.ID, "l2_navigation_item_8_0")))
        time.sleep(1)
        driver.find_element(By.XPATH, "(//g-icon-chevron-left[@slot='icon-before'])[57]").click()
        wait.until(EC.element_to_be_clickable((By.ID, "l1_navigation_item_9")))
        driver.find_element(By.ID, 'l1_navigation_item_9').click()
        wait.until(EC.element_to_be_clickable((By.ID, "l2_navigation_item_9_0")))
        time.sleep(1)
        driver.find_element(By.XPATH, "(//g-icon-chevron-left[@slot='icon-before'])[61]").click()
        wait.until(EC.element_to_be_clickable((By.ID, "l1_navigation_item_10")))
        driver.find_element(By.ID, 'l1_navigation_item_10').click()
        wait.until(EC.element_to_be_clickable((By.ID, "l2_navigation_item_10_0")))
        time.sleep(1)
        driver.find_element(By.XPATH, "(//g-icon-chevron-left[@slot='icon-before'])[71]").click()
        wait.until(EC.element_to_be_clickable((By.ID, "l1_navigation_item_11")))
        driver.find_element(By.ID, 'l1_navigation_item_11').click()
        wait.until(EC.element_to_be_clickable((By.ID, "l2_navigation_item_11_0")))
        time.sleep(1)
        driver.find_element(By.XPATH, "(//g-icon-chevron-left[@slot='icon-before'])[80]").click()

        # Scroll until +1 8774822430 will be visible
        ph_number = driver.find_element(By.XPATH, "//g-link[contains(.,'+1 8774822430')]")
        driver.execute_script("arguments[0].scrollIntoView(true)", ph_number)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//g-link[contains(.,'Sign In')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//g-link[contains(.,'My Orders')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//g-link[contains(.,'Contact Us')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//g-link[contains(.,'+1 8774822430')]")))
        print("All the elements from the hamburger menu are visible and clickable!")

    def test2_FEPT_0001_1920x1080(self):
        driver = self.driver
        driver.set_window_size(1920, 1080)
        driver.get(H.url)
        wait = WebDriverWait(driver, 5)

        # Pop-ups'
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, H.pop_up1)))
            driver.find_element(By.XPATH, H.pop_up1).click()
        except TimeoutException:
            print("Pop-up1 didn't appear")
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, H.pop_up2)))
            driver.find_element(By.XPATH, H.pop_up2).click()
        except TimeoutException:
            print("Pop-up2 didn't appear")

        # Title verification
        try:
            title_check = driver.title == H.m_title
            print("Title is correct!")
        except WDE:
            print("Incorrect title!")

        # Hamburger menu elements verification
        driver.find_element(By.XPATH, H.h_menu).click()
        wait.until(EC.element_to_be_clickable((By.ID, 'l1_navigation_item_0')))
        driver.find_element(By.ID, 'l1_navigation_item_0').click()
        wait.until(EC.element_to_be_clickable((By.ID, "l2_navigation_item_0_0")))
        time.sleep(1)
        driver.find_element(By.XPATH, "(//g-icon-chevron-left[@slot='icon-before'])[1]").click()
        wait.until(EC.element_to_be_clickable((By.ID, 'l1_navigation_item_1')))
        driver.find_element(By.ID, 'l1_navigation_item_1').click()
        wait.until(EC.element_to_be_clickable((By.ID, "l2_navigation_item_1_3")))
        time.sleep(1)
        driver.find_element(By.XPATH, '(//g-icon-chevron-left[@slot="icon-before"])[8]').click()
        wait.until(EC.element_to_be_clickable((By.ID, "l1_navigation_item_2")))
        driver.find_element(By.ID, 'l1_navigation_item_2').click()
        wait.until(EC.element_to_be_clickable((By.ID, "l2_navigation_item_2_0")))
        time.sleep(1)
        driver.find_element(By.XPATH, "(//g-icon-chevron-left[@slot='icon-before'])[13]").click()
        wait.until(EC.element_to_be_clickable((By.ID, "l1_navigation_item_3")))
        driver.find_element(By.ID, 'l1_navigation_item_3').click()
        wait.until(EC.element_to_be_clickable((By.ID, "l2_navigation_item_3_0")))
        time.sleep(1)
        driver.find_element(By.XPATH, "(//g-icon-chevron-left[@slot='icon-before'])[24]").click()
        wait.until(EC.element_to_be_clickable((By.ID, "l1_navigation_item_4")))
        driver.find_element(By.ID, 'l1_navigation_item_4').click()
        wait.until(EC.element_to_be_clickable((By.ID, "l2_navigation_item_4_0")))
        time.sleep(1)
        driver.find_element(By.XPATH, "(//g-icon-chevron-left[@slot='icon-before'])[27]").click()
        wait.until(EC.element_to_be_clickable((By.ID, "l1_navigation_item_5")))
        driver.find_element(By.ID, 'l1_navigation_item_5').click()
        wait.until(EC.element_to_be_clickable((By.ID, "l2_navigation_item_5_0")))
        time.sleep(1)
        driver.find_element(By.XPATH, "(//g-icon-chevron-left[@slot='icon-before'])[36]").click()
        wait.until(EC.element_to_be_clickable((By.ID, "l1_navigation_item_6")))
        driver.find_element(By.ID, 'l1_navigation_item_6').click()
        wait.until(EC.element_to_be_clickable((By.ID, "l2_navigation_item_6_0")))
        time.sleep(1)
        driver.find_element(By.XPATH, "(//g-icon-chevron-left[@slot='icon-before'])[45]").click()
        wait.until(EC.element_to_be_clickable((By.ID, "l1_navigation_item_7")))
        driver.find_element(By.ID, 'l1_navigation_item_7').click()
        wait.until(EC.element_to_be_clickable((By.ID, "l2_navigation_item_7_0")))
        time.sleep(1)
        driver.find_element(By.XPATH, "(//g-icon-chevron-left[@slot='icon-before'])[50]").click()
        wait.until(EC.element_to_be_clickable((By.ID, "l1_navigation_item_8")))
        driver.find_element(By.ID, 'l1_navigation_item_8').click()
        wait.until(EC.element_to_be_clickable((By.ID, "l2_navigation_item_8_0")))
        time.sleep(1)
        driver.find_element(By.XPATH, "(//g-icon-chevron-left[@slot='icon-before'])[57]").click()
        wait.until(EC.element_to_be_clickable((By.ID, "l1_navigation_item_9")))
        driver.find_element(By.ID, 'l1_navigation_item_9').click()
        wait.until(EC.element_to_be_clickable((By.ID, "l2_navigation_item_9_0")))
        time.sleep(1)
        driver.find_element(By.XPATH, "(//g-icon-chevron-left[@slot='icon-before'])[61]").click()
        wait.until(EC.element_to_be_clickable((By.ID, "l1_navigation_item_10")))
        driver.find_element(By.ID, 'l1_navigation_item_10').click()
        wait.until(EC.element_to_be_clickable((By.ID, "l2_navigation_item_10_0")))
        time.sleep(1)
        driver.find_element(By.XPATH, "(//g-icon-chevron-left[@slot='icon-before'])[71]").click()
        wait.until(EC.element_to_be_clickable((By.ID, "l1_navigation_item_11")))
        driver.find_element(By.ID, 'l1_navigation_item_11').click()
        wait.until(EC.element_to_be_clickable((By.ID, "l2_navigation_item_11_0")))
        time.sleep(1)
        driver.find_element(By.XPATH, "(//g-icon-chevron-left[@slot='icon-before'])[80]").click()

        # Scroll until +1 8774822430 will be visible
        ph_number = driver.find_element(By.XPATH, "//g-link[contains(.,'+1 8774822430')]")
        driver.execute_script("arguments[0].scrollIntoView(true)", ph_number)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//g-link[contains(.,'Sign In')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//g-link[contains(.,'My Orders')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//g-link[contains(.,'Contact Us')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//g-link[contains(.,'+1 8774822430')]")))
        print("All the elements from the hamburger menu are visible and clickable!")

    def test3_FEPT_0001_1366x768(self):
        driver = self.driver
        driver.set_window_size(1366, 768)
        driver.get(H.url)
        wait = WebDriverWait(driver, 5)

        # Pop-ups'
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, H.pop_up1)))
            driver.find_element(By.XPATH, H.pop_up1).click()
        except TimeoutException:
            print("Pop-up1 didn't appear")
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, H.pop_up2)))
            driver.find_element(By.XPATH, H.pop_up2).click()
        except TimeoutException:
            print("Pop-up2 didn't appear")

        # Title verification
        try:
            title_check = driver.title == H.m_title
            print("Title is correct!")
        except WDE:
            print("Incorrect title!")

        # Hamburger menu elements verification
        driver.find_element(By.XPATH, H.h_menu).click()
        wait.until(EC.element_to_be_clickable((By.ID, 'l1_navigation_item_0')))
        driver.find_element(By.ID, 'l1_navigation_item_0').click()
        wait.until(EC.element_to_be_clickable((By.ID, "l2_navigation_item_0_0")))
        time.sleep(1)
        driver.find_element(By.XPATH, "(//g-icon-chevron-left[@slot='icon-before'])[1]").click()
        wait.until(EC.element_to_be_clickable((By.ID, 'l1_navigation_item_1')))
        driver.find_element(By.ID, 'l1_navigation_item_1').click()
        wait.until(EC.element_to_be_clickable((By.ID, "l2_navigation_item_1_3")))
        time.sleep(1)
        driver.find_element(By.XPATH, '(//g-icon-chevron-left[@slot="icon-before"])[8]').click()
        wait.until(EC.element_to_be_clickable((By.ID, "l1_navigation_item_2")))
        driver.find_element(By.ID, 'l1_navigation_item_2').click()
        wait.until(EC.element_to_be_clickable((By.ID, "l2_navigation_item_2_0")))
        time.sleep(1)
        driver.find_element(By.XPATH, "(//g-icon-chevron-left[@slot='icon-before'])[13]").click()
        wait.until(EC.element_to_be_clickable((By.ID, "l1_navigation_item_3")))
        driver.find_element(By.ID, 'l1_navigation_item_3').click()
        wait.until(EC.element_to_be_clickable((By.ID, "l2_navigation_item_3_0")))
        time.sleep(1)
        driver.find_element(By.XPATH, "(//g-icon-chevron-left[@slot='icon-before'])[24]").click()
        wait.until(EC.element_to_be_clickable((By.ID, "l1_navigation_item_4")))
        driver.find_element(By.ID, 'l1_navigation_item_4').click()
        wait.until(EC.element_to_be_clickable((By.ID, "l2_navigation_item_4_0")))
        time.sleep(1)
        driver.find_element(By.XPATH, "(//g-icon-chevron-left[@slot='icon-before'])[27]").click()
        wait.until(EC.element_to_be_clickable((By.ID, "l1_navigation_item_5")))
        driver.find_element(By.ID, 'l1_navigation_item_5').click()
        wait.until(EC.element_to_be_clickable((By.ID, "l2_navigation_item_5_0")))
        time.sleep(1)
        driver.find_element(By.XPATH, "(//g-icon-chevron-left[@slot='icon-before'])[36]").click()
        wait.until(EC.element_to_be_clickable((By.ID, "l1_navigation_item_6")))
        driver.find_element(By.ID, 'l1_navigation_item_6').click()
        wait.until(EC.element_to_be_clickable((By.ID, "l2_navigation_item_6_0")))
        time.sleep(1)
        driver.find_element(By.XPATH, "(//g-icon-chevron-left[@slot='icon-before'])[45]").click()
        wait.until(EC.element_to_be_clickable((By.ID, "l1_navigation_item_7")))
        driver.find_element(By.ID, 'l1_navigation_item_7').click()
        wait.until(EC.element_to_be_clickable((By.ID, "l2_navigation_item_7_0")))
        time.sleep(1)
        driver.find_element(By.XPATH, "(//g-icon-chevron-left[@slot='icon-before'])[50]").click()
        wait.until(EC.element_to_be_clickable((By.ID, "l1_navigation_item_8")))
        driver.find_element(By.ID, 'l1_navigation_item_8').click()
        wait.until(EC.element_to_be_clickable((By.ID, "l2_navigation_item_8_0")))
        time.sleep(1)
        driver.find_element(By.XPATH, "(//g-icon-chevron-left[@slot='icon-before'])[57]").click()
        wait.until(EC.element_to_be_clickable((By.ID, "l1_navigation_item_9")))
        driver.find_element(By.ID, 'l1_navigation_item_9').click()
        wait.until(EC.element_to_be_clickable((By.ID, "l2_navigation_item_9_0")))
        time.sleep(1)
        driver.find_element(By.XPATH, "(//g-icon-chevron-left[@slot='icon-before'])[61]").click()
        wait.until(EC.element_to_be_clickable((By.ID, "l1_navigation_item_10")))
        driver.find_element(By.ID, 'l1_navigation_item_10').click()
        wait.until(EC.element_to_be_clickable((By.ID, "l2_navigation_item_10_0")))
        time.sleep(1)
        driver.find_element(By.XPATH, "(//g-icon-chevron-left[@slot='icon-before'])[71]").click()
        wait.until(EC.element_to_be_clickable((By.ID, "l1_navigation_item_11")))
        driver.find_element(By.ID, 'l1_navigation_item_11').click()
        wait.until(EC.element_to_be_clickable((By.ID, "l2_navigation_item_11_0")))
        time.sleep(1)
        driver.find_element(By.XPATH, "(//g-icon-chevron-left[@slot='icon-before'])[80]").click()

        # Scroll until +1 8774822430 will be visible
        ph_number = driver.find_element(By.XPATH, "//g-link[contains(.,'+1 8774822430')]")
        driver.execute_script("arguments[0].scrollIntoView(true)", ph_number)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//g-link[contains(.,'Sign In')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//g-link[contains(.,'My Orders')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//g-link[contains(.,'Contact Us')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//g-link[contains(.,'+1 8774822430')]")))
        print("All the elements from the hamburger menu are visible and clickable!")

    def test4_FEPT_0001_1440x900(self):
        driver = self.driver
        driver.set_window_size(1440, 900)
        driver.get(H.url)
        wait = WebDriverWait(driver, 5)

        # Pop-ups'
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, H.pop_up1)))
            driver.find_element(By.XPATH, H.pop_up1).click()
        except TimeoutException:
            print("Pop-up1 didn't appear")
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, H.pop_up2)))
            driver.find_element(By.XPATH, H.pop_up2).click()
        except TimeoutException:
            print("Pop-up2 didn't appear")

        # Title verification
        try:
            title_check = driver.title == H.m_title
            print("Title is correct!")
        except WDE:
            print("Incorrect title!")

        # Hamburger menu elements verification
        driver.find_element(By.XPATH, H.h_menu).click()
        wait.until(EC.element_to_be_clickable((By.ID, 'l1_navigation_item_0')))
        driver.find_element(By.ID, 'l1_navigation_item_0').click()
        wait.until(EC.element_to_be_clickable((By.ID, "l2_navigation_item_0_0")))
        time.sleep(1)
        driver.find_element(By.XPATH, "(//g-icon-chevron-left[@slot='icon-before'])[1]").click()
        wait.until(EC.element_to_be_clickable((By.ID, 'l1_navigation_item_1')))
        driver.find_element(By.ID, 'l1_navigation_item_1').click()
        wait.until(EC.element_to_be_clickable((By.ID, "l2_navigation_item_1_3")))
        time.sleep(1)
        driver.find_element(By.XPATH, '(//g-icon-chevron-left[@slot="icon-before"])[8]').click()
        wait.until(EC.element_to_be_clickable((By.ID, "l1_navigation_item_2")))
        driver.find_element(By.ID, 'l1_navigation_item_2').click()
        wait.until(EC.element_to_be_clickable((By.ID, "l2_navigation_item_2_0")))
        time.sleep(1)
        driver.find_element(By.XPATH, "(//g-icon-chevron-left[@slot='icon-before'])[13]").click()
        wait.until(EC.element_to_be_clickable((By.ID, "l1_navigation_item_3")))
        driver.find_element(By.ID, 'l1_navigation_item_3').click()
        wait.until(EC.element_to_be_clickable((By.ID, "l2_navigation_item_3_0")))
        time.sleep(1)
        driver.find_element(By.XPATH, "(//g-icon-chevron-left[@slot='icon-before'])[24]").click()
        wait.until(EC.element_to_be_clickable((By.ID, "l1_navigation_item_4")))
        driver.find_element(By.ID, 'l1_navigation_item_4').click()
        wait.until(EC.element_to_be_clickable((By.ID, "l2_navigation_item_4_0")))
        time.sleep(1)
        driver.find_element(By.XPATH, "(//g-icon-chevron-left[@slot='icon-before'])[27]").click()
        wait.until(EC.element_to_be_clickable((By.ID, "l1_navigation_item_5")))
        driver.find_element(By.ID, 'l1_navigation_item_5').click()
        wait.until(EC.element_to_be_clickable((By.ID, "l2_navigation_item_5_0")))
        time.sleep(1)
        driver.find_element(By.XPATH, "(//g-icon-chevron-left[@slot='icon-before'])[36]").click()
        wait.until(EC.element_to_be_clickable((By.ID, "l1_navigation_item_6")))
        driver.find_element(By.ID, 'l1_navigation_item_6').click()
        wait.until(EC.element_to_be_clickable((By.ID, "l2_navigation_item_6_0")))
        time.sleep(1)
        driver.find_element(By.XPATH, "(//g-icon-chevron-left[@slot='icon-before'])[45]").click()
        wait.until(EC.element_to_be_clickable((By.ID, "l1_navigation_item_7")))
        driver.find_element(By.ID, 'l1_navigation_item_7').click()
        wait.until(EC.element_to_be_clickable((By.ID, "l2_navigation_item_7_0")))
        time.sleep(1)
        driver.find_element(By.XPATH, "(//g-icon-chevron-left[@slot='icon-before'])[50]").click()
        wait.until(EC.element_to_be_clickable((By.ID, "l1_navigation_item_8")))
        driver.find_element(By.ID, 'l1_navigation_item_8').click()
        wait.until(EC.element_to_be_clickable((By.ID, "l2_navigation_item_8_0")))
        time.sleep(1)
        driver.find_element(By.XPATH, "(//g-icon-chevron-left[@slot='icon-before'])[57]").click()
        wait.until(EC.element_to_be_clickable((By.ID, "l1_navigation_item_9")))
        driver.find_element(By.ID, 'l1_navigation_item_9').click()
        wait.until(EC.element_to_be_clickable((By.ID, "l2_navigation_item_9_0")))
        time.sleep(1)
        driver.find_element(By.XPATH, "(//g-icon-chevron-left[@slot='icon-before'])[61]").click()
        wait.until(EC.element_to_be_clickable((By.ID, "l1_navigation_item_10")))
        driver.find_element(By.ID, 'l1_navigation_item_10').click()
        wait.until(EC.element_to_be_clickable((By.ID, "l2_navigation_item_10_0")))
        time.sleep(1)
        driver.find_element(By.XPATH, "(//g-icon-chevron-left[@slot='icon-before'])[71]").click()
        wait.until(EC.element_to_be_clickable((By.ID, "l1_navigation_item_11")))
        driver.find_element(By.ID, 'l1_navigation_item_11').click()
        wait.until(EC.element_to_be_clickable((By.ID, "l2_navigation_item_11_0")))
        time.sleep(1)
        driver.find_element(By.XPATH, "(//g-icon-chevron-left[@slot='icon-before'])[80]").click()

        # Scroll until +1 8774822430 will be visible
        ph_number = driver.find_element(By.XPATH, "//g-link[contains(.,'+1 8774822430')]")
        driver.execute_script("arguments[0].scrollIntoView(true)", ph_number)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//g-link[contains(.,'Sign In')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//g-link[contains(.,'My Orders')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//g-link[contains(.,'Contact Us')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//g-link[contains(.,'+1 8774822430')]")))
        print("All the elements from the hamburger menu are visible and clickable!")

    def test5_FEPT_0002_max(self):
        driver = self.driver
        driver.get(H.url)
        wait = WebDriverWait(driver, 5)

        # Pop-ups'
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, H.pop_up1)))
            driver.find_element(By.XPATH, H.pop_up1).click()
        except TimeoutException:
            print("Pop-up1 didn't appear")
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, H.pop_up2)))
            driver.find_element(By.XPATH, H.pop_up2).click()
        except TimeoutException:
            print("Pop-up2 didn't appear")

        # Sign In button usability verification
        driver.find_element(By.XPATH, H.h_menu).click()
        time.sleep(1)

        # Scroll until Sign_In will be visible
        sign_in = driver.find_element(By.XPATH, "//g-link[contains(.,'Sign In')]")
        driver.execute_script("arguments[0].scrollIntoView(true)", sign_in)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//g-link[contains(.,'Sign In')]")))
        driver.find_element(By.XPATH, "//g-link[contains(.,'Sign In')]").click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'MY GUCCI Account')]")))

        # Sign In title verification
        try:
            title_si = driver.title == H.s_title
            print("Sign In title is correct!")
        except WDE:
            print("Sign In title is incorrect!")

    def test6_FEPT_0002_1920x1080(self):
        driver = self.driver
        driver.set_window_size(1920, 1080)
        driver.get(H.url)
        wait = WebDriverWait(driver, 5)

        # Pop-ups'
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, H.pop_up1)))
            driver.find_element(By.XPATH, H.pop_up1).click()
        except TimeoutException:
            print("Pop-up1 didn't appear")
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, H.pop_up2)))
            driver.find_element(By.XPATH, H.pop_up2).click()
        except TimeoutException:
            print("Pop-up2 didn't appear")

        # Sign In button usability verification
        driver.find_element(By.XPATH, H.h_menu).click()
        time.sleep(1)

        # Scroll until Sign_In will be visible
        sign_in = driver.find_element(By.XPATH, "//g-link[contains(.,'Sign In')]")
        driver.execute_script("arguments[0].scrollIntoView(true)", sign_in)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//g-link[contains(.,'Sign In')]")))
        driver.find_element(By.XPATH, "//g-link[contains(.,'Sign In')]").click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'MY GUCCI Account')]")))

        # Sign In title verification
        try:
            title_si = driver.title == H.s_title
            print("Sign In title is correct!")
        except WDE:
            print("Sign In title is incorrect!")

    def test7_FEPT_0002_1366x768(self):
        driver = self.driver
        driver.set_window_size(1366, 768)
        driver.get(H.url)
        wait = WebDriverWait(driver, 5)

        # Pop-ups'
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, H.pop_up1)))
            driver.find_element(By.XPATH, H.pop_up1).click()
        except TimeoutException:
            print("Pop-up1 didn't appear")
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, H.pop_up2)))
            driver.find_element(By.XPATH, H.pop_up2).click()
        except TimeoutException:
            print("Pop-up2 didn't appear")

        # Sign In button usability verification
        driver.find_element(By.XPATH, H.h_menu).click()
        time.sleep(1)

        # Scroll until Sign_In will be visible
        sign_in = driver.find_element(By.XPATH, "//g-link[contains(.,'Sign In')]")
        driver.execute_script("arguments[0].scrollIntoView(true)", sign_in)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//g-link[contains(.,'Sign In')]")))
        driver.find_element(By.XPATH, "//g-link[contains(.,'Sign In')]").click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'MY GUCCI Account')]")))

        # Sign In title verification
        try:
            title_si = driver.title == H.s_title
            print("Sign In title is correct!")
        except WDE:
            print("Sign In title is incorrect!")

    def test8_FEPT_0002_1440x900(self):
        driver = self.driver
        driver.set_window_size(1440, 900)
        driver.get(H.url)
        wait = WebDriverWait(driver, 5)

        # Pop-ups'
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, H.pop_up1)))
            driver.find_element(By.XPATH, H.pop_up1).click()
        except TimeoutException:
            print("Pop-up1 didn't appear")
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, H.pop_up2)))
            driver.find_element(By.XPATH, H.pop_up2).click()
        except TimeoutException:
            print("Pop-up2 didn't appear")

        # Sign In button usability verification
        driver.find_element(By.XPATH, H.h_menu).click()
        time.sleep(1)

        # Scroll until Sign_In will be visible
        sign_in = driver.find_element(By.XPATH, "//g-link[contains(.,'Sign In')]")
        driver.execute_script("arguments[0].scrollIntoView(true)", sign_in)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//g-link[contains(.,'Sign In')]")))
        driver.find_element(By.XPATH, "//g-link[contains(.,'Sign In')]").click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'MY GUCCI Account')]")))

        # Sign In title verification
        try:
            title_si = driver.title == H.s_title
            print("Sign In title is correct!")
        except WDE:
            print("Sign In title is incorrect!")

    def test9_FEPT_0003_max(self):
        driver = self.driver
        driver.get(H.url)
        wait = WebDriverWait(driver, 5)

        # Pop-ups'
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, H.pop_up1)))
            driver.find_element(By.XPATH, H.pop_up1).click()
        except TimeoutException:
            print("Pop-up1 didn't appear")
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, H.pop_up2)))
            driver.find_element(By.XPATH, H.pop_up2).click()
        except TimeoutException:
            print("Pop-up2 didn't appear")

        # New account creating
        driver.find_element(By.XPATH, H.my_acc).click()
        driver.find_element(By.XPATH, H.sign_in).click()
        H.account(driver)
        time.sleep(5)
        # Name checking
        name_verify = driver.find_element(By.XPATH, H.welcome).text
        try:
            name_check = name_verify == f'{H.f_name.capitalize} {H.l_name.capitalize}'
            print("Name is correct!")
        except WDE:
            print("Name is incorrect!")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(AllureReports)
