import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

@pytest.mark.usefixtures()
class Test_Pesonal_details_Inpassing:

    def test_Name_and_contactdetails(self):
        self.driver.find_element(By.XPATH,"(//div[contains(@class,'col-xl-3 d-flex grid-margin stretch-card')])[1]").click()
        self.driver.find_element(By.XPATH, "//h4[normalize-space()='Name and contact details']").click()

        element1 = self.driver.find_element(By.ID, "FirstName")
        element1.clear()  # Clears the input field
        element1.send_keys("John")
        print(element1.text)

        element2 = self.driver.find_element(By.ID, "LastName")
        element2.clear()  # Clears the input field
        element2.send_keys("Cena")
        print(element2.text)

        element3 = self.driver.find_element(By.ID, "Addressline1")
        element3.clear()  # Clears the input field
        element3.send_keys("H.NO- 115, A-BLOCK, 3rd Floor")
        print(element3.text)

        element4 = self.driver.find_element(By.ID, "Addressline2")
        element4.clear()  # Clears the input field
        element4.send_keys("DLF NAT-WEST SOCIETY SOUTH LONDON")
        print(element4.text)

        element5 = self.driver.find_element(By.ID, "Addressline3")
        element5.clear()  # Clears the input field
        element5.send_keys("BIRGHINGHAM")
        print(element5.text)

        select_country_dropdown = self.driver.find_element(By.ID,'Countryid')
        # Create Select object
        select = Select(select_country_dropdown)
        # Check if the element is enabled
        if select_country_dropdown.is_enabled():
            print("enabled")
            # Select by visible text
            select.select_by_visible_text("India")
            time.sleep(1)
            select.select_by_visible_text("UK overseas territories")
            print("Selected:", select.first_selected_option.text)
        else:
            print("not enabled")

        element6 = self.driver.find_element(By.ID, "Postcode")
        element6.clear()  # Clears the input field
        element6.send_keys("BRIG78965UK")
        print(element6.text)

        self.driver.find_element(By.ID,"submit").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR,"div >button[class$='swal2-confirm swal2-styled']").click()
        time.sleep(2)

    def test_PersonalInformation(self):
        #personaldetails icon
        self.driver.find_element(By.XPATH,"(//div[contains(@class,'col-xl-3 d-flex grid-margin stretch-card')])[1]").click()
        #personalinformation icon
        self.driver.find_element(By.XPATH, "//h4[normalize-space()='Personal information']").click()

        Date_of_birth = self.driver.find_element(By.XPATH,"//input[@id='DOB']")
        Date_of_birth.clear()
        Date_of_birth.send_keys("02/07/1995")
        print(Date_of_birth.get_attribute("value"))

        select_Gender_dropdown = self.driver.find_element(By.ID, 'Gender')
        # Create Select object
        select : Select = Select(select_Gender_dropdown)
        # Check if the element is enabled
        if select_Gender_dropdown.is_enabled():
            print("enabled")
            # Select by visible text
            select.select_by_visible_text("Male")
            time.sleep(1)
            select.select_by_visible_text("Female")
            print("Selected:", select.first_selected_option.text)
        else:
            print("not enabled")

        select_Domicile_dropdown = self.driver.find_element(By.ID, 'Domicile')
        # Create Select object
        select : Select = Select(select_Domicile_dropdown)
        # Check if the element is enabled
        if select_Domicile_dropdown.is_enabled():
            print("enabled")
            # Select by visible text
            select.select_by_visible_text("United Arab Emirates")
            time.sleep(1)
            select.select_by_visible_text("United Kingdom")
            print("Selected:", select.first_selected_option.text)
        else:
            print("not enabled")


        select_Tax_dropdown = self.driver.find_element(By.ID, 'Taxresidence')
        # Create Select object
        select : Select = Select(select_Tax_dropdown)
        # Check if the element is enabled
        if select_Tax_dropdown.is_enabled():
            print("enabled")
            # Select by visible text
            select.select_by_visible_text("Brazil")
            select.select_by_visible_text("Cook Islands")
            select.select_by_visible_text("India")
            print("Selected:", select.first_selected_option.text)
        else:
            print("not enabled")

        # for option in select.options:
        #     print(option.text)

        self.driver.find_element(By.ID,"submit").click()

        self.driver.find_element(By.CSS_SELECTOR, "div >button[class$='swal2-confirm swal2-styled']").click()

        modal = self.driver.find_element(By.XPATH,"//div[contains(text(),'The personal information has been Updated successfully.')]")
        print(modal.text)
        time.sleep(5)



