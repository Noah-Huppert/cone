import falcon

from health import HealthCheckResource

def add_routes(api: falcon.API):
    """ Registers endpoints with Falcon
    Args:
        - api: Falcon API object
    """
    api.add_route(HealthCheckResource.Path, HealthCheckResource())
