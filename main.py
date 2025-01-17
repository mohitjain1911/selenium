from utility.login import login_to_dashboard
from admin import bookingManagement, coupounManagement, leadsManagement, user
from utility.selenium_report import *
from static import healer, remedy, offerings, category, addresses
from utility.database import fetch_coupouns
from utility.database import fetch_lead_names

class AdminTasks:
    def perform(driver):
        # AdminTasks.manage_coupons(driver)
        # AdminTasks.manage_leads(driver)
        # AdminTasks.manage_users(driver)
        AdminTasks.change_roles(driver)

    def manage_coupons(driver):
        coupounManagement.delete(driver)
        coupounManagement.actions(driver)
        coupoun_names = fetch_coupouns()
        for coupon_code in coupoun_names:
            print(f"Searching for coupon: {coupon_code}")
            coupounManagement.search_coupon_by_code(driver, coupon_code)

    def manage_leads(driver):
        leadsManagement.delete_lead(driver)
        lead_names = fetch_lead_names()
        for lead_name in lead_names:
            leadsManagement.search_lead_by_name(driver, lead_name)
        leadsManagement.toggle_checkboxes(driver)
        leadsManagement.bulk_delete_users(driver)
        

    def manage_bookings(driver):
        bookingManagement.transfer_booking(driver)

    def manage_users(driver):
        user.remove_user(driver)
        user.delete_user(driver)
        user.change_status(driver)

    def change_roles(driver):
        user.change_role_api_user(driver)
        user.change_role_api_admin(driver)
        user.change_role_user(driver)
        user.change_role_admin(driver)

class StaticTasks:
    def healer(driver):
        healer.add_new_healer(driver)
        healer.edit_healer(driver)
        healer.delete_healer(driver)
        healer.filters(driver)

    def remedy(driver):
        remedy.add_remedy(driver)
        remedy.edit_remedy(driver)
        remedy.delete_remedy(driver)
    
    def offerings(driver):
        offerings.add_offerings(driver)
        offerings.edit_offering(driver)
        offerings.delete_offering(driver)
    
    def category(driver):
        category.add_new_category(driver)
        category.edit_category(driver)
        category.delete_category(driver)
        
    def addresses(driver):
        addresses.add_addresses(driver)
        addresses.edit_addresses(driver)
        addresses.delete_addresses(driver)

    def perform(driver):
        # StaticTasks.healer(driver)
        # StaticTasks.remedy(driver)
        # StaticTasks.offerings(driver)
        # StaticTasks.category(driver)
        StaticTasks.addresses(driver)
    
def main():
    driver = login_to_dashboard()
    try:
        AdminTasks.perform(driver)
        # StaticTasks.perform(driver)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
