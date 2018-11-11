import os

class Config:
    """ API configuration.
    Values are loaded from environment variables.

    Fields:
        - JWTSecret: Secret used to sign a AuthToken JWT, environment
            variable: JWT_SECRET
    """
    def __init__(self):
        """ Loads configuration from environment variables
        Raises:
            - KeyError: If a required environment variable is not present
        """
        try:
            self.JWTSecret = os.environ['JWT_SECRET']
        except KeyError as e:
            raise KeyError("missing environment variable for "+
                           "configuration: {}".format(e))

