from typing import Dict

import jwt

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

    def encode(self, jwt_secret: str) -> str:
        """ Encode an auth token to a string
        Args:
            - jwt_secret: Secret used to sign JWT hash
        """
        return jwt.encode(vars(self), jwt_secret, algorithm='HS256')

    def decode(self, encoded_jwt: str, jwt_secret: str):
        """ Decode an auth token from a string and save in class fields.
        Args:
            - encoded_jwt: Encoded auth token to decode
            - jwt_secret: Secret used to sign JWT hash

        Raises:
            - KeyError: If the encoded JWT is missing a required field
        """
        token = jwt.decode(encoded_jwt, jwt_secret, algorithms=['HS256'])

        self.sub = token['sub']
