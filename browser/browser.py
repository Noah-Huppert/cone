from selenium import webdriver

class Browser:
    """ Wrapper around a Selenium browser which keeps track of state and
    provides helper methods.

    Fields:
        - __browser__: Selenium browser
        - __logged_in__: Indicates if the user has logged into SPIRE
    """
    def __init__(self):
        """ Creates a wrapper around a selenium browser
        """
        self.__browser__: webdriver.Firefox = webdriver.Firefox(
            executable_path="./geckodriver")
        self.__logged_in__ = False
