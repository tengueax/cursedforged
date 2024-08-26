from datetime import datetime

from pydantic import BaseModel, Field

from .enums import (
    FileRelationType,
    FileReleaseType,
    FileStatus,
    HashAlgo,
    ModLoaderType,
)


class FileDependency(BaseModel):
    """https://docs.curseforge.com/#tocS_FileDependency"""

    mod_id: int = Field(alias="modId")
    relation_type: FileRelationType = Field(alias="relationType")


class FileHash(BaseModel):
    """https://docs.curseforge.com/#tocS_FileHash"""

    value: str = Field(alias="value")
    algo: HashAlgo = Field(alias="algo")


class FileIndex(BaseModel):
    """https://docs.curseforge.com/#tocS_FileIndex"""

    game_version: str = Field(alias="gameVersion")
    file_id: int = Field(alias="fileId")
    filename: str = Field(alias="filename")
    release_type: FileReleaseType = Field(alias="releaseType")
    game_version_type_id: int | None = Field(alias="gameVersionTypeId", default=None)
    mod_loader: ModLoaderType = Field(alias="modLoader")


class FileModule(BaseModel):
    """https://docs.curseforge.com/#tocS_FileModule"""

    name: str = Field(alias="name")
    fingerprint: int = Field(alias="fingerprint")


class SortableGameVersion(BaseModel):
    """https://docs.curseforge.com/#tocS_SortableGameVersion"""

    game_version_name: str = Field(
        alias="gameVersionName", description="Original version name (e.g. 1.5b)"
    )
    game_version_padded: str = Field(
        alias="gameVersionPadded",
        description="Used for sorting (e.g. 0000000001.0000000005)",
    )
    game_version: str = Field(
        alias="gameVersion", description="Game version clean name (e.g. 1.5)"
    )
    game_version_release_date: datetime = Field(
        alias="gameVersionReleaseDate", description="Game version release date"
    )
    game_version_type_id: int | None = Field(
        alias="gameVersionTypeId", description="Game version type id", default=None
    )


class File(BaseModel):
    """https://docs.curseforge.com/#tocS_File"""

    id: int = Field(alias="id", description="The file id")
    game_id: int = Field(
        alias="gameId",
        description="The game id related to the mod that this file belongs to",
    )
    mod_id: int = Field(alias="modId", description="The mod id")
    is_available: bool = Field(
        alias="isAvailable", description="Whether the file is available to download"
    )
    display_name: str = Field(
        alias="displayName", description="Display name of the file"
    )
    file_name: str = Field(alias="fileName", description="Exact file name")
    release_type: FileReleaseType = Field(
        alias="releaseType", description="The file release type"
    )
    file_status: FileStatus = Field(
        alias="fileStatus", description="Status of the file"
    )
    hashes: list[FileHash] = Field(
        alias="hashes", description="The file hash (i.e. md5 or sha1)"
    )
    file_date: datetime = Field(alias="fileDate", description="The file timestamp")
    file_length: int = Field(alias="fileLength", description="The file length in bytes")
    download_count: int = Field(
        alias="downloadCount", description="The number of downloads for the file"
    )
    file_size_on_disk: int | None = Field(
        alias="fileSizeOnDisk", description="The file's size on disk", default=None
    )
    download_url: str = Field(alias="downloadUrl", description="The file download URL")
    game_versions: list[str] = Field(
        alias="gameVersions",
        description="List of game versions this file is relevant for",
    )
    sortable_game_versions: list[SortableGameVersion] = Field(
        alias="sortableGameVersions",
        description="Metadata used for sorting by game versions",
    )
    dependencies: list[FileDependency] = Field(
        alias="dependencies", description="List of dependencies files"
    )
    expose_as_alternative: bool | None = Field(
        alias="exposeAsAlternative", default=None
    )
    parent_project_file_id: int | None = Field(
        alias="parentProjectFileId", default=None
    )
    alternate_file_id: int | None = Field(alias="alternateFileId", default=None)
    is_server_pack: bool | None = Field(alias="isServerPack", default=None)
    server_pack_file_id: int | None = Field(alias="serverPackFileId", default=None)
    is_early_access_content: bool | None = Field(
        alias="isEarlyAccessContent", default=None
    )
    early_access_end_date: datetime | None = Field(
        alias="earlyAccessEndDate", default=None
    )
    file_fingerprint: int = Field(alias="fileFingerprint")
    modules: list[FileModule] = Field(alias="modules")
