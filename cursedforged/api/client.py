import requests
from typing import Any

from .base import BaseAPIClient
from .v1 import API_v1
from .v2 import API_v2


class APIClient(BaseAPIClient):
    def __init__(
        self,
        api_key: str,
        base_url: str = "https://api.curseforge.com",
        client: requests.Session | None = None,
    ):
        self.api_key = api_key
        self.base_url = base_url
        self.client = self._init_client(client)

        self.v1 = API_v1(self)
        self.v2 = API_v2(self)

    def _init_client(self, client: requests.Session | None) -> requests.Session:
        """Initialize the client with the specified client or create a new one if none is provided.

        Args:
            client (requests.Session | None, optional): The client to use. Defaults to None.

        Returns:
            requests.Session: The initialized client.
        """
        _client = client or requests.Session()
        _client.headers.update(
            {
                "x-api-key": self.api_key,
                "Accept": "application/json",
            }
        )
        return _client

    def _build_request_uri(self, endpoint: str) -> str:
        """Build the request URI for the specified endpoint.

        Args:
            endpoint (str): The endpoint to build the URI for.

        Returns:
            str: The built URI.
        """
        return "{}/{}/".format(self.base_url, endpoint.strip("/"))

    def get(self, endpoint: str, params: dict[str, Any] | None = None) -> Any:
        """Send a GET request to the specified endpoint.

        Args:
            endpoint (str): The endpoint to send the request to.
            params (dict[str, Any] | None, optional): The parameters to send with the request. Defaults to None.

        Returns:
            Any: The response data.
        """
        response = self.client.get(
            url=self._build_request_uri(endpoint),
            params=params or {},
        )

        return response.json()

    def post(self, endpoint: str, data: dict[str, Any] | None = None) -> Any:
        """Send a POST request to the specified endpoint.

        Args:
            endpoint (str): The endpoint to send the request to.
            data (dict[str, Any] | None, optional): The data to send with the request. Defaults to None.

        Returns:
            Any: The response data.
        """
        response = self.client.post(
            url=self._build_request_uri(endpoint),
            data=data or {},
        )

        return response.json()
