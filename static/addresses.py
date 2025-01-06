import random
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from utility.database import fetch_customer_names
from selenium.common.exceptions import NoSuchElementException
from utility.logs import LoggingDriver
from selenium.webdriver.support.ui import Select
def populate_customer_name_field(driver, customer_name):
    # Wait for the input field to appear
    customer_name_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "search"))
    )
    customer_name_field.clear()  # Clear any existing text
    customer_name_field.send_keys(customer_name)
    print(f"Populated 'Customer Name' field with: {customer_name}")

def add_addresses(driver):
    logging_driver = LoggingDriver(driver)
    print("Navigating to the category management page...")
    logging_driver.get("http://185.199.53.169:5000/static/get_all_address")
    time.sleep(3)
    # Fetch customer names from the database
    customer_names = fetch_customer_names()
    if not customer_names:
        print("No customer names found in the database.")
        return
    print("Clicking the 'Add New' button...")
    add_new_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-bs-target='#create_new_address']"))
    )
    add_new_button.click()
    time.sleep(2)
    populate_customer_name_field(driver, customer_names)

    print("Selecting the address type...")
    address_type_dropdown = Select(
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "address_type"))
        )
    )
    address_type_dropdown.select_by_value("HOME")  # You can change this as needed
    time.sleep(2)

    # Enter Flat No. and Building Name
    print("Entering Flat No. and Building Name...")
    flat_no_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "flatNoBuildingName"))
    )
    flat_no_input.clear()
    flat_no_input.send_keys("Flat 101, Sunshine Apartments")
    time.sleep(2)

    # Enter Local Area and Street Name
    print("Entering Local Area and Street Name...")
    locality_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "localityAreaStreet"))
    )
    locality_input.clear()
    locality_input.send_keys("Downtown Street, Near Central Park")
    time.sleep(2)

    # Click the "Save" button
    print("Clicking the 'Save' button...")
    save_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    )
    save_button.click()
    time.sleep(2)


