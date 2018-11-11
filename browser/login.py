from selenium import webdriver

""" XPath for SPIRE login user ID
"""
XPATH_SPIRE_LOGIN_USER_ID = '//*[@id="userid"]'

""" XPath for SPIRE login password
"""
XPATH_SPIRE_LOGIN_PASSWORD ='//*[@id="pwd"]'


def login(browser: webdriver.Firefox, user_id: str, password: str):
        """ Logins the user into SPIRE.
        Args:
            - browser: Selenium browser
            - user_id: ID of user to login as
            - password: Password to login with
        """
        # Navigate to SPIRE login page
        browser.get(URL_SPIRE_LOGIN)

        # Enter user credentials
        browser.find_element_by_xpath(XPATH_SPIRE_LOGIN_USER_ID)\
            .send_keys(user_id)
        browser.find_element_by_xpath(XPATH_SPIRE_LOGIN_PASSWORD)\
            .send_keys(password)

        # TODO: Determine if login succeeded or not
