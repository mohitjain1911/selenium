from selenium.webdriver.remote.webelement import WebElement
from datetime import datetime
from utility.selenium_report import generate_html_report  # Import the report generator function

LOG_FILE = "selenium_actions.log"
logged_elements = set()  # Track already logged elements to prevent duplicates

def log_action(step_name, result, message):
    """Logs actions with timestamp."""
    with open(LOG_FILE, "a") as file:
        file.write(f"{datetime.now()} - {step_name} - {result} - {message}\n")

class LoggingDriver:
    def __init__(self, driver):
        self.driver = driver

    def get(self, url):
        self.driver.get(url)
        log_action("Navigation", "Pass", f"Navigated to URL: {url}")

    def execute_script(self, script, *args):
        """Executes JavaScript and logs the action."""
        log_action("Execute Script", "Pass", f"Executed script: '{script}' with arguments: {args}")
        return self.driver.execute_script(script, *args)

    def find_element(self, *args, **kwargs):
        element = self.driver.find_element(*args, **kwargs)
        
        # Try to dynamically extract a human-readable name for the element
        try:
            readable_name = element.text.strip() if element.text.strip() else (
                element.get_attribute("aria-label") or 
                element.get_attribute("name") or 
                element.get_attribute("title") or 
                element.tag_name
            )
        except Exception:
            readable_name = "Unnamed Element"
        
        element_info = f"Located element: '{readable_name}'"
        if element_info not in logged_elements:
            log_action("Find Element", "Pass", element_info)
            logged_elements.add(element_info)  # Mark this element as logged
        
        return LoggingElement(element)

    def __getattr__(self, attr):
        return getattr(self.driver, attr)

    def quit(self):
        """Quit browser and trigger report generation."""
        self.driver.quit()
        log_action("Quit Browser", "Pass", "Closed the browser")
        print("Browser closed. Generating HTML report...")
        generate_html_report()  # Automatically generate the report when quitting the browser

# Logging Element Class to log interactions with web elements
class LoggingElement(WebElement):
    def __init__(self, element: WebElement):
        self.element = element

    def get_element_name(self):
        """Generate a user-friendly name for the element."""
        text = self.element.text.strip() if self.element.text.strip() else None
        aria_label = self.element.get_attribute("aria-label")
        title = self.element.get_attribute("title")
        placeholder = self.element.get_attribute("placeholder")
        name = self.element.get_attribute("name")
        class_attr = self.element.get_attribute("class")

        if text:
            return text
        elif aria_label:
            return aria_label
        elif title:
            return title
        elif placeholder:
            return placeholder
        elif name:
            return name
        elif class_attr:
            return class_attr.split()[0]
        return "Unnamed Element"

    def click(self):
        element_name = self.get_element_name()
        log_action("Click", "Pass", f"Clicked element: '{element_name}'")
        self.element.click()

    def send_keys(self, keys):
        element_name = self.get_element_name()
        log_action("Send Keys", "Pass", f"Entered '{keys}' into element: '{element_name}'")
        self.element.send_keys(keys)

    def __getattr__(self, attr):
        return getattr(self.element, attr)
