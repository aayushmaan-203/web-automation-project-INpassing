import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select



# def pytest_addoption(parser):
#     parser.addoption("--browser")

@pytest.fixture(scope="function",autouse=True)
def test_setup_and_tear_down(request):
    driver = webdriver.Chrome()
    # brwsr = request.config.getoption("--browser")
    # if brwsr == "chrome":
    #     driver = webdriver.Chrome()
    #
    # elif brwsr == "firefox":
    #     driver = webdriver.Firefox()
    #
    # elif brwsr == "edge":
    #     driver = webdriver.Edge()
    # else:
    #     print("not valid browser")
    # Open your application
    driver.get("http://20.77.0.8/inpassing")
    print("Inapssing login page showing", driver.title)

    # maximize Window
    driver.maximize_window()
    driver.implicitly_wait(5)

    # Set the driver for the test class
    request.cls.driver = driver

    # enter mail id
    email_id = driver.find_element(By.XPATH, "//input[@placeholder='Enter Email ID']")
    email_id.send_keys("aayushmaan@igspectrum.com")

    print("email is entered")

    # enter password
    pass_word = driver.find_element(By.ID, "Password")
    pass_word.send_keys("Abinash1!")

    print("password is entered")
    time.sleep(2)

    # choose role

    role_dropdown = Select(driver.find_element(By.ID, "RoleID"))

    # drop-down check

    time.sleep(1)

    if role_dropdown.is_multiple:
        print("this drop down is multi select drop down")
    else:
        print("this drop down is single select")



    # role_dropdown.select_by_visible_text("Primary User")

    # role_dropdown.select_by_visible_text("Secondry User")

    # print("role selected:", role_dropdown.first_selected_option.text)



    # login button

    login_button = driver.find_element(By.XPATH,
                                       "//input[@class='btn btn-block btn-primary btn-rounded  btn-lg font-weight-medium auth-form-btn']")
    login_button.click()

    print(" login button successful ")

    submit_button = driver.find_element(By.ID,'btnsubmit')
    submit_button.click()
    print("click on submit button")
    time.sleep(1)

    yield
    driver.find_element(By.XPATH,"//a[@class='nav-link dropdown-toggle']").click()
    print("expand logut toggle")

    driver.find_element(By.XPATH,"(//i[@class='mdi mdi-logout text-primary'])[1]").click()
    print("logut successfull")
    time.sleep(1)
    driver.quit()
