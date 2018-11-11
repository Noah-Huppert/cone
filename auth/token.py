from typing import Dict

class AuthToken:
    """ JSON web token used to identify users with API
    Fields:
        - sub: User ID
    """
    def __init__(self, sub: str):
        """ Creates an AuthToken
        Args:
            - sub: Sub field value
        """
        self.sub: str = sub

    def to_dict(self) -> Dict[str]str:
        """ Returns a representation of the class in dict form
        Return: dict representation of class
        """
        return {
            'sub': self.sub
        }

    def encode(self, encode_secret: str) -> str:
        """ Encode an auth token to a string
        Args:
            - encode_secret: Secret used to sign JWT hash
        """
        pass
