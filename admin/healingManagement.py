from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

def transfer_healing(driver):
    try:
        # Navigate to the page
        driver.get("http://185.199.53.169:5000/admin/healings-management?page=2")
        time.sleep(3)  # Allow the page to load

        # Find and click "Transfer Healing" button
        transfer_div = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[text()='Transfer Healing']"))
        )
        transfer_div.click()
        print("Transfer Healing button clicked.")
        time.sleep(2)  

        # Find and open the dropdown
        dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='ts-control']"))
        )
        dropdown.click()
        print("Dropdown opened.")
        time.sleep(1.5)

        # Get all options inside the dropdown
        options = driver.find_elements(By.XPATH, "//div[@class='ts-dropdown']//div[@class='option']")
        if options:
            random_option = random.choice(options)
            random_option.click()
            print(f"Selected: {random_option.text}")
        else:
            print("No options found in dropdown.")

        time.sleep(2)

        # Select and enter start date
        start_date_input = driver.find_element(By.ID, "start-date")
        start_date_input.clear()
        start_date_input.send_keys("01-02-2025")
        print("Start date entered.")
        time.sleep(1.5)

        # Select and enter start time
        start_time_input = driver.find_element(By.ID, "start-time")
        start_time_input.clear()
        start_time_input.send_keys("10:00 AM")
        print("Start time entered.")
        time.sleep(2)

        # Click "Transfer Booking" button
        transfer_button = driver.find_element(By.ID, "confirm-yes")
        transfer_button.click()
        print("Transfer Booking confirmed.")
        time.sleep(3)

        # Click "OK" button to finalize
        success_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "global_Success_Message_Btn"))
        )
        success_btn.click()
        print("Transfer completed successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        time.sleep(2)
