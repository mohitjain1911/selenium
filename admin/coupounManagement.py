# coupounManagement.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import random

def actions(driver):

    try:
        # Navigate to the coupon management page
        driver.get("http://185.199.53.169:5000/admin/coupons-management")
        time.sleep(3)  # Wait for the page to load

        # Click the dropdown button to see actions
        dropdown_button_xpath = '/html/body/div[4]/div/div[4]/table/tbody/tr[2]/td[7]/div/div[1]/button'
        dropdown_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, dropdown_button_xpath))
        )
        dropdown_button.click()
        time.sleep(3)
        
        # Click the 'Change Usage' option in the dropdown
        change_usage_option_xpath = '/html/body/div[4]/div/div[4]/table/tbody/tr[2]/td[7]/div/div[1]/div/div[2]/div[2]'
        change_usage_option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, change_usage_option_xpath))
        )
        change_usage_option.click()
        time.sleep(3)

        # Enter a new usage number
        usage_input_xpath = '/html/body/div[4]/div/div[5]/div/form/div[2]/div[2]/input'
        usage_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, usage_input_xpath))
        )
        time.sleep(3)
        usage_number = random.randint(1, 100)  # Generate a random usage number
        usage_input.clear()
        usage_input.send_keys(str(usage_number))
        time.sleep(3)

        # Click the 'Confirm' button to save changes
        confirm_button_class = 'btn.border.rounded-1.bg-primary.text-white'
        confirm_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, confirm_button_class))
        )
        confirm_button.click()
        time.sleep(3)

        print(f"Successfully updated usage to {usage_number}.")
        try:
             # Wait for the 'OK' button to become clickable
            ok_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "global_Success_Message_Btn"))
            )
            ok_button.click()
            print("Clicked the OK button successfully.")
        except Exception as e:
            print(f"An error occurred while clicking the OK button: {e}")

  
        
    except Exception as e:
        print(f"An error occurred: {e}")

def change_date(driver):
    
        driver.get("http://185.199.53.169:5000/admin/coupons-management")
        time.sleep(3)  # Wait for the page to load
        dropdown_button_xpath = '/html/body/div[4]/div/div[4]/table/tbody/tr[2]/td[7]/div/div[1]/button'
        dropdown_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, dropdown_button_xpath))
        )
        dropdown_button.click()
        time.sleep(3)
        wait = WebDriverWait(driver, 10)
        
        # Click the 'Change Usage' option in the dropdown
        change_date_option_xpath = '/html/body/div[4]/div/div[4]/table/tbody/tr[2]/td[7]/div/div[1]/div/div[3]/div[2]'
        change_date_option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, change_date_option_xpath))
        )
        change_date_option.click()
        time.sleep(3)
        date_input_xpath = '/html/body/div[4]/div/div[5]/div/form/div[3]/div[2]/input'
        date_input = wait.until(
            EC.element_to_be_clickable((By.XPATH, date_input_xpath))
        )
        date_input.click()
        print("Calendar opened.")

        # Wait for calendar dates to be visible
        calendar_dates_xpath = '/html/body/div[13]/table/tbody/tr/td/a'
        calendar_dates = wait.until(
            EC.presence_of_all_elements_located((By.XPATH, calendar_dates_xpath))
        )

        # Select a random date
        if calendar_dates:
            random_date = random.choice(calendar_dates)
            random_date_text = random_date.get_attribute("data-date")
            random_date.click()
            print(f"Selected random date: {random_date_text}")
        else:
            print("No dates available in the calendar.")

     # Click the 'Confirm' button to save changes
        confirm_button_class = 'btn.border.rounded-1.bg-primary.text-white'
        confirm_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, confirm_button_class))
        )
        confirm_button.click()
        time.sleep(3)

        print(f"Successfully updated datet to {random_date}.")
        try:
             # Wait for the 'OK' button to become clickable
            ok_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "global_Success_Message_Btn"))
            )
            ok_button.click()
            print("Clicked the OK button successfully.")
        except Exception as e:
            print(f"An error occurred while clicking the OK button: {e}")

def delete(driver):
        driver.get("http://185.199.53.169:5000/admin/coupons-management")
        time.sleep(3)
        delete_button = driver.find_element(By.XPATH, "/html/body/div[4]/div/div[4]/table/tbody/tr[2]/td[7]/div/div[2]")
        time.sleep(3)
        # Click the first delete button
        delete_button.click()
        time.sleep(3)
        print("First coupon deleted.")

        try:
             # Wait for the 'OK' button to become clickable
            ok_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "global_Success_Message_Btn"))
            )
            ok_button.click()
            print("Clicked the OK button successfully.")
        except Exception as e:
            print(f"An error occurred while clicking the OK button: {e}")
        time.sleep(3)
        back_btn = driver.find_element(By.CSS_SELECTOR, ".pointer.text-secondary")
        back_btn.click()
        print("back Success")
def fetch_coupouns(driver):
    driver.get("http://185.199.53.169:5000/admin/coupons-management")
    time.sleep(3)
    
    """
    Connects to the database and retrieves a list of coupon codes.
    Returns a list of coupon codes.
    """
    from dotenv import dotenv_values  # Load database config
    import mysql.connector
    config = dotenv_values("config.txt")

    try:
        # Establish database connection
        conn = mysql.connector.connect(
            host=config['host'],
            user=config['db_user'],
            password=config['db_password'],
            database=config['database'],
            port=config['port']
        )
        cursor = conn.cursor()

        # Query to fetch coupon codes
        query = "SELECT name FROM coupons LIMIT 1"  # Example: Fetching first 10 coupon codes
        cursor.execute(query)
        coupoun_names = [row[0] for row in cursor.fetchall()]  # Extract coupon codes

        conn.close()
        return coupoun_names
        
    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
        return []
def search_coupon_by_code(driver, coupon_code):
    """
    Searches for a coupon by code using the search field on the Coupons Management page.
    """
    try:
        # Navigate to the Coupons Management page
        driver.get("http://185.199.53.169:5000/admin/coupons-management")
        time.sleep(2)  # Wait for the page to load

        # Locate the search input field
        search_input = driver.find_element(By.ID, "input-search")
        search_input.clear()  # Clear any existing input
        search_input.send_keys(coupon_code)  # Enter the coupon code
        search_input.send_keys("\n")  # Simulate pressing Enter

        # Wait for results to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".coupon-item"))  # Update with the correct CSS selector for coupon items
        )

        # Verify if the coupon appears in the results
        results = driver.find_elements(By.CSS_SELECTOR, ".coupon-item")  # Update with the correct selector
        for result in results:
            if coupon_code.lower() in result.text.lower():
                print(f"Coupon '{coupon_code}' found in the results.")
                return
        print(f"Coupon '{coupon_code}' not found.")
    except Exception as e:
        print(f"Error occurred while searching for coupon '{coupon_code}': {e}")