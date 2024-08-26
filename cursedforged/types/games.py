from datetime import datetime

from pydantic import BaseModel, Field

from .enums import CoreApiStatus, CoreStatus, GameVersionTypeStatus


class GameAssets(BaseModel):
    """https://docs.curseforge.com/#tocS_GameAssets"""

    icon_url: str | None = Field(alias="iconUrl")
    tile_url: str | None = Field(alias="tileUrl")
    cover_url: str | None = Field(alias="coverUrl")


class GameVersion(BaseModel):
    """https://docs.curseforge.com/#tocS_GameVersion"""

    id: int = Field(alias="id")
    slug: str = Field(alias="slug")
    name: str = Field(alias="name")


class GameVersionsByType(BaseModel):
    """https://docs.curseforge.com/#tocS_GameVersionsByType"""

    type: int = Field(alias="type")
    versions: list[str] = Field(alias="versions")


class GameVersionsByType2(BaseModel):
    """https://docs.curseforge.com/#tocS_GameVersionsByType2"""

    type: int = Field(alias="type")
    versions: list[str] = Field(alias="versions")


class GameVersionType(BaseModel):
    """https://docs.curseforge.com/#tocS_GameVersionType"""

    id: int = Field(alias="id")
    game_id: int = Field(alias="gameId")
    name: str = Field(alias="name")
    slug: str = Field(alias="slug")
    is_syncable: bool = Field(alias="isSyncable")
    status: GameVersionTypeStatus = Field(alias="status")


class Game(BaseModel):
    """https://docs.curseforge.com/#tocS_Game"""

    id: int = Field(alias="id")
    name: str = Field(alias="name")
    slug: str = Field(alias="slug")
    date_modified: datetime = Field(alias="dateModified")
    assets: GameAssets = Field(alias="assets")
    status: CoreStatus = Field(alias="status")
    api_status: CoreApiStatus = Field(alias="apiStatus")
