import falcon

from .health import HealthCheckResource
from config import Config

def add_routes(api: falcon.API, cfg: Config):
    """ Registers endpoints with Falcon
    Args:
        - api: Falcon API object
        - cfg: Configuration
    """
    api.add_route(HealthCheckResource.Path, HealthCheckResource())
