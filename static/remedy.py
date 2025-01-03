import random
import time
import string

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from utility.database import fetch_customer_names
from selenium.common.exceptions import NoSuchElementException
from utility.logs import LoggingDriver
from selenium.webdriver.support.ui import Select


def generate_random_text(length=10):
    """
    Generate a random string of a given length.
    :param length: Length of the string
    :return: Randomly generated string
    """
    letters = string.ascii_letters + string.digits + " "
    return "".join(random.choice(letters) for _ in range(length))


def edit_remedy(driver):
    logging_driver = LoggingDriver(driver)
    logging_driver.get("http://185.199.53.169:5000/getRemedy")
    print("Navigated to remedy page.")
    time.sleep(3)

    wait = WebDriverWait(driver, 10)

    # Locate the remedy ID link and click it
    print("Locating remedy links...")
    remedy_links = wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "a[href*='/individualremedy/']")
        )
    )
    remedy_link = random.choice(remedy_links)
    remedy_link.click()
    print("Clicked on a remedy link.")
    time.sleep(2)

    # Locate and click the "Edit" button
    print("Locating the Edit button...")
    edit_button = wait.until(EC.element_to_be_clickable((By.ID, "edit")))
    edit_button.click()
    print("Clicked the Edit button.")
    time.sleep(2)

    # Edit the remedy name
    print("Editing the remedy name...")
    remedy_name_field = wait.until(
        EC.presence_of_element_located((By.ID, "edit-remedy-name"))
    )
    remedy_name_field.clear()
    random_name = generate_random_text(length=20)  # Generate random text
    remedy_name_field.send_keys(random_name)
    print(f"Set remedy name to: {random_name}")
    time.sleep(2)

    # Select remedy type from the dropdown
    print("Selecting remedy type...")
    remedy_type_dropdown = wait.until(
        EC.presence_of_element_located((By.ID, "edit-remedy-type"))
    )
    select = Select(remedy_type_dropdown)
    remedy_types = [
        option.get_attribute("value")
        for option in select.options
        if option.get_attribute("value")
    ]
    selected_remedy_type = random.choice(remedy_types)
    select.select_by_value(selected_remedy_type)
    print(f"Selected remedy type: {selected_remedy_type}")
    time.sleep(2)

    # Edit the remedy description
    print("Editing the remedy description...")
    remedy_desc_field = wait.until(
        EC.presence_of_element_located((By.ID, "edit-remedy-desc"))
    )
    remedy_desc_field.clear()
    random_description = generate_random_text(length=40)  # Generate random text
    remedy_desc_field.send_keys(random_description)
    print(f"Set remedy description to: {random_description}")
    time.sleep(2)

    # Locate and click the "Save" button
    print("Locating and clicking the Save button...")
    save_button = wait.until(EC.element_to_be_clickable((By.ID, "save")))
    save_button.click()
    print("Changes saved successfully.")
    time.sleep(2)

    ok_button = driver.find_element(By.ID, "global_Success_Message_Btn")
    ok_button.click()
    time.sleep(3)  # Adjust the sleep time based on how long it takes for the


def delete_remedy(driver):

    logging_driver = LoggingDriver(driver)
    logging_driver.get("http://185.199.53.169:5000/getRemedy")
    print("Navigated to remedy page.")
    time.sleep(3)

    wait = WebDriverWait(driver, 10)
    print("Locating remedy links...")
    remedy_links = wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "a[href*='/individualremedy/']")
        )
    )
    remedy_link = random.choice(remedy_links)
    remedy_link.click()
    print("Clicked on a remedy link.")
    time.sleep(2)
    # Locate and click the "Delete" button
    print("Locating the Delete button...")
    delete_button = wait.until(EC.element_to_be_clickable((By.ID, "delete")))
    delete_button.click()
    print("Clicked the Delete button.")
    time.sleep(2)

    # Handle the modal popup: click "Cancel" button
    print("Locating the Cancel button in the modal...")
    cancel_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-bs-dismiss='modal']"))
    )
    cancel_button.click()
    print("Clicked the Cancel button in the modal.")
    time.sleep(2)

    # Locate and click the "Delete" button again
    print("Locating the Delete button again...")
    delete_button = wait.until(EC.element_to_be_clickable((By.ID, "delete")))
    delete_button.click()
    print("Clicked the Delete button again.")
    time.sleep(2)

    # Confirm delete by clicking the confirmation "Delete" button in the modal
    print("Locating the Confirm Delete button in the modal...")
    confirm_delete_button = wait.until(
        EC.element_to_be_clickable((By.ID, "confirmDeleteButton"))
    )
    confirm_delete_button.click()
    print("Confirmed and executed the delete operation.")
    time.sleep(2)
