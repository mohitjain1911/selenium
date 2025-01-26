from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from utility.database import fetch_healer_name  # Assuming this is needed

def transfer_healing(driver):
    try:
        # Navigate to the page
        driver.get("http://185.199.53.169:5000/admin/healings-management?page=2")
        time.sleep(3)  # Allow the page to load

        # Find the "Transfer Healing" button and click it
        transfer_div = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[text()='Transfer Healing']"))
        )
        transfer_div.click()
        print("Transfer Healing button clicked.")
        time.sleep(2)  # Allow the page to load

        # Find the dropdown and click to open it
        dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='ts-control']"))
        )
        dropdown.click()
        print("Dropdown opened.")
        time.sleep(1)

        # Get all options inside the dropdown
        options = driver.find_elements(By.XPATH, "//div[@class='ts-dropdown']//div[@class='option']")
        random_option = random.choice(options)
        random_option.click()
        print(f"Selected: {random_option.text}")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Add a short wait before ending
        time.sleep(2)

