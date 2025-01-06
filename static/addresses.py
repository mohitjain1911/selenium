import random
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utility.database import fetch_customer_names
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

def select_random_option_from_dropdown(driver, element_id):
    try:
        # Wait for the dropdown to be visible
        dropdown_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, element_id))
        )
        # Ensure the dropdown is clickable
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, element_id))
        )
        # Initialize the Select object
        dropdown = Select(dropdown_element)
        # Get all available options except the default "Select" option
        options = dropdown.options[1:]  # Exclude the first option if it's a placeholder
        if not options:
            print(f"No options available in dropdown with ID '{element_id}'.")
            return None
        # Select a random option
        random_choice = random.choice(options)
        dropdown.select_by_value(random_choice.get_attribute("value"))
        print(f"Selected '{random_choice.text}' from dropdown with ID '{element_id}'.")
        return random_choice.get_attribute("value")

    except Exception as e:
        print(f"Error selecting random option from dropdown with ID '{element_id}': {e}")
        return None

def click_random_link_in_table(driver):
    try:
        # Wait for the table links to be visible
        table_links = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "td.ps-2.py-2 a.text-decoration-none"))
        )
        
        if not table_links:
            print("No links found in the table.")
            return

        # Select a random link from the table
        random_link = random.choice(table_links)
        link_text = random_link.text
        random_link.click()
        print(f"Clicked on the link with text: {link_text}")

    except Exception as e:
        print(f"Error clicking a random link in the table: {e}")

def add_addresses(driver):
    logging_driver = LoggingDriver(driver)
    print("Navigating to the address management page...")
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
    populate_customer_name_field(driver, random.choice(customer_names))

    # Select a random address type
    print("Selecting a random address type...")
    address_type_dropdown = Select(
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "address_type"))
        )
    )
    # Get all available options except the default "Select" option
    options = address_type_dropdown.options[1:]  # Exclude the first option if it's a placeholder
    if options:
        random_choice = random.choice(options)
        address_type_dropdown.select_by_value(random_choice.get_attribute("value"))
        print(f"Selected address type: {random_choice.text}")
    else:
        print("No address type options available.")
    time.sleep(2)

    # Enter Flat No. and Building Name
    print("Entering Flat No. and Building Name...")
    flat_no_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "flatNoBuildingName"))
    )
    flat_no_input.clear()
    flat_no_input.send_keys("Flat 101, Sunshine Apartments")
    time.sleep(3)

    # Enter Local Area and Street Name
    print("Entering Local Area and Street Name...")
    locality_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "localityAreaStreet"))
    )
    locality_input.clear()
    locality_input.send_keys("Downtown Street, Near Central Park")
    time.sleep(3)

    # Select a random country
    print("Selecting a random country...")
    selected_country = select_random_option_from_dropdown(driver, "country")
    time.sleep(2)
    # Select a random state
    if selected_country:
        print("Selecting a random state...")
        selected_state = select_random_option_from_dropdown(driver, "state")
        time.sleep(2)
        # Wait for city dropdown to become enabled, if applicable
        if selected_state:
            print("Waiting for the city dropdown to be enabled...")
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "city"))
            )
            print("Selecting a random city...")
            select_random_option_from_dropdown(driver, "city")
            time.sleep(2)

    # Enter Postal Code
    print("Entering Postal Code...")
    postal_code_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "postalCode"))
    )
    postal_code_input.clear()
    postal_code_input.send_keys("411048")
    time.sleep(2)

    # Click the "Save" button
    add_address_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary.btn-sm"))
    )
    add_address_button.click()
    print("Clicked the 'Add Address' button.")
    time.sleep(2)
    OK = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[13]/div/div/div/div[4]/div/button"))
    )
    OK.click()
    time.sleep(2)
    # print("Address added successfully!")

def edit_addresses(driver):
    driver.get("http://185.199.53.169:5000/static/get_all_address")
    time.sleep(3)

    click_random_link_in_table(driver)

    print("Clicking the 'Edit' button...")
    edit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "edit_button"))
    )
    edit_button.click()
    time.sleep(2)

    print("Editing 'Type' dropdown...")
    select_random_option_from_dropdown(driver, "type")
    time.sleep(2)

    print("Editing 'Flat No/Building Name' field...")
    flat_no_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "flatNoBuildingName"))
    )
    flat_no_input.clear()
    flat_no_input.send_keys("Flat 202, Emerald Heights")

    print("Editing 'Locality and Street' field...")
    locality_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "localityAreaStreet"))
    )
    locality_input.clear()
    locality_input.send_keys("Uptown Avenue")
    time.sleep(2)
    
    print("Selecting a random country...")
    selected_country = select_random_option_from_dropdown(driver, "country")
    time.sleep(2)
    # Select a random state
    if selected_country:
        print("Selecting a random state...")
        selected_state = select_random_option_from_dropdown(driver, "state")
        time.sleep(2)
        # Wait for city dropdown to become enabled, if applicable
        if selected_state:
            print("Waiting for the city dropdown to be enabled...")
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "city"))
            )
            print("Selecting a random city...")
            select_random_option_from_dropdown(driver, "city")
            time.sleep(2)

    print("Entering Postal Code...")
    postal_code_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "postalCode"))
    )
    postal_code_input.clear()
    postal_code_input.send_keys("411048")
    time.sleep(2)

    print("Saving changes...")
    save_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    )
    save_button.click()
    time.sleep(2)
    print("Changes saved successfully.")
