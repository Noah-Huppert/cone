from voluptuous.error import Invalid
from falcon import HTTPBadRequest

class ValidateComponent:
    """ Validates a request body.
    Will be active if the resource which is set to respond to a request has a
    field named `Schema`.
    """
    def process_resource(self, req, resp, resource, params):
        """ Validates a request.
        Args:
            - req: Request
            - resp: Response
            - resource: Resource which will respond to request
            - params: Route parameters
        """
        # Check if resource has Schema field
        if 'Schema' not in vars(resource):
            return

        # Validate schema
        try:
            resource.Schema(req)
        except Invalid as e:
            raise HTTPBadRequest(description=str(e))
