
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException, TimeoutException

@pytest.mark.usefixtures()
class Test_Mylegacy_Page_Icon:

    def test_my_legacy_will (self):

        self.driver.find_element(By.XPATH, "//h4[starts-with(text(),'My Legacy')]").click()
        print("my legacy ICON")

        self.driver.find_element(By.XPATH,"//h4[normalize-space()='My Will']").click()
        print("click on will ICON ")
        time.sleep(5)

        time.sleep(5)

        try:
            element = self.driver.find_element(By.XPATH,"//a[@class='btn btn-success btn-rounded' or  @href= '/inpassing/(S(aw2rgvxeeampa0j41rpptfda))/Legacy/Last_Will_Testament?UType=User style']")
            wait = WebDriverWait(self.driver, 10, poll_frequency=2,
                                 ignored_exceptions=[NoSuchElementException, TimeoutException, Exception])
            wait.until(EC.element_to_be_clickable(element)) # <- Fixed argument here
            element.click()
            print("add will")
        except ElementClickInterceptedException:
            print("Click intercepted. Trying JS click as fallback.")

    #___________________________________add my executors and trustees_______________________
        action = ActionChains(self.driver)
        element = self.driver.find_element(By.ID,"btnAddOwnerSample")
        action.move_to_element(element)
        self.driver.execute_script("window.scrollTo(0, 0);")
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        print("click on add icon")
        action.click()
        action.perform()

        # Select dropdown interaction
        action = ActionChains(self.driver)
        select_element = self.driver.find_element(By.XPATH, "(//select[@id='PeopleName0'])")
        action.move_to_element(select_element).click().perform()

        # Create Select object
        select = Select(select_element)

        # Check if the element is enabled
        if select_element.is_enabled():
            print("enabled")

            # Print all dropdown options
            for option in select.options:
                print(option.text)

            # Select by visible text
            select.select_by_visible_text("JAI SINGH (LIC INDIA)")
            print("Selected:", select.first_selected_option.text)
            self.driver.find_element(By.CSS_SELECTOR, "#btnSave1").click()
            time.sleep(5)
    #____________________________________________________________________________________________
        # header = self.driver.find_element(By.XPATH,"//h4[contains(.,'Last Will and Testament Details')]")
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", header)

    #_________________________________when edit any existing row in executor and trustee________________________________________________________________
        action = ActionChains(self.driver)

        time.sleep(8)
        edit_icon = self.driver.find_element(By.XPATH,"//tr[@ng-repeat='l in ExecutorsAndTrusteesList']//div[3]//button[1]")
        action.move_to_element(edit_icon)
        action.click()
        action.perform()
        print("click on edit existing row icon")
        time.sleep(10)
        dropdown = Select(self.driver.find_element(By.ID, "PeopleName0"))
        if dropdown.is_multiple:
            print("this dropdown is multiselect")
        else:
            print("This dropdown is not multiselect")
        # to select the name and relationship dropdown
        dropdown.select_by_visible_text("Select")
        time.sleep(2)
        dropdown.select_by_visible_text("Deepak Sharma (Friend)")
        print("Selected option executor and trustee:", dropdown.first_selected_option.text)
        self.driver.find_element(By.ID,"btnUpdate1").click()
        print("btnUpdate1 is clicked")
    # ------- when add new row in my executor and trustee____________________________________
        element = self.driver.find_element(By.XPATH, "//button[@id='btnAddOwnerSample']//span[contains(text(),'Add')]")
        action.move_to_element(element)
        action.click()
        action.perform()
        print("click on add icon")
        time.sleep(5)
        dropdown1 = Select(self.driver.find_element(By.XPATH,"//select[@id='PeopleName1']"))
        dropdown1.select_by_visible_text("Neeraj Igspectrum (Family)")
        self.driver.find_element(By.XPATH,"(//button[@id='btnSave1'])[2]").click()
        print("selected option executor and trustee:",dropdown1.first_selected_option.text)
        time.sleep(5)
        self.driver.find_element(By.XPATH,"(//button[@id='btnCancel1'])[5]").click()
        print("edit icon is clicked")
        dropdown1 = Select(self.driver.find_element(By.XPATH, "//select[@id='PeopleName1']"))
        dropdown1.select_by_visible_text("Test01 sars (Solicitor)")
        print("Selected update option executor and trustee:", dropdown1.first_selected_option.text)
        self.driver.find_element(By.XPATH,"(//button[@id='btnUpdate1'])[2]").click()
        time.sleep(8)

        dropdown2 = Select(self.driver.find_element(By.XPATH,"(//select[@id='Peoplename2'])[1]"))

        if dropdown.is_multiple:
            print("this dropdown is multiselect")
        else:
            print("This dropdown is not multiselect")

        dropdown2.select_by_visible_text("Rathi Dikhsa (Contact person)")
        print(f"Selected option {dropdown2.first_selected_option.text} as executor in their place:")
        dropdown2.select_by_index(5)
        print("Selected update option:", dropdown2.first_selected_option.text)
        time.sleep(5)

        dropdown6 = Select(self.driver.find_element(By.ID,"Peoplename21"))
        dropdown6.select_by_visible_text("Test01 sars (Solicitor)")

        print(f"Selected option {dropdown6.first_selected_option.text}: dies before me I appoint" )

        dropdown6.select_by_index(10)
        print(f"Selected option {dropdown6.first_selected_option.text}: dies before me I appoint")
        time.sleep(5)
        self.driver.execute_script("window.scrollTo(0,250);")
        time.sleep(5)

    def test_my_children_under_eighteen_years_age(self):
        self.driver.find_element(By.XPATH, "//h4[starts-with(text(),'My Legacy')]").click()
        print("my legacy")
        self.driver.find_element(By.XPATH,"//h4[normalize-space()='My Will").click()
        print("click on will ")
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//a[@class='btn btn-success btn-rounded' or  @href= '/inpassing/(S(aw2rgvxeeampa0j41rpptfda))/Legacy/Last_Will_Testament?UType=User style']").click()
        print("add will")
        self.driver.execute_script("window.scrollTo(0,0);")
        time.sleep(5)
        # click on Add button
        try:
            element = self.driver.find_element(By.ID, "btnAddOwnerSample_3")
            wait = WebDriverWait(self.driver, 10, poll_frequency=2,
                                 ignored_exceptions=[NoSuchElementException, TimeoutException,
                                                     Exception])  # wait for 10 sec
            wait.until(EC.element_to_be_clickable(element))
            element.click()
        except ElementClickInterceptedException:
            print("Click intercepted. Trying JS click as fallback.")
        time.sleep(8)

        select = Select(self.driver.find_element(By.CSS_SELECTOR,"#PeopleName1"))
        print("select dropdown7 click")
        # self.driver.execute_script("arguments[0].removeAttribute('ng-disabled')", select)
        select.select_by_visible_text("JAI SINGH (LIC INDIA)")
        print(select.first_selected_option.text)
        time.sleep(2)
        action = ActionChains(self.driver)
        element = self.driver.find_element(By.XPATH,"(//button[@id='btnSave3'])[2]")
        action.move_to_element(element)
        action.click()
        action.perform()
        print("click on save icon",f"{select.first_selected_option.text}as Guardians of any of my children under eighteen years of age")
        time.sleep(5)

    def test_gifts_of_money(self):

        self.driver.find_element(By.XPATH, "//h4[starts-with(text(),'My Legacy')]").click()
        print("my legacy")

        self.driver.find_element(By.XPATH,"//h4[normalize-space()='My Will']").click()
        print("click on my will ")
        time.sleep(5)

        self.driver.find_element(By.XPATH,"//a[@class='btn btn-success btn-rounded' or  @href= '/inpassing/(S(aw2rgvxeeampa0j41rpptfda))/Legacy/Last_Will_Testament?UType=User style']").click()
        print("add will")
        time.sleep(5)
        # to find add button in gifts of money
        try:
            element = self.driver.find_element(By.ID, "btnAddOwnerSample_4")
            wait = WebDriverWait(self.driver, 10, poll_frequency=2,
                                 ignored_exceptions=[NoSuchElementException, TimeoutException, Exception])
            wait.until(EC.element_to_be_clickable((By.ID, "btnAddOwnerSample_4")))  # <- Fixed argument here
            element.click()
        except ElementClickInterceptedException:
            print("Click intercepted. Trying JS click as fallback.")
            self.driver.execute_script("arguments[0].click();", element)  # Fallback JS click

        time.sleep(8)  # Static wait: Replace with dynamic wait if possible

        # Select dropdown interaction in gifts of money
        action = ActionChains(self.driver)
        select_element = self.driver.find_element(By.XPATH, "(//select[@id='PeopleName0'])[1]")
        action.move_to_element(select_element).click().perform()

        # Create Select object
        select : Select = Select(select_element)

        # Check if the element is enabled
        if select_element.is_enabled():
            print("enabled")

            # Print all dropdown options
            for option in select.options:
                print(option.text)

            # Select by visible text
            select.select_by_visible_text("JAI SINGH (LIC INDIA)")
            print("Selected:", select.first_selected_option.text)

            # Enter gift amount
            self.driver.find_element(By.ID, "Gifts_Amount0").send_keys("1000")

        else:
            print("not enabled")

        self.driver.find_element(By.CSS_SELECTOR,"#btnSave4").click()
        time.sleep(5)

       # to edit the select dropdown in make of gifts____________________________
        element = self.driver.find_element(By.XPATH,"(//button[@id='btnCancel4'])[2]")
        wait = WebDriverWait(self.driver, 10, poll_frequency=2,
                             ignored_exceptions=[NoSuchElementException, TimeoutException, Exception])
        wait.until(EC.element_to_be_clickable((By.XPATH,"(//button[@id='btnCancel4'])[2]")))  # <- Fixed argument here
        element.click()

        action = ActionChains(self.driver)
        select_element = self.driver.find_element(By.XPATH, "(//select[@id='PeopleName0'])[1]")
        action.move_to_element(select_element).click().perform()

        # Create Select object
        select = Select(select_element)

        # Check if the element is enabled
        if select_element.is_enabled():
            print("enabled")
            # Select by visible text
            select.select_by_visible_text("Urvashi rathod (TATA ELXI)")
            print("Selected:", select.first_selected_option.text)
        else:
            print("not enabled")

        # self.driver.find_element(By.CSS_SELECTOR,"#btnUpdate4").click()
        time.sleep(5)


















