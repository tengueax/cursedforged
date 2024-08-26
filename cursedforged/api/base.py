import requests
from typing import Any

from abc import ABC, abstractmethod


class BaseAPIClient(ABC):
    def __init__(
        self,
        api_key: str,
        base_url: str = "https://api.curseforge.com",
        client: requests.Session | None = None,
    ):
        self.api_key = api_key
        self.base_url = base_url
        self.client = client or requests.Session()

    @abstractmethod
    def get(self, endpoint: str, params: dict[str, Any] | None = None) -> Any:
        """Send a GET request to the specified endpoint.

        Args:
            endpoint (str): The endpoint to send the request to.
            params (dict[str, Any] | None, optional): The parameters to send with the request. Defaults to None.

        Returns:
            Any: The response data.
        """
        pass

    @abstractmethod
    def post(self, endpoint: str, data: dict[str, Any] | None = None) -> Any:
        """Send a POST request to the specified endpoint.

        Args:
            endpoint (str): The endpoint to send the request to.
            data (dict[str, Any] | None, optional): The data to send with the request. Defaults to None.

        Returns:
            Any: The response data.
        """
        pass
