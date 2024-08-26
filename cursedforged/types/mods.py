from datetime import datetime

from pydantic import BaseModel, Field

from .category import Category
from .enums import ModStatus
from .files import File, FileIndex


class ModAsset(BaseModel):
    """https://docs.curseforge.com/#tocS_ModAsset"""

    id: int = Field(alias="id")
    mod_id: int = Field(alias="modId")
    title: str = Field(alias="title")
    description: str = Field(alias="description")
    thumbnail_url: str = Field(alias="thumbnailUrl")
    url: str = Field(alias="url")


class ModAuthor(BaseModel):
    """https://docs.curseforge.com/#tocS_ModAuthor"""

    id: int = Field(alias="id")
    name: str = Field(alias="name")
    url: str = Field(alias="url")


class ModLinks(BaseModel):
    """https://docs.curseforge.com/#tocS_ModLinks"""

    website_url: str | None = Field(alias="websiteUrl")
    wiki_url: str | None = Field(alias="wikiUrl")
    issues_url: str | None = Field(alias="issuesUrl")
    source_url: str | None = Field(alias="sourceUrl")


class Mod(BaseModel):
    """https://docs.curseforge.com/#tocS_Mod"""

    id: int = Field(alias="id", description="The mod id")
    game_id: int = Field(alias="gameId", description="The game id this mod is for")
    name: str = Field(alias="name", description="The name of the mod")
    slug: str = Field(
        alias="slug", description="The mod slug that would appear in the URL"
    )
    links: ModLinks = Field(
        alias="links",
        description="Relevant links for the mod such as Issue tracker and Wiki",
    )
    summary: str = Field(alias="summary", description="Mod summary")
    status: ModStatus = Field(alias="status", description="Current mod status")
    download_count: int = Field(
        alias="downloadCount", description="Number of downloads for the mod"
    )
    is_featured: bool = Field(
        alias="isFeatured",
        description="Whether the mod is included in the featured mods list",
    )
    primary_category_id: int = Field(
        alias="primaryCategoryId",
        description="The main category of the mod as it was chosen by the mod author",
    )
    categories: list[Category] = Field(
        alias="categories", description="List of categories that this mod is related to"
    )
    class_id: int = Field(
        alias="classId", description="The class id this mod belongs to"
    )
    authors: list[ModAuthor] = Field(
        alias="authors", description="List of the mod's authors"
    )
    logo: ModAsset = Field(alias="logo", description="The mod's logo asset")
    screenshots: list[ModAsset] = Field(
        alias="screenshots", description="List of screenshots assets"
    )
    main_file_id: int = Field(
        alias="mainFileId", description="The id of the main file of the mod"
    )
    latest_files: list[File] = Field(
        alias="latestFiles", description="List of latest files of the mod"
    )
    latest_files_indexes: list[FileIndex] = Field(
        alias="latestFilesIndexes",
        description="List of file related details for the latest files of the mod",
    )
    latest_early_access_files_indexes: list[FileIndex] = Field(
        alias="latestEarlyAccessFilesIndexes",
        description="List of file related details for the latest early access files of the mod",
    )
    date_created: datetime = Field(
        alias="dateCreated", description="The creation date of the mod"
    )
    date_modified: datetime = Field(
        alias="dateModified", description="The last time the mod was modified"
    )
    date_released: datetime = Field(
        alias="dateReleased", description="The release date of the mod"
    )
    allow_mod_distribution: bool | None = Field(
        alias="allowModDistribution",
        description="Is mod allowed to be distributed",
        default=None,
    )
    game_popularity_rank: int = Field(
        alias="gamePopularityRank", description="The mod popularity rank for the game"
    )
    is_available: bool = Field(
        alias="isAvailable",
        description="Is the mod available for search. This can be false when a mod is experimental, in a deleted state or has only alpha files",
    )
    thumbs_up_count: int = Field(
        alias="thumbsUpCount", description="The mod's thumbs up count"
    )
    rating: float | None = Field(
        alias="rating", description="The mod's Rating", default=None
    )
