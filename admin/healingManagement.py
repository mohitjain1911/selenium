from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from utility.database import fetch_healer_name

def transfer_healing(driver):
    try:
        # Navigate to the page
        driver.get("http://185.199.53.169:5000/admin/healings-management?page=2")
        time.sleep(3)  # Allow the page to load

        # Find the div with the text "Transfer Healing"
        transfer_div = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[text()='Transfer Healing']")))
        transfer_div.click()
        print("Transfer Healing button clicked.")
        time.sleep(2)  # Allow the page to load

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Add a short wait before ending
        time.sleep(2)
