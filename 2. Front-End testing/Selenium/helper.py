from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException as WDE
import time
from faker import Faker
import random

fake = Faker()

# Elements locators
url = "https://www.gucci.com/us/en/"
pop_up1 = "//button[@id='onetrust-accept-btn-handler']"
pop_up2 = "//body/div[@id='bx-campaign-1927696']/div[3]/div[1]/div[1]/div[1]/a[1]/*[1]"
m_title = "GUCCI® US Official Site | Redefining Luxury Fashion"
s_title = "My Account | Gucci"
h_menu = "//g-icon-menu[@variant='24']"
my_acc = "//g-icon-myaccount[@variant='24']"
sign_in = "//a[contains(@data-testid,'sign-in')]"

# Random data
month = random.randint(1, 12)
day = random.randint(1, 30)
year = random.randint(1950, 2005)
f_name = fake.first_name()
l_name = fake.last_name()
email = fake.email()
password = "p@sSword" + str(random.randint(0, 9999999))
welcome = "//span[contains(@class,'hero-account-landing-first-name')]"


# Account creating
def account(driver):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'MY GUCCI Account')]")))
    driver.find_element(By.ID, "email-input").send_keys('\n', "vasiliy_1200@ebanina.com")
    driver.find_element(By.ID, "confirm-button").click()
    time.sleep(1)
    wait.until(
        EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Please enter at least 8 characters')]")))
    driver.find_element(By.ID, "password-input").send_keys('\n', password)
    driver.find_element(By.ID, "first-name-input").send_keys('\n', f_name)
    time.sleep(3)
    driver.find_element(By.ID, "last-name-input").send_keys('\n', l_name)
    driver.find_element(By.ID, "month-input").send_keys('\n', month)
    driver.find_element(By.ID, "day-input").send_keys('\n', day)
    driver.find_element(By.ID, "year-input").send_keys('\n', year)
    driver.find_element(By.ID, "title-select").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//li[contains(.,'I’d rather not say')]").click()
    time.sleep(1)
    wait.until(EC.element_to_be_clickable((By.ID, "confirm-button")))
    try:
        driver.find_element(By.ID, "confirm-button").click()
    except WDE:
        driver.find_element(By.ID, "confirm-button").click()
    time.sleep(2)
