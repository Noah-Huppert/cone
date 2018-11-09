#!/usr/bin/env python3

import falcon

import routes

api = falcon.API(media_type=falcon.MEDIA_JSON)
routes.add_routes(api)
