from pydantic import BaseModel, Field

from .category import Category
from .minecraft import (
    MinecraftGameVersion,
    MinecraftModLoaderIndex,
    MinecraftModLoaderVersion,
)
from .mods import Mod
from .files import File
from .games import Game, GameVersionType, GameVersionsByType
from .fingerprints import FingerprintMatchesResult, FingerprintFuzzyMatchResult


class Pagination(BaseModel):
    """https://docs.curseforge.com/#tocS_Pagination"""

    index: int = Field(
        alias="index",
        description="A zero based index of the first item that is included in the response",
    )
    page_size: int = Field(
        alias="pageSize",
        description="The requested number of items to be included in the response",
    )
    result_count: int = Field(
        alias="resultCount",
        description="The actual number of items that were included in the response",
    )
    total_count: int = Field(
        alias="totalCount",
        description="The total number of items available by the request",
    )


class ApiResponseOfListOfMinecraftModLoaderIndex(BaseModel):
    """https://docs.curseforge.com/#tocS_ApiResponseOfListOfMinecraftModLoaderIndex"""

    data: list[MinecraftModLoaderIndex]


class ApiResponseOfMinecraftGameVersion(BaseModel):
    """https://docs.curseforge.com/#tocS_ApiResponseOfMinecraftGameVersion"""

    data: MinecraftGameVersion


class ApiResponseOfMinecraftModLoaderVersion(BaseModel):
    """https://docs.curseforge.com/#tocS_ApiResponseOfMinecraftModLoaderVersion"""

    data: MinecraftModLoaderVersion


class GetCategoriesResponse(BaseModel):
    """https://docs.curseforge.com/#tocS_Get%20Categories%20Response"""

    data: list[Category]


class GetFeaturedModsResponse(BaseModel):
    """https://docs.curseforge.com/#tocS_Get%20Featured%20Mods%20Response"""

    featured: list[Mod] = Field(alias="featured")
    popular: list[Mod] = Field(alias="popular")
    recently_updated: list[Mod] = Field(alias="recentlyUpdated")


class GetFilesResponse(BaseModel):
    """https://docs.curseforge.com/#tocS_Get%20Files%20Response"""

    data: list[File]


class GetGameResponse(BaseModel):
    """https://docs.curseforge.com/#tocS_Get%20Game%20Response"""

    data: Game


class GetGamesResponse(BaseModel):
    """https://docs.curseforge.com/#tocS_Get%20Games%20Response"""

    data: list[Game]
    pagination: Pagination


class GetModFileResponse(BaseModel):
    """https://docs.curseforge.com/#tocS_Get%20Mod%20File%20Response"""

    data: File


class GetModFilesResponse(BaseModel):
    """https://docs.curseforge.com/#tocS_Get%20Mod%20Files%20Response"""

    data: list[File]
    pagination: Pagination


class GetModResponse(BaseModel):
    """https://docs.curseforge.com/#tocS_Get%20Mod%20Response"""

    data: Mod


class GetModsResponse(BaseModel):
    """https://docs.curseforge.com/#tocS_Get%20Mods%20Response"""

    data: list[Mod]


class GetVersionTypesResponse(BaseModel):
    """https://docs.curseforge.com/#tocS_Get%20Version%20Types%20Response"""

    data: list[GameVersionType]


class GetVersionsResponse(BaseModel):
    """https://docs.curseforge.com/#tocS_Get%20Versions%20Response%20-%20V1"""

    data: list[GameVersionsByType]


class GetVersionsResponse2(BaseModel):
    """https://docs.curseforge.com/#tocS_Get%20Versions%20Response%20-%20V2"""

    data: list[GameVersionsByType]


class SearchModsResponse(BaseModel):
    data: list[Mod]
    pagination: Pagination


class ApiResponseOfListOfMinecraftGameVersion(BaseModel):
    """https://docs.curseforge.com/#tocS_ApiResponseOfListOfMinecraftGameVersion"""

    data: list[MinecraftGameVersion]


class StringResponse(BaseModel):
    """https://docs.curseforge.com/#tocS_String%20Response"""

    data: str


class GetFingerprintMatchesResponse(BaseModel):
    """https://docs.curseforge.com/#tocS_Get%20Fingerprint%20Matches%20Response"""

    data: list[FingerprintMatchesResult]


class GetFingerprintsFuzzyMatchesResponse(BaseModel):
    """https://docs.curseforge.com/#tocS_Get%20Fingerprints%20Fuzzy%20Matches%20Response"""

    data: list[FingerprintFuzzyMatchResult]
