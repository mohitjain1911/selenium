#bookingManagemnt.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

def transfer_booking(driver):
    url = "http://185.199.53.169:5000/admin/bookings-management"
    # Open the specified URL
    driver.get(url)

    # Wait for the booking management page to load
    wait = WebDriverWait(driver, 10)
    driver.execute_script("arguments[0].scrollIntoView();", transfer_booking_button)
    time.sleep(3)

    # Click on the "Transfer Booking" button
    transfer_booking_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".d-flex.align-items-center.justify-content-center.pointer.border-primary"))
    )
    transfer_booking_button.click()

    # Wait for the modal form to appear
    time.sleep(2)
        # Open the dropdown
    dropdown_wrapper = driver.find_element(By.CSS_SELECTOR, "div.ts-wrapper.form-select.rounded-0.single")
    dropdown_wrapper.click()

    # Wait for the dropdown options to become visible
    WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div.ts-dropdown-content div.option"))
    )

    # Get all available options
    options = driver.find_elements(By.CSS_SELECTOR, "div.ts-dropdown-content div.option")
    if not options:
        raise ValueError("No options found in the dropdown.")

    # Select a random option
    selected_option = random.choice(options)
    selected_option.click()

    # Print the selected option's text
    print(f"Selected option: {selected_option.text}")

    # Step 2: Select a date using the calendar
    start_date_field = driver.find_element(By.ID, "start-date")
    start_date_field.click()

    # Wait for the calendar to appear and select a random date
    calendar_days = wait.until(
        EC.presence_of_all_elements_located((By.XPATH, "//table[@class='ui-datepicker-calendar']//a"))
    )
    random.choice(calendar_days).click()

    # Step 3: Enter a start time
    start_time_field = driver.find_element(By.ID, "start-time")
    start_time_field.send_keys("09:00 AM")

    # Step 4: Submit the form
    submit_button = driver.find_element(By.ID, "confirm-yes")
    submit_button.click()

    # Wait for the action to complete
    time.sleep(3)
