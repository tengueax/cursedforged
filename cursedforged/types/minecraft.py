from datetime import datetime

from pydantic import BaseModel, Field

from .enums import (
    GameVersionStatus,
    GameVersionTypeStatus,
    ModLoaderInstallMethod,
    ModLoaderType,
)


class MinecraftGameVersion(BaseModel):
    """https://docs.curseforge.com/#tocS_MinecraftGameVersion"""

    id: int = Field(alias="id")
    game_version_id: int = Field(alias="gameVersionId")
    version_string: str = Field(alias="versionString")
    jar_download_url: str = Field(alias="jarDownloadUrl")
    json_download_url: str = Field(alias="jsonDownloadUrl")
    approved: bool = Field(alias="approved")
    date_modified: datetime = Field(alias="dateModified")
    game_version_type_id: int = Field(alias="gameVersionTypeId")
    game_version_status: GameVersionStatus = Field(alias="gameVersionStatus")
    game_version_type_status: GameVersionTypeStatus = Field(
        alias="gameVersionTypeStatus"
    )


class MinecraftModLoaderIndex(BaseModel):
    """https://docs.curseforge.com/#tocS_MinecraftModLoaderIndex"""

    name: str = Field(alias="name")
    game_version: str = Field(alias="gameVersion")
    latest: bool = Field(alias="latest")
    recommended: bool = Field(alias="recommended")
    date_modified: datetime = Field(alias="dateModified")
    type: ModLoaderType = Field(alias="type")


class MinecraftModLoaderVersion(BaseModel):
    """https://docs.curseforge.com/#tocS_MinecraftModLoaderVersion"""

    id: int = Field(alias="id")
    game_version_id: int = Field(alias="gameVersionId")
    minecraft_game_version_id: int = Field(alias="minecraftGameVersionId")
    forge_version: str = Field(alias="forgeVersion")
    name: str = Field(alias="name")
    type: ModLoaderType = Field(alias="type")
    download_url: str = Field(alias="downloadUrl")
    filename: str = Field(alias="filename")
    install_method: ModLoaderInstallMethod = Field(alias="installMethod")
    latest: bool = Field(alias="latest")
    recommended: bool = Field(alias="recommended")
    approved: bool = Field(alias="approved")
    date_modified: datetime = Field(alias="dateModified")
    maven_version_string: str = Field(alias="mavenVersionString")
    version_json: str = Field(alias="versionJson")
    libraries_install_location: str = Field(alias="librariesInstallLocation")
    minecraft_version: str = Field(alias="minecraftVersion")
    additional_files_json: str = Field(alias="additionalFilesJson")
    mod_loader_game_version_id: int = Field(alias="modLoaderGameVersionId")
    mod_loader_game_version_type_id: int = Field(alias="modLoaderGameVersionTypeId")
    mod_loader_game_version_status: GameVersionStatus = Field(
        alias="modLoaderGameVersionStatus"
    )
    mod_loader_game_version_type_status: GameVersionTypeStatus = Field(
        alias="modLoaderGameVersionTypeStatus"
    )
    mc_game_version_id: int = Field(alias="mcGameVersionId")
    mc_game_version_type_id: int = Field(alias="mcGameVersionTypeId")
    mc_game_version_status: GameVersionStatus = Field(alias="mcGameVersionStatus")
    mc_game_version_type_status: GameVersionTypeStatus = Field(
        alias="mcGameVersionTypeStatus"
    )
