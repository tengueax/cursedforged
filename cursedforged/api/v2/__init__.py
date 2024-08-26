from cursedforged.api.base import BaseAPIClient

from cursedforged.types import GetVersionsResponse2


class API_v2:
    def __init__(self, client: BaseAPIClient):
        self.client = client

    def get_game_versions(self, game_id: int) -> GetVersionsResponse2:
        """Get all available versions for each known version type of the specified game. A private game is only accessible to its respective API key.

        https://docs.curseforge.com/#get-versions-v2

        Args:
            game_id (int): A game unique id

        Returns:
            GetVersionsResponse2: A response object
        """
        response = self.client.get(
            "v2/games/{}/versions".format(game_id),
        )

        return GetVersionsResponse2(**response)
