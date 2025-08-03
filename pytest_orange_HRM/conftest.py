import time
import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support import expected_conditions as EC

# addoption should only define the CLI argument.
def pytest_addoption(parser):
    parser.addoption("--browser",action="store", default="chrome", help="Browser name: chrome/firefox/edge")

#Chrome Option(headless) Inside Your Fixture

@pytest.fixture(scope="function",autouse=True)
def test_setup_and_tear_down(request):
    # driver = webdriver.Chrome()
    driver = None
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("--headless")
        chrome_options.add_argument("--start-maximized")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=chrome_options)

    elif browser == "firefox":
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument("--headless")
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install(),options=firefox_options))

    elif browser == "edge":
        edge_options = webdriver.EdgeOptions()
        edge_options.add_argument("--headless=new")
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install(),options=edge_options))
    else:
        raise ValueError (f"❌ Unsupported browser: {browser}")

    # Open your application
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    print("Inapssing login page showing", driver.title)

    # maximize Window
    driver.maximize_window()
    driver.implicitly_wait(5)

    # Set the driver for the test class
    request.cls.driver = driver

    #enter user_name
    user_name= driver.find_element(By.XPATH,"(//input[@placeholder='Username'])[1]")
    wait = WebDriverWait(driver, 10, poll_frequency=2,
                             ignored_exceptions=[NoSuchElementException, TimeoutException, Exception])
    wait.until(EC.element_to_be_clickable(user_name))
    user_name.send_keys("Admin")

    print("user name enterted ")
    time.sleep(5)

    # enter password
    pass_word = driver.find_element(By.NAME,"password")
    pass_word.send_keys("admin123")

    print("password is entered")
    time.sleep(2)


    # login button

    login_button = driver.find_element(By.CSS_SELECTOR,
                                       "button[type='submit']")
    login_button.click()
    print(" login button successful ")

    yield
    driver.find_element(By.XPATH,"//p[@class='oxd-userdropdown-name']").click()
    print("expand logut toggle")

    driver.find_element(By.XPATH,"//a[@href='/web/index.php/auth/logout']").click()
    print("logut successfull")
    time.sleep(1)
    driver.quit()



