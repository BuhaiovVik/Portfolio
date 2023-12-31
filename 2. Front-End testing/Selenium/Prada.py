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
from functools import reduce
from itertools import takewhile

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
            print("Title is correct. Test PASS!")
        except WDE:
            print("Incorrect title. Test FALL!")
        print("Account was successful created")

        # Test case fept_002

        # Opening the address form menu
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
        time.sleep(2)
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
        wait.until(EC.element_to_be_clickable((By.XPATH, H.confirm_2)))
        driver.find_element(By.XPATH, H.confirm_2).click()
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

        # Test case fept_003

        # New address generation
        address = H.addresses[random.randint(0, 194)]
        zip_code = address[-5:]
        add_a = reduce(lambda acc, x: acc + x, takewhile(lambda x: x != ",", address), "")
        add = str(add_a)
        city = address[len(add)+2: -9]
        state = address[-8: -6]
        state_city = H.us_abb.get(state)

        # Address changing functionality
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Payment methods')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, H.address_change)))
        driver.find_element(By.XPATH, H.address_change).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, H.address_1)))
        driver.find_element(By.XPATH, H.address_1).send_keys(Keys.CONTROL + "a")
        driver.find_element(By.XPATH, H.address_1).send_keys(Keys.DELETE)
        driver.find_element(By.XPATH, H.address_1).send_keys(add)
        driver.find_element(By.XPATH, "//input[contains(@id,'city_')]").send_keys(Keys.CONTROL + "a")
        driver.find_element(By.XPATH, "//input[contains(@id,'city_')]").send_keys(Keys.DELETE)
        driver.find_element(By.XPATH, "//input[contains(@id,'city_')]").send_keys(city)
        driver.find_element(By.XPATH, H.state_dd).click()
        scroll_to_state = driver.find_element(By.XPATH, state_city)
        driver.execute_script("arguments[0].scrollIntoView(true)", scroll_to_state)
        wait.until(EC.element_to_be_clickable((By.XPATH, state_city)))
        driver.find_element(By.XPATH, state_city).click()
        driver.find_element(By.XPATH, "//input[contains(@id,'zip_code_')]").send_keys(Keys.CONTROL + "a")
        driver.find_element(By.XPATH, "//input[contains(@id,'zip_code_')]").send_keys(Keys.DELETE)
        driver.find_element(By.XPATH, "//input[contains(@id,'zip_code_')]").send_keys(zip_code)
        driver.find_element(By.XPATH, H.check_box).click()
        driver.find_element(By.XPATH, H.confirm).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, H.confirm_2)))
        driver.find_element(By.XPATH, H.confirm_2).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, H.ship_address)))

        # Shipping addresses changing verification
        shipp_change = driver.find_element(By.XPATH, H.ship_address).text
        try:
            shipp_address_check = shipp_change != shipp
            print("Address was changed. Test PASS!")
        except WDE:
            print("Shipping address wasn't changed. Test FALL")

        # Shipping and billing addresses verification
        bill_change = driver.find_element(By.XPATH, H.bill_address).text
        try:
            bill_address_check = bill_change == bill
            print("Billing addresses are the same. Test PASS!")
        except WDE:
            print("Billing addresses are different. Test FALL!")

        # Test case fept_004

        # Go to Prada-Edition bag
        time.sleep(6)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(.,'Bags')]" )))
        driver.find_element(By.XPATH, "//span[contains(.,'Bags')]").click()
        driver.find_element(By.XPATH, H.re_edition).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, H.bag_img)))
        driver.find_element(By.XPATH, H.bag_img).click()

        # Buy black, white and orange bags Prada-Edition
        wait.until(EC.element_to_be_clickable((By.XPATH, H.add_shop_bag)))
        driver.find_element(By.XPATH, H.bag_alabaster_button).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, H.bag_alabaster_img)))
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

        # fept-005

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

        # fept_006

        driver.find_element(By.XPATH, "//span[@class='menu__linkText'][contains(.,'Beauty and Fragrances')]").click()
        driver.find_element(By.XPATH, "(//a[@href='/us/en/womens/fragrances/womens-fragrances/c/10464US'])[2]").click()
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

        # fept_007


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(AllureReports)
