#!/usr/bin/env python3

import falcon

import routes
from config import Config
from middleware import ValidateComponent

api = falcon.API(
    media_type=falcon.MEDIA_JSON,
    middleware=[
        ValidateComponent()
    ]
)

cfg = Config()
routes.add_routes(api, cfg)
