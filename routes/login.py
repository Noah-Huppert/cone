from config import Config
from auth import AuthToken
from browser import UserBrowsers

from voluptuous import Schema

class LoginResource:
    """ Starts a browser for the user and logs into SPIRE with the
    provided credentials. Returns an AuthToken for the user.
    """

    Path = '/api/v0/auth/login'

    Schema = Schema({
        'user_id': str,
        'password': str
    })

    def __init__(self, cfg: Config, user_browsers: UserBrowsers):
        """ Initialize LoginResource.
        Args:
            - cfg: Configuration
            - user_browsers: Collection of user browsers
        """
        self.cfg: Config = cfg
        self.user_browsers: UserBrowsers = user_browsers

    def on_get(self, req, resp):
        # Start browser
        browser = self.user_browsers.get_browser(req['user_id'])

