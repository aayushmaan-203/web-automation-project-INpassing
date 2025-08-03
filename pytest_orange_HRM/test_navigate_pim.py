
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException, TimeoutException

@pytest.mark.usefixtures()
class Test_PIM_naviagte:

# navigation PIM
    def test_navigation_password_mismatch_task1(self):

        #navigate PIM
        self.driver.find_element(By.XPATH,"(//span[normalize-space()='PIM'])[1]").click()
        # Step 4: Click on "Add Employee"
        wait = WebDriverWait(self.driver,timeout=10,poll_frequency=2,ignored_exceptions=[TimeoutException,ElementClickInterceptedException,NoSuchElementException])
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Add']"))).click()

        # Step 5: Fill in Employee details
        first_name = wait.until(EC.presence_of_element_located((By.NAME, "firstName")))
        first_name.send_keys("Aayushmaan")

        self.driver.find_element(By.NAME, "lastName").send_keys("Singh")

        time.sleep(2)

        # Enable "Create Login Details"
        self.driver.find_element(By.XPATH, "//span[@class='oxd-switch-input oxd-switch-input--active --label-right']").click()

        # Step 6: Enter login details with mismatching passwords
        #to locate username field

        wait = WebDriverWait(self.driver,timeout=10,poll_frequency=2,ignored_exceptions=[TimeoutException,ElementClickInterceptedException])
        wait.until(EC.presence_of_element_located((By.XPATH, "//label[text()='Username']/following::input[1]"))).send_keys("aayush")

        # to locate password fields
        self.driver.find_element(By.XPATH, "//label[text()='Password']/following::input[1]").send_keys("Password123!")
        self.driver.find_element(By.XPATH, "//label[text()='Confirm Password']/following::input[1]").send_keys("Password321!")

        # Click Save
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()

        # Step 7: Verify error message for password mismatch
        element = self.driver.find_element(By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message']")
        assert element.is_displayed(), "Error message not displayed!"
        print("✅ Password mismatch validation is working correctly.")

        time.sleep(3)

    def test_valid_employee_task2(self):

        #navigate PIM
        self.driver.find_element(By.XPATH, "(//span[normalize-space()='PIM'])[1]").click()
        # Step 4: Click on "Add Employee"
        wait = WebDriverWait(self.driver, timeout=10, poll_frequency=2,
                             ignored_exceptions=[TimeoutException, ElementClickInterceptedException, NoSuchElementException])
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Add']"))).click()
        time.sleep(5)

        # Step 5: Fill in Employee details
        first_name = self.driver.find_element(By.NAME, "firstName")
        first_name.clear()
        first_name.send_keys("Harry")
        print(first_name.get_attribute("value"))

        last_name = self.driver.find_element(By.NAME, "lastName")
        last_name.clear()
        last_name.send_keys("Porter")
        print("last name is porter")

        #employee id
        employee_id = self.driver.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[2]")
        employee_id.clear()
        time.sleep(5)
        employee_id.send_keys("963")
        print(employee_id.get_attribute("value"))

        time.sleep(5)

        # Enable "Create Login Details"
        self.driver.find_element(By.XPATH, "//span[@class='oxd-switch-input oxd-switch-input--active --label-right']").click()

        # Step 6: Enter login details with mismatching passwords
        # to locate username field

        wait = WebDriverWait(self.driver, timeout=10, poll_frequency=2,
                             ignored_exceptions=[TimeoutException, ElementClickInterceptedException])
        wait.until(EC.presence_of_element_located((By.XPATH, "//label[text()='Username']/following::input[1]"))).send_keys(
            "harry")

        # to locate password fields

        password = self.driver.find_element(By.XPATH, "//label[text()='Password']/following::input[1]")
        password.clear()
        password.send_keys("Harry1!")

        confirm_password = self.driver.find_element(By.XPATH, "//label[text()='Confirm Password']/following::input[1]")
        confirm_password.clear()
        confirm_password.send_keys("Harry1!")

        # Click Save
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()

        time.sleep(8)

        self.driver.find_element(By.XPATH,"//div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']//button[@type='submit'][normalize-space()='Save']").click()

        ############## take a look below comment statement to complete the task 2 ##########################################

        # After creating the valid employee, what if user wants to Log In with a valid newly created employee whose credential shown below.
        #username = harry
        #password = Harry1!
        # to log in again, then update the username and password in the respective conftest.py.

    def test_valid_employee_login(self,test_setup_and_tear_down):
        print("Successfully landed on dashboard")

















