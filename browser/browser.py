from .login import login

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

""" SPIRE login URL
"""
URL_SPIRE_LOGIN = 'https://www.spire.umass.edu/psp/heproda/?cmd=login&languageCd=ENG'

""" XPath for element which indicates that the version of SPIRE we are using
is in production mode. Is on every SPIRE page.
"""
XPATH_SPIRE_ENVIRONMENT = '/html/body/div[2]/div/div/div[2]/table/tbody/tr/td[2]/div'

class Browser:
    """ Wrapper around a Selenium browser which keeps track of state and
    provides helper methods.

    Fields:
        - __browser__: Selenium browser
    """
    def __init__(self):
        """ Creates a wrapper around a selenium browser
        """
        self.__browser__: webdriver.Firefox = webdriver.Firefox(
            executable_path="./geckodriver")

    def is_logged_in(self) -> bool:
        """ Determines if the user is logged into SPIRE
        Returns: True if user is logged in
        """
        try:
            self.__browser__.find_element_by_xpath(XPATH_SPIRE_ENVIRONMENT)
            return True
        except NoSuchElementException:
            return False

    def login(self, user_id: str, password: str):
        """ Logins the user into SPIRE if they they are not already
        Args:
            - user_id: ID of user to login as
            - password: Password to login with
        """
        # If already logged in exit early
        if self.is_logged_in():
            return

        # Login
        login(self.__browser__, user_id, password)
