from enum import IntEnum, StrEnum


class CoreApiStatus(IntEnum):
    """https://docs.curseforge.com/#tocS_CoreApiStatus"""

    PRIVATE = 1
    PUBLIC = 2


class CoreStatus(IntEnum):
    """https://docs.curseforge.com/#tocS_CoreStatus"""

    DRAFT = 1
    TEST = 2
    PENDING_REVIEW = 3
    REJECTED = 4
    APPROVED = 5
    LIVE = 6


class GameVersionStatus(IntEnum):
    """https://docs.curseforge.com/#tocS_GameVersionStatus"""

    APPROVED = 1
    DELETED = 2
    NEW = 3


class GameVersionTypeStatus(IntEnum):
    """https://docs.curseforge.com/#tocS_GameVersionTypeStatus"""

    NORMAL = 1
    DELETED = 2


class ModStatus(IntEnum):
    """https://docs.curseforge.com/#tocS_ModStatus"""

    NEW = 1
    CHANGES_REQUIRED = 2
    UNDER_SOFT_REVIEW = 3
    APPROVED = 4
    REJECTED = 5
    CHANGES_MADE = 6
    INACTIVE = 7
    ABANDONED = 8
    DELETED = 9
    UNDER_REVIEW = 10


class ModsSearchSortField(IntEnum):
    """https://docs.curseforge.com/#tocS_ModsSearchSortField"""

    FEATURED = 1
    POPULARITY = 2
    LAST_UPDATED = 3
    NAME = 4
    AUTHOR = 5
    TOTAL_DOWNLOADS = 6
    CATEGORY = 7
    GAME_VERSION = 8
    EARLY_ACCESS = 9
    FEATURED_RELEASED = 10
    RELEASED_DATE = 11
    RATING = 12


class ModLoaderInstallMethod(IntEnum):
    """https://docs.curseforge.com/#tocS_ModLoaderInstallMethod"""

    FORGE_INSTALLER = 1
    FORGE_JAR_INSTALL = 2
    FORGE_INSTALLER_V2 = 3


class ModLoaderType(IntEnum):
    """https://docs.curseforge.com/#tocS_ModLoaderType"""

    ANY = 0
    FORGE = 1
    CAULDRON = 2
    LITELOADER = 3
    FABRIC = 4
    QUILT = 5
    NEOFORGE = 6


class FileRelationType(IntEnum):
    """https://docs.curseforge.com/#tocS_FileRelationType"""

    EMBEDDED_LIBRARY = 1
    OPTIONAL_DEPENDENCY = 2
    REQUIRED_DEPENDENCY = 3
    TOOL = 4
    INCOMPATIBLE = 5
    INCLUDE = 6


class FileReleaseType(IntEnum):
    """https://docs.curseforge.com/#tocS_FileReleaseType"""

    RELEASE = 1
    BETA = 2
    ALPHA = 3


class FileStatus(IntEnum):
    """https://docs.curseforge.com/#tocS_FileStatus"""

    PROCESSING = 1
    CHANGES_REQUIRED = 2
    UNDER_REVIEW = 3
    APPROVED = 4
    REJECTED = 5
    MALWARE_DETECTED = 6
    DELETED = 7
    ARCHIVED = 8
    TESTING = 9
    RELEASED = 10
    READY_FOR_REVIEW = 11
    DEPRECATED = 12
    BAKING = 13
    AWAITING_PUBLISHING = 14
    FAILED_PUBLISHING = 15


class HashAlgo(IntEnum):
    """https://docs.curseforge.com/#tocS_HashAlgo"""

    SHA1 = 1
    MD5 = 2


class SortOrder(StrEnum):
    """https://docs.curseforge.com/#tocS_SortOrder"""

    ASC = "asc"
    DESC = "desc"
