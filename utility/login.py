from dotenv import dotenv_values
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Import your custom logging driver and element
from utility.logs import LoggingDriver, LoggingElement

# Load configuration
config = dotenv_values('utility/config.txt')

def login_to_dashboard():
    """
    Logs into the application using credentials from the configuration file.
    Returns the LoggingDriver instance.
    """
    # Use LoggingDriver instead of the regular WebDriver
    driver = webdriver.Chrome()
    logging_driver = LoggingDriver(driver)  # Wrap the driver in the LoggingDriver
    
    logging_driver.get("http://185.199.53.169:5000/login")
    
    # Wait for username and password fields
    WebDriverWait(logging_driver, 10).until(EC.visibility_of_element_located((By.ID, "username")))
    WebDriverWait(logging_driver, 10).until(EC.visibility_of_element_located((By.ID, "password")))

    # Find fields and fill in credentials using LoggingElement
    username_field = logging_driver.find_element(By.ID, "username")
    password_field = logging_driver.find_element(By.ID, "password")

    username = config.get('username')
    password = config.get('password')

    username_field.send_keys(username)
    password_field.send_keys(password + "\n")  # Press Enter

    # Wait for login to process
    time.sleep(2)

    # Verify login success
    if "/dashboard" in logging_driver.driver.current_url:
        print("Login Successful - Redirected to Dashboard")
    else:
        print("Login Failed - Redirected to Unexpected URL")
    
    return logging_driver
