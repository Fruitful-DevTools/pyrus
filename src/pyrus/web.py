from . import *

class Requests:

    def __init__(self, base_url):
        self.base_url = base_url

    def __call__(self, path, params=None):
        """Makes a GET request to the specified path.

        Args:
            path: The path to the API endpoint.
            params: A dictionary of parameters to send with the request.

        Returns:
            The response from the API.
        """
        response = rq.get(self.base_url + path, params=params)
        if response.status_code == 200:
            response = ChainMap(json.loads(response.content)["public"], json.loads(response.content)["private"])
            return response
        else:
            print("Error making request:", response.status_code)
