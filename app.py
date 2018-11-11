#!/usr/bin/env python3

import falcon

import routes
from config import Config

api = falcon.API(media_type=falcon.MEDIA_JSON)

cfg = Config()
routes.add_routes(api, cfg)
