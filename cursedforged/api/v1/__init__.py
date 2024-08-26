from ..base import BaseAPIClient

from cursedforged.types import (
    Game,
    ModsSearchSortField,
    SortOrder,
    ModLoaderType,
    GetGamesResponse,
    GetVersionsResponse,
    GetVersionTypesResponse,
    GetCategoriesResponse,
    GetModResponse,
    GetModsResponse,
    GetFeaturedModsResponse,
    StringResponse,
    GetModFileResponse,
    GetModFilesResponse,
    GetFilesResponse,
    ApiResponseOfListOfMinecraftGameVersion,
    ApiResponseOfMinecraftGameVersion,
    ApiResponseOfListOfMinecraftModLoaderIndex,
    ApiResponseOfMinecraftModLoaderVersion,
    GetFingerprintMatchesResponse,
    FolderFingerprint,
    GetFingerprintsFuzzyMatchesResponse,
)


class API_v1:
    def __init__(self, client: BaseAPIClient):
        self.client = client

    def get_games(self, index: int = 0, page_size: int = 50) -> GetGamesResponse:
        """Get all games

        https://docs.curseforge.com/#get-games

        Args:
            index (int, optional): A zero based index of the first item to include in the response, the limit is: (index + pageSize <= 10,000).
            page_size (int, optional): The number of items to include in the response, the default/maximum value is 50.

        Returns:
            GetGamesResponse: A response object
        """
        response = self.client.get(
            "v1/games",
            params={
                "index": index,
                "pageSize": page_size,
            },
        )

        return GetGamesResponse(**response)

    def get_game(self, game_id: int) -> Game:
        """Get a game

        https://docs.curseforge.com/#get-game

        Args:
            game_id (int): A game unique id

        Returns:
            Game: A game object
        """
        response = self.client.get(
            "v1/games/{}".format(game_id),
        )
        return Game(**dict(response).get("data", {}))

    def get_game_versions(self, game_id: int) -> GetVersionsResponse:
        """Get all available versions for each known version type of the specified game. A private game is only accessible to its respective API key.

        https://docs.curseforge.com/#get-versions

        Args:
            game_id (int): A game unique id

        Returns:
            GetVersionsResponse: A response object
        """
        response = self.client.get(
            "v1/games/{}/versions".format(game_id),
        )

        return GetVersionsResponse(**response)

    def get_game_version_types(self, game_id: int) -> GetVersionTypesResponse:
        """Get all available version types of the specified game.

        https://docs.curseforge.com/#get-version-types

        A private game is only accessible to its respective API key.

        Currently, when creating games via the CurseForge for Studios Console, you are limited to a single game version type. This means that this endpoint is probably not useful in most cases and is relevant mostly when handling existing games that have multiple game versions such as World of Warcraft and Minecraft (e.g. 517 for wow_retail).

        Args:
            game_id (int): A game unique id

        Returns:
            GetVersionTypesResponse: A response object
        """
        response = self.client.get(
            "v1/games/{}/version-types".format(game_id),
        )
        return GetVersionTypesResponse(**response)

    def get_categories(
        self, game_id: int, class_id: int | None = None, classes_only: bool = False
    ) -> GetCategoriesResponse:
        """Get all available classes and categories of the specified game. Specify a game id for a list of all game categories, or a class id for a list of categories under that class. specifiy the classes Only flag to just get the classes for a given game.

        https://docs.curseforge.com/#get-categories

        Args:
            game_id (int): A game unique id
            class_id (int | None, optional): A class unique id. Defaults to None.
            classes_only (bool, optional): If true, only return the classes for the specified game. Defaults to False.

        Returns:
            GetCategoriesResponse: A response object
        """

        response = self.client.get(
            "v1/categories",
            params={
                "gameId": game_id,
                "classId": class_id,
                "classesOnly": classes_only,
            },
        )
        return GetCategoriesResponse(**response)

    def search_mods(
        self,
        game_id: int,
        class_id: int | None = None,
        category_id: int | None = None,
        category_ids: list[int] | None = None,
        game_version: str | None = None,
        game_versions: list[str] | None = None,
        search_filter: str | None = None,
        sort_field: ModsSearchSortField | None = None,
        sort_order: SortOrder | None = None,
        mod_loader_type: ModLoaderType | None = None,
        mod_loader_types: list[ModLoaderType] | None = None,
        game_version_type_id: int | None = None,
        author_id: int | None = None,
        primary_author_id: int | None = None,
        slug: str | None = None,
        index: int | None = 0,
        page_size: int | None = 50,
    ):
        """Get all mods that match the search criteria.

        https://docs.curseforge.com/#search-mods

        Args:
            game_id (int): A game unique id
            class_id (int | None, optional): Filter by section id (discoverable via Categories)
            category_id (int | None, optional): Filter by category id
            category_ids (list[int] | None, optional): Filter by a list of category ids - this will override categoryId
            game_version (str | None, optional): Filter by game version string
            game_versions (list[str] | None, optional): Filter by a list of game version strings - this will override
            search_filter (str | None, optional): Filter by free text search in the mod name and author
            sort_field (ModsSearchSortField | None, optional): Filter by ModsSearchSortField enumeration
            sort_order (SortOrder | None, optional): 'asc' if sort is in ascending order, 'desc' if sort is in descending order
            mod_loader_type (ModLoaderType | None, optional): Filter only mods associated to a given modloader (Forge, Fabric ...). Must be coupled with gameVersion.
            mod_loader_types (list[ModLoaderType] | None, optional): Filter by a list of mod loader types - this will override modLoaderType
            game_version_type_id (int | None, optional): Filter only mods that contain files tagged with versions of the given gameVersionTypeId
            author_id (int | None, optional): Filter only mods that the given authorId is a member of.
            primary_author_id (int | None, optional): Filter only mods that the given primaryAuthorId is the owner of.
            slug (str | None, optional): Filter by slug (coupled with classId will result in a unique result).
            index (int | None, optional): A zero based index of the first item to include in the response, the limit is: (index + pageSize <= 10,000).
            page_size (int | None, optional): The number of items to include in the response, the default/maximum value is 50.

        Returns:
            GetCategoriesResponse: A response object
        """
        response = self.client.get(
            "v1/mods/search",
            params={
                "gameId": game_id,
                "classId": class_id,
                "categoryId": category_id,
                "categoryIds": category_ids,
                "gameVersion": game_version,
                "gameVersions": game_versions,
                "searchFilter": search_filter,
                "sortField": sort_field,
                "sortOrder": sort_order,
                "modLoaderType": mod_loader_type,
                "modLoaderTypes": mod_loader_types,
                "gameVersionTypeId": game_version_type_id,
                "authorId": author_id,
                "primaryAuthorId": primary_author_id,
                "slug": slug,
                "index": index,
                "pageSize": page_size,
            },
        )
        return GetCategoriesResponse(**response)

    def get_mod(self, mod_id: int) -> GetModResponse:
        """Get a single mod.

        https://docs.curseforge.com/#get-mod

        Args:
            mod_id (int): The mod id

        Returns:
            GetModResponse: A response object
        """
        response = self.client.get(
            "v1/mods/{}".format(mod_id),
        )
        return GetModResponse(**response)

    def get_mods(
        self, mod_ids: list[int], filter_pc_only: bool | None = False
    ) -> GetModsResponse:
        """Get a list of mods belonging the the same game.

        https://docs.curseforge.com/#get-mods

        Args:
            mod_ids (list[int]): A list of mod ids
            filter_pc_only (bool | None, optional): Filter mods that are only available for PC. Defaults to False.

        Returns:
            GetModsResponse: A response object
        """
        response = self.client.post(
            "v1/mods",
            data={
                "modIds": mod_ids,
                "filterPcOnly": filter_pc_only,
            },
        )
        return GetModsResponse(**response)

    def get_featured_mods(
        self,
        game_id: int,
        excluded_mod_ids: list[int] | None = None,
        game_version_type_id: int | None = None,
    ) -> GetFeaturedModsResponse:
        """Get a list of featured, popular and recently updated mods.

        https://docs.curseforge.com/#get-featured-mods

        Args:
            game_id (int): A game unique id
            excluded_mod_ids (list[int] | None, optional): A list of mod ids to exclude from the response. Defaults to None.
            game_version_type_id (int | None, optional): Filter mods by game version type. Defaults to None.

        Returns:
            GetFeaturedModsResponse: A response object
        """
        response = self.client.post(
            "v1/mods/featured",
            data={
                "gameId": game_id,
                "excludedModIds": excluded_mod_ids,
                "gameVersionTypeId": game_version_type_id,
            },
        )
        return GetFeaturedModsResponse(**response)

    def get_mod_description(
        self,
        mod_id: int,
        raw: bool | None = None,
        stripped: bool | None = None,
        markup: bool | None = None,
    ) -> StringResponse:
        """Get the full description of a mod in HTML format.

        https://docs.curseforge.com/#get-mod-description

        Args:
            mod_id (int): The mod id
            raw (bool | None, optional): If true, the description will be returned as it is stored in the database. Defaults to None.
            stripped (bool | None, optional): If true, the description will be stripped of all HTML tags. Defaults to None.
            markup (bool | None, optional): If true, the description will be returned as it is stored in the database. Defaults to None.

        Returns:
            StringResponse: The mod description
        """
        response = self.client.get(
            "v1/mods/{}/description".format(mod_id),
            params={
                "raw": raw,
                "stripped": stripped,
                "markup": markup,
            },
        )
        return StringResponse(**response)

    def get_mod_file(self, mod_id: int, file_id: int) -> GetModFileResponse:
        """Get a single file of the specified mod.

        https://docs.curseforge.com/#get-mod-file

        Args:
            mod_id (int): The mod id the file belongs to
            file_id (int): The file id

        Returns:
            GetModFileResponse: The mod file
        """
        response = self.client.get(
            "v1/mods/{}/files/{}".format(mod_id, file_id),
        )
        return GetModFileResponse(**response)

    def get_mod_files(
        self,
        mod_id: int,
        game_version: str | None = None,
        mod_loader_type: ModLoaderType | None = None,
        game_version_type_id: int | None = None,
        index: int | None = 0,
        page_size: int | None = 50,
    ) -> GetModFilesResponse:
        """Get all files of the specified mod.

        https://docs.curseforge.com/#get-mod-files

        Args:
            mod_id (int): The mod id the files belong to
            game_version (str | None, optional): Filter by game version string. Defaults to None.
            mod_loader_type (ModLoaderType | None, optional): ModLoaderType enumeration. Defaults to None.
            game_version_type_id (int | None, optional): Filter only files that are tagged with versions of the given gameVersionTypeId. Defaults to None.
            index (int | None, optional): A zero based index of the first item to include in the response, the limit is: (index + pageSize <= 10,000).
            page_size (int | None, optional): The number of items to include in the response, the default/maximum value is 50.

        Returns:
            GetModFilesResponse: A response object
        """
        response = self.client.post(
            "v1/mods/{}/files".format(mod_id),
            data={
                "gameVersion": game_version,
                "modLoaderType": mod_loader_type,
                "gameVersionTypeId": game_version_type_id,
                "index": index,
                "pageSize": page_size,
            },
        )
        return GetModFilesResponse(**response)

    def get_files(self, file_ids: list[int]) -> GetFilesResponse:
        """Get a list of files.

        https://docs.curseforge.com/#get-files

        Args:
            file_ids (list[int]): A list of file ids

        Returns:
            GetFilesResponse: A response object
        """
        response = self.client.post(
            "v1/mods/files",
            data={
                "fileIds": file_ids,
            },
        )
        return GetFilesResponse(**response)

    def get_mod_file_changelog(self, mod_id: int, file_id: int) -> StringResponse:
        """Get the changelog of a file in HTML format.

        https://docs.curseforge.com/#get-mod-file-changelog

        Args:
            mod_id (int): The mod id the file belongs to
            file_id (int): The file id

        Returns:
            StringResponse: A response object
        """
        response = self.client.get(
            "v1/mods/{}/files/{}/changelog".format(mod_id, file_id),
        )
        return StringResponse(**response)

    def get_mod_file_download_url(self, mod_id: int, file_id: int) -> StringResponse:
        """Get a download url for a specific file.

        https://docs.curseforge.com/#get-mod-file-download-url

        Args:
            mod_id (int): The mod id the file belongs to
            file_id (int): The file id

        Returns:
            StringResponse: A response object
        """
        response = self.client.get(
            "v1/mods/{}/files/{}/download-url".format(mod_id, file_id),
        )
        return StringResponse(**response)

    def get_fingerprints_matches_by_game_id(
        self, game_id: int, fingerprints: list[int]
    ) -> GetFingerprintMatchesResponse:
        """Get mod files that match a list of fingerprints for a given game id.

        https://docs.curseforge.com/#get-fingerprints-matches-by-game-id

        Args:
            game_id (int): The game id for matching fingerprints
            fingerprints (list[int]): The request body containing an array of fingerprints

        Returns:
            GetFingerprintMatchesResponse: A response object
        """
        response = self.client.post(
            "v1/fingerprints/{}".format(game_id),
            data={
                "fingerprints": fingerprints,
            },
        )
        return GetFingerprintMatchesResponse(**response)

    def get_fingerprints_matches(
        self, fingerprints: list[int]
    ) -> GetFingerprintMatchesResponse:
        """Get mod files that match a list of fingerprints.

        https://docs.curseforge.com/#get-fingerprints-matches

        Args:
            fingerprints (list[int]): The request body containing an array of fingerprints

        Returns:
            GetFingerprintMatchesResponse: A response object
        """
        response = self.client.post(
            "v1/fingerprints",
            data={
                "fingerprints": fingerprints,
            },
        )
        return GetFingerprintMatchesResponse(**response)

    def get_fingerprints_fuzzy_matches_by_game_id(
        self, game_id: int, fingerprints: list[FolderFingerprint]
    ) -> GetFingerprintsFuzzyMatchesResponse:
        """Get mod files that match a list of fingerprints using fuzzy matching.

        https://docs.curseforge.com/#get-fingerprints-fuzzy-matches-by-game-id

        Args:
            game_id (int): The game id for matching fingerprints
            fingerprints (list[FolderFingerprint]): Game id and folder fingerprints options for the fuzzy matching

        Returns:
            GetFingerprintsFuzzyMatchesResponse: A response object
        """
        response = self.client.post(
            "/v1/fingerprints/fuzzy/{}".format(game_id),
            data={
                "fingerprints": fingerprints,
            },
        )
        return GetFingerprintsFuzzyMatchesResponse(**response)

    def get_fingerprints_fuzzy_matches(
        self, fingerprints: list[FolderFingerprint]
    ) -> GetFingerprintsFuzzyMatchesResponse:
        """Get mod files that match a list of fingerprints using fuzzy matching.

        https://docs.curseforge.com/#get-fingerprints-fuzzy-matches

        Args:
            fingerprints (list[FolderFingerprint]): Game id and folder fingerprints options for the fuzzy matching

        Returns:
            GetFingerprintsFuzzyMatchesResponse: A response object
        """
        response = self.client.post(
            "/v1/fingerprints/fuzzy",
            data={
                "fingerprints": fingerprints,
            },
        )
        return GetFingerprintsFuzzyMatchesResponse(**response)

    def get_minecraft_versions(
        self, sort_descending: bool | None = None
    ) -> ApiResponseOfListOfMinecraftGameVersion:
        """Get a list of all available Minecraft versions.

        https://docs.curseforge.com/#get-minecraft-versions

        Args:
            sort_descending (bool, optional): If true, the list will be sorted in descending order. Defaults to None.

        Returns:
            ApiResponseOfListOfMinecraftGameVersion: A response object
        """
        response = self.client.get(
            "v1/minecraft/version",
            params={
                "sortDescending": sort_descending,
            },
        )
        return ApiResponseOfListOfMinecraftGameVersion(**response)

    def get_minecraft_version(
        self, game_version_string: str
    ) -> ApiResponseOfMinecraftGameVersion:
        """Get a single Minecraft version.

        https://docs.curseforge.com/#get-specific-minecraft-version

        Args:
            game_version_string (str): The game version string

        Returns:
            ApiResponseOfMinecraftGameVersion: A response object
        """
        response = self.client.get(
            "v1/minecraft/version/{}".format(game_version_string),
        )
        return ApiResponseOfMinecraftGameVersion(**response)

    def get_minecraft_modloaders(
        self, version: str | None = None, include_all: bool | None = None
    ) -> ApiResponseOfListOfMinecraftModLoaderIndex:
        """Get a list of all available Minecraft modloaders.

        https://docs.curseforge.com/#get-minecraft-modloaders

        Args:
            version (str | None, optional): Filter by game version string. Defaults to None.
            include_all (bool | None, optional): If true, include all modloaders. Defaults to None.

        Returns:
            ApiResponseOfListOfMinecraftModLoaderIndex: A response object
        """
        response = self.client.get(
            "v1/minecraft/modloader",
            params={
                "version": version,
                "includeAll": include_all,
            },
        )
        return ApiResponseOfListOfMinecraftModLoaderIndex(**response)

    def get_minecraft_modloader(
        self, mod_loader_name: str
    ) -> ApiResponseOfMinecraftModLoaderVersion:
        """Get a single Minecraft modloader.

        https://docs.curseforge.com/#get-specific-minecraft-modloader

        Args:
            modloader_id (str): The modloader name

        Returns:
            ApiResponseOfMinecraftModLoaderVersion: A response object
        """
        response = self.client.get(
            "v1/minecraft/modloader/{}".format(mod_loader_name),
        )
        return ApiResponseOfMinecraftModLoaderVersion(**response)
