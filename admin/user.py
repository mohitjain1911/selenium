from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from utility.logs import *


def change_role_admin(driver):
    logging_driver = LoggingDriver(driver)
    logging_driver.get("http://185.199.53.169:5000/admin/user-management")
    time.sleep(3)

    # Click the dropdown button
    dropdown_button_xpath = "//button[div[text()='Change Role'] and contains(@class, 'border border-primary') and contains(@class, 'dropdown-toggle')]"
    dropdown_button = WebDriverWait(logging_driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, dropdown_button_xpath))
    )
    dropdown_button.click()
    time.sleep(3)

    # Select "Make Admin" option
    make_admin_xpath = "//div[text()='Make Admin']"
    make_admin = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, make_admin_xpath))
    )
    make_admin.click()
    time.sleep(3)

    
    success_ok_button_selector = "button.btn-success"  # Button with 'btn-success' class
    failure_ok_button_selector = "button.btn-danger"   # Button with 'btn-danger' class
    default_ok_button_selector = "#Admin_Success_Message_Btn"  # Button with specific ID

    # Look for one of the OK buttons
    try:
        # Use WebDriverWait to wait for the button to appear
        ok_button = WebDriverWait(driver, 10).until(
            lambda d: d.find_element(By.CSS_SELECTOR, success_ok_button_selector) 
            if len(d.find_elements(By.CSS_SELECTOR, success_ok_button_selector)) > 0 
            else d.find_element(By.CSS_SELECTOR, failure_ok_button_selector)
            if len(d.find_elements(By.CSS_SELECTOR, failure_ok_button_selector)) > 0
            else d.find_element(By.CSS_SELECTOR, default_ok_button_selector)
        )
        
        # Scroll to the button and click it
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", ok_button)
        time.sleep(1)  # Allow modal transition to complete
        ok_button.click()
        print("Clicked on the appropriate 'OK' button to confirm.")
    except Exception as e:
        print(f"Failed to find or click the 'OK' button: {e}")

def change_role_user(driver):
    driver.get("http://185.199.53.169:5000/admin/user-management")
    time.sleep(3)
   # Click the dropdown button
    dropdown_button_xpath = '/html/body/div[4]/div/div[6]/table/tbody/tr[1]/td[5]/div/div[1]/button'
    dropdown_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, dropdown_button_xpath))
    )
    dropdown_button.click()
    time.sleep(3)
    make_user_xpath = '/html/body/div[4]/div/div[6]/table/tbody/tr[1]/td[5]/div/div[1]/ul/li[2]/div[2]'
    make_user = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, make_user_xpath))
    )
    make_user.click()
    time.sleep(3)
     # Define possible OK button XPaths
    success_ok_button_xpath = '/html/body/div[4]/div/div[8]/div/div/div/div[3]/div/button'
    failure_ok_button_xpath = '/html/body/div[4]/div/div[7]/div/div/div/div[3]/div/button'

    # Look for one of the OK buttons
    try:
        ok_button = WebDriverWait(driver, 10).until(
            lambda d: d.find_element(By.XPATH, success_ok_button_xpath) 
            if len(d.find_elements(By.XPATH, success_ok_button_xpath)) > 0 
            else d.find_element(By.XPATH, failure_ok_button_xpath)
        )
        
        # Scroll to the button and click it
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", ok_button)
        time.sleep(1)  # Allow animation or modal transition to complete
        ok_button.click()
        print("Clicked on the appropriate 'OK' button to confirm.")
    except Exception as e:
        print(f"Failed to find or click the 'OK' button: {e}")
def change_role_api_admin(driver):
    driver.get("http://185.199.53.169:5000/admin/user-management")
    time.sleep(3)
    dropdown_button_xpath = '/html/body/div[4]/div/div[6]/table/tbody/tr[1]/td[5]/div/div[1]/button'
    dropdown_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, dropdown_button_xpath))
    )
    dropdown_button.click()
    time.sleep(3)

    # Select "Make Admin" option
    api_admin_xpath = '/html/body/div[4]/div/div[6]/table/tbody/tr[1]/td[5]/div/div[1]/ul/li[3]/div[2]'
    api_admin = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, api_admin_xpath))
    )
    api_admin.click()
    time.sleep(3)

    # Confirm role change with the OK button
  # Define possible OK button XPaths
    success_ok_button_xpath = '/html/body/div[4]/div/div[8]/div/div/div/div[3]/div/button'
    failure_ok_button_xpath = '/html/body/div[4]/div/div[7]/div/div/div/div[3]/div/button'

    # Look for one of the OK buttons
    try:
        ok_button = WebDriverWait(driver, 10).until(
            lambda d: d.find_element(By.XPATH, success_ok_button_xpath) 
            if len(d.find_elements(By.XPATH, success_ok_button_xpath)) > 0 
            else d.find_element(By.XPATH, failure_ok_button_xpath)
        )
        
        # Scroll to the button and click it
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", ok_button)
        time.sleep(1)  # Allow animation or modal transition to complete
        ok_button.click()
        print("Clicked on the appropriate 'OK' button to confirm.")
    except Exception as e:
        print(f"Failed to find or click the 'OK' button: {e}")

def change_role_api_user(driver):

    driver.get("http://185.199.53.169:5000/admin/user-management")
    time.sleep(3)
    dropdown_button_xpath = '/html/body/div[4]/div/div[6]/table/tbody/tr[1]/td[5]/div/div[1]/button'
    dropdown_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, dropdown_button_xpath))
    )
    dropdown_button.click()
    time.sleep(3)

    # Select "Make Admin" option
    api_user_xpath = '/html/body/div[4]/div/div[6]/table/tbody/tr[1]/td[5]/div/div[1]/ul/li[4]/div[2]'
    api_user = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, api_user_xpath))
    )
    api_user.click()
    time.sleep(3)

    # Confirm role change with the OK button
   # Define possible OK button XPaths
    success_ok_button_xpath = '/html/body/div[4]/div/div[8]/div/div/div/div[3]/div/button'
    failure_ok_button_xpath = '/html/body/div[4]/div/div[7]/div/div/div/div[3]/div/button'

    # Look for one of the OK buttons
    try:
        ok_button = WebDriverWait(driver, 10).until(
            lambda d: d.find_element(By.XPATH, success_ok_button_xpath) 
            if len(d.find_elements(By.XPATH, success_ok_button_xpath)) > 0 
            else d.find_element(By.XPATH, failure_ok_button_xpath)
        )
        
        # Scroll to the button and click it
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", ok_button)
        time.sleep(1)  # Allow animation or modal transition to complete
        ok_button.click()
        print("Clicked on the appropriate 'OK' button to confirm.")
    except Exception as e:
        print(f"Failed to find or click the 'OK' button: {e}")


def remove_user(driver):
    driver.get("http://185.199.53.169:5000/admin/user-management")
    time.sleep(3)
    remove_xpath = '/html/body/div[4]/div/div[6]/table/tbody/tr[1]/td[5]/div/div[2]/div[2]'
    remove = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, remove_xpath))
    )
    remove.click()
    time.sleep(3)
  # Define possible OK button XPaths
    success_ok_button_xpath = '/html/body/div[4]/div/div[8]/div/div/div/div[3]/div/button'
    failure_ok_button_xpath = '/html/body/div[4]/div/div[7]/div/div/div/div[3]/div/button'

    # Look for one of the OK buttons
    try:
        ok_button = WebDriverWait(driver, 10).until(
            lambda d: d.find_element(By.XPATH, success_ok_button_xpath) 
            if len(d.find_elements(By.XPATH, success_ok_button_xpath)) > 0 
            else d.find_element(By.XPATH, failure_ok_button_xpath)
        )
        
        # Scroll to the button and click it
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", ok_button)
        time.sleep(1)  # Allow animation or modal transition to complete
        ok_button.click()
        print("Clicked on the appropriate 'OK' button to confirm.")
    except Exception as e:
        print(f"Failed to find or click the 'OK' button: {e}")
        
def delete_user(driver):
    driver.get("http://185.199.53.169:5000/admin/user-management")
    time.sleep(3)
    
    # Click on the delete button
    delete_xpath = '/html/body/div[4]/div/div[6]/table/tbody/tr[1]/td[5]/div/div[3]/div[2]'
    delete = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, delete_xpath))
    )
    delete.click()
    time.sleep(3)

    # Define possible OK button XPaths
    success_ok_button_xpath = '/html/body/div[4]/div/div[8]/div/div/div/div[3]/div/button'
    failure_ok_button_xpath = '/html/body/div[4]/div/div[7]/div/div/div/div[3]/div/button'

    # Look for one of the OK buttons
    try:
        ok_button = WebDriverWait(driver, 10).until(
            lambda d: d.find_element(By.XPATH, success_ok_button_xpath) 
            if len(d.find_elements(By.XPATH, success_ok_button_xpath)) > 0 
            else d.find_element(By.XPATH, failure_ok_button_xpath)
        )
        
        # Scroll to the button and click it
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", ok_button)
        time.sleep(1)  # Allow animation or modal transition to complete
        ok_button.click()
        print("Clicked on the appropriate 'OK' button to confirm.")
    except Exception as e:
        print(f"Failed to find or click the 'OK' button: {e}")
def change_status(driver):
    driver.get("http://185.199.53.169:5000/admin/user-management")
    time.sleep(3)
    
    # Click on the delete button
    change_status_xpath = '/html/body/div[4]/div/div[6]/table/tbody/tr[1]/td[6]/div/div[2]/input'
    change_status = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, change_status_xpath))
    )
    change_status.click()
    time.sleep(3)

    # Define possible OK button XPaths
    success_ok_button_xpath = '/html/body/div[4]/div/div[7]/div/div/div/div[3]/div/button'
    failure_ok_button_xpath = '/html/body/div[4]/div/div[7]/div/div/div/div[3]/div/button'

    # Look for one of the OK buttons
    try:
        ok_button = WebDriverWait(driver, 10).until(
            lambda d: d.find_element(By.XPATH, success_ok_button_xpath) 
            if len(d.find_elements(By.XPATH, success_ok_button_xpath)) > 0 
            else d.find_element(By.XPATH, failure_ok_button_xpath)
        )
        
        # Scroll to the button and click it
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", ok_button)
        time.sleep(1)  # Allow animation or modal transition to complete
        ok_button.click()
        print("Clicked on the appropriate 'OK' button to confirm.")
    except Exception as e:
        print(f"Failed to find or click the 'OK' button: {e}")
    change_status_xpath = '//html/body/div[4]/div/div[6]/table/tbody/tr[1]/td[6]/div/div[1]/input'
    change_status = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, change_status_xpath))
    )
    change_status.click()
    time.sleep(3)

    # Define possible OK button XPaths
    success_ok_button_xpath = '/html/body/div[4]/div/div[7]/div/div/div/div[3]/div/button'
    failure_ok_button_xpath = '/html/body/div[4]/div/div[7]/div/div/div/div[3]/div/button'

    # Look for one of the OK buttons
    try:
        ok_button = WebDriverWait(driver, 10).until(
            lambda d: d.find_element(By.XPATH, success_ok_button_xpath) 
            if len(d.find_elements(By.XPATH, success_ok_button_xpath)) > 0 
            else d.find_element(By.XPATH, failure_ok_button_xpath)
        )
        
        # Scroll to the button and click it
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", ok_button)
        time.sleep(1)  # Allow animation or modal transition to complete
        ok_button.click()
        print("Clicked on the appropriate 'OK' button to confirm.")
    except Exception as e:
        print(f"Failed to find or click the 'OK' button: {e}")