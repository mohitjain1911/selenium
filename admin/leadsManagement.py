# leadsManagement.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import mysql.connector
import time
def delete_lead(driver):
    """
    Navigate to the Leads Management page and test the 'Delete Lead' functionality.
    """
    try:
        # Navigate to the leads management page
        driver.get("http://185.199.53.169:5000/admin/leads-management")
        time.sleep(2)  # Wait for the page to load

        # Locate the "Delete Lead" button using CSS selector
        delete_button = driver.find_element(By.CSS_SELECTOR, "div.border.border-primary.d-flex.align-items-center.p-1.gap-2.pointer div:nth-child(2)")

        # Click the button to test its functionality
        delete_button.click()
        print("Delete Lead button clicked.")

        time.sleep(3)
        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located((By.ID, "loading"))
        )

        # Handle success/error message
        time.sleep(2)
        try:
            success_message = driver.find_element(By.CSS_SELECTOR, ".alert-success")
            print(f"Success Message: {success_message.text}")
        except Exception:
            print("No success message found.")
    except Exception as e:
        print(f"Error occurred: {e}")


def toggle_checkboxes(driver):

    try:
        driver.get("http://185.199.53.169:5000/admin/leads-management")
        time.sleep(2)  # Wait for the page to load

        # Wait for the 'Verified' checkbox to be visible
        verified_checkbox = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "enable-1"))
        )

        # Wait for the 'Move to Spam' checkbox to be visible
        spam_checkbox = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "disable-1"))
        )

        # Check the current status of both checkboxes
        is_verified_checked = verified_checkbox.is_selected()
        is_spam_checked = spam_checkbox.is_selected()

        # Toggle checkboxes based on current state
        if is_verified_checked:
            verified_checkbox.click()  # Uncheck 'Verified'
            print("Unchecked 'Verified' checkbox.")
            if not is_spam_checked:
                spam_checkbox.click()  # Check 'Move to spam'
                print("Checked 'Move to spam' checkbox.")
        else:
            verified_checkbox.click()  # Check 'Verified'
            print("Checked 'Verified' checkbox.")
            if is_spam_checked:
                spam_checkbox.click()  # Uncheck 'Move to spam'
                print("Unchecked 'Move to spam' checkbox.")

        time.sleep(2)  # Adjust if needed for UI updates

    except Exception as e:
        print(f"Error occurred while toggling checkboxes: {e}")




# Function to connect to the database and fetch lead names
def fetch_lead_names():
    """
    Connects to the database and retrieves a list of lead names.
    Returns a list of lead names.
    """
    from dotenv import dotenv_values  # Load database config
    config = dotenv_values("config.txt")

    try:
        # Establish database connection
        conn = mysql.connector.connect(
            host=config['host'],
            user=config['db_user'],
            password=config['db_password'],
            database=config['database'],
            port=config['port']
        )
        cursor = conn.cursor()

        # Query to fetch names
        query = "SELECT name FROM marketing_leads LIMIT 1"  # Update the table name to your actual table
        cursor.execute(query)
        lead_names = [row[0] for row in cursor.fetchall()]  # Extract names

        conn.close()
        return lead_names
    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
        return []

# Function to search for a lead by name
def search_lead_by_name(driver, lead_name):
    """
    Searches for a lead by name using the search field.
    """
    try:
        # Navigate to the Leads Management page
        driver.get("http://185.199.53.169:5000/admin/leads-management")
        time.sleep(2)  # Wait for the page to load

        # Find the search input field and enter the lead name
        search_input = driver.find_element(By.ID, "input-search")
        search_input.clear()  # Clear any existing input
        search_input.send_keys(lead_name)
        search_input.send_keys("\n")  # Simulate pressing Enter

        # Wait for results to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".lead-item"))  # Update selector for lead items
        )

        # Verify if the lead appears in the results
        results = driver.find_elements(By.CSS_SELECTOR, ".lead-item")  # Update selector based on your page
        for result in results:
            if lead_name.lower() in result.text.lower():
                print(f"Lead '{lead_name}' found in the results.")
                return
        print(f"Lead '{lead_name}' not found.")
    except Exception as e:
        print(f"Error occurred while searching for lead '{lead_name}': {e}")
def scroll_into_view(driver, element):
    """
    Scrolls the page so that the specified element is in the viewport.
    """
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

def bulk_delete_users(driver):
    try:
        # Step 1: Navigate to the Leads Management page
        driver.get("http://185.199.53.169:5000/admin/leads-management")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "user-checked")))
        time.sleep(3)
        # Step 2: Select a few checkboxes
        checkboxes = driver.find_elements(By.CLASS_NAME, "user-checked")
        if len(checkboxes) < 3:
            raise ValueError("Not enough checkboxes to select.")

        for checkbox in checkboxes[:3]:  # Select first 3 checkboxes
            if not checkbox.is_selected():
                scroll_into_view(driver, checkbox)  # Scroll into view
                checkbox.click()
                print(f"Checkbox with data-user-id '{checkbox.get_attribute('data-user-id')}' selected.")
        time.sleep(3)
        # Step 3: Click Bulk Action button
        bulk_action_button = driver.find_element(By.CSS_SELECTOR, ".dropdown-toggle")
        scroll_into_view(driver, bulk_action_button)  # Scroll into view
        bulk_action_button.click()
        print("Bulk Action dropdown clicked.")
        time.sleep(3)
        # Step 4: Click Bulk Delete
        bulk_delete_option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".dropdown-item.action"))
        )
        scroll_into_view(driver, bulk_delete_option)  # Scroll into view
        bulk_delete_option.click()
        print("Bulk Delete option clicked.")
        time.sleep(3)
        # Step 5: Handle confirmation (if any)
        confirmation_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "confirm-yes"))
        )
        confirmation_button.click()
        print("Confirmation clicked for bulk delete.")
        time.sleep(3)
        # Wait for deletion to complete
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.ID, "loading")))
       
    except Exception as e:
        print(f"Error during bulk delete: {e}")