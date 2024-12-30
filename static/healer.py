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
def click_new_healer_button(driver):
    try:
        # Wait for the button to be clickable
        new_healer_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-bs-target='#new_healer']"))
        )
        new_healer_button.click()
        print("Clicked 'New Healer' button.")
    except Exception as e:
        print(f"Error clicking 'New Healer' button: {e}")

def populate_customer_name_field(driver, customer_name):
    # Wait for the input field to appear
    customer_name_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "healer_name"))
    )
    customer_name_field.clear()  # Clear any existing text
    customer_name_field.send_keys(customer_name) 
    print(f"Populated 'Customer Name' field with: {customer_name}")
    dropdown_items = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#Dropdown .ps-2.py-1'))
    )
    if dropdown_items:
        random_choice = random.choice(dropdown_items)

        driver.execute_script("arguments[0].scrollIntoView(true);", random_choice)

        driver.execute_script("arguments[0].click();", random_choice)
    
    # Try to locate the name suggestion and click it
    # You can find the suggestion by the text inside the span or by its ID, which seems to be dynamic here
    try:
        # Find the span element by its text content (e.g., Kalyani Bakal)
        suggestion = driver.find_element(By.XPATH, f"//span[text()='{customer_name}']")  # Adjust for exact match
        suggestion.click()
        print(f"Selected suggestion for: {customer_name}")
    except Exception as e:
        print(f"Error: {e}")

    # Optional: Print message to confirm
    time.sleep(1)
    print(f"Populated 'Customer Name' field with: {customer_name}") 

def add_new_healer(driver):
    logging_driver = LoggingDriver(driver)
    logging_driver.get("http://185.199.53.169:5000/getHealers")
    time.sleep(3)

    try:
        # Fetch customer names from the database
        customer_names = fetch_customer_names()
        if not customer_names:
            print("No customer names found in the database.")
            return
        click_new_healer_button(driver)
        populate_customer_name_field(driver, customer_names)
        ###########################################################################################################
        experience_in_months = random.randint(1, 36)
        experience_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "experienceInMonths"))
        )
        experience_field.clear()
        experience_field.send_keys(experience_in_months)
        print(f"Populated 'Experience in Months' field with: {experience_in_months}")
        time.sleep(2)
        ###########################################################################################################
       
       
        start_time_input = driver.find_element(By.CSS_SELECTOR, "#Start_timeInput")
        hours = random.randint(0, 12)
        minutes = random.randint(0, 59)
        time_string = f"{hours:02}:{minutes:02}"
        start_time_input.clear()
        start_time_input.send_keys(time_string)
        print(f"Set start time to {time_string}")
        time.sleep(2)
        
        ###########################################################################################################
       
        toggle_switch = driver.find_element(By.CSS_SELECTOR, ".toggle-switch_start_time")
        am_pm_value = random.choice(["AM", "PM"])
        # Get the current selected value by checking the "checked" attribute
        current_am_pm = driver.find_element(By.ID, "start_time_am").is_selected()
        if (am_pm_value == "AM" and not current_am_pm) or (am_pm_value == "PM" and current_am_pm):
            # Click the toggle switch if the desired value is different from the current value
            toggle_switch.click()
            print(f"Toggled start time period to {am_pm_value}")
        else:
            print(f"Start time period is already set to {am_pm_value}")
        time.sleep(2)
       ###########################################################################################################
   
        End_timeInput_input = driver.find_element(By.CSS_SELECTOR, "#End_timeInput")
        hours = random.randint(0, 12)
        minutes = random.randint(0, 59)
        time_string = f"{hours:02}:{minutes:02}"
        End_timeInput_input.clear()
        End_timeInput_input.send_keys(time_string)
        print(f"Set start time to {time_string}")
        time.sleep(2)


        toggle_switch = driver.find_element(By.CSS_SELECTOR, ".toggle-switch_end_time")
        am_pm_value = random.choice(["AM", "PM"])
        am_pm_value = "PM"
        # Get the current selected value by checking the "checked" attribute
        current_am_pm = driver.find_element(By.ID, "end_time_am").is_selected()
        if (am_pm_value == "AM" and not current_am_pm) or (am_pm_value == "PM" and current_am_pm):
            # Click the toggle switch if the desired value is different from the current value
            toggle_switch.click()
            print(f"Toggled start time period to {am_pm_value}")
        else:
            print(f"Start time period is already set to {am_pm_value}")
        time.sleep(2)
    
        healing_minutes = random.randint(0, 59)
        healing_minutes_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "healingTimeMins"))
        )
        healing_minutes_field.clear()
        healing_minutes_field.send_keys(healing_minutes)
        print(f"Populated 'healingTimeMins' field with: {healing_minutes}")
        time.sleep(2)
       
        healingsPerDay = random.randint(0, 59)
        healingsPerDay_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "healingsPerDay"))
        )
        healingsPerDay_field.clear()
        healingsPerDay_field.send_keys(healingsPerDay)
        print(f"Populated 'healingsPerDay' field with: {healingsPerDay}")
        time.sleep(2)

        dropdown = Select(driver.find_element(By.ID, "isDistressedHelplineMember"))
        selected_value = random.choice(["true", "false"])
        dropdown.select_by_value(selected_value)
        print(f"Selected value in dropdown: {selected_value}")
        time.sleep(2)
        
        # Automatic Payout
        dropdown_automatic_payout = Select(driver.find_element(By.ID, "automaticPayout"))
        automatic_payout_value = random.choice(["true", "false"])
        dropdown_automatic_payout.select_by_value(automatic_payout_value)
        print(f"Selected 'Automatic Payout': {automatic_payout_value}")
        time.sleep(2)

        # Is Inactive
        dropdown_is_inactive = Select(driver.find_element(By.ID, "isInactive"))
        is_inactive_value = random.choice(["true", "false"])
        dropdown_is_inactive.select_by_value(is_inactive_value)
        print(f"Selected 'Is Inactive': {is_inactive_value}")
        time.sleep(2)

        # Plan
        dropdown_plan = Select(driver.find_element(By.ID, "plan"))
        plan_value = random.choice(["FREE", "PREMIUM", "LOVENHEAL"])
        dropdown_plan.select_by_value(plan_value)
        print(f"Selected 'Plan': {plan_value}")
        time.sleep(2)

        # Data Verified
        dropdown_data_verified = Select(driver.find_element(By.ID, "dataVerified"))
        data_verified_value = random.choice(["true", "false"])
        dropdown_data_verified.select_by_value(data_verified_value)
        print(f"Selected 'Data Verified': {data_verified_value}")
        time.sleep(2)

        # Healer Rank
        dropdown_healer_rank = Select(driver.find_element(By.ID, "healerRank"))
        healer_rank_value = str(random.randint(1, 10))  # Random rank between 1 and 10
        dropdown_healer_rank.select_by_value(healer_rank_value)
        print(f"Selected 'Healer Rank': {healer_rank_value}")
        time.sleep(2)

        # Healing Level
        dropdown_healing_level = Select(driver.find_element(By.ID, "healingLevel"))
        healing_level_value = random.choice(["LEVEL1", "LEVEL2", "LEVEL3"])
        dropdown_healing_level.select_by_value(healing_level_value)
        print(f"Selected 'Healing Level': {healing_level_value}")
        time.sleep(2)

        # Data Verification Stage
        dropdown_data_verification_stage = Select(driver.find_element(By.ID, "dataVerificationStage"))
        data_verification_stage_value = random.choice([
            "NOT_INITIATED", "INITIATED", "VERIFICATION_PENDING", 
            "VERIFICATION_HOLD", "VERIFICATION_REJECTED", "VERIFIED"
        ])
        dropdown_data_verification_stage.select_by_value(data_verification_stage_value)
        print(f"Selected 'Data Verification Stage': {data_verification_stage_value}")
        time.sleep(2)

        dropdown_id = "selectBox"
        options_container_id = "optionsList"
        dropdown = driver.find_element(By.ID, dropdown_id)
        dropdown.click()
        time.sleep(2)  # Allow dropdown to expand

        # Locate all options in the dropdown
        options = driver.find_elements(By.CSS_SELECTOR, f"#{options_container_id} .option")

        if not options:
            raise Exception("No options found in the dropdown.")

        if len(options) < 10:
            raise ValueError("Requested number of options exceeds available options.")

        # Randomly select options
        selected_options = random.sample(options, 10)

        for option in selected_options:
            option.click()  # Click to select the option
            print(f"Selected option: {option.text.strip()}")
            time.sleep(1)  # Pause between selections for clarity

        # Optionally close the dropdown by clicking outside or on the dropdown again
        dropdown.click()
        
        time.sleep(1)
        # Locate the short bio input field
        short_bio = driver.find_element(By.ID, "shortBio")
        short_bio.clear()  # Clear any existing text
        short_bio.send_keys("This is a short bio of the healer.")  # Enter the short bio

        # Locate the long bio textarea
        long_bio = driver.find_element(By.ID, "longBio")
        long_bio.clear()  # Clear any existing text
        long_bio.send_keys("This is a detailed and comprehensive bio of the healer, describing their experience, methods, and specialties.")  # Enter the long bio

        # Optional: Verify the entered text
        print("Short Bio:", short_bio.get_attribute("value"))
        print("Long Bio:", long_bio.get_attribute("value"))

        
        save_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary.btn-sm.px-3")
        save_button.click()
        time.sleep(2)  # Adjust the sleep time as needed
        
        ok_button = driver.find_element(By.ID, "global_Success_Message_Btn")
        ok_button.click()
        time.sleep(3)  # Adjust the sleep time based on how long it takes for the 
    except Exception as e:
        print(f"Error in adding new healer: {e}")

def edit_healer(driver):
    logging_driver = LoggingDriver(driver)
    logging_driver.get("http://185.199.53.169:5000/getHealers")
    time.sleep(3)


    table_rows = driver.find_elements(By.CSS_SELECTOR, "#table_body tr")
    random_row = random.choice(table_rows)
    random_row.click()
    time.sleep(2)
    # Find and click the "Edit" button to open the edit form
    edit_button = driver.find_element(By.ID, "editHealer")
    edit_button.click()
    time.sleep(2)  # Wait for the edit form to load

    # Edit the "No Disturb Start Time"
    no_disturb_start_time_input = driver.find_element(By.ID, "noDisturbStartTime")
    no_disturb_start_time_input.clear()  # Clear the existing value
    no_disturb_start_time_input.send_keys("11:00 AM")  # Set the new time
    time.sleep(2)

    # Edit the "No Disturb End Time"
    no_disturb_end_time_input = driver.find_element(By.ID, "noDisturbEndTime")
    no_disturb_end_time_input.clear()  # Clear the existing value
    no_disturb_end_time_input.send_keys("12:00 PM")  # Set the new time
    time.sleep(2)

    # Edit the "Healer Rank"
    healer_rank_input = driver.find_element(By.NAME, "healerRank")
    healer_rank_input.clear()  # Clear the existing value
    healer_rank_input.send_keys("1.2")  # Set the new healer rank
    time.sleep(2)

    # Edit the "Healings Per Day"
    healings_per_day_input = driver.find_element(By.NAME, "healingsPerDay")
    healings_per_day_input.clear()  # Clear the existing value
    healings_per_day_input.send_keys("30")  # Set the new healings per day
    time.sleep(2)
    healing_time_input = driver.find_element(By.NAME, "healingTimeMins")
    healing_time_input.clear()  # Clear the existing value
    healing_time_input.send_keys("16")  # Set the new healing time
    time.sleep(2)

    # Edit the "Experience in Months"
    experience_months_input = driver.find_element(By.NAME, "experienceInMonths")
    experience_months_input.clear()  # Clear the existing value
    experience_months_input.send_keys("2")  # Set the new experience in months
    time.sleep(2)
    scroll(driver, direction="up", amount=700) 
    ######################################################################################################################################
    dropdown_selector = "#selectBox"  # Selector for the dropdown
    checkbox_selector = ".options input.option"  # Adjust to target checkboxes inside the dropdown
    dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, dropdown_selector))
    )
    dropdown.click()
    time.sleep(2)  # Wait for the dropdown to expand
  
    # Step 2: Locate all checkboxes
    checkboxes = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, checkbox_selector))
    )
    num_checkboxes=10
    # Ensure we do not select more checkboxes than available
    num_checkboxes = min(num_checkboxes, len(checkboxes))

    # Step 3: Randomly select checkboxes
    selected_checkboxes = random.sample(checkboxes, num_checkboxes)
    for checkbox in selected_checkboxes:
        driver.execute_script("arguments[0].scrollIntoView(true);", checkbox)  # Ensure visibility
        if not checkbox.is_selected():
            checkbox.click()
            time.sleep(1)  # Small delay between clicks

    print(f"Selected {num_checkboxes} random checkboxes.")
    ##################################################################################################################################

    # Select a random option for healingLevel
    healing_level_dropdown = Select(driver.find_element(By.ID, "healingLevel"))
    random_healing_level = random.choice(["LEVEL1", "LEVEL2", "LEVEL3"])
    healing_level_dropdown.select_by_value(random_healing_level)
    time.sleep(2)

    # Select a random option for dataVerificationStage
    verification_stage_dropdown = Select(driver.find_element(By.ID, "dataVerificationStage"))
    random_verification_stage = random.choice([
        "NOT_INITIATED", "INITIATED", "VERIFICATION_PENDING", 
        "VERIFICATION_HOLD", "VERIFICATION_REJECTED", "VERIFIED"
    ])
    verification_stage_dropdown.select_by_value(random_verification_stage)
    time.sleep(2)

    # Select a random option for plan
    plan_dropdown = Select(driver.find_element(By.ID, "plan"))
    random_plan = random.choice(["FREE", "PREMIUM", "LOVENHEAL"])
    plan_dropdown.select_by_value(random_plan)
    time.sleep(2)

    # Choose "Yes" or "No" for dataVerified
    data_verified_option = random.choice(["dataVerifiedYes", "dataVerifiedNo"])
    data_verified_radio = driver.find_element(By.ID, data_verified_option)
    data_verified_radio.click()
    time.sleep(2)

    # Choose "Yes" or "No" for automaticPayout
    automatic_payout_option = random.choice(["isautomaticPayoutYes", "isautomaticPayoutNo"])
    automatic_payout_radio = driver.find_element(By.ID, automatic_payout_option)
    automatic_payout_radio.click()
    time.sleep(2)

    # Choose "Yes" or "No" for isDistressedHelplineMember
    distressed_option = random.choice(["isDistressedYes", "isDistressedNo"])
    distressed_radio = driver.find_element(By.ID, distressed_option)
    distressed_radio.click()
    time.sleep(2)

    # Toggle the checkbox (switch) state
    flex_switch = driver.find_element(By.ID, "flexSwitchCheckChecked")
    flex_switch.click()
    time.sleep(2)
    short_bio_text = "This is a short bio example."
    long_bio_text = "This is a detailed long bio example, demonstrating automation of text input in textareas using Selenium."
    short_bio = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "shortBio"))
    )
    short_bio.clear()  # Clear any existing text
    short_bio.send_keys(short_bio_text)
    print("Short bio filled.")

    # Step 2: Locate and fill the long bio textarea
    long_bio = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "longBio"))
    )
    long_bio.clear()  # Clear any existing text
    long_bio.send_keys(long_bio_text)
    print("Long bio filled.")
    print("All elements interacted with successfully.")
    time.sleep(3)
    
    scroll(driver, direction="up", amount=700) 
    save_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "saveHealer"))
    )
    save_button = driver.find_element(By.XPATH, '//*[@id="saveHealer"]')
    save_button.click()
    time.sleep(3)

    try:
        # Try to locate the "success" button by its specific ID
        success_button = driver.find_element("id", "global_Success_Message_Btn")
        success_button.click()  # Click the success button if found
        print("Clicked the success button!")
    except NoSuchElementException:
        try:
            # If the "success" button is not found, try to locate the generic button by its class or text
            generic_button = driver.find_element("xpath", "//button[text()='OK' and @data-bs-dismiss='modal']")
            generic_button.click()  # Click the generic button if found
            print("Clicked the generic button!")
        except NoSuchElementException:
            # If neither button is found, handle accordingly
            print("No button found!")
def delete_healer(driver):
    logging_driver = LoggingDriver(driver)
    logging_driver.get("http://185.199.53.169:5000/getHealers")
    print("Navigated to 'getHealers' page.")
    time.sleep(3)

    table_rows = driver.find_elements(By.CSS_SELECTOR, "#table_body tr")
    random_row = random.choice(table_rows)
    random_row.click()
    print("Clicked on a random healer row.")

    view_all_healers_link = driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[1]/form/div[2]/a')
    view_all_healers_link.click()
    print("Clicked 'View All Healers' link.")
    time.sleep(2)

    table_rows = driver.find_elements(By.CSS_SELECTOR, "#table_body tr")
    random_row = random.choice(table_rows)
    random_row.click()
    print("Clicked on a random healer row again.")

    delete_button = driver.find_element(By.ID, "delete")
    delete_button.click()
    print("Clicked Delete button.")
    time.sleep(2)
    
    # Click the "No" button in the confirmation dialog
    no_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div[1]/div[2]/div/div/div/div[2]/div/form/button[2]"))
    )
    no_button.click()
    print("Clicked 'No' button in the confirmation dialog.")
    
    # Click the "Delete" button again
    delete_button = driver.find_element(By.ID, "delete")
    delete_button.click()
    print("Clicked Delete button again.")
    time.sleep(2)

    # Click the "Yes" button to confirm deletion
    yes_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div[1]/div[2]/div/div/div/div[2]/div/form/button[1]"))
    )
    yes_button.click()
    print("Clicked 'Yes' button to confirm deletion.")
    time.sleep(2)

    try:
        # Try to locate the "success" button by its specific ID
        success_button = driver.find_element("id", "global_Success_Message_Btn")
        success_button.click()  # Click the success button if found
        print("Clicked the success button!")
    except NoSuchElementException:
        try:
            # If the "success" button is not found, try to locate the generic button by its class or text
            generic_button = driver.find_element("xpath", "//button[text()='OK' and @data-bs-dismiss='modal']")
            generic_button.click()  # Click the generic button if found
            print("Clicked the generic button!")
        except NoSuchElementException:
            # If neither button is found, handle accordingly
            print("No button found!")


def scroll(driver, direction="down", amount=700):
    """
    Scroll the page either up or down.

    :param driver: The WebDriver instance (e.g., Chrome, Firefox)
    :param direction: "up" or "down", determines the scroll direction
    :param amount: The amount of pixels to scroll
    """
    if direction == "down":
        driver.execute_script(f"window.scrollBy(0, {amount});")
    elif direction == "up":
        driver.execute_script(f"window.scrollBy(0, -{amount});")
    else:
        print("Invalid direction. Use 'up' or 'down'.")

    # Wait for the page to adjust after scrolling
    time.sleep(1)