from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from utility.logs import *

def transfer_healing(driver):
    logging_driver = LoggingDriver(driver)
    logging_driver.get("http://185.199.53.169:5000/admin/healings-management?page=2")
    time.sleep(3)  # Allow the page to load fully

    try:
        # Wait for the "Transfer Healing" button to be visible
        transfer_btn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "pointer"))
        )
        
        # Ensure it's the correct button by verifying its text or child elements
        btn_text = transfer_btn.text
        if "Transfer Healing" in btn_text:
            logging_driver.info("Found the Transfer Healing button. Clicking it...")
            transfer_btn.click()
        else:
            logging_driver.warning("Transfer Healing button not found on this page.")
        
        # If there's a modal or next step after clicking, handle it here
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "healing-modal"))
        )
        logging_driver.info("Healing modal appeared successfully.")

    except Exception as e:
        logging_driver.error(f"An error occurred: {str(e)}")
    finally:
        # Clean-up actions or further navigation can be handled here
        time.sleep(random.randint(2, 5))  # Random wait to mimic human behavior

# Example usage:
# from selenium import webdriver
# driver = webdriver.Chrome()
# transfer_healing(driver)
