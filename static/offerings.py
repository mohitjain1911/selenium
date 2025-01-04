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


def add_offerings(driver):
    logging_driver = LoggingDriver(driver)
    logging_driver.get("http://185.199.53.169:5000/offerings")
    print("Navigated to offerings page.")
    time.sleep(3)

    try:
        # Click the "New" button
        new_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "new"))
        )
        new_button.click()
        print("Clicked the 'New' button.")
        time.sleep(2)

        # Fill out the offering name
        offering_name = driver.find_element(By.ID, "offeringName")
        offering_name.send_keys("Test Offering")
        print("Filled out the 'Offering Name' field.")
        time.sleep(2)

        # Select a random offering type
        offering_type = Select(driver.find_element(By.ID, "offeringType"))
        random_choice = random.choice(["SERVICE", "PRODUCT"])
        offering_type.select_by_value(random_choice)
        print(f"Selected offering type: {random_choice}.")
        time.sleep(2)

        # Fill out the required days
        required_days = driver.find_element(By.ID, "requiredDays")
        required_days.send_keys("5")
        print("Filled out the 'Required Days' field.")
        time.sleep(2)

        # Fill out the MRP
        mrp = driver.find_element(By.ID, "mrp")
        mrp.send_keys("500")
        print("Filled out the 'MRP' field.")
        time.sleep(2)

        # Fill out the short description
        short_description = driver.find_element(By.ID, "shortDescription")
        short_description.send_keys("This is a test offering.")
        print("Filled out the 'Short Description' field.")
        time.sleep(2)

        # Randomly select "Is redeemable"
        is_redeemable_choice = random.choice(["true", "false"])
        redeemable_element = driver.find_element(
            By.CSS_SELECTOR, f'input[name="isRedeemable"][value="{is_redeemable_choice}"]'
        )
        redeemable_element.click()
        print(f"Selected 'Is redeemable' as: {'Yes' if is_redeemable_choice == 'true' else 'No'}.")
        time.sleep(2)

        # Fill out the loyalty points required (only if redeemable is "Yes")
        if is_redeemable_choice == "true":
            loyalty_points = driver.find_element(By.ID, "loyaltyPointsRequired")
            loyalty_points.send_keys("100")
            print("Filled out the 'Loyalty Points Required' field.")
            time.sleep(2)

        # Submit the form
        submit_button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")
        submit_button.click()
        print("Clicked the 'Save' button.")
        time.sleep(3)
        ok_button = driver.find_element(By.XPATH, "/html/body/div[15]/div/div/div/div[4]/div/button")
        ok_button.click()
        time.sleep(3)  # Adjust the sleep time based on how long it takes for the 
        print("Offering added successfully.")
    except NoSuchElementException as e:
        
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
