import random
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from utility.logs import LoggingDriver
from selenium.webdriver.support.ui import Select
def add_new_category(driver):
    logging_driver = LoggingDriver(driver)
    print("Navigating to the category management page...")
    logging_driver.get("http://185.199.53.169:5000/static/category/get_all_category")
    time.sleep(3)

    try:
        # Click the "New" button to open the modal
        print("Clicking the 'New' button to open the modal...")
        new_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-bs-target='#new_category']"))
        )
        new_button.click()
        time.sleep(2)

        # Enter the category name
        print("Entering the category name...")
        category_name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "category_name"))
        )
        category_name_input.send_keys("Test Category")
        time.sleep(2)

        # Select "Yes" for Is_distance_therapy
        print("Selecting 'Yes' for Is_distance_therapy...")
        is_distance_therapy_dropdown = Select(
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "Is_distance_therapy"))
            )
        )
        is_distance_therapy_dropdown.select_by_value("yes")
        time.sleep(2)

        # Enter a description
        print("Entering the description...")
        description_textarea = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "description"))
        )
        description_textarea.send_keys("This is a test description for the category.")
        time.sleep(2)

        # Click the Save button
        print("Clicking the 'Save' button...")
        save_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
        )
        save_button.click()
        time.sleep(2)
        print("Category added successfully!")

    except NoSuchElementException as e:
        print(f"An element was not found: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def edit_category(driver):
    logging_driver = LoggingDriver(driver)
    print("Navigating to the category management page...")
    logging_driver.get("http://185.199.53.169:5000/static/category/get_all_category")
    time.sleep(3)

    try:
        # Select a random row from the table
        print("Selecting a random category to edit...")
        table_rows = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#table_body tr"))
        )
        random_row = random.choice(table_rows)
        random_row.click()
        time.sleep(2)

        # Click the "Edit" button
        print("Clicking the 'Edit' button...")
        edit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "edit"))
        )
        edit_button.click()
        time.sleep(2)

        # Update the category name
        print("Updating the category name...")
        category_name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "category_name"))
        )
        category_name_input.clear()
        category_name_input.send_keys("Updated Test Category")
        time.sleep(2)

        # Update the "Is distance therapy" dropdown
        print("Updating the 'Is distance therapy' dropdown...")
        is_distance_therapy_dropdown = Select(
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "Is_distance_therapy"))
            )
        )
        is_distance_therapy_dropdown.select_by_value("No")
        time.sleep(2)

        # Update the description
        print("Updating the description...")
        description_textarea = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "description"))
        )
        description_textarea.clear()
        description_textarea.send_keys("Updated description for the category.")
        time.sleep(2)

        # Click the "Update" button
        print("Clicking the 'Update' button...")
        update_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
        )
        update_button.click()
        time.sleep(2)
        # Handle the final "OK" button 
        ok_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[10]/div/div/div/div[3]/div/button"))
        )
        ok_button.click()
        time.sleep(2)
        
        print("Category updated successfully!")

    except NoSuchElementException as e:
        print(f"An element was not found: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
