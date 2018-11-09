from typing import Dict

from .browser import Browser

class UserBrowsers:
    """ Manages Selenium browsers for users
    Fields:
        - __browsers__: Current active browsers. Keys are user IDs.
    """
    def __init__(self):
        self.__browsers__: Dict[str]Browser = {}

    def get_browser(self, user_id: str) -> Browser:
        """ Get a browser for a specific user
        Args:
            - user_id: ID of user to get browser for

        Returns: Selenium browser for user
        """
        if user_id not in self.__browsers__:
            self.__browsers__[user_id] = Browser()

        return self.__browsers__[user_id]
