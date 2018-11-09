class HealthCheckResource:
    """ Static health check endpoint
    """

    Path = '/api/v0/healthz'

    def on_get(self, req, resp):
        resp.media = {
            'ok': True
        }
