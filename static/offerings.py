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

def edit_offering(driver):
    logging_driver = LoggingDriver(driver)
    logging_driver.get("http://185.199.53.169:5000/offerings")
    print("Navigated to offerings page.")
    time.sleep(3)
    try:
        # Wait for the offering table to load and select a random offering
        offering_links = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "td.pe-0.text-start a"))
        )
        random_offering = random.choice(offering_links)
        offering_name = random_offering.text
        random_offering.click()
        print(f"Selected and opened offering: {offering_name}")
        time.sleep(2)

        # Click the Edit button
        edit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "editBtn"))
        )
        edit_button.click()
        print("Clicked the 'Edit' button.")
        time.sleep(2)

        # Edit the offering name
        offering_name_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "offeringName"))
        )
        offering_name_field.clear()
        new_name = "Updated " + offering_name
        offering_name_field.send_keys(new_name)
        print(f"Updated the 'Offering Name' to: {new_name}")
        time.sleep(2)

        # Edit the offering type
        offering_type_field = Select(driver.find_element(By.ID, "editOfferingType"))
        new_type = random.choice(["PRODUCT", "SERVICE"])
        offering_type_field.select_by_value(new_type)
        print(f"Updated the 'Offering Type' to: {new_type}")
        time.sleep(2)

        # Edit the required days
        required_days_field = driver.find_element(By.ID, "editRequiredDays")
        required_days_field.clear()
        new_days = str(random.randint(1, 10))
        required_days_field.send_keys(new_days)
        print(f"Updated the 'Required Days' to: {new_days}")
        time.sleep(2)

        # Check and log the "Is Redeemable" radio buttons
        is_redeemable_yes = driver.find_element(By.ID, "isRedeemableYes")
        is_redeemable_no = driver.find_element(By.ID, "isRedeemableNo")
        if is_redeemable_yes.get_attribute("disabled") and is_redeemable_no.get_attribute("disabled"):
            print("The 'Is Redeemable' options are disabled. No changes can be made.")
        else:
            # Optionally update the "Is Redeemable" value if enabled
            new_redeemable_choice = random.choice(["true", "false"])
            redeemable_element = driver.find_element(
                By.CSS_SELECTOR, f'input[name="flexRadioDefault"][value="{new_redeemable_choice}"]'
            )
            redeemable_element.click()
            print(f"Updated 'Is Redeemable' to: {'Yes' if new_redeemable_choice == 'true' else 'No'}")
        time.sleep(2)
        
        # Edit the MRP
        mrp_field = driver.find_element(By.ID, "mrp")
        mrp_field.clear()
        new_mrp = str(random.randint(500, 1500))
        mrp_field.send_keys(new_mrp)
        print(f"Updated the 'MRP' to: {new_mrp}")
        time.sleep(2)

        # Edit the loyalty points required
        loyalty_points_field = driver.find_element(By.ID, "loyaltyPointsRequired")
        loyalty_points_field.clear()
        new_points = str(random.randint(500, 2000))
        loyalty_points_field.send_keys(new_points)
        print(f"Updated the 'Loyalty Points Required' to: {new_points}")
        time.sleep(2)

        # Edit the short description
        short_description_field = driver.find_element(By.ID, "editShortDescription")
        short_description_field.clear()
        new_short_description = "Updated: A quick consultation session."
        short_description_field.send_keys(new_short_description)
        print(f"Updated the 'Short Description' to: {new_short_description}")
        time.sleep(2)

        # Edit the long description
        long_description_field = driver.find_element(By.ID, "editLongDescription")
        long_description_field.clear()
        new_long_description = (
            "Updated: A comprehensive 30-min consultation call with experienced professionals "
            "to address and guide you on your healing journey."
        )
        long_description_field.send_keys(new_long_description)
        print(f"Updated the 'Long Description' to: {new_long_description}")
        time.sleep(2)

        # Update the offering
        update_button = driver.find_element(By.ID, "updateOfferingBtn")
        update_button.click()
        print("Clicked the 'Update' button.")
        time.sleep(3)

        print("Offering updated successfully.")
    except NoSuchElementException as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
