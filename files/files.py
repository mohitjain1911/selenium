from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from utility.logs import *

def filters(driver):
    logging_driver = LoggingDriver(driver)
    logging_driver.get("http://185.199.53.169:5000/files")
    time.sleep(3)

    try:
        # Locate and click the Filter button
        filter_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "filterBtn"))
        )
        filter_button.click()
        time.sleep(2)  # Adding sleep for stability

        # Input file name
        file_name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "filename"))
        )
        file_name_input.clear()
        file_name_input.send_keys("example_file")
        time.sleep(2)  # Adding sleep for stability

        # Select a random content type
        content_type_dropdown = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "contentType"))
        )
        content_type_dropdown.click()
        time.sleep(2)  # Adding sleep for stability
        content_type_options = driver.find_elements(By.XPATH, "//select[@name='contentType']/option")
        random_content_choice = random.choice(content_type_options[1:])  # Exclude the first default option
        random_content_choice.click()
        time.sleep(2)  # Adding sleep for stability

        # Select a random source type
        source_type_dropdown = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "sourceType"))
        )
        source_type_dropdown.click()
        time.sleep(2)  # Adding sleep for stability
        source_type_options = driver.find_elements(By.XPATH, "//select[@name='sourceType']/option")
        random_source_choice = random.choice(source_type_options[1:])  # Exclude the first default option
        random_source_choice.click()
        time.sleep(2)  # Adding sleep for stability

        # Input start date
        start_date_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "start-date"))
        )
        start_date_input.clear()
        start_date_input.send_keys("01-01-2025")
        time.sleep(2)  # Adding sleep for stability

        # Input end date
        end_date_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "end-date"))
        )
        end_date_input.clear()
        end_date_input.send_keys("15-01-2025")
        time.sleep(2)  # Adding sleep for stability

        # Click the Search button
        search_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and contains(text(), 'Search')]"))
        )
        search_button.click()
        time.sleep(2)  # Adding sleep for stability

        print("Filters applied successfully.")

    except Exception as e:
        print(f"An error occurred while applying filters: {e}")
