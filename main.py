from utility.login import *
from static.healer import *
from admin.bookingManagement import *
from admin.coupounManagement import *
from admin.leadsManagement import *
from admin.user import *
from utility.selenium_report import *
def admin_tasks(driver):
    change_date(driver)
    delete(driver)  # Call delete coupoun functionality
    delete_lead(driver)  # Call delete lead functionality
    toggle_checkboxes(driver)  # Call toggle checkbox functionality
    transfer_booking(driver)
    bulk_delete_users(driver)

    lead_names = fetch_lead_names()
    for lead_name in lead_names:
        search_lead_by_name(driver, lead_name)

    coupoun_names = fetch_coupouns(driver)
    for coupon_code in coupoun_names:
        print(f"Searching for coupon: {coupon_code}")
        search_coupon_by_code(driver, coupon_code)

    change_role_api_user(driver)
    change_role_api_admin(driver)
    change_role_user(driver)
    change_role_admin(driver)
    remove_user(driver)
    delete_user(driver)
    change_status(driver)


def static_tasks(driver):
    add_new_healer(driver)
    # edit_healer(driver)


def main():
    driver = login_to_dashboard()
    try:
        # admin_tasks(driver)
        static_tasks(driver)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
