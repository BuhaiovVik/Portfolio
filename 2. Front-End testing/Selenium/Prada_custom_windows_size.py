import unittest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
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
import random
import helper as H

fake = Faker()

# You can change windows size for the all tests below
width = 1920
height = 1080


class Chrome(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.set_window_size(width, height)

    def test01_fept_001_max(self):
        driver = self.driver
        driver.get("https://internxt.com/temporary-email")
        wait = WebDriverWait(driver, 50)

        # Get email
        time.sleep(2)
        driver.find_element(By.XPATH, "//p[contains(text(),'Copy email')]").click()

        # Save email in the email.txt file
        email = driver.find_element(By.XPATH,
                                    '//*[@class="flex h-full w-full cursor-pointer flex-row items-center '
                                    'justify-between rounded-xl bg-gray-1 shadow-sm  px-4 py-3"]').text
        with open("email.txt", "w") as file:
            file.write(email)

        # Save password as pass.txt file
        password = "p@sSword" + str(random.randint(0, 999))
        with open("pass.txt", "w") as file:
            file.write(password)

        # Open new tab "prada.com" and star registration
        driver.switch_to.new_window('tab')
        driver.get("https://www.prada.com/us/en.html")
        driver.find_element(By.XPATH, "//div[@class='banner_cta cta_accept'][contains(.,'ACCEPT ALL')]").click()
        driver.find_element(By.XPATH, "//span[contains(@class,'utils__icon pr-icon-new-login')]").click()
        wait.until(EC.visibility_of_element_located((By.ID, "gigya-textbox-100719189608483120")))
        driver.find_element(By.ID, "gigya-textbox-100719189608483120").send_keys(Keys.CONTROL + "v")
        driver.find_element(By.XPATH, "//input[contains(@value,'Next')]").click()
        time.sleep(10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Resend')]")))

        # Switch to temporary email and wait for verification code
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

        # Switch to prada tab and complete registration
        driver.switch_to.window(driver.window_handles[1])
        driver.find_element(By.XPATH, '//*[@placeholder="Verification code*"]').send_keys(code)
        driver.find_element(By.XPATH, H.drop_down).click()
        driver.find_element(By.ID, "gigya-textbox-105760616358098000").send_keys(H.f_name)
        driver.find_element(By.ID, "gigya-textbox-21007040083017830").send_keys(H.l_name)
        driver.find_element(By.ID, "gigya-textbox-74329674452397740").send_keys(H.mm_dd)
        driver.find_element(By.ID, "gigya-password-60262223393983710").send_keys(password)
        driver.find_element(By.ID, "visibleTextMarketing").click()
        driver.find_element(By.XPATH, "//input[@value='Register']").click()
        print("Verification code was correct")

        # Registration validation
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(@class,'utils__icon pr-icon-new-bag')]")))
        try:
            title_check = driver.title == "Prada Official Website | Thinking fashion since 1913 | PRADA"
            print("Title is correct. Test PASS!")
        except WDE:
            print("Incorrect title. Test FALL!")
        print("Account was successful created")

    def test02_fept_002_max(self):
        driver = self.driver
        driver.get("https://www.prada.com/us/en/login-register.html")
        wait = WebDriverWait(driver, 10)

        # Login to the account
        H.login(driver)

        # Open the address form menu
        driver.find_element(By.XPATH, H.log_icon).click()
        driver.find_element(By.XPATH, H.address_dd).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Personal information')]")))
        try:
            title_check = driver.title == H.address_title
            print("Title is correct. Test PASS!")
        except WDE:
            print("Incorrect title. Test FALL!")
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
        wait.until(EC.element_to_be_clickable((By.XPATH, H.state_city)))
        driver.find_element(By.XPATH, H.state_city).click()
        driver.find_element(By.XPATH, "//input[contains(@id,'zip_code_')]").send_keys(H.zip_code)
        driver.find_element(By.XPATH, "//input[contains(@id,'phone_')]").send_keys(H.phone)
        driver.find_element(By.XPATH, H.check_box).click()
        driver.find_element(By.XPATH, H.confirm).click()
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, H.confirm_2)))
            driver.find_element(By.XPATH, H.confirm_2).click()
        except WDE:
            wait.until(EC.visibility_of_element_located((By.XPATH, H.ship_address)))
        wait.until(EC.visibility_of_element_located((By.XPATH, H.ship_address)))

        # Shipping and billing addresses verification
        shipp = driver.find_element(By.XPATH, H.ship_address).text
        bill = driver.find_element(By.XPATH, H.bill_address).text
        try:
            address_check = shipp == bill
            print("Shipping and billing addresses are correct. Test PASS!")
        except WDE:
            print("Shipping and billing addresses are incorrect. Test FALL!")
        print("Address was successful created")

    def test03_fept_003_max(self):
        driver = self.driver
        driver.get("https://www.prada.com/us/en/login-register.html")
        wait = WebDriverWait(driver, 10)

        # Login to the account
        H.login(driver)

        # Open the address form menu
        driver.find_element(By.XPATH, H.log_icon).click()
        driver.find_element(By.XPATH, H.address_dd).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Personal information')]")))

        # Address change functionality
        wait.until(EC.visibility_of_element_located((By.XPATH, H.address_change)))
        wait.until(EC.element_to_be_clickable((By.XPATH, H.address_change)))
        driver.find_element(By.XPATH, H.address_change).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, H.address_1)))
        driver.find_element(By.XPATH, H.address_1).send_keys(Keys.CONTROL + "a")
        driver.find_element(By.XPATH, H.address_1).send_keys(Keys.DELETE)
        driver.find_element(By.XPATH, H.address_1).send_keys(H.add_new)
        driver.find_element(By.XPATH, "//input[contains(@id,'city_')]").send_keys(Keys.CONTROL + "a")
        driver.find_element(By.XPATH, "//input[contains(@id,'city_')]").send_keys(Keys.DELETE)
        driver.find_element(By.XPATH, "//input[contains(@id,'city_')]").send_keys(H.city_new)
        driver.find_element(By.XPATH, H.state_dd).click()
        scroll_to_state = driver.find_element(By.XPATH, H.state_city_new)
        driver.execute_script("arguments[0].scrollIntoView(true)", scroll_to_state)
        wait.until(EC.element_to_be_clickable((By.XPATH, H.state_city_new)))
        driver.find_element(By.XPATH, H.state_city_new).click()
        driver.find_element(By.XPATH, "//input[contains(@id,'zip_code_')]").send_keys(Keys.CONTROL + "a")
        driver.find_element(By.XPATH, "//input[contains(@id,'zip_code_')]").send_keys(Keys.DELETE)
        driver.find_element(By.XPATH, "//input[contains(@id,'zip_code_')]").send_keys(H.zip_code_new)
        driver.find_element(By.XPATH, H.check_box).click()
        driver.find_element(By.XPATH, H.confirm).click()
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, H.confirm_2)))
            driver.find_element(By.XPATH, H.confirm_2).click()
        except WDE:
            wait.until(EC.visibility_of_element_located((By.XPATH, H.ship_address)))
        wait.until(EC.visibility_of_element_located((By.XPATH, H.ship_address)))
        print("Address was successfully changed")

    def test04_fept_004_max(self):
        driver = self.driver
        driver.get("https://www.prada.com/us/en/login-register.html")
        wait = WebDriverWait(driver, 20)

        # Login to the account
        H.login(driver)

        # Go to Prada-Edition bag
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(.,'Bags')]")))
        driver.find_element(By.XPATH, "//span[contains(.,'Bags')]").click()
        driver.find_element(By.XPATH, H.re_edition).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, H.bag_img)))
        driver.find_element(By.XPATH, H.bag_img).click()

        # Buy mint green, white and orange bags Prada-Edition
        wait.until(EC.element_to_be_clickable((By.XPATH, H.add_shop_bag)))
        driver.find_element(By.XPATH, H.bag_mintgreen_button).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, H.bag_mintgreen_img)))
        time.sleep(2)
        driver.find_element(By.XPATH, H.add_shop_bag).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, H.check_out)))
        driver.find_element(By.XPATH, H.cross).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, H.add_shop_bag)))
        driver.find_element(By.XPATH, H.bag_white_button).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, H.bag_white_img)))
        time.sleep(2)
        driver.find_element(By.XPATH, H.add_shop_bag).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, H.check_out)))
        driver.find_element(By.XPATH, H.cross).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, H.add_shop_bag)))
        driver.find_element(By.XPATH, H.bag_orange_button).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, H.bag_orange_img)))
        time.sleep(2)
        driver.find_element(By.XPATH, H.add_shop_bag).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, H.check_out)))
        driver.find_element(By.XPATH, H.cross).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, H.add_shop_bag)))

        # Verify quantity in the cart
        cart_quantity = driver.find_element(By.XPATH, "//span[contains(.,'Your selection (')]").text
        try:
            cart_quantity_check = cart_quantity == "3"
            print("Correct quantity. Test PASS!")
        except WDE:
            print("Incorrect quantity. Test FALL")

    def test05_fept_005_max(self):
        driver = self.driver
        driver.get("https://www.prada.com/us/en/login-register.html")
        wait = WebDriverWait(driver, 10)

        # Login to the account
        H.login(driver)

        # Go to "Home and decor"
        driver.find_element(By.XPATH, "//span[contains(text(),'HOME')]").click()
        driver.find_element(By.XPATH, H.home_decor).click()
        wait.until(EC.title_is("Prada Home: Home Decor and Accessories | PRADA"))
        driver.find_element(By.XPATH, H.show_more).click()

        # Buy "Saffiano leather Go set"
        wait.until(EC.element_to_be_clickable((By.XPATH, H.go_set)))
        driver.find_element(By.XPATH, H.go_set).click()

        # Webpage link verify
        try:
            link_check = driver.page_source == "https://prada.com/us/en/p/saffiano-leather-go-set/2SG008_0DC_F0002"
            print("Webpage like text is correct. PASS!")
        except TimeoutException:
            print("Webpage like text is incorrect. FALL!")

        # Buy Go and remove from the cart
        wait.until(EC.element_to_be_clickable((By.XPATH, H.add_shop_bag)))
        driver.find_element(By.XPATH, H.add_shop_bag).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'Remove')])[1]")))
        driver.find_element(By.XPATH, "(//span[contains(.,'Remove')])[1]").click()
        wait.until_not(EC.visibility_of_element_located((By.XPATH, H.go_img)))

        # Verify item was removed
        cart_quantity = driver.find_element(By.XPATH, "//span[contains(.,'Your selection (')]").text
        try:
            cart_quantity_check = cart_quantity == "3"
            print("Correct quantity. Test PASS!")
        except WDE:
            print("Incorrect quantity. Test FALL")

    def test06_fept_006_max(self):
        driver = self.driver
        driver.get("https://www.prada.com/us/en/login-register.html")
        wait = WebDriverWait(driver, 10)

        # Login to the account
        H.login(driver)

        driver.find_element(By.XPATH, "//span[@class='menu__linkText'][contains(.,'Beauty and Fragrances')]").click()
        driver.find_element(By.XPATH, H.frag_dd).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, H.frag_img)))
        driver.find_element(By.XPATH, H.frag_img).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, H.add_shop_bag)))
        driver.find_element(By.XPATH, H.add_shop_bag).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Go to shopping bag')]")))
        driver.find_element(By.XPATH, "//button[contains(.,'Go to shopping bag')]").click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'Edit')])[1]")))
        driver.find_element(By.XPATH, "(//span[contains(.,'Edit')])[1]").click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='pr-icon-add']")))
        driver.find_element(By.XPATH, "//span[@class='pr-icon-add']").click()
        driver.find_element(By.XPATH, "//span[@class='pr-icon-add']").click()
        driver.find_element(By.XPATH, "//span[@class='pr-icon-add']").click()
        driver.find_element(By.XPATH, "//span[@class='pr-icon-add']").click()
        quantity_edit = driver.find_element(By.XPATH, '//*[@class="detail-product-quantity-selector__value"]').text
        try:
            quantity_edit_check = quantity_edit == "5"
            print("Correct quantity. Test PASS!")
        except WDE:
            print("Incorrect quantity. Test FALL")
        driver.find_element(By.XPATH, H.confirm_cart).click()

    def test07_fept_007_max(self):
        driver = self.driver
        driver.get("https://www.prada.com/us/en/login-register.html")
        wait = WebDriverWait(driver, 10)

        # Login to the account
        H.login(driver)

        # Go to the payment form
        wait.until(EC.element_to_be_clickable((By.XPATH, H.cart_icon)))
        driver.find_element(By.XPATH, H.cart_icon).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text() = "Proceed to checkout"]')))
        driver.find_element(By.XPATH, '//*[text() = "Proceed to checkout"]').click()
        wait.until(EC.element_to_be_clickable((By.XPATH, H.confirm_address_checkout)))

        # If test will run not a first time some steps will be completed
        try:
            cac = driver.find_element(By.XPATH, '//*[text() = "Confirm"]')
            driver.execute_script("arguments[0].scrollIntoView(true)", cac)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text() = "Confirm"]')))
            driver.find_element(By.XPATH, '//*[text() = "Confirm"]').click()
            driver.find_element(By.XPATH, '//*[text() = "Confirm"]').click()
        except WDE:
            print("Confirm button wasn't appeared")
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text() = "Confirm and proceed"]')))
            driver.find_element(By.XPATH, '//*[text() = "Confirm and proceed"]').click()
        except WDE:
            print("Confirm and proceed button wasn't appeared")

        # Input payment details (because this is tested example I use uncorrected card details for positive testing)
        wait.until(EC.element_to_be_clickable((By.XPATH, H.card_name)))
        driver.find_element(By.XPATH, H.card_name).send_keys(H.f_name)
        driver.find_element(By.XPATH, H.card_lname).send_keys(H.l_name)
        driver.find_element(By.XPATH, H.card_lname).click()
        time.sleep(1)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.send_keys(Keys.NUMPAD1)
        actions.send_keys(Keys.NUMPAD1)
        actions.send_keys(Keys.NUMPAD1)
        actions.send_keys(Keys.NUMPAD1)
        actions.send_keys(Keys.NUMPAD1)
        actions.send_keys(Keys.NUMPAD1)
        actions.send_keys(Keys.NUMPAD1)
        actions.send_keys(Keys.NUMPAD1)
        actions.send_keys(Keys.NUMPAD1)
        actions.send_keys(Keys.NUMPAD1)
        actions.send_keys(Keys.NUMPAD1)
        actions.send_keys(Keys.NUMPAD1)
        actions.send_keys(Keys.NUMPAD1)
        actions.send_keys(Keys.NUMPAD1)
        actions.send_keys(Keys.NUMPAD1)
        actions.send_keys(Keys.NUMPAD1)
        actions.send_keys(Keys.TAB)
        actions.send_keys(Keys.NUMPAD0)
        actions.send_keys(Keys.NUMPAD5)
        actions.send_keys(Keys.NUMPAD2)
        actions.send_keys(Keys.NUMPAD5)
        actions.send_keys(Keys.TAB)
        actions.send_keys(Keys.NUMPAD3)
        actions.send_keys(Keys.NUMPAD4)
        actions.send_keys(Keys.NUMPAD6)
        actions.perform()
        driver.find_element(By.XPATH, "//button[contains(.,'Confirm and proceed')]").click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'Credit card not accepted')]")))
        print("Payment work correctly")

    def test08_fept_008_max(self):
        driver = self.driver
        driver.get("https://www.prada.com/us/en/login-register.html")
        wait = WebDriverWait(driver, 10)

        # Login to the account
        H.login(driver)
        print("User was successfully logged with correct data")

        # Title verify
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Start shopping')]")))
        try:
            title_check = driver.title == "Logged Area | PRADA"
            print("Title is correct. Test PASS!")
        except WDE:
            print("Incorrect title. Test FALL!")

        # Log out
        driver.find_element(By.XPATH, H.log_out_icon).click()
        driver.find_element(By.XPATH, H.log_out).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//body/div[3]/div[1]/div[2]/div[1]")))
        print("User was successful log out. Test PASS")

    def test09_feng_001_max(self):
        driver = self.driver
        driver.get("https://www.prada.com/us/en/login-register.html")
        wait = WebDriverWait(driver, 10)

        # Log In with wrong email
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text() = 'ACCEPT ALL']")))
        driver.find_element(By.XPATH, "//*[text() = 'ACCEPT ALL']").click()
        wait.until(EC.visibility_of_element_located((By.ID, "gigya-textbox-100719189608483120")))
        with open("email.txt", "r") as file:
            email_text = file.read().strip()
        driver.find_element(By.ID, "gigya-textbox-100719189608483120").send_keys("1" + email_text)
        driver.find_element(By.XPATH, "//input[contains(@value,'Next')]").click()
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@value='Register']")))
            print("User was redirected to register area. Test FALL")
        except WDE:
            wait.until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@value,'Login')]")))
            print("User was redirected to login area. Test FALL")

    def test10_feng_002_max(self):
        driver = self.driver
        driver.get("https://www.prada.com/us/en/login-register.html")
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text() = 'ACCEPT ALL']")))
        driver.find_element(By.XPATH, "//*[text() = 'ACCEPT ALL']").click()
        wait.until(EC.visibility_of_element_located((By.ID, "gigya-textbox-100719189608483120")))
        with open("email.txt", "r") as file:
            email_text = file.read().strip()
        driver.find_element(By.ID, "gigya-textbox-100719189608483120").send_keys(email_text)
        driver.find_element(By.XPATH, "//input[contains(@value,'Next')]").click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@value,'Login')]")))
        with open("pass.txt", "r") as file:
            pass_text = file.read().strip()
        driver.find_element(By.ID, "gigya-password-83462624292152350").send_keys(pass_text + "1")
        driver.find_element(By.XPATH, "//input[contains(@value,'Login')]").click()
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text() = "Invalid login or password"]')))
        print("User not abel to log in with wrong password. Test PASS")

    def test11_feng_003_max(self):
        driver = self.driver
        driver.get("https://www.prada.com/us/en/login-register.html")
        wait = WebDriverWait(driver, 10)

        # Login to the account
        H.login(driver)

        # Go to the payment form
        wait.until(EC.element_to_be_clickable((By.XPATH, H.cart_icon)))
        driver.find_element(By.XPATH, H.cart_icon).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text() = "Proceed to checkout"]')))
        driver.find_element(By.XPATH, '//*[text() = "Proceed to checkout"]').click()
        wait.until(EC.element_to_be_clickable((By.XPATH, H.confirm_address_checkout)))

        # If test will run not a first time some steps will be completed
        try:
            cac = driver.find_element(By.XPATH, '//*[text() = "Confirm"]')
            driver.execute_script("arguments[0].scrollIntoView(true)", cac)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text() = "Confirm"]')))
            driver.find_element(By.XPATH, '//*[text() = "Confirm"]').click()
            driver.find_element(By.XPATH, '//*[text() = "Confirm"]').click()
        except WDE:
            print("Confirm button wasn't appeared")
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text() = "Confirm and proceed"]')))
            driver.find_element(By.XPATH, '//*[text() = "Confirm and proceed"]').click()
        except WDE:
            print("Confirm and proceed button wasn't appeared")

        # Input wrong payment details
        wait.until(EC.element_to_be_clickable((By.XPATH, H.card_name)))
        driver.find_element(By.XPATH, H.card_name).send_keys(H.f_name)
        driver.find_element(By.XPATH, H.card_lname).send_keys(H.l_name)
        driver.find_element(By.XPATH, H.card_lname).click()
        time.sleep(1)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.send_keys(Keys.NUMPAD7)
        actions.send_keys(Keys.NUMPAD7)
        actions.send_keys(Keys.NUMPAD7)
        actions.send_keys(Keys.NUMPAD7)
        actions.send_keys(Keys.NUMPAD7)
        actions.send_keys(Keys.NUMPAD7)
        actions.send_keys(Keys.NUMPAD7)
        actions.send_keys(Keys.NUMPAD7)
        actions.send_keys(Keys.NUMPAD7)
        actions.send_keys(Keys.NUMPAD7)
        actions.send_keys(Keys.NUMPAD7)
        actions.send_keys(Keys.NUMPAD7)
        actions.send_keys(Keys.NUMPAD7)
        actions.send_keys(Keys.NUMPAD7)
        actions.send_keys(Keys.NUMPAD7)
        actions.send_keys(Keys.NUMPAD7)
        actions.send_keys(Keys.TAB)
        actions.send_keys(Keys.NUMPAD0)
        actions.send_keys(Keys.NUMPAD5)
        actions.send_keys(Keys.NUMPAD2)
        actions.send_keys(Keys.NUMPAD2)
        actions.send_keys(Keys.TAB)
        actions.send_keys(Keys.NUMPAD3)
        actions.send_keys(Keys.NUMPAD4)
        actions.send_keys(Keys.NUMPAD5)
        actions.perform()
        driver.find_element(By.XPATH, "//button[contains(.,'Confirm and proceed')]").click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'Credit card not accepted')]")))
        print("Incorrect credit card wasn't accepted. Test PASS")

    def test12_feng_004_max(self):
        driver = self.driver
        driver.get("https://www.prada.com/us/en/login-register.html")
        wait = WebDriverWait(driver, 10)

        # Login to the account
        H.login(driver)

        # Go to the personal information and delete address if it presents
        driver.find_element(By.XPATH, "//a[@href='#'][contains(.,'Personal information')]").click()
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, H.basket_del)))
            driver.find_element(By.XPATH, H.basket_del).click()
            wait.until(EC.element_to_be_clickable((By.XPATH, H.delete_confirm)))
            driver.find_element(By.XPATH, H.delete_confirm).click()
        except WDE:
            print("Address wasn't create previously")

        # Create new address with incorrect name
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Personal information')]")))
        driver.find_element(By.XPATH, '//*[contains(text(),"Add new shipping address")]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h3[contains(text(),'Shipping address')]")))
        driver.find_element(By.XPATH, "//input[contains(@id,'first_name_')]").send_keys("$$$")
        driver.find_element(By.XPATH, "//input[contains(@id,'last_name_')]").send_keys(H.l_name)
        driver.find_element(By.XPATH, "//input[contains(@id,'company_')]").send_keys(H.company)
        time.sleep(3)
        driver.find_element(By.XPATH, H.address_1).send_keys(H.add)
        driver.find_element(By.XPATH, "//input[contains(@id,'city_')]").send_keys(H.city)
        driver.find_element(By.XPATH, H.state_dd).click()
        scroll_to_state = driver.find_element(By.XPATH, H.state_city)
        driver.execute_script("arguments[0].scrollIntoView(true)", scroll_to_state)
        wait.until(EC.element_to_be_clickable((By.XPATH, H.state_city)))
        driver.find_element(By.XPATH, H.state_city).click()
        driver.find_element(By.XPATH, "//input[contains(@id,'zip_code_')]").send_keys(H.zip_code)
        driver.find_element(By.XPATH, "//input[contains(@id,'phone_')]").send_keys(H.phone)
        driver.find_element(By.XPATH, H.check_box).click()
        driver.find_element(By.XPATH, H.confirm).click()
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, '// *[contains(text(), "The First name field '
                                                                   'format is invalid")]')))
            print("User not abel to create address with incorrect name. Test PASS")
        except WDE:
            print("User abel to create address with incorrect name. Test FALL")
        wait.until(EC.visibility_of_element_located((By.XPATH, '// *[contains(text(), "The First name field format is '
                                                               'invalid")]')))

    def test13_feng_005_max(self):
        driver = self.driver
        driver.get("https://www.prada.com/us/en/login-register.html")
        wait = WebDriverWait(driver, 10)

        # Login to the account
        H.login(driver)

        # Go to the personal information and delete address if it presents
        driver.find_element(By.XPATH, "//a[@href='#'][contains(.,'Personal information')]").click()
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, H.basket_del)))
            driver.find_element(By.XPATH, H.basket_del).click()
            wait.until(EC.element_to_be_clickable((By.XPATH, H.delete_confirm)))
            driver.find_element(By.XPATH, H.delete_confirm).click()
        except WDE:
            print("Address wasn't create previously")

        # Create new address with incorrect address1
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Personal information')]")))
        driver.find_element(By.XPATH, '//*[contains(text(),"Add new shipping address")]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h3[contains(text(),'Shipping address')]")))
        driver.find_element(By.XPATH, "//input[contains(@id,'first_name_')]").send_keys(H.f_name)
        driver.find_element(By.XPATH, "//input[contains(@id,'last_name_')]").send_keys(H.l_name)
        driver.find_element(By.XPATH, "//input[contains(@id,'company_')]").send_keys(H.company)
        time.sleep(3)
        driver.find_element(By.XPATH, H.address_1).send_keys("$$$")
        driver.find_element(By.XPATH, "//input[contains(@id,'city_')]").send_keys(H.city)
        driver.find_element(By.XPATH, H.state_dd).click()
        scroll_to_state = driver.find_element(By.XPATH, H.state_city)
        driver.execute_script("arguments[0].scrollIntoView(true)", scroll_to_state)
        wait.until(EC.element_to_be_clickable((By.XPATH, H.state_city)))
        driver.find_element(By.XPATH, H.state_city).click()
        driver.find_element(By.XPATH, "//input[contains(@id,'zip_code_')]").send_keys(H.zip_code)
        driver.find_element(By.XPATH, "//input[contains(@id,'phone_')]").send_keys(H.phone)
        driver.find_element(By.XPATH, H.check_box).click()
        driver.find_element(By.XPATH, H.confirm).click()
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(.,'Cancel')])[7]")))
            print("User not abel to create address with incorrect address1. Test PASS")
        except WDE:
            print("User abel to create address with incorrect address1. Test FALL")
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(.,'Cancel')])[7]")))

    def test14_feng_006_max(self):
        driver = self.driver
        driver.get("https://www.prada.com/us/en/login-register.html")
        wait = WebDriverWait(driver, 10)

        # Login to the account
        H.login(driver)

        # Go to the personal information and delete address if it presents
        driver.find_element(By.XPATH, "//a[@href='#'][contains(.,'Personal information')]").click()
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, H.basket_del)))
            driver.find_element(By.XPATH, H.basket_del).click()
            wait.until(EC.element_to_be_clickable((By.XPATH, H.delete_confirm)))
            driver.find_element(By.XPATH, H.delete_confirm).click()
        except WDE:
            print("Address wasn't create previously")

        # Create new address with incorrect zip code
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Personal information')]")))
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
        wait.until(EC.element_to_be_clickable((By.XPATH, H.state_city)))
        driver.find_element(By.XPATH, H.state_city).click()
        driver.find_element(By.XPATH, "//input[contains(@id,'zip_code_')]").send_keys("0000")
        driver.find_element(By.XPATH, "//input[contains(@id,'phone_')]").send_keys(H.phone)
        driver.find_element(By.XPATH, H.check_box).click()
        driver.find_element(By.XPATH, H.confirm).click()
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[contains(text(),"The Zip code field format is '
                                                                   'invalid")]')))
            print("User not abel to create address with incorrect zip code. Test PASS")
        except WDE:
            print("User abel to create address with incorrect zip code. Test FALL")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[contains(text(),"The Zip code field format is '
                                                               'invalid")]')))

    def test15_feng_007_max(self):
        driver = self.driver
        driver.get("https://www.prada.com/us/en/login-register.html")
        wait = WebDriverWait(driver, 10)

        # Login to the account
        H.login(driver)

        # Go to the personal information and delete address if it presents
        driver.find_element(By.XPATH, "//a[@href='#'][contains(.,'Personal information')]").click()
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, H.basket_del)))
            driver.find_element(By.XPATH, H.basket_del).click()
            wait.until(EC.element_to_be_clickable((By.XPATH, H.delete_confirm)))
            driver.find_element(By.XPATH, H.delete_confirm).click()
        except WDE:
            print("Address wasn't create previously")

        # Create new address with incorrect city
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Personal information')]")))
        driver.find_element(By.XPATH, '//*[contains(text(),"Add new shipping address")]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h3[contains(text(),'Shipping address')]")))
        driver.find_element(By.XPATH, "//input[contains(@id,'first_name_')]").send_keys(H.f_name)
        driver.find_element(By.XPATH, "//input[contains(@id,'last_name_')]").send_keys(H.l_name)
        driver.find_element(By.XPATH, "//input[contains(@id,'company_')]").send_keys(H.company)
        time.sleep(3)
        driver.find_element(By.XPATH, H.address_1).send_keys(H.add)
        driver.find_element(By.XPATH, "//input[contains(@id,'city_')]").send_keys("$$$")
        driver.find_element(By.XPATH, H.state_dd).click()
        scroll_to_state = driver.find_element(By.XPATH, H.state_city)
        driver.execute_script("arguments[0].scrollIntoView(true)", scroll_to_state)
        wait.until(EC.element_to_be_clickable((By.XPATH, H.state_city)))
        driver.find_element(By.XPATH, H.state_city).click()
        driver.find_element(By.XPATH, "//input[contains(@id,'zip_code_')]").send_keys(H.zip_code)
        driver.find_element(By.XPATH, "//input[contains(@id,'phone_')]").send_keys(H.phone)
        driver.find_element(By.XPATH, H.check_box).click()
        driver.find_element(By.XPATH, H.confirm).click()
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[contains(.,'Cancel')])[7]")))
            print("User not abel to create address with incorrect city. Test PASS")
            locator = "(//a[contains(.,'Cancel')])[7]"
        except WDE:
            locator = "//span[contains(.,'The address you entered seems to have some incorrect information')]"
            print("User not abel to create address with incorrect city. Test PASS")
        wait.until(EC.visibility_of_element_located((By.XPATH, locator)))

    def test16_feng_008_max(self):
        driver = self.driver
        driver.get("https://www.prada.com/us/en/login-register.html")
        wait = WebDriverWait(driver, 10)

        # Login to the account
        H.login(driver)

        # Go to the personal information and delete address if it presents
        driver.find_element(By.XPATH, "//a[@href='#'][contains(.,'Personal information')]").click()
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, H.basket_del)))
            driver.find_element(By.XPATH, H.basket_del).click()
            wait.until(EC.element_to_be_clickable((By.XPATH, H.delete_confirm)))
            driver.find_element(By.XPATH, H.delete_confirm).click()
        except WDE:
            print("Address wasn't create previously")

        # Create new address with incorrect phone number
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Personal information')]")))
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
        wait.until(EC.element_to_be_clickable((By.XPATH, H.state_city)))
        driver.find_element(By.XPATH, H.state_city).click()
        driver.find_element(By.XPATH, "//input[contains(@id,'zip_code_')]").send_keys(H.zip_code)
        driver.find_element(By.XPATH, "//input[contains(@id,'phone_')]").send_keys("000000")
        driver.find_element(By.XPATH, H.check_box).click()
        driver.find_element(By.XPATH, H.confirm).click()
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, '// *[contains(text(), "The Phone field format is '
                                                                   'invalid")]')))
            print("User not abel to create address with incorrect phone number. Test PASS")
        except WDE:
            print("User abel to create address with incorrect phone number. Test FALL")
        wait.until(EC.visibility_of_element_located((By.XPATH, '// *[contains(text(), "The Phone field format is '
                                                               'invalid")]')))

    def test17_febd_001_max(self):
        driver = self.driver
        driver.get("https://internxt.com/temporary-email")
        wait = WebDriverWait(driver, 50)

        # Get email
        time.sleep(2)
        driver.find_element(By.XPATH, "//p[contains(text(),'Copy email')]").click()

        # Open new tab "prada.com" and star registration
        driver.switch_to.new_window('tab')
        driver.get("https://www.prada.com/us/en.html")
        driver.find_element(By.XPATH, "//div[@class='banner_cta cta_accept'][contains(.,'ACCEPT ALL')]").click()
        driver.find_element(By.XPATH, "//span[contains(@class,'utils__icon pr-icon-new-login')]").click()
        wait.until(EC.visibility_of_element_located((By.ID, "gigya-textbox-100719189608483120")))
        driver.find_element(By.ID, "gigya-textbox-100719189608483120").send_keys(Keys.CONTROL + "v")
        driver.find_element(By.XPATH, "//input[contains(@value,'Next')]").click()
        time.sleep(10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Resend')]")))

        # Switch to temporary email and wait for verification code
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

        # Switch to prada tab and complete registration
        driver.switch_to.window(driver.window_handles[1])
        driver.find_element(By.XPATH, '//*[@placeholder="Verification code*"]').send_keys(code)
        driver.find_element(By.XPATH, H.drop_down).click()
        driver.find_element(By.ID, "gigya-textbox-105760616358098000").send_keys(H.f_name)
        driver.find_element(By.ID, "gigya-textbox-21007040083017830").send_keys(H.l_name)
        driver.find_element(By.ID, "gigya-textbox-74329674452397740").send_keys(H.mm_dd)
        driver.find_element(By.ID, "gigya-password-60262223393983710").send_keys("Df1!0:-")
        driver.find_element(By.ID, "visibleTextMarketing").click()
        driver.find_element(By.XPATH, "//input[@value='Register']").click()
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(.,'Check that your password "
                                                                   "respects the criteria.')]")))
            print("User can't create account with weak password. Test PASS")
        except WDE:
            print("User can create account with weak password.. Test FALL")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(.,'Check that your password respects "
                                                               "the criteria.')]")))

    def test18_febd_002_max(self):
        driver = self.driver
        driver.get("https://internxt.com/temporary-email")
        wait = WebDriverWait(driver, 50)

        # Get email
        time.sleep(2)
        driver.find_element(By.XPATH, "//p[contains(text(),'Copy email')]").click()

        # Open new tab "prada.com" and star registration
        driver.switch_to.new_window('tab')
        driver.get("https://www.prada.com/us/en.html")
        driver.find_element(By.XPATH, "//div[@class='banner_cta cta_accept'][contains(.,'ACCEPT ALL')]").click()
        driver.find_element(By.XPATH, "//span[contains(@class,'utils__icon pr-icon-new-login')]").click()
        wait.until(EC.visibility_of_element_located((By.ID, "gigya-textbox-100719189608483120")))
        driver.find_element(By.ID, "gigya-textbox-100719189608483120").send_keys(Keys.CONTROL + "v")
        driver.find_element(By.XPATH, "//input[contains(@value,'Next')]").click()
        time.sleep(10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Resend')]")))

        # Switch to temporary email and wait for verification code
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

        # Switch to prada tab and complete registration
        driver.switch_to.window(driver.window_handles[1])
        driver.find_element(By.XPATH, '//*[@placeholder="Verification code*"]').send_keys(code)
        driver.find_element(By.XPATH, H.drop_down).click()
        driver.find_element(By.ID, "gigya-textbox-105760616358098000").send_keys(H.f_name)
        driver.find_element(By.ID, "gigya-textbox-21007040083017830").send_keys(H.l_name)
        driver.find_element(By.ID, "gigya-textbox-74329674452397740").send_keys(H.mm_dd)
        driver.find_element(By.ID, "gigya-password-60262223393983710").send_keys("Df1!0:-a")
        driver.find_element(By.ID, "visibleTextMarketing").click()
        driver.find_element(By.XPATH, "//input[@value='Register']").click()

        # Registration validation
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(@class,'utils__icon pr-icon-new-bag')]")))
        try:
            title_check = driver.title == "Prada Official Website | Thinking fashion since 1913 | PRADA"
            print("Title is correct. Test PASS!")
        except WDE:
            print("Incorrect title. Test FALL!")

    def test19_febd_003_max(self):
        driver = self.driver
        driver.get("https://internxt.com/temporary-email")
        wait = WebDriverWait(driver, 50)

        # Get email
        time.sleep(2)
        driver.find_element(By.XPATH, "//p[contains(text(),'Copy email')]").click()

        # Open new tab "prada.com" and star registration
        driver.switch_to.new_window('tab')
        driver.get("https://www.prada.com/us/en.html")
        driver.find_element(By.XPATH, "//div[@class='banner_cta cta_accept'][contains(.,'ACCEPT ALL')]").click()
        driver.find_element(By.XPATH, "//span[contains(@class,'utils__icon pr-icon-new-login')]").click()
        wait.until(EC.visibility_of_element_located((By.ID, "gigya-textbox-100719189608483120")))
        driver.find_element(By.ID, "gigya-textbox-100719189608483120").send_keys(Keys.CONTROL + "v")
        driver.find_element(By.XPATH, "//input[contains(@value,'Next')]").click()
        time.sleep(10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Resend')]")))

        # Switch to temporary email and wait for verification code
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

        # Switch to prada tab and complete registration
        driver.switch_to.window(driver.window_handles[1])
        driver.find_element(By.XPATH, '//*[@placeholder="Verification code*"]').send_keys(code)
        driver.find_element(By.XPATH, H.drop_down).click()
        driver.find_element(By.ID, "gigya-textbox-105760616358098000").send_keys(H.f_name)
        driver.find_element(By.ID, "gigya-textbox-21007040083017830").send_keys(H.l_name)
        driver.find_element(By.ID, "gigya-textbox-74329674452397740").send_keys(H.mm_dd)
        driver.find_element(By.ID, "gigya-password-60262223393983710").send_keys("Df1!0:-as")
        driver.find_element(By.ID, "visibleTextMarketing").click()
        driver.find_element(By.XPATH, "//input[@value='Register']").click()

        # Registration validation
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(@class,'utils__icon pr-icon-new-bag')]")))
        try:
            title_check = driver.title == "Prada Official Website | Thinking fashion since 1913 | PRADA"
            print("Title is correct. Test PASS!")
        except WDE:
            print("Incorrect title. Test FALL!")

    def test20_febd_004_max(self):
        driver = self.driver
        driver.get("https://internxt.com/temporary-email")
        wait = WebDriverWait(driver, 50)

        # Get email
        time.sleep(2)
        driver.find_element(By.XPATH, "//p[contains(text(),'Copy email')]").click()

        # Open new tab "prada.com" and star registration
        driver.switch_to.new_window('tab')
        driver.get("https://www.prada.com/us/en.html")
        driver.find_element(By.XPATH, "//div[@class='banner_cta cta_accept'][contains(.,'ACCEPT ALL')]").click()
        driver.find_element(By.XPATH, "//span[contains(@class,'utils__icon pr-icon-new-login')]").click()
        wait.until(EC.visibility_of_element_located((By.ID, "gigya-textbox-100719189608483120")))
        driver.find_element(By.ID, "gigya-textbox-100719189608483120").send_keys(Keys.CONTROL + "v")
        driver.find_element(By.XPATH, "//input[contains(@value,'Next')]").click()
        time.sleep(10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Resend')]")))

        # Switch to temporary email and wait for verification code
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

        # Switch to prada tab and complete registration
        driver.switch_to.window(driver.window_handles[1])
        driver.find_element(By.XPATH, '//*[@placeholder="Verification code*"]').send_keys(code)
        driver.find_element(By.XPATH, H.drop_down).click()
        driver.find_element(By.ID, "gigya-textbox-105760616358098000").send_keys(H.f_name)
        driver.find_element(By.ID, "gigya-textbox-21007040083017830").send_keys(H.l_name)
        driver.find_element(By.ID, "gigya-textbox-74329674452397740").send_keys(H.mm_dd)
        driver.find_element(By.ID, "gigya-password-60262223393983710").send_keys("Df1!0:-asDf1!0:")
        driver.find_element(By.ID, "visibleTextMarketing").click()
        driver.find_element(By.XPATH, "//input[@value='Register']").click()

        # Registration validation
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(@class,'utils__icon pr-icon-new-bag')]")))
        try:
            title_check = driver.title == "Prada Official Website | Thinking fashion since 1913 | PRADA"
            print("Title is correct. Test PASS!")
        except WDE:
            print("Incorrect title. Test FALL!")

    def test21_febd_005_max(self):
        driver = self.driver
        driver.get("https://internxt.com/temporary-email")
        wait = WebDriverWait(driver, 50)

        # Get email
        time.sleep(2)
        driver.find_element(By.XPATH, "//p[contains(text(),'Copy email')]").click()

        # Open new tab "prada.com" and star registration
        driver.switch_to.new_window('tab')
        driver.get("https://www.prada.com/us/en.html")
        driver.find_element(By.XPATH, "//div[@class='banner_cta cta_accept'][contains(.,'ACCEPT ALL')]").click()
        driver.find_element(By.XPATH, "//span[contains(@class,'utils__icon pr-icon-new-login')]").click()
        wait.until(EC.visibility_of_element_located((By.ID, "gigya-textbox-100719189608483120")))
        driver.find_element(By.ID, "gigya-textbox-100719189608483120").send_keys(Keys.CONTROL + "v")
        driver.find_element(By.XPATH, "//input[contains(@value,'Next')]").click()
        time.sleep(10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Resend')]")))

        # Switch to temporary email and wait for verification code
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

        # Switch to prada tab and complete registration
        driver.switch_to.window(driver.window_handles[1])
        driver.find_element(By.XPATH, '//*[@placeholder="Verification code*"]').send_keys(code)
        driver.find_element(By.XPATH, H.drop_down).click()
        driver.find_element(By.ID, "gigya-textbox-105760616358098000").send_keys(H.f_name)
        driver.find_element(By.ID, "gigya-textbox-21007040083017830").send_keys(H.l_name)
        driver.find_element(By.ID, "gigya-textbox-74329674452397740").send_keys(H.mm_dd)
        driver.find_element(By.ID, "gigya-password-60262223393983710").send_keys("Df1!0:-asDf1!0:-")
        driver.find_element(By.ID, "visibleTextMarketing").click()
        driver.find_element(By.XPATH, "//input[@value='Register']").click()

        # Registration validation
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(@class,'utils__icon pr-icon-new-bag')]")))
        try:
            title_check = driver.title == "Prada Official Website | Thinking fashion since 1913 | PRADA"
            print("Title is correct. Test PASS!")
        except WDE:
            print("Incorrect title. Test FALL!")

    def test22_febd_006_max(self):
        driver = self.driver
        driver.get("https://internxt.com/temporary-email")
        wait = WebDriverWait(driver, 50)

        # Get email
        time.sleep(2)
        driver.find_element(By.XPATH, "//p[contains(text(),'Copy email')]").click()

        # Open new tab "prada.com" and star registration
        driver.switch_to.new_window('tab')
        driver.get("https://www.prada.com/us/en.html")
        driver.find_element(By.XPATH, "//div[@class='banner_cta cta_accept'][contains(.,'ACCEPT ALL')]").click()
        driver.find_element(By.XPATH, "//span[contains(@class,'utils__icon pr-icon-new-login')]").click()
        wait.until(EC.visibility_of_element_located((By.ID, "gigya-textbox-100719189608483120")))
        driver.find_element(By.ID, "gigya-textbox-100719189608483120").send_keys(Keys.CONTROL + "v")
        driver.find_element(By.XPATH, "//input[contains(@value,'Next')]").click()
        time.sleep(10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Resend')]")))

        # Switch to temporary email and wait for verification code
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

        # Switch to prada tab and complete registration
        driver.switch_to.window(driver.window_handles[1])
        driver.find_element(By.XPATH, '//*[@placeholder="Verification code*"]').send_keys(code)
        driver.find_element(By.XPATH, H.drop_down).click()
        driver.find_element(By.ID, "gigya-textbox-105760616358098000").send_keys(H.f_name)
        driver.find_element(By.ID, "gigya-textbox-21007040083017830").send_keys(H.l_name)
        driver.find_element(By.ID, "gigya-textbox-74329674452397740").send_keys(H.mm_dd)
        driver.find_element(By.ID, "gigya-password-60262223393983710").send_keys("Df1!0:-asDf1!0:-a")
        driver.find_element(By.ID, "visibleTextMarketing").click()
        driver.find_element(By.XPATH, "//input[@value='Register']").click()
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(.,'Check that your password "
                                                                   "respects the criteria.')]")))
            print("User can't create account with weak password. Test PASS")
        except WDE:
            print("User can create account with weak password.. Test FALL")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(.,'Check that your password respects "
                                                               "the criteria.')]")))

    def tearDown(self):
        self.driver.quit()


class Edge(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        self.driver.set_window_size(width, height)

    def test01_fept_001_max(self):
        driver = self.driver
        driver.get("https://internxt.com/temporary-email")
        wait = WebDriverWait(driver, 50)

        # Get email
        time.sleep(2)
        driver.find_element(By.XPATH, "//p[contains(text(),'Copy email')]").click()

        # Save email in the email.txt file
        email = driver.find_element(By.XPATH,
                                    '//*[@class="flex h-full w-full cursor-pointer flex-row items-center '
                                    'justify-between rounded-xl bg-gray-1 shadow-sm  px-4 py-3"]').text
        with open("email.txt", "w") as file:
            file.write(email)

        # Save password as pass.txt file
        password = "p@sSword" + str(random.randint(0, 999))
        with open("pass.txt", "w") as file:
            file.write(password)

        # Open new tab "prada.com" and star registration
        driver.switch_to.new_window('tab')
        driver.get("https://www.prada.com/us/en.html")
        driver.find_element(By.XPATH, "//div[@class='banner_cta cta_accept'][contains(.,'ACCEPT ALL')]").click()
        driver.find_element(By.XPATH, "//span[contains(@class,'utils__icon pr-icon-new-login')]").click()
        wait.until(EC.visibility_of_element_located((By.ID, "gigya-textbox-100719189608483120")))
        driver.find_element(By.ID, "gigya-textbox-100719189608483120").send_keys(Keys.CONTROL + "v")
        driver.find_element(By.XPATH, "//input[contains(@value,'Next')]").click()
        time.sleep(10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Resend')]")))

        # Switch to temporary email and wait for verification code
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

        # Switch to prada tab and complete registration
        driver.switch_to.window(driver.window_handles[1])
        driver.find_element(By.XPATH, '//*[@placeholder="Verification code*"]').send_keys(code)
        driver.find_element(By.XPATH, H.drop_down).click()
        driver.find_element(By.ID, "gigya-textbox-105760616358098000").send_keys(H.f_name)
        driver.find_element(By.ID, "gigya-textbox-21007040083017830").send_keys(H.l_name)
        driver.find_element(By.ID, "gigya-textbox-74329674452397740").send_keys(H.mm_dd)
        driver.find_element(By.ID, "gigya-password-60262223393983710").send_keys(password)
        driver.find_element(By.ID, "visibleTextMarketing").click()
        driver.find_element(By.XPATH, "//input[@value='Register']").click()
        print("Verification code was correct")

        # Registration validation
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(@class,'utils__icon pr-icon-new-bag')]")))
        try:
            title_check = driver.title == "Prada Official Website | Thinking fashion since 1913 | PRADA"
            print("Title is correct. Test PASS!")
        except WDE:
            print("Incorrect title. Test FALL!")
        print("Account was successful created")

    def test02_fept_002_max(self):
        driver = self.driver
        driver.get("https://www.prada.com/us/en/login-register.html")
        wait = WebDriverWait(driver, 10)

        # Login to the account
        H.login(driver)

        # Open the address form menu
        driver.find_element(By.XPATH, H.log_icon).click()
        driver.find_element(By.XPATH, H.address_dd).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Personal information')]")))
        try:
            title_check = driver.title == H.address_title
            print("Title is correct. Test PASS!")
        except WDE:
            print("Incorrect title. Test FALL!")
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
        wait.until(EC.element_to_be_clickable((By.XPATH, H.state_city)))
        driver.find_element(By.XPATH, H.state_city).click()
        driver.find_element(By.XPATH, "//input[contains(@id,'zip_code_')]").send_keys(H.zip_code)
        driver.find_element(By.XPATH, "//input[contains(@id,'phone_')]").send_keys(H.phone)
        driver.find_element(By.XPATH, H.check_box).click()
        driver.find_element(By.XPATH, H.confirm).click()
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, H.confirm_2)))
            driver.find_element(By.XPATH, H.confirm_2).click()
        except WDE:
            wait.until(EC.visibility_of_element_located((By.XPATH, H.ship_address)))
        wait.until(EC.visibility_of_element_located((By.XPATH, H.ship_address)))

        # Shipping and billing addresses verification
        shipp = driver.find_element(By.XPATH, H.ship_address).text
        bill = driver.find_element(By.XPATH, H.bill_address).text
        try:
            address_check = shipp == bill
            print("Shipping and billing addresses are correct. Test PASS!")
        except WDE:
            print("Shipping and billing addresses are incorrect. Test FALL!")
        print("Address was successful created")

    def test03_fept_003_max(self):
        driver = self.driver
        driver.get("https://www.prada.com/us/en/login-register.html")
        wait = WebDriverWait(driver, 10)

        # Login to the account
        H.login(driver)

        # Open the address form menu
        driver.find_element(By.XPATH, H.log_icon).click()
        driver.find_element(By.XPATH, H.address_dd).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Personal information')]")))

        # Address change functionality
        wait.until(EC.visibility_of_element_located((By.XPATH, H.address_change)))
        wait.until(EC.element_to_be_clickable((By.XPATH, H.address_change)))
        driver.find_element(By.XPATH, H.address_change).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, H.address_1)))
        driver.find_element(By.XPATH, H.address_1).send_keys(Keys.CONTROL + "a")
        driver.find_element(By.XPATH, H.address_1).send_keys(Keys.DELETE)
        driver.find_element(By.XPATH, H.address_1).send_keys(H.add_new)
        driver.find_element(By.XPATH, "//input[contains(@id,'city_')]").send_keys(Keys.CONTROL + "a")
        driver.find_element(By.XPATH, "//input[contains(@id,'city_')]").send_keys(Keys.DELETE)
        driver.find_element(By.XPATH, "//input[contains(@id,'city_')]").send_keys(H.city_new)
        driver.find_element(By.XPATH, H.state_dd).click()
        scroll_to_state = driver.find_element(By.XPATH, H.state_city_new)
        driver.execute_script("arguments[0].scrollIntoView(true)", scroll_to_state)
        wait.until(EC.element_to_be_clickable((By.XPATH, H.state_city_new)))
        driver.find_element(By.XPATH, H.state_city_new).click()
        driver.find_element(By.XPATH, "//input[contains(@id,'zip_code_')]").send_keys(Keys.CONTROL + "a")
        driver.find_element(By.XPATH, "//input[contains(@id,'zip_code_')]").send_keys(Keys.DELETE)
        driver.find_element(By.XPATH, "//input[contains(@id,'zip_code_')]").send_keys(H.zip_code_new)
        driver.find_element(By.XPATH, H.check_box).click()
        driver.find_element(By.XPATH, H.confirm).click()
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, H.confirm_2)))
            driver.find_element(By.XPATH, H.confirm_2).click()
        except WDE:
            wait.until(EC.visibility_of_element_located((By.XPATH, H.ship_address)))
        wait.until(EC.visibility_of_element_located((By.XPATH, H.ship_address)))
        print("Address was successfully changed")

    def test04_fept_004_max(self):
        driver = self.driver
        driver.get("https://www.prada.com/us/en/login-register.html")
        wait = WebDriverWait(driver, 20)

        # Login to the account
        H.login(driver)

        # Go to Prada-Edition bag
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(.,'Bags')]")))
        driver.find_element(By.XPATH, "//span[contains(.,'Bags')]").click()
        driver.find_element(By.XPATH, H.re_edition).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, H.bag_img)))
        driver.find_element(By.XPATH, H.bag_img).click()

        # Buy mint green, white and orange bags Prada-Edition
        wait.until(EC.element_to_be_clickable((By.XPATH, H.add_shop_bag)))
        driver.find_element(By.XPATH, H.bag_mintgreen_button).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, H.bag_mintgreen_img)))
        time.sleep(2)
        driver.find_element(By.XPATH, H.add_shop_bag).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, H.check_out)))
        driver.find_element(By.XPATH, H.cross).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, H.add_shop_bag)))
        driver.find_element(By.XPATH, H.bag_white_button).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, H.bag_white_img)))
        time.sleep(2)
        driver.find_element(By.XPATH, H.add_shop_bag).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, H.check_out)))
        driver.find_element(By.XPATH, H.cross).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, H.add_shop_bag)))
        driver.find_element(By.XPATH, H.bag_orange_button).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, H.bag_orange_img)))
        time.sleep(2)
        driver.find_element(By.XPATH, H.add_shop_bag).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, H.check_out)))
        driver.find_element(By.XPATH, H.cross).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, H.add_shop_bag)))

        # Verify quantity in the cart
        cart_quantity = driver.find_element(By.XPATH, "//span[contains(.,'Your selection (')]").text
        try:
            cart_quantity_check = cart_quantity == "3"
            print("Correct quantity. Test PASS!")
        except WDE:
            print("Incorrect quantity. Test FALL")

    def test05_fept_005_max(self):
        driver = self.driver
        driver.get("https://www.prada.com/us/en/login-register.html")
        wait = WebDriverWait(driver, 10)

        # Login to the account
        H.login(driver)

        # Go to "Home and decor"
        driver.find_element(By.XPATH, "//span[contains(text(),'HOME')]").click()
        driver.find_element(By.XPATH, H.home_decor).click()
        wait.until(EC.title_is("Prada Home: Home Decor and Accessories | PRADA"))
        driver.find_element(By.XPATH, H.show_more).click()

        # Buy "Saffiano leather Go set"
        wait.until(EC.element_to_be_clickable((By.XPATH, H.go_set)))
        driver.find_element(By.XPATH, H.go_set).click()

        # Webpage link verify
        try:
            link_check = driver.page_source == "https://prada.com/us/en/p/saffiano-leather-go-set/2SG008_0DC_F0002"
            print("Webpage like text is correct. PASS!")
        except TimeoutException:
            print("Webpage like text is incorrect. FALL!")

        # Buy Go and remove from the cart
        wait.until(EC.element_to_be_clickable((By.XPATH, H.add_shop_bag)))
        driver.find_element(By.XPATH, H.add_shop_bag).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'Remove')])[1]")))
        driver.find_element(By.XPATH, "(//span[contains(.,'Remove')])[1]").click()
        wait.until_not(EC.visibility_of_element_located((By.XPATH, H.go_img)))

        # Verify item was removed
        cart_quantity = driver.find_element(By.XPATH, "//span[contains(.,'Your selection (')]").text
        try:
            cart_quantity_check = cart_quantity == "3"
            print("Correct quantity. Test PASS!")
        except WDE:
            print("Incorrect quantity. Test FALL")

    def test06_fept_006_max(self):
        driver = self.driver
        driver.get("https://www.prada.com/us/en/login-register.html")
        wait = WebDriverWait(driver, 10)

        # Login to the account
        H.login(driver)

        driver.find_element(By.XPATH, "//span[@class='menu__linkText'][contains(.,'Beauty and Fragrances')]").click()
        driver.find_element(By.XPATH, H.frag_dd).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, H.frag_img)))
        driver.find_element(By.XPATH, H.frag_img).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, H.add_shop_bag)))
        driver.find_element(By.XPATH, H.add_shop_bag).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Go to shopping bag')]")))
        driver.find_element(By.XPATH, "//button[contains(.,'Go to shopping bag')]").click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'Edit')])[1]")))
        driver.find_element(By.XPATH, "(//span[contains(.,'Edit')])[1]").click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='pr-icon-add']")))
        driver.find_element(By.XPATH, "//span[@class='pr-icon-add']").click()
        driver.find_element(By.XPATH, "//span[@class='pr-icon-add']").click()
        driver.find_element(By.XPATH, "//span[@class='pr-icon-add']").click()
        driver.find_element(By.XPATH, "//span[@class='pr-icon-add']").click()
        quantity_edit = driver.find_element(By.XPATH, '//*[@class="detail-product-quantity-selector__value"]').text
        try:
            quantity_edit_check = quantity_edit == "5"
            print("Correct quantity. Test PASS!")
        except WDE:
            print("Incorrect quantity. Test FALL")
        driver.find_element(By.XPATH, H.confirm_cart).click()

    def test07_fept_007_max(self):
        driver = self.driver
        driver.get("https://www.prada.com/us/en/login-register.html")
        wait = WebDriverWait(driver, 10)

        # Login to the account
        H.login(driver)

        # Go to the payment form
        wait.until(EC.element_to_be_clickable((By.XPATH, H.cart_icon)))
        driver.find_element(By.XPATH, H.cart_icon).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text() = "Proceed to checkout"]')))
        driver.find_element(By.XPATH, '//*[text() = "Proceed to checkout"]').click()
        wait.until(EC.element_to_be_clickable((By.XPATH, H.confirm_address_checkout)))

        # If test will run not a first time some steps will be completed
        try:
            cac = driver.find_element(By.XPATH, '//*[text() = "Confirm"]')
            driver.execute_script("arguments[0].scrollIntoView(true)", cac)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text() = "Confirm"]')))
            driver.find_element(By.XPATH, '//*[text() = "Confirm"]').click()
            driver.find_element(By.XPATH, '//*[text() = "Confirm"]').click()
        except WDE:
            print("Confirm button wasn't appeared")
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text() = "Confirm and proceed"]')))
            driver.find_element(By.XPATH, '//*[text() = "Confirm and proceed"]').click()
        except WDE:
            print("Confirm and proceed button wasn't appeared")

        # Input payment details (because this is tested example I use uncorrected card details for positive testing)
        wait.until(EC.element_to_be_clickable((By.XPATH, H.card_name)))
        driver.find_element(By.XPATH, H.card_name).send_keys(H.f_name)
        driver.find_element(By.XPATH, H.card_lname).send_keys(H.l_name)
        driver.find_element(By.XPATH, H.card_lname).click()
        time.sleep(1)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.send_keys(Keys.NUMPAD1)
        actions.send_keys(Keys.NUMPAD1)
        actions.send_keys(Keys.NUMPAD1)
        actions.send_keys(Keys.NUMPAD1)
        actions.send_keys(Keys.NUMPAD1)
        actions.send_keys(Keys.NUMPAD1)
        actions.send_keys(Keys.NUMPAD1)
        actions.send_keys(Keys.NUMPAD1)
        actions.send_keys(Keys.NUMPAD1)
        actions.send_keys(Keys.NUMPAD1)
        actions.send_keys(Keys.NUMPAD1)
        actions.send_keys(Keys.NUMPAD1)
        actions.send_keys(Keys.NUMPAD1)
        actions.send_keys(Keys.NUMPAD1)
        actions.send_keys(Keys.NUMPAD1)
        actions.send_keys(Keys.NUMPAD1)
        actions.send_keys(Keys.TAB)
        actions.send_keys(Keys.NUMPAD0)
        actions.send_keys(Keys.NUMPAD5)
        actions.send_keys(Keys.NUMPAD2)
        actions.send_keys(Keys.NUMPAD5)
        actions.send_keys(Keys.TAB)
        actions.send_keys(Keys.NUMPAD3)
        actions.send_keys(Keys.NUMPAD4)
        actions.send_keys(Keys.NUMPAD6)
        actions.perform()
        driver.find_element(By.XPATH, "//button[contains(.,'Confirm and proceed')]").click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'Credit card not accepted')]")))
        print("Payment work correctly")

    def test08_fept_008_max(self):
        driver = self.driver
        driver.get("https://www.prada.com/us/en/login-register.html")
        wait = WebDriverWait(driver, 10)

        # Login to the account
        H.login(driver)
        print("User was successfully logged with correct data")

        # Title verify
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Start shopping')]")))
        try:
            title_check = driver.title == "Logged Area | PRADA"
            print("Title is correct. Test PASS!")
        except WDE:
            print("Incorrect title. Test FALL!")

        # Log out
        driver.find_element(By.XPATH, H.log_out_icon).click()
        driver.find_element(By.XPATH, H.log_out).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//body/div[3]/div[1]/div[2]/div[1]")))
        print("User was successful log out. Test PASS")

    def test09_feng_001_max(self):
        driver = self.driver
        driver.get("https://www.prada.com/us/en/login-register.html")
        wait = WebDriverWait(driver, 10)

        # Log In with wrong email
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text() = 'ACCEPT ALL']")))
        driver.find_element(By.XPATH, "//*[text() = 'ACCEPT ALL']").click()
        wait.until(EC.visibility_of_element_located((By.ID, "gigya-textbox-100719189608483120")))
        with open("email.txt", "r") as file:
            email_text = file.read().strip()
        driver.find_element(By.ID, "gigya-textbox-100719189608483120").send_keys("1" + email_text)
        driver.find_element(By.XPATH, "//input[contains(@value,'Next')]").click()
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@value='Register']")))
            print("User was redirected to register area. Test FALL")
        except WDE:
            wait.until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@value,'Login')]")))
            print("User was redirected to login area. Test FALL")

    def test10_feng_002_max(self):
        driver = self.driver
        driver.get("https://www.prada.com/us/en/login-register.html")
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text() = 'ACCEPT ALL']")))
        driver.find_element(By.XPATH, "//*[text() = 'ACCEPT ALL']").click()
        wait.until(EC.visibility_of_element_located((By.ID, "gigya-textbox-100719189608483120")))
        with open("email.txt", "r") as file:
            email_text = file.read().strip()
        driver.find_element(By.ID, "gigya-textbox-100719189608483120").send_keys(email_text)
        driver.find_element(By.XPATH, "//input[contains(@value,'Next')]").click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@value,'Login')]")))
        with open("pass.txt", "r") as file:
            pass_text = file.read().strip()
        driver.find_element(By.ID, "gigya-password-83462624292152350").send_keys(pass_text + "1")
        driver.find_element(By.XPATH, "//input[contains(@value,'Login')]").click()
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text() = "Invalid login or password"]')))
        print("User not abel to log in with wrong password. Test PASS")

    def test11_feng_003_max(self):
        driver = self.driver
        driver.get("https://www.prada.com/us/en/login-register.html")
        wait = WebDriverWait(driver, 10)

        # Login to the account
        H.login(driver)

        # Go to the payment form
        wait.until(EC.element_to_be_clickable((By.XPATH, H.cart_icon)))
        driver.find_element(By.XPATH, H.cart_icon).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text() = "Proceed to checkout"]')))
        driver.find_element(By.XPATH, '//*[text() = "Proceed to checkout"]').click()
        wait.until(EC.element_to_be_clickable((By.XPATH, H.confirm_address_checkout)))

        # If test will run not a first time some steps will be completed
        try:
            cac = driver.find_element(By.XPATH, '//*[text() = "Confirm"]')
            driver.execute_script("arguments[0].scrollIntoView(true)", cac)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text() = "Confirm"]')))
            driver.find_element(By.XPATH, '//*[text() = "Confirm"]').click()
            driver.find_element(By.XPATH, '//*[text() = "Confirm"]').click()
        except WDE:
            print("Confirm button wasn't appeared")
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text() = "Confirm and proceed"]')))
            driver.find_element(By.XPATH, '//*[text() = "Confirm and proceed"]').click()
        except WDE:
            print("Confirm and proceed button wasn't appeared")

        # Input wrong payment details
        wait.until(EC.element_to_be_clickable((By.XPATH, H.card_name)))
        driver.find_element(By.XPATH, H.card_name).send_keys(H.f_name)
        driver.find_element(By.XPATH, H.card_lname).send_keys(H.l_name)
        driver.find_element(By.XPATH, H.card_lname).click()
        time.sleep(1)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.send_keys(Keys.NUMPAD7)
        actions.send_keys(Keys.NUMPAD7)
        actions.send_keys(Keys.NUMPAD7)
        actions.send_keys(Keys.NUMPAD7)
        actions.send_keys(Keys.NUMPAD7)
        actions.send_keys(Keys.NUMPAD7)
        actions.send_keys(Keys.NUMPAD7)
        actions.send_keys(Keys.NUMPAD7)
        actions.send_keys(Keys.NUMPAD7)
        actions.send_keys(Keys.NUMPAD7)
        actions.send_keys(Keys.NUMPAD7)
        actions.send_keys(Keys.NUMPAD7)
        actions.send_keys(Keys.NUMPAD7)
        actions.send_keys(Keys.NUMPAD7)
        actions.send_keys(Keys.NUMPAD7)
        actions.send_keys(Keys.NUMPAD7)
        actions.send_keys(Keys.TAB)
        actions.send_keys(Keys.NUMPAD0)
        actions.send_keys(Keys.NUMPAD5)
        actions.send_keys(Keys.NUMPAD2)
        actions.send_keys(Keys.NUMPAD2)
        actions.send_keys(Keys.TAB)
        actions.send_keys(Keys.NUMPAD3)
        actions.send_keys(Keys.NUMPAD4)
        actions.send_keys(Keys.NUMPAD5)
        actions.perform()
        driver.find_element(By.XPATH, "//button[contains(.,'Confirm and proceed')]").click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'Credit card not accepted')]")))
        print("Incorrect credit card wasn't accepted. Test PASS")

    def test12_feng_004_max(self):
        driver = self.driver
        driver.get("https://www.prada.com/us/en/login-register.html")
        wait = WebDriverWait(driver, 10)

        # Login to the account
        H.login(driver)

        # Go to the personal information and delete address if it presents
        driver.find_element(By.XPATH, "//a[@href='#'][contains(.,'Personal information')]").click()
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, H.basket_del)))
            driver.find_element(By.XPATH, H.basket_del).click()
            wait.until(EC.element_to_be_clickable((By.XPATH, H.delete_confirm)))
            driver.find_element(By.XPATH, H.delete_confirm).click()
        except WDE:
            print("Address wasn't create previously")

        # Create new address with incorrect name
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Personal information')]")))
        driver.find_element(By.XPATH, '//*[contains(text(),"Add new shipping address")]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h3[contains(text(),'Shipping address')]")))
        driver.find_element(By.XPATH, "//input[contains(@id,'first_name_')]").send_keys("$$$")
        driver.find_element(By.XPATH, "//input[contains(@id,'last_name_')]").send_keys(H.l_name)
        driver.find_element(By.XPATH, "//input[contains(@id,'company_')]").send_keys(H.company)
        time.sleep(3)
        driver.find_element(By.XPATH, H.address_1).send_keys(H.add)
        driver.find_element(By.XPATH, "//input[contains(@id,'city_')]").send_keys(H.city)
        driver.find_element(By.XPATH, H.state_dd).click()
        scroll_to_state = driver.find_element(By.XPATH, H.state_city)
        driver.execute_script("arguments[0].scrollIntoView(true)", scroll_to_state)
        wait.until(EC.element_to_be_clickable((By.XPATH, H.state_city)))
        driver.find_element(By.XPATH, H.state_city).click()
        driver.find_element(By.XPATH, "//input[contains(@id,'zip_code_')]").send_keys(H.zip_code)
        driver.find_element(By.XPATH, "//input[contains(@id,'phone_')]").send_keys(H.phone)
        driver.find_element(By.XPATH, H.check_box).click()
        driver.find_element(By.XPATH, H.confirm).click()
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, '// *[contains(text(), "The First name field '
                                                                   'format is invalid")]')))
            print("User not abel to create address with incorrect name. Test PASS")
        except WDE:
            print("User abel to create address with incorrect name. Test FALL")
        wait.until(EC.visibility_of_element_located((By.XPATH, '// *[contains(text(), "The First name field format is '
                                                               'invalid")]')))

    def test13_feng_005_max(self):
        driver = self.driver
        driver.get("https://www.prada.com/us/en/login-register.html")
        wait = WebDriverWait(driver, 10)

        # Login to the account
        H.login(driver)

        # Go to the personal information and delete address if it presents
        driver.find_element(By.XPATH, "//a[@href='#'][contains(.,'Personal information')]").click()
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, H.basket_del)))
            driver.find_element(By.XPATH, H.basket_del).click()
            wait.until(EC.element_to_be_clickable((By.XPATH, H.delete_confirm)))
            driver.find_element(By.XPATH, H.delete_confirm).click()
        except WDE:
            print("Address wasn't create previously")

        # Create new address with incorrect address1
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Personal information')]")))
        driver.find_element(By.XPATH, '//*[contains(text(),"Add new shipping address")]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h3[contains(text(),'Shipping address')]")))
        driver.find_element(By.XPATH, "//input[contains(@id,'first_name_')]").send_keys(H.f_name)
        driver.find_element(By.XPATH, "//input[contains(@id,'last_name_')]").send_keys(H.l_name)
        driver.find_element(By.XPATH, "//input[contains(@id,'company_')]").send_keys(H.company)
        time.sleep(3)
        driver.find_element(By.XPATH, H.address_1).send_keys("$$$")
        driver.find_element(By.XPATH, "//input[contains(@id,'city_')]").send_keys(H.city)
        driver.find_element(By.XPATH, H.state_dd).click()
        scroll_to_state = driver.find_element(By.XPATH, H.state_city)
        driver.execute_script("arguments[0].scrollIntoView(true)", scroll_to_state)
        wait.until(EC.element_to_be_clickable((By.XPATH, H.state_city)))
        driver.find_element(By.XPATH, H.state_city).click()
        driver.find_element(By.XPATH, "//input[contains(@id,'zip_code_')]").send_keys(H.zip_code)
        driver.find_element(By.XPATH, "//input[contains(@id,'phone_')]").send_keys(H.phone)
        driver.find_element(By.XPATH, H.check_box).click()
        driver.find_element(By.XPATH, H.confirm).click()
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(.,'Cancel')])[7]")))
            print("User not abel to create address with incorrect address1. Test PASS")
        except WDE:
            print("User abel to create address with incorrect address1. Test FALL")
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(.,'Cancel')])[7]")))

    def test14_feng_006_max(self):
        driver = self.driver
        driver.get("https://www.prada.com/us/en/login-register.html")
        wait = WebDriverWait(driver, 10)

        # Login to the account
        H.login(driver)

        # Go to the personal information and delete address if it presents
        driver.find_element(By.XPATH, "//a[@href='#'][contains(.,'Personal information')]").click()
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, H.basket_del)))
            driver.find_element(By.XPATH, H.basket_del).click()
            wait.until(EC.element_to_be_clickable((By.XPATH, H.delete_confirm)))
            driver.find_element(By.XPATH, H.delete_confirm).click()
        except WDE:
            print("Address wasn't create previously")

        # Create new address with incorrect zip code
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Personal information')]")))
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
        wait.until(EC.element_to_be_clickable((By.XPATH, H.state_city)))
        driver.find_element(By.XPATH, H.state_city).click()
        driver.find_element(By.XPATH, "//input[contains(@id,'zip_code_')]").send_keys("0000")
        driver.find_element(By.XPATH, "//input[contains(@id,'phone_')]").send_keys(H.phone)
        driver.find_element(By.XPATH, H.check_box).click()
        driver.find_element(By.XPATH, H.confirm).click()
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[contains(text(),"The Zip code field format is '
                                                                   'invalid")]')))
            print("User not abel to create address with incorrect zip code. Test PASS")
        except WDE:
            print("User abel to create address with incorrect zip code. Test FALL")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[contains(text(),"The Zip code field format is '
                                                               'invalid")]')))

    def test15_feng_007_max(self):
        driver = self.driver
        driver.get("https://www.prada.com/us/en/login-register.html")
        wait = WebDriverWait(driver, 10)

        # Login to the account
        H.login(driver)

        # Go to the personal information and delete address if it presents
        driver.find_element(By.XPATH, "//a[@href='#'][contains(.,'Personal information')]").click()
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, H.basket_del)))
            driver.find_element(By.XPATH, H.basket_del).click()
            wait.until(EC.element_to_be_clickable((By.XPATH, H.delete_confirm)))
            driver.find_element(By.XPATH, H.delete_confirm).click()
        except WDE:
            print("Address wasn't create previously")

        # Create new address with incorrect city
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Personal information')]")))
        driver.find_element(By.XPATH, '//*[contains(text(),"Add new shipping address")]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h3[contains(text(),'Shipping address')]")))
        driver.find_element(By.XPATH, "//input[contains(@id,'first_name_')]").send_keys(H.f_name)
        driver.find_element(By.XPATH, "//input[contains(@id,'last_name_')]").send_keys(H.l_name)
        driver.find_element(By.XPATH, "//input[contains(@id,'company_')]").send_keys(H.company)
        time.sleep(3)
        driver.find_element(By.XPATH, H.address_1).send_keys(H.add)
        driver.find_element(By.XPATH, "//input[contains(@id,'city_')]").send_keys("$$$")
        driver.find_element(By.XPATH, H.state_dd).click()
        scroll_to_state = driver.find_element(By.XPATH, H.state_city)
        driver.execute_script("arguments[0].scrollIntoView(true)", scroll_to_state)
        wait.until(EC.element_to_be_clickable((By.XPATH, H.state_city)))
        driver.find_element(By.XPATH, H.state_city).click()
        driver.find_element(By.XPATH, "//input[contains(@id,'zip_code_')]").send_keys(H.zip_code)
        driver.find_element(By.XPATH, "//input[contains(@id,'phone_')]").send_keys(H.phone)
        driver.find_element(By.XPATH, H.check_box).click()
        driver.find_element(By.XPATH, H.confirm).click()
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[contains(.,'Cancel')])[7]")))
            print("User not abel to create address with incorrect city. Test PASS")
            locator = "(//a[contains(.,'Cancel')])[7]"
        except WDE:
            locator = "//span[contains(.,'The address you entered seems to have some incorrect information')]"
            print("User not abel to create address with incorrect city. Test PASS")
        wait.until(EC.visibility_of_element_located((By.XPATH, locator)))

    def test16_feng_008_max(self):
        driver = self.driver
        driver.get("https://www.prada.com/us/en/login-register.html")
        wait = WebDriverWait(driver, 10)

        # Login to the account
        H.login(driver)

        # Go to the personal information and delete address if it presents
        driver.find_element(By.XPATH, "//a[@href='#'][contains(.,'Personal information')]").click()
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, H.basket_del)))
            driver.find_element(By.XPATH, H.basket_del).click()
            wait.until(EC.element_to_be_clickable((By.XPATH, H.delete_confirm)))
            driver.find_element(By.XPATH, H.delete_confirm).click()
        except WDE:
            print("Address wasn't create previously")

        # Create new address with incorrect phone number
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Personal information')]")))
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
        wait.until(EC.element_to_be_clickable((By.XPATH, H.state_city)))
        driver.find_element(By.XPATH, H.state_city).click()
        driver.find_element(By.XPATH, "//input[contains(@id,'zip_code_')]").send_keys(H.zip_code)
        driver.find_element(By.XPATH, "//input[contains(@id,'phone_')]").send_keys("000000")
        driver.find_element(By.XPATH, H.check_box).click()
        driver.find_element(By.XPATH, H.confirm).click()
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, '// *[contains(text(), "The Phone field format is '
                                                                   'invalid")]')))
            print("User not abel to create address with incorrect phone number. Test PASS")
        except WDE:
            print("User abel to create address with incorrect phone number. Test FALL")
        wait.until(EC.visibility_of_element_located((By.XPATH, '// *[contains(text(), "The Phone field format is '
                                                               'invalid")]')))

    def test17_febd_001_max(self):
        driver = self.driver
        driver.get("https://internxt.com/temporary-email")
        wait = WebDriverWait(driver, 50)

        # Get email
        time.sleep(2)
        driver.find_element(By.XPATH, "//p[contains(text(),'Copy email')]").click()

        # Open new tab "prada.com" and star registration
        driver.switch_to.new_window('tab')
        driver.get("https://www.prada.com/us/en.html")
        driver.find_element(By.XPATH, "//div[@class='banner_cta cta_accept'][contains(.,'ACCEPT ALL')]").click()
        driver.find_element(By.XPATH, "//span[contains(@class,'utils__icon pr-icon-new-login')]").click()
        wait.until(EC.visibility_of_element_located((By.ID, "gigya-textbox-100719189608483120")))
        driver.find_element(By.ID, "gigya-textbox-100719189608483120").send_keys(Keys.CONTROL + "v")
        driver.find_element(By.XPATH, "//input[contains(@value,'Next')]").click()
        time.sleep(10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Resend')]")))

        # Switch to temporary email and wait for verification code
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

        # Switch to prada tab and complete registration
        driver.switch_to.window(driver.window_handles[1])
        driver.find_element(By.XPATH, '//*[@placeholder="Verification code*"]').send_keys(code)
        driver.find_element(By.XPATH, H.drop_down).click()
        driver.find_element(By.ID, "gigya-textbox-105760616358098000").send_keys(H.f_name)
        driver.find_element(By.ID, "gigya-textbox-21007040083017830").send_keys(H.l_name)
        driver.find_element(By.ID, "gigya-textbox-74329674452397740").send_keys(H.mm_dd)
        driver.find_element(By.ID, "gigya-password-60262223393983710").send_keys("Df1!0:-")
        driver.find_element(By.ID, "visibleTextMarketing").click()
        driver.find_element(By.XPATH, "//input[@value='Register']").click()
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(.,'Check that your password "
                                                                   "respects the criteria.')]")))
            print("User can't create account with weak password. Test PASS")
        except WDE:
            print("User can create account with weak password.. Test FALL")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(.,'Check that your password respects "
                                                               "the criteria.')]")))

    def test18_febd_002_max(self):
        driver = self.driver
        driver.get("https://internxt.com/temporary-email")
        wait = WebDriverWait(driver, 50)

        # Get email
        time.sleep(2)
        driver.find_element(By.XPATH, "//p[contains(text(),'Copy email')]").click()

        # Open new tab "prada.com" and star registration
        driver.switch_to.new_window('tab')
        driver.get("https://www.prada.com/us/en.html")
        driver.find_element(By.XPATH, "//div[@class='banner_cta cta_accept'][contains(.,'ACCEPT ALL')]").click()
        driver.find_element(By.XPATH, "//span[contains(@class,'utils__icon pr-icon-new-login')]").click()
        wait.until(EC.visibility_of_element_located((By.ID, "gigya-textbox-100719189608483120")))
        driver.find_element(By.ID, "gigya-textbox-100719189608483120").send_keys(Keys.CONTROL + "v")
        driver.find_element(By.XPATH, "//input[contains(@value,'Next')]").click()
        time.sleep(10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Resend')]")))

        # Switch to temporary email and wait for verification code
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

        # Switch to prada tab and complete registration
        driver.switch_to.window(driver.window_handles[1])
        driver.find_element(By.XPATH, '//*[@placeholder="Verification code*"]').send_keys(code)
        driver.find_element(By.XPATH, H.drop_down).click()
        driver.find_element(By.ID, "gigya-textbox-105760616358098000").send_keys(H.f_name)
        driver.find_element(By.ID, "gigya-textbox-21007040083017830").send_keys(H.l_name)
        driver.find_element(By.ID, "gigya-textbox-74329674452397740").send_keys(H.mm_dd)
        driver.find_element(By.ID, "gigya-password-60262223393983710").send_keys("Df1!0:-a")
        driver.find_element(By.ID, "visibleTextMarketing").click()
        driver.find_element(By.XPATH, "//input[@value='Register']").click()

        # Registration validation
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(@class,'utils__icon pr-icon-new-bag')]")))
        try:
            title_check = driver.title == "Prada Official Website | Thinking fashion since 1913 | PRADA"
            print("Title is correct. Test PASS!")
        except WDE:
            print("Incorrect title. Test FALL!")

    def test19_febd_003_max(self):
        driver = self.driver
        driver.get("https://internxt.com/temporary-email")
        wait = WebDriverWait(driver, 50)

        # Get email
        time.sleep(2)
        driver.find_element(By.XPATH, "//p[contains(text(),'Copy email')]").click()

        # Open new tab "prada.com" and star registration
        driver.switch_to.new_window('tab')
        driver.get("https://www.prada.com/us/en.html")
        driver.find_element(By.XPATH, "//div[@class='banner_cta cta_accept'][contains(.,'ACCEPT ALL')]").click()
        driver.find_element(By.XPATH, "//span[contains(@class,'utils__icon pr-icon-new-login')]").click()
        wait.until(EC.visibility_of_element_located((By.ID, "gigya-textbox-100719189608483120")))
        driver.find_element(By.ID, "gigya-textbox-100719189608483120").send_keys(Keys.CONTROL + "v")
        driver.find_element(By.XPATH, "//input[contains(@value,'Next')]").click()
        time.sleep(10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Resend')]")))

        # Switch to temporary email and wait for verification code
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

        # Switch to prada tab and complete registration
        driver.switch_to.window(driver.window_handles[1])
        driver.find_element(By.XPATH, '//*[@placeholder="Verification code*"]').send_keys(code)
        driver.find_element(By.XPATH, H.drop_down).click()
        driver.find_element(By.ID, "gigya-textbox-105760616358098000").send_keys(H.f_name)
        driver.find_element(By.ID, "gigya-textbox-21007040083017830").send_keys(H.l_name)
        driver.find_element(By.ID, "gigya-textbox-74329674452397740").send_keys(H.mm_dd)
        driver.find_element(By.ID, "gigya-password-60262223393983710").send_keys("Df1!0:-as")
        driver.find_element(By.ID, "visibleTextMarketing").click()
        driver.find_element(By.XPATH, "//input[@value='Register']").click()

        # Registration validation
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(@class,'utils__icon pr-icon-new-bag')]")))
        try:
            title_check = driver.title == "Prada Official Website | Thinking fashion since 1913 | PRADA"
            print("Title is correct. Test PASS!")
        except WDE:
            print("Incorrect title. Test FALL!")

    def test20_febd_004_max(self):
        driver = self.driver
        driver.get("https://internxt.com/temporary-email")
        wait = WebDriverWait(driver, 50)

        # Get email
        time.sleep(2)
        driver.find_element(By.XPATH, "//p[contains(text(),'Copy email')]").click()

        # Open new tab "prada.com" and star registration
        driver.switch_to.new_window('tab')
        driver.get("https://www.prada.com/us/en.html")
        driver.find_element(By.XPATH, "//div[@class='banner_cta cta_accept'][contains(.,'ACCEPT ALL')]").click()
        driver.find_element(By.XPATH, "//span[contains(@class,'utils__icon pr-icon-new-login')]").click()
        wait.until(EC.visibility_of_element_located((By.ID, "gigya-textbox-100719189608483120")))
        driver.find_element(By.ID, "gigya-textbox-100719189608483120").send_keys(Keys.CONTROL + "v")
        driver.find_element(By.XPATH, "//input[contains(@value,'Next')]").click()
        time.sleep(10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Resend')]")))

        # Switch to temporary email and wait for verification code
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

        # Switch to prada tab and complete registration
        driver.switch_to.window(driver.window_handles[1])
        driver.find_element(By.XPATH, '//*[@placeholder="Verification code*"]').send_keys(code)
        driver.find_element(By.XPATH, H.drop_down).click()
        driver.find_element(By.ID, "gigya-textbox-105760616358098000").send_keys(H.f_name)
        driver.find_element(By.ID, "gigya-textbox-21007040083017830").send_keys(H.l_name)
        driver.find_element(By.ID, "gigya-textbox-74329674452397740").send_keys(H.mm_dd)
        driver.find_element(By.ID, "gigya-password-60262223393983710").send_keys("Df1!0:-asDf1!0:")
        driver.find_element(By.ID, "visibleTextMarketing").click()
        driver.find_element(By.XPATH, "//input[@value='Register']").click()

        # Registration validation
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(@class,'utils__icon pr-icon-new-bag')]")))
        try:
            title_check = driver.title == "Prada Official Website | Thinking fashion since 1913 | PRADA"
            print("Title is correct. Test PASS!")
        except WDE:
            print("Incorrect title. Test FALL!")

    def test21_febd_005_max(self):
        driver = self.driver
        driver.get("https://internxt.com/temporary-email")
        wait = WebDriverWait(driver, 50)

        # Get email
        time.sleep(2)
        driver.find_element(By.XPATH, "//p[contains(text(),'Copy email')]").click()

        # Open new tab "prada.com" and star registration
        driver.switch_to.new_window('tab')
        driver.get("https://www.prada.com/us/en.html")
        driver.find_element(By.XPATH, "//div[@class='banner_cta cta_accept'][contains(.,'ACCEPT ALL')]").click()
        driver.find_element(By.XPATH, "//span[contains(@class,'utils__icon pr-icon-new-login')]").click()
        wait.until(EC.visibility_of_element_located((By.ID, "gigya-textbox-100719189608483120")))
        driver.find_element(By.ID, "gigya-textbox-100719189608483120").send_keys(Keys.CONTROL + "v")
        driver.find_element(By.XPATH, "//input[contains(@value,'Next')]").click()
        time.sleep(10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Resend')]")))

        # Switch to temporary email and wait for verification code
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

        # Switch to prada tab and complete registration
        driver.switch_to.window(driver.window_handles[1])
        driver.find_element(By.XPATH, '//*[@placeholder="Verification code*"]').send_keys(code)
        driver.find_element(By.XPATH, H.drop_down).click()
        driver.find_element(By.ID, "gigya-textbox-105760616358098000").send_keys(H.f_name)
        driver.find_element(By.ID, "gigya-textbox-21007040083017830").send_keys(H.l_name)
        driver.find_element(By.ID, "gigya-textbox-74329674452397740").send_keys(H.mm_dd)
        driver.find_element(By.ID, "gigya-password-60262223393983710").send_keys("Df1!0:-asDf1!0:-")
        driver.find_element(By.ID, "visibleTextMarketing").click()
        driver.find_element(By.XPATH, "//input[@value='Register']").click()

        # Registration validation
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(@class,'utils__icon pr-icon-new-bag')]")))
        try:
            title_check = driver.title == "Prada Official Website | Thinking fashion since 1913 | PRADA"
            print("Title is correct. Test PASS!")
        except WDE:
            print("Incorrect title. Test FALL!")

    def test22_febd_006_max(self):
        driver = self.driver
        driver.get("https://internxt.com/temporary-email")
        wait = WebDriverWait(driver, 50)

        # Get email
        time.sleep(2)
        driver.find_element(By.XPATH, "//p[contains(text(),'Copy email')]").click()

        # Open new tab "prada.com" and star registration
        driver.switch_to.new_window('tab')
        driver.get("https://www.prada.com/us/en.html")
        driver.find_element(By.XPATH, "//div[@class='banner_cta cta_accept'][contains(.,'ACCEPT ALL')]").click()
        driver.find_element(By.XPATH, "//span[contains(@class,'utils__icon pr-icon-new-login')]").click()
        wait.until(EC.visibility_of_element_located((By.ID, "gigya-textbox-100719189608483120")))
        driver.find_element(By.ID, "gigya-textbox-100719189608483120").send_keys(Keys.CONTROL + "v")
        driver.find_element(By.XPATH, "//input[contains(@value,'Next')]").click()
        time.sleep(10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Resend')]")))

        # Switch to temporary email and wait for verification code
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

        # Switch to prada tab and complete registration
        driver.switch_to.window(driver.window_handles[1])
        driver.find_element(By.XPATH, '//*[@placeholder="Verification code*"]').send_keys(code)
        driver.find_element(By.XPATH, H.drop_down).click()
        driver.find_element(By.ID, "gigya-textbox-105760616358098000").send_keys(H.f_name)
        driver.find_element(By.ID, "gigya-textbox-21007040083017830").send_keys(H.l_name)
        driver.find_element(By.ID, "gigya-textbox-74329674452397740").send_keys(H.mm_dd)
        driver.find_element(By.ID, "gigya-password-60262223393983710").send_keys("Df1!0:-asDf1!0:-a")
        driver.find_element(By.ID, "visibleTextMarketing").click()
        driver.find_element(By.XPATH, "//input[@value='Register']").click()
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(.,'Check that your password "
                                                                   "respects the criteria.')]")))
            print("User can't create account with weak password. Test PASS")
        except WDE:
            print("User can create account with weak password.. Test FALL")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(.,'Check that your password respects "
                                                               "the criteria.')]")))

    def tearDown(self):
        self.driver.quit()


class Firefox(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.set_window_size(width, height)

    def test01_fept_001_max(self):
        driver = self.driver
        driver.get("https://internxt.com/temporary-email")
        wait = WebDriverWait(driver, 50)

        # Get email
        time.sleep(2)
        driver.find_element(By.XPATH, "//p[contains(text(),'Copy email')]").click()

        # Save email in the email.txt file
        email = driver.find_element(By.XPATH,
                                    '//*[@class="flex h-full w-full cursor-pointer flex-row items-center '
                                    'justify-between rounded-xl bg-gray-1 shadow-sm  px-4 py-3"]').text
        with open("email.txt", "w") as file:
            file.write(email)

        # Save password as pass.txt file
        password = "p@sSword" + str(random.randint(0, 999))
        with open("pass.txt", "w") as file:
            file.write(password)

        # Open new tab "prada.com" and star registration
        driver.switch_to.new_window('tab')
        driver.get("https://www.prada.com/us/en.html")
        driver.find_element(By.XPATH, "//div[@class='banner_cta cta_accept'][contains(.,'ACCEPT ALL')]").click()
        driver.find_element(By.XPATH, "//span[contains(@class,'utils__icon pr-icon-new-login')]").click()
        wait.until(EC.visibility_of_element_located((By.ID, "gigya-textbox-100719189608483120")))
        driver.find_element(By.ID, "gigya-textbox-100719189608483120").send_keys(Keys.CONTROL + "v")
        driver.find_element(By.XPATH, "//input[contains(@value,'Next')]").click()
        time.sleep(10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Resend')]")))

        # Switch to temporary email and wait for verification code
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

        # Switch to prada tab and complete registration
        driver.switch_to.window(driver.window_handles[1])
        driver.find_element(By.XPATH, '//*[@placeholder="Verification code*"]').send_keys(code)
        driver.find_element(By.XPATH, H.drop_down).click()
        driver.find_element(By.ID, "gigya-textbox-105760616358098000").send_keys(H.f_name)
        driver.find_element(By.ID, "gigya-textbox-21007040083017830").send_keys(H.l_name)
        driver.find_element(By.ID, "gigya-textbox-74329674452397740").send_keys(H.mm_dd)
        driver.find_element(By.ID, "gigya-password-60262223393983710").send_keys(password)
        driver.find_element(By.ID, "visibleTextMarketing").click()
        driver.find_element(By.XPATH, "//input[@value='Register']").click()
        print("Verification code was correct")

        # Registration validation
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(@class,'utils__icon pr-icon-new-bag')]")))
        try:
            title_check = driver.title == "Prada Official Website | Thinking fashion since 1913 | PRADA"
            print("Title is correct. Test PASS!")
        except WDE:
            print("Incorrect title. Test FALL!")
        print("Account was successful created")

    def test02_fept_002_max(self):
        driver = self.driver
        driver.get("https://www.prada.com/us/en/login-register.html")
        wait = WebDriverWait(driver, 10)

        # Login to the account
        H.login(driver)

        # Open the address form menu
        driver.find_element(By.XPATH, H.log_icon).click()
        driver.find_element(By.XPATH, H.address_dd).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Personal information')]")))
        try:
            title_check = driver.title == H.address_title
            print("Title is correct. Test PASS!")
        except WDE:
            print("Incorrect title. Test FALL!")
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
        wait.until(EC.element_to_be_clickable((By.XPATH, H.state_city)))
        driver.find_element(By.XPATH, H.state_city).click()
        driver.find_element(By.XPATH, "//input[contains(@id,'zip_code_')]").send_keys(H.zip_code)
        driver.find_element(By.XPATH, "//input[contains(@id,'phone_')]").send_keys(H.phone)
        driver.find_element(By.XPATH, H.check_box).click()
        driver.find_element(By.XPATH, H.confirm).click()
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, H.confirm_2)))
            driver.find_element(By.XPATH, H.confirm_2).click()
        except WDE:
            wait.until(EC.visibility_of_element_located((By.XPATH, H.ship_address)))
        wait.until(EC.visibility_of_element_located((By.XPATH, H.ship_address)))

        # Shipping and billing addresses verification
        shipp = driver.find_element(By.XPATH, H.ship_address).text
        bill = driver.find_element(By.XPATH, H.bill_address).text
        try:
            address_check = shipp == bill
            print("Shipping and billing addresses are correct. Test PASS!")
        except WDE:
            print("Shipping and billing addresses are incorrect. Test FALL!")
        print("Address was successful created")

    def test03_fept_003_max(self):
        driver = self.driver
        driver.get("https://www.prada.com/us/en/login-register.html")
        wait = WebDriverWait(driver, 10)

        # Login to the account
        H.login(driver)

        # Open the address form menu
        driver.find_element(By.XPATH, H.log_icon).click()
        driver.find_element(By.XPATH, H.address_dd).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Personal information')]")))

        # Address change functionality
        wait.until(EC.visibility_of_element_located((By.XPATH, H.address_change)))
        wait.until(EC.element_to_be_clickable((By.XPATH, H.address_change)))
        driver.find_element(By.XPATH, H.address_change).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, H.address_1)))
        driver.find_element(By.XPATH, H.address_1).send_keys(Keys.CONTROL + "a")
        driver.find_element(By.XPATH, H.address_1).send_keys(Keys.DELETE)
        driver.find_element(By.XPATH, H.address_1).send_keys(H.add_new)
        driver.find_element(By.XPATH, "//input[contains(@id,'city_')]").send_keys(Keys.CONTROL + "a")
        driver.find_element(By.XPATH, "//input[contains(@id,'city_')]").send_keys(Keys.DELETE)
        driver.find_element(By.XPATH, "//input[contains(@id,'city_')]").send_keys(H.city_new)
        driver.find_element(By.XPATH, H.state_dd).click()
        scroll_to_state = driver.find_element(By.XPATH, H.state_city_new)
        driver.execute_script("arguments[0].scrollIntoView(true)", scroll_to_state)
        wait.until(EC.element_to_be_clickable((By.XPATH, H.state_city_new)))
        driver.find_element(By.XPATH, H.state_city_new).click()
        driver.find_element(By.XPATH, "//input[contains(@id,'zip_code_')]").send_keys(Keys.CONTROL + "a")
        driver.find_element(By.XPATH, "//input[contains(@id,'zip_code_')]").send_keys(Keys.DELETE)
        driver.find_element(By.XPATH, "//input[contains(@id,'zip_code_')]").send_keys(H.zip_code_new)
        driver.find_element(By.XPATH, H.check_box).click()
        driver.find_element(By.XPATH, H.confirm).click()
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, H.confirm_2)))
            driver.find_element(By.XPATH, H.confirm_2).click()
        except WDE:
            wait.until(EC.visibility_of_element_located((By.XPATH, H.ship_address)))
        wait.until(EC.visibility_of_element_located((By.XPATH, H.ship_address)))
        print("Address was successfully changed")

    def test04_fept_004_max(self):
        driver = self.driver
        driver.get("https://www.prada.com/us/en/login-register.html")
        wait = WebDriverWait(driver, 20)

        # Login to the account
        H.login(driver)

        # Go to Prada-Edition bag
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(.,'Bags')]")))
        driver.find_element(By.XPATH, "//span[contains(.,'Bags')]").click()
        driver.find_element(By.XPATH, H.re_edition).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, H.bag_img)))
        driver.find_element(By.XPATH, H.bag_img).click()

        # Buy mint green, white and orange bags Prada-Edition
        wait.until(EC.element_to_be_clickable((By.XPATH, H.add_shop_bag)))
        driver.find_element(By.XPATH, H.bag_mintgreen_button).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, H.bag_mintgreen_img)))
        time.sleep(2)
        driver.find_element(By.XPATH, H.add_shop_bag).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, H.check_out)))
        driver.find_element(By.XPATH, H.cross).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, H.add_shop_bag)))
        driver.find_element(By.XPATH, H.bag_white_button).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, H.bag_white_img)))
        time.sleep(2)
        driver.find_element(By.XPATH, H.add_shop_bag).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, H.check_out)))
        driver.find_element(By.XPATH, H.cross).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, H.add_shop_bag)))
        driver.find_element(By.XPATH, H.bag_orange_button).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, H.bag_orange_img)))
        time.sleep(2)
        driver.find_element(By.XPATH, H.add_shop_bag).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, H.check_out)))
        driver.find_element(By.XPATH, H.cross).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, H.add_shop_bag)))

        # Verify quantity in the cart
        cart_quantity = driver.find_element(By.XPATH, "//span[contains(.,'Your selection (')]").text
        try:
            cart_quantity_check = cart_quantity == "3"
            print("Correct quantity. Test PASS!")
        except WDE:
            print("Incorrect quantity. Test FALL")

    def test05_fept_005_max(self):
        driver = self.driver
        driver.get("https://www.prada.com/us/en/login-register.html")
        wait = WebDriverWait(driver, 10)

        # Login to the account
        H.login(driver)

        # Go to "Home and decor"
        driver.find_element(By.XPATH, "//span[contains(text(),'HOME')]").click()
        driver.find_element(By.XPATH, H.home_decor).click()
        wait.until(EC.title_is("Prada Home: Home Decor and Accessories | PRADA"))
        driver.find_element(By.XPATH, H.show_more).click()

        # Buy "Saffiano leather Go set"
        wait.until(EC.element_to_be_clickable((By.XPATH, H.go_set)))
        driver.find_element(By.XPATH, H.go_set).click()

        # Webpage link verify
        try:
            link_check = driver.page_source == "https://prada.com/us/en/p/saffiano-leather-go-set/2SG008_0DC_F0002"
            print("Webpage like text is correct. PASS!")
        except TimeoutException:
            print("Webpage like text is incorrect. FALL!")

        # Buy Go and remove from the cart
        wait.until(EC.element_to_be_clickable((By.XPATH, H.add_shop_bag)))
        driver.find_element(By.XPATH, H.add_shop_bag).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'Remove')])[1]")))
        driver.find_element(By.XPATH, "(//span[contains(.,'Remove')])[1]").click()
        wait.until_not(EC.visibility_of_element_located((By.XPATH, H.go_img)))

        # Verify item was removed
        cart_quantity = driver.find_element(By.XPATH, "//span[contains(.,'Your selection (')]").text
        try:
            cart_quantity_check = cart_quantity == "3"
            print("Correct quantity. Test PASS!")
        except WDE:
            print("Incorrect quantity. Test FALL")

    def test06_fept_006_max(self):
        driver = self.driver
        driver.get("https://www.prada.com/us/en/login-register.html")
        wait = WebDriverWait(driver, 10)

        # Login to the account
        H.login(driver)

        driver.find_element(By.XPATH, "//span[@class='menu__linkText'][contains(.,'Beauty and Fragrances')]").click()
        driver.find_element(By.XPATH, H.frag_dd).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, H.frag_img)))
        driver.find_element(By.XPATH, H.frag_img).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, H.add_shop_bag)))
        driver.find_element(By.XPATH, H.add_shop_bag).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Go to shopping bag')]")))
        driver.find_element(By.XPATH, "//button[contains(.,'Go to shopping bag')]").click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(.,'Edit')])[1]")))
        driver.find_element(By.XPATH, "(//span[contains(.,'Edit')])[1]").click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='pr-icon-add']")))
        driver.find_element(By.XPATH, "//span[@class='pr-icon-add']").click()
        driver.find_element(By.XPATH, "//span[@class='pr-icon-add']").click()
        driver.find_element(By.XPATH, "//span[@class='pr-icon-add']").click()
        driver.find_element(By.XPATH, "//span[@class='pr-icon-add']").click()
        quantity_edit = driver.find_element(By.XPATH, '//*[@class="detail-product-quantity-selector__value"]').text
        try:
            quantity_edit_check = quantity_edit == "5"
            print("Correct quantity. Test PASS!")
        except WDE:
            print("Incorrect quantity. Test FALL")
        driver.find_element(By.XPATH, H.confirm_cart).click()

    def test07_fept_007_max(self):
        driver = self.driver
        driver.get("https://www.prada.com/us/en/login-register.html")
        wait = WebDriverWait(driver, 10)

        # Login to the account
        H.login(driver)

        # Go to the payment form
        wait.until(EC.element_to_be_clickable((By.XPATH, H.cart_icon)))
        driver.find_element(By.XPATH, H.cart_icon).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text() = "Proceed to checkout"]')))
        driver.find_element(By.XPATH, '//*[text() = "Proceed to checkout"]').click()
        wait.until(EC.element_to_be_clickable((By.XPATH, H.confirm_address_checkout)))

        # If test will run not a first time some steps will be completed
        try:
            cac = driver.find_element(By.XPATH, '//*[text() = "Confirm"]')
            driver.execute_script("arguments[0].scrollIntoView(true)", cac)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text() = "Confirm"]')))
            driver.find_element(By.XPATH, '//*[text() = "Confirm"]').click()
            driver.find_element(By.XPATH, '//*[text() = "Confirm"]').click()
        except WDE:
            print("Confirm button wasn't appeared")
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text() = "Confirm and proceed"]')))
            driver.find_element(By.XPATH, '//*[text() = "Confirm and proceed"]').click()
        except WDE:
            print("Confirm and proceed button wasn't appeared")

        # Input payment details (because this is tested example I use uncorrected card details for positive testing)
        wait.until(EC.element_to_be_clickable((By.XPATH, H.card_name)))
        driver.find_element(By.XPATH, H.card_name).send_keys(H.f_name)
        driver.find_element(By.XPATH, H.card_lname).send_keys(H.l_name)
        driver.find_element(By.XPATH, H.card_lname).click()
        time.sleep(1)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.send_keys(Keys.NUMPAD1)
        actions.send_keys(Keys.NUMPAD1)
        actions.send_keys(Keys.NUMPAD1)
        actions.send_keys(Keys.NUMPAD1)
        actions.send_keys(Keys.NUMPAD1)
        actions.send_keys(Keys.NUMPAD1)
        actions.send_keys(Keys.NUMPAD1)
        actions.send_keys(Keys.NUMPAD1)
        actions.send_keys(Keys.NUMPAD1)
        actions.send_keys(Keys.NUMPAD1)
        actions.send_keys(Keys.NUMPAD1)
        actions.send_keys(Keys.NUMPAD1)
        actions.send_keys(Keys.NUMPAD1)
        actions.send_keys(Keys.NUMPAD1)
        actions.send_keys(Keys.NUMPAD1)
        actions.send_keys(Keys.NUMPAD1)
        actions.send_keys(Keys.TAB)
        actions.send_keys(Keys.NUMPAD0)
        actions.send_keys(Keys.NUMPAD5)
        actions.send_keys(Keys.NUMPAD2)
        actions.send_keys(Keys.NUMPAD5)
        actions.send_keys(Keys.TAB)
        actions.send_keys(Keys.NUMPAD3)
        actions.send_keys(Keys.NUMPAD4)
        actions.send_keys(Keys.NUMPAD6)
        actions.perform()
        driver.find_element(By.XPATH, "//button[contains(.,'Confirm and proceed')]").click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'Credit card not accepted')]")))
        print("Payment work correctly")

    def test08_fept_008_max(self):
        driver = self.driver
        driver.get("https://www.prada.com/us/en/login-register.html")
        wait = WebDriverWait(driver, 10)

        # Login to the account
        H.login(driver)
        print("User was successfully logged with correct data")

        # Title verify
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Start shopping')]")))
        try:
            title_check = driver.title == "Logged Area | PRADA"
            print("Title is correct. Test PASS!")
        except WDE:
            print("Incorrect title. Test FALL!")

        # Log out
        driver.find_element(By.XPATH, H.log_out_icon).click()
        driver.find_element(By.XPATH, H.log_out).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//body/div[3]/div[1]/div[2]/div[1]")))
        print("User was successful log out. Test PASS")

    def test09_feng_001_max(self):
        driver = self.driver
        driver.get("https://www.prada.com/us/en/login-register.html")
        wait = WebDriverWait(driver, 10)

        # Log In with wrong email
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text() = 'ACCEPT ALL']")))
        driver.find_element(By.XPATH, "//*[text() = 'ACCEPT ALL']").click()
        wait.until(EC.visibility_of_element_located((By.ID, "gigya-textbox-100719189608483120")))
        with open("email.txt", "r") as file:
            email_text = file.read().strip()
        driver.find_element(By.ID, "gigya-textbox-100719189608483120").send_keys("1" + email_text)
        driver.find_element(By.XPATH, "//input[contains(@value,'Next')]").click()
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@value='Register']")))
            print("User was redirected to register area. Test FALL")
        except WDE:
            wait.until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@value,'Login')]")))
            print("User was redirected to login area. Test FALL")

    def test10_feng_002_max(self):
        driver = self.driver
        driver.get("https://www.prada.com/us/en/login-register.html")
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text() = 'ACCEPT ALL']")))
        driver.find_element(By.XPATH, "//*[text() = 'ACCEPT ALL']").click()
        wait.until(EC.visibility_of_element_located((By.ID, "gigya-textbox-100719189608483120")))
        with open("email.txt", "r") as file:
            email_text = file.read().strip()
        driver.find_element(By.ID, "gigya-textbox-100719189608483120").send_keys(email_text)
        driver.find_element(By.XPATH, "//input[contains(@value,'Next')]").click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@value,'Login')]")))
        with open("pass.txt", "r") as file:
            pass_text = file.read().strip()
        driver.find_element(By.ID, "gigya-password-83462624292152350").send_keys(pass_text + "1")
        driver.find_element(By.XPATH, "//input[contains(@value,'Login')]").click()
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text() = "Invalid login or password"]')))
        print("User not abel to log in with wrong password. Test PASS")

    def test11_feng_003_max(self):
        driver = self.driver
        driver.get("https://www.prada.com/us/en/login-register.html")
        wait = WebDriverWait(driver, 10)

        # Login to the account
        H.login(driver)

        # Go to the payment form
        wait.until(EC.element_to_be_clickable((By.XPATH, H.cart_icon)))
        driver.find_element(By.XPATH, H.cart_icon).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text() = "Proceed to checkout"]')))
        driver.find_element(By.XPATH, '//*[text() = "Proceed to checkout"]').click()
        wait.until(EC.element_to_be_clickable((By.XPATH, H.confirm_address_checkout)))

        # If test will run not a first time some steps will be completed
        try:
            cac = driver.find_element(By.XPATH, '//*[text() = "Confirm"]')
            driver.execute_script("arguments[0].scrollIntoView(true)", cac)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text() = "Confirm"]')))
            driver.find_element(By.XPATH, '//*[text() = "Confirm"]').click()
            driver.find_element(By.XPATH, '//*[text() = "Confirm"]').click()
        except WDE:
            print("Confirm button wasn't appeared")
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text() = "Confirm and proceed"]')))
            driver.find_element(By.XPATH, '//*[text() = "Confirm and proceed"]').click()
        except WDE:
            print("Confirm and proceed button wasn't appeared")

        # Input wrong payment details
        wait.until(EC.element_to_be_clickable((By.XPATH, H.card_name)))
        driver.find_element(By.XPATH, H.card_name).send_keys(H.f_name)
        driver.find_element(By.XPATH, H.card_lname).send_keys(H.l_name)
        driver.find_element(By.XPATH, H.card_lname).click()
        time.sleep(1)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB)
        actions.send_keys(Keys.NUMPAD7)
        actions.send_keys(Keys.NUMPAD7)
        actions.send_keys(Keys.NUMPAD7)
        actions.send_keys(Keys.NUMPAD7)
        actions.send_keys(Keys.NUMPAD7)
        actions.send_keys(Keys.NUMPAD7)
        actions.send_keys(Keys.NUMPAD7)
        actions.send_keys(Keys.NUMPAD7)
        actions.send_keys(Keys.NUMPAD7)
        actions.send_keys(Keys.NUMPAD7)
        actions.send_keys(Keys.NUMPAD7)
        actions.send_keys(Keys.NUMPAD7)
        actions.send_keys(Keys.NUMPAD7)
        actions.send_keys(Keys.NUMPAD7)
        actions.send_keys(Keys.NUMPAD7)
        actions.send_keys(Keys.NUMPAD7)
        actions.send_keys(Keys.TAB)
        actions.send_keys(Keys.NUMPAD0)
        actions.send_keys(Keys.NUMPAD5)
        actions.send_keys(Keys.NUMPAD2)
        actions.send_keys(Keys.NUMPAD2)
        actions.send_keys(Keys.TAB)
        actions.send_keys(Keys.NUMPAD3)
        actions.send_keys(Keys.NUMPAD4)
        actions.send_keys(Keys.NUMPAD5)
        actions.perform()
        driver.find_element(By.XPATH, "//button[contains(.,'Confirm and proceed')]").click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'Credit card not accepted')]")))
        print("Incorrect credit card wasn't accepted. Test PASS")

    def test12_feng_004_max(self):
        driver = self.driver
        driver.get("https://www.prada.com/us/en/login-register.html")
        wait = WebDriverWait(driver, 10)

        # Login to the account
        H.login(driver)

        # Go to the personal information and delete address if it presents
        driver.find_element(By.XPATH, "//a[@href='#'][contains(.,'Personal information')]").click()
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, H.basket_del)))
            driver.find_element(By.XPATH, H.basket_del).click()
            wait.until(EC.element_to_be_clickable((By.XPATH, H.delete_confirm)))
            driver.find_element(By.XPATH, H.delete_confirm).click()
        except WDE:
            print("Address wasn't create previously")

        # Create new address with incorrect name
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Personal information')]")))
        driver.find_element(By.XPATH, '//*[contains(text(),"Add new shipping address")]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h3[contains(text(),'Shipping address')]")))
        driver.find_element(By.XPATH, "//input[contains(@id,'first_name_')]").send_keys("$$$")
        driver.find_element(By.XPATH, "//input[contains(@id,'last_name_')]").send_keys(H.l_name)
        driver.find_element(By.XPATH, "//input[contains(@id,'company_')]").send_keys(H.company)
        time.sleep(3)
        driver.find_element(By.XPATH, H.address_1).send_keys(H.add)
        driver.find_element(By.XPATH, "//input[contains(@id,'city_')]").send_keys(H.city)
        driver.find_element(By.XPATH, H.state_dd).click()
        scroll_to_state = driver.find_element(By.XPATH, H.state_city)
        driver.execute_script("arguments[0].scrollIntoView(true)", scroll_to_state)
        wait.until(EC.element_to_be_clickable((By.XPATH, H.state_city)))
        driver.find_element(By.XPATH, H.state_city).click()
        driver.find_element(By.XPATH, "//input[contains(@id,'zip_code_')]").send_keys(H.zip_code)
        driver.find_element(By.XPATH, "//input[contains(@id,'phone_')]").send_keys(H.phone)
        driver.find_element(By.XPATH, H.check_box).click()
        driver.find_element(By.XPATH, H.confirm).click()
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, '// *[contains(text(), "The First name field '
                                                                   'format is invalid")]')))
            print("User not abel to create address with incorrect name. Test PASS")
        except WDE:
            print("User abel to create address with incorrect name. Test FALL")
        wait.until(EC.visibility_of_element_located((By.XPATH, '// *[contains(text(), "The First name field format is '
                                                               'invalid")]')))

    def test13_feng_005_max(self):
        driver = self.driver
        driver.get("https://www.prada.com/us/en/login-register.html")
        wait = WebDriverWait(driver, 10)

        # Login to the account
        H.login(driver)

        # Go to the personal information and delete address if it presents
        driver.find_element(By.XPATH, "//a[@href='#'][contains(.,'Personal information')]").click()
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, H.basket_del)))
            driver.find_element(By.XPATH, H.basket_del).click()
            wait.until(EC.element_to_be_clickable((By.XPATH, H.delete_confirm)))
            driver.find_element(By.XPATH, H.delete_confirm).click()
        except WDE:
            print("Address wasn't create previously")

        # Create new address with incorrect address1
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Personal information')]")))
        driver.find_element(By.XPATH, '//*[contains(text(),"Add new shipping address")]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h3[contains(text(),'Shipping address')]")))
        driver.find_element(By.XPATH, "//input[contains(@id,'first_name_')]").send_keys(H.f_name)
        driver.find_element(By.XPATH, "//input[contains(@id,'last_name_')]").send_keys(H.l_name)
        driver.find_element(By.XPATH, "//input[contains(@id,'company_')]").send_keys(H.company)
        time.sleep(3)
        driver.find_element(By.XPATH, H.address_1).send_keys("$$$")
        driver.find_element(By.XPATH, "//input[contains(@id,'city_')]").send_keys(H.city)
        driver.find_element(By.XPATH, H.state_dd).click()
        scroll_to_state = driver.find_element(By.XPATH, H.state_city)
        driver.execute_script("arguments[0].scrollIntoView(true)", scroll_to_state)
        wait.until(EC.element_to_be_clickable((By.XPATH, H.state_city)))
        driver.find_element(By.XPATH, H.state_city).click()
        driver.find_element(By.XPATH, "//input[contains(@id,'zip_code_')]").send_keys(H.zip_code)
        driver.find_element(By.XPATH, "//input[contains(@id,'phone_')]").send_keys(H.phone)
        driver.find_element(By.XPATH, H.check_box).click()
        driver.find_element(By.XPATH, H.confirm).click()
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(.,'Cancel')])[7]")))
            print("User not abel to create address with incorrect address1. Test PASS")
        except WDE:
            print("User abel to create address with incorrect address1. Test FALL")
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(.,'Cancel')])[7]")))

    def test14_feng_006_max(self):
        driver = self.driver
        driver.get("https://www.prada.com/us/en/login-register.html")
        wait = WebDriverWait(driver, 10)

        # Login to the account
        H.login(driver)

        # Go to the personal information and delete address if it presents
        driver.find_element(By.XPATH, "//a[@href='#'][contains(.,'Personal information')]").click()
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, H.basket_del)))
            driver.find_element(By.XPATH, H.basket_del).click()
            wait.until(EC.element_to_be_clickable((By.XPATH, H.delete_confirm)))
            driver.find_element(By.XPATH, H.delete_confirm).click()
        except WDE:
            print("Address wasn't create previously")

        # Create new address with incorrect zip code
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Personal information')]")))
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
        wait.until(EC.element_to_be_clickable((By.XPATH, H.state_city)))
        driver.find_element(By.XPATH, H.state_city).click()
        driver.find_element(By.XPATH, "//input[contains(@id,'zip_code_')]").send_keys("0000")
        driver.find_element(By.XPATH, "//input[contains(@id,'phone_')]").send_keys(H.phone)
        driver.find_element(By.XPATH, H.check_box).click()
        driver.find_element(By.XPATH, H.confirm).click()
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[contains(text(),"The Zip code field format is '
                                                                   'invalid")]')))
            print("User not abel to create address with incorrect zip code. Test PASS")
        except WDE:
            print("User abel to create address with incorrect zip code. Test FALL")
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[contains(text(),"The Zip code field format is '
                                                               'invalid")]')))

    def test15_feng_007_max(self):
        driver = self.driver
        driver.get("https://www.prada.com/us/en/login-register.html")
        wait = WebDriverWait(driver, 10)

        # Login to the account
        H.login(driver)

        # Go to the personal information and delete address if it presents
        driver.find_element(By.XPATH, "//a[@href='#'][contains(.,'Personal information')]").click()
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, H.basket_del)))
            driver.find_element(By.XPATH, H.basket_del).click()
            wait.until(EC.element_to_be_clickable((By.XPATH, H.delete_confirm)))
            driver.find_element(By.XPATH, H.delete_confirm).click()
        except WDE:
            print("Address wasn't create previously")

        # Create new address with incorrect city
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Personal information')]")))
        driver.find_element(By.XPATH, '//*[contains(text(),"Add new shipping address")]').click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h3[contains(text(),'Shipping address')]")))
        driver.find_element(By.XPATH, "//input[contains(@id,'first_name_')]").send_keys(H.f_name)
        driver.find_element(By.XPATH, "//input[contains(@id,'last_name_')]").send_keys(H.l_name)
        driver.find_element(By.XPATH, "//input[contains(@id,'company_')]").send_keys(H.company)
        time.sleep(3)
        driver.find_element(By.XPATH, H.address_1).send_keys(H.add)
        driver.find_element(By.XPATH, "//input[contains(@id,'city_')]").send_keys("$$$")
        driver.find_element(By.XPATH, H.state_dd).click()
        scroll_to_state = driver.find_element(By.XPATH, H.state_city)
        driver.execute_script("arguments[0].scrollIntoView(true)", scroll_to_state)
        wait.until(EC.element_to_be_clickable((By.XPATH, H.state_city)))
        driver.find_element(By.XPATH, H.state_city).click()
        driver.find_element(By.XPATH, "//input[contains(@id,'zip_code_')]").send_keys(H.zip_code)
        driver.find_element(By.XPATH, "//input[contains(@id,'phone_')]").send_keys(H.phone)
        driver.find_element(By.XPATH, H.check_box).click()
        driver.find_element(By.XPATH, H.confirm).click()
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "(//a[contains(.,'Cancel')])[7]")))
            print("User not abel to create address with incorrect city. Test PASS")
            locator = "(//a[contains(.,'Cancel')])[7]"
        except WDE:
            locator = "//span[contains(.,'The address you entered seems to have some incorrect information')]"
            print("User not abel to create address with incorrect city. Test PASS")
        wait.until(EC.visibility_of_element_located((By.XPATH, locator)))

    def test16_feng_008_max(self):
        driver = self.driver
        driver.get("https://www.prada.com/us/en/login-register.html")
        wait = WebDriverWait(driver, 10)

        # Login to the account
        H.login(driver)

        # Go to the personal information and delete address if it presents
        driver.find_element(By.XPATH, "//a[@href='#'][contains(.,'Personal information')]").click()
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, H.basket_del)))
            driver.find_element(By.XPATH, H.basket_del).click()
            wait.until(EC.element_to_be_clickable((By.XPATH, H.delete_confirm)))
            driver.find_element(By.XPATH, H.delete_confirm).click()
        except WDE:
            print("Address wasn't create previously")

        # Create new address with incorrect phone number
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Personal information')]")))
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
        wait.until(EC.element_to_be_clickable((By.XPATH, H.state_city)))
        driver.find_element(By.XPATH, H.state_city).click()
        driver.find_element(By.XPATH, "//input[contains(@id,'zip_code_')]").send_keys(H.zip_code)
        driver.find_element(By.XPATH, "//input[contains(@id,'phone_')]").send_keys("000000")
        driver.find_element(By.XPATH, H.check_box).click()
        driver.find_element(By.XPATH, H.confirm).click()
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, '// *[contains(text(), "The Phone field format is '
                                                                   'invalid")]')))
            print("User not abel to create address with incorrect phone number. Test PASS")
        except WDE:
            print("User abel to create address with incorrect phone number. Test FALL")
        wait.until(EC.visibility_of_element_located((By.XPATH, '// *[contains(text(), "The Phone field format is '
                                                               'invalid")]')))

    def test17_febd_001_max(self):
        driver = self.driver
        driver.get("https://internxt.com/temporary-email")
        wait = WebDriverWait(driver, 50)

        # Get email
        time.sleep(2)
        driver.find_element(By.XPATH, "//p[contains(text(),'Copy email')]").click()

        # Open new tab "prada.com" and star registration
        driver.switch_to.new_window('tab')
        driver.get("https://www.prada.com/us/en.html")
        driver.find_element(By.XPATH, "//div[@class='banner_cta cta_accept'][contains(.,'ACCEPT ALL')]").click()
        driver.find_element(By.XPATH, "//span[contains(@class,'utils__icon pr-icon-new-login')]").click()
        wait.until(EC.visibility_of_element_located((By.ID, "gigya-textbox-100719189608483120")))
        driver.find_element(By.ID, "gigya-textbox-100719189608483120").send_keys(Keys.CONTROL + "v")
        driver.find_element(By.XPATH, "//input[contains(@value,'Next')]").click()
        time.sleep(10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Resend')]")))

        # Switch to temporary email and wait for verification code
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

        # Switch to prada tab and complete registration
        driver.switch_to.window(driver.window_handles[1])
        driver.find_element(By.XPATH, '//*[@placeholder="Verification code*"]').send_keys(code)
        driver.find_element(By.XPATH, H.drop_down).click()
        driver.find_element(By.ID, "gigya-textbox-105760616358098000").send_keys(H.f_name)
        driver.find_element(By.ID, "gigya-textbox-21007040083017830").send_keys(H.l_name)
        driver.find_element(By.ID, "gigya-textbox-74329674452397740").send_keys(H.mm_dd)
        driver.find_element(By.ID, "gigya-password-60262223393983710").send_keys("Df1!0:-")
        driver.find_element(By.ID, "visibleTextMarketing").click()
        driver.find_element(By.XPATH, "//input[@value='Register']").click()
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(.,'Check that your password "
                                                                   "respects the criteria.')]")))
            print("User can't create account with weak password. Test PASS")
        except WDE:
            print("User can create account with weak password.. Test FALL")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(.,'Check that your password respects "
                                                               "the criteria.')]")))

    def test18_febd_002_max(self):
        driver = self.driver
        driver.get("https://internxt.com/temporary-email")
        wait = WebDriverWait(driver, 50)

        # Get email
        time.sleep(2)
        driver.find_element(By.XPATH, "//p[contains(text(),'Copy email')]").click()

        # Open new tab "prada.com" and star registration
        driver.switch_to.new_window('tab')
        driver.get("https://www.prada.com/us/en.html")
        driver.find_element(By.XPATH, "//div[@class='banner_cta cta_accept'][contains(.,'ACCEPT ALL')]").click()
        driver.find_element(By.XPATH, "//span[contains(@class,'utils__icon pr-icon-new-login')]").click()
        wait.until(EC.visibility_of_element_located((By.ID, "gigya-textbox-100719189608483120")))
        driver.find_element(By.ID, "gigya-textbox-100719189608483120").send_keys(Keys.CONTROL + "v")
        driver.find_element(By.XPATH, "//input[contains(@value,'Next')]").click()
        time.sleep(10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Resend')]")))

        # Switch to temporary email and wait for verification code
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

        # Switch to prada tab and complete registration
        driver.switch_to.window(driver.window_handles[1])
        driver.find_element(By.XPATH, '//*[@placeholder="Verification code*"]').send_keys(code)
        driver.find_element(By.XPATH, H.drop_down).click()
        driver.find_element(By.ID, "gigya-textbox-105760616358098000").send_keys(H.f_name)
        driver.find_element(By.ID, "gigya-textbox-21007040083017830").send_keys(H.l_name)
        driver.find_element(By.ID, "gigya-textbox-74329674452397740").send_keys(H.mm_dd)
        driver.find_element(By.ID, "gigya-password-60262223393983710").send_keys("Df1!0:-a")
        driver.find_element(By.ID, "visibleTextMarketing").click()
        driver.find_element(By.XPATH, "//input[@value='Register']").click()

        # Registration validation
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(@class,'utils__icon pr-icon-new-bag')]")))
        try:
            title_check = driver.title == "Prada Official Website | Thinking fashion since 1913 | PRADA"
            print("Title is correct. Test PASS!")
        except WDE:
            print("Incorrect title. Test FALL!")

    def test19_febd_003_max(self):
        driver = self.driver
        driver.get("https://internxt.com/temporary-email")
        wait = WebDriverWait(driver, 50)

        # Get email
        time.sleep(2)
        driver.find_element(By.XPATH, "//p[contains(text(),'Copy email')]").click()

        # Open new tab "prada.com" and star registration
        driver.switch_to.new_window('tab')
        driver.get("https://www.prada.com/us/en.html")
        driver.find_element(By.XPATH, "//div[@class='banner_cta cta_accept'][contains(.,'ACCEPT ALL')]").click()
        driver.find_element(By.XPATH, "//span[contains(@class,'utils__icon pr-icon-new-login')]").click()
        wait.until(EC.visibility_of_element_located((By.ID, "gigya-textbox-100719189608483120")))
        driver.find_element(By.ID, "gigya-textbox-100719189608483120").send_keys(Keys.CONTROL + "v")
        driver.find_element(By.XPATH, "//input[contains(@value,'Next')]").click()
        time.sleep(10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Resend')]")))

        # Switch to temporary email and wait for verification code
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

        # Switch to prada tab and complete registration
        driver.switch_to.window(driver.window_handles[1])
        driver.find_element(By.XPATH, '//*[@placeholder="Verification code*"]').send_keys(code)
        driver.find_element(By.XPATH, H.drop_down).click()
        driver.find_element(By.ID, "gigya-textbox-105760616358098000").send_keys(H.f_name)
        driver.find_element(By.ID, "gigya-textbox-21007040083017830").send_keys(H.l_name)
        driver.find_element(By.ID, "gigya-textbox-74329674452397740").send_keys(H.mm_dd)
        driver.find_element(By.ID, "gigya-password-60262223393983710").send_keys("Df1!0:-as")
        driver.find_element(By.ID, "visibleTextMarketing").click()
        driver.find_element(By.XPATH, "//input[@value='Register']").click()

        # Registration validation
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(@class,'utils__icon pr-icon-new-bag')]")))
        try:
            title_check = driver.title == "Prada Official Website | Thinking fashion since 1913 | PRADA"
            print("Title is correct. Test PASS!")
        except WDE:
            print("Incorrect title. Test FALL!")

    def test20_febd_004_max(self):
        driver = self.driver
        driver.get("https://internxt.com/temporary-email")
        wait = WebDriverWait(driver, 50)

        # Get email
        time.sleep(2)
        driver.find_element(By.XPATH, "//p[contains(text(),'Copy email')]").click()

        # Open new tab "prada.com" and star registration
        driver.switch_to.new_window('tab')
        driver.get("https://www.prada.com/us/en.html")
        driver.find_element(By.XPATH, "//div[@class='banner_cta cta_accept'][contains(.,'ACCEPT ALL')]").click()
        driver.find_element(By.XPATH, "//span[contains(@class,'utils__icon pr-icon-new-login')]").click()
        wait.until(EC.visibility_of_element_located((By.ID, "gigya-textbox-100719189608483120")))
        driver.find_element(By.ID, "gigya-textbox-100719189608483120").send_keys(Keys.CONTROL + "v")
        driver.find_element(By.XPATH, "//input[contains(@value,'Next')]").click()
        time.sleep(10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Resend')]")))

        # Switch to temporary email and wait for verification code
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

        # Switch to prada tab and complete registration
        driver.switch_to.window(driver.window_handles[1])
        driver.find_element(By.XPATH, '//*[@placeholder="Verification code*"]').send_keys(code)
        driver.find_element(By.XPATH, H.drop_down).click()
        driver.find_element(By.ID, "gigya-textbox-105760616358098000").send_keys(H.f_name)
        driver.find_element(By.ID, "gigya-textbox-21007040083017830").send_keys(H.l_name)
        driver.find_element(By.ID, "gigya-textbox-74329674452397740").send_keys(H.mm_dd)
        driver.find_element(By.ID, "gigya-password-60262223393983710").send_keys("Df1!0:-asDf1!0:")
        driver.find_element(By.ID, "visibleTextMarketing").click()
        driver.find_element(By.XPATH, "//input[@value='Register']").click()

        # Registration validation
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(@class,'utils__icon pr-icon-new-bag')]")))
        try:
            title_check = driver.title == "Prada Official Website | Thinking fashion since 1913 | PRADA"
            print("Title is correct. Test PASS!")
        except WDE:
            print("Incorrect title. Test FALL!")

    def test21_febd_005_max(self):
        driver = self.driver
        driver.get("https://internxt.com/temporary-email")
        wait = WebDriverWait(driver, 50)

        # Get email
        time.sleep(2)
        driver.find_element(By.XPATH, "//p[contains(text(),'Copy email')]").click()

        # Open new tab "prada.com" and star registration
        driver.switch_to.new_window('tab')
        driver.get("https://www.prada.com/us/en.html")
        driver.find_element(By.XPATH, "//div[@class='banner_cta cta_accept'][contains(.,'ACCEPT ALL')]").click()
        driver.find_element(By.XPATH, "//span[contains(@class,'utils__icon pr-icon-new-login')]").click()
        wait.until(EC.visibility_of_element_located((By.ID, "gigya-textbox-100719189608483120")))
        driver.find_element(By.ID, "gigya-textbox-100719189608483120").send_keys(Keys.CONTROL + "v")
        driver.find_element(By.XPATH, "//input[contains(@value,'Next')]").click()
        time.sleep(10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Resend')]")))

        # Switch to temporary email and wait for verification code
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

        # Switch to prada tab and complete registration
        driver.switch_to.window(driver.window_handles[1])
        driver.find_element(By.XPATH, '//*[@placeholder="Verification code*"]').send_keys(code)
        driver.find_element(By.XPATH, H.drop_down).click()
        driver.find_element(By.ID, "gigya-textbox-105760616358098000").send_keys(H.f_name)
        driver.find_element(By.ID, "gigya-textbox-21007040083017830").send_keys(H.l_name)
        driver.find_element(By.ID, "gigya-textbox-74329674452397740").send_keys(H.mm_dd)
        driver.find_element(By.ID, "gigya-password-60262223393983710").send_keys("Df1!0:-asDf1!0:-")
        driver.find_element(By.ID, "visibleTextMarketing").click()
        driver.find_element(By.XPATH, "//input[@value='Register']").click()

        # Registration validation
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(@class,'utils__icon pr-icon-new-bag')]")))
        try:
            title_check = driver.title == "Prada Official Website | Thinking fashion since 1913 | PRADA"
            print("Title is correct. Test PASS!")
        except WDE:
            print("Incorrect title. Test FALL!")

    def test22_febd_006_max(self):
        driver = self.driver
        driver.get("https://internxt.com/temporary-email")
        wait = WebDriverWait(driver, 50)

        # Get email
        time.sleep(2)
        driver.find_element(By.XPATH, "//p[contains(text(),'Copy email')]").click()

        # Open new tab "prada.com" and star registration
        driver.switch_to.new_window('tab')
        driver.get("https://www.prada.com/us/en.html")
        driver.find_element(By.XPATH, "//div[@class='banner_cta cta_accept'][contains(.,'ACCEPT ALL')]").click()
        driver.find_element(By.XPATH, "//span[contains(@class,'utils__icon pr-icon-new-login')]").click()
        wait.until(EC.visibility_of_element_located((By.ID, "gigya-textbox-100719189608483120")))
        driver.find_element(By.ID, "gigya-textbox-100719189608483120").send_keys(Keys.CONTROL + "v")
        driver.find_element(By.XPATH, "//input[contains(@value,'Next')]").click()
        time.sleep(10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Resend')]")))

        # Switch to temporary email and wait for verification code
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

        # Switch to prada tab and complete registration
        driver.switch_to.window(driver.window_handles[1])
        driver.find_element(By.XPATH, '//*[@placeholder="Verification code*"]').send_keys(code)
        driver.find_element(By.XPATH, H.drop_down).click()
        driver.find_element(By.ID, "gigya-textbox-105760616358098000").send_keys(H.f_name)
        driver.find_element(By.ID, "gigya-textbox-21007040083017830").send_keys(H.l_name)
        driver.find_element(By.ID, "gigya-textbox-74329674452397740").send_keys(H.mm_dd)
        driver.find_element(By.ID, "gigya-password-60262223393983710").send_keys("Df1!0:-asDf1!0:-a")
        driver.find_element(By.ID, "visibleTextMarketing").click()
        driver.find_element(By.XPATH, "//input[@value='Register']").click()
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(.,'Check that your password "
                                                                   "respects the criteria.')]")))
            print("User can't create account with weak password. Test PASS")
        except WDE:
            print("User can create account with weak password.. Test FALL")
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(.,'Check that your password respects "
                                                               "the criteria.')]")))

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(AllureReports)
