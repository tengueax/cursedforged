from pydantic import BaseModel, Field

from .files import File


class FingerprintMatch(BaseModel):
    """https://docs.curseforge.com/#tocS_FingerprintMatch"""

    id: int = Field(alias="id")
    file: File = Field(alias="file")
    latest_files: list[File] = Field(alias="latestFiles")


class FingerprintMatchesResult(BaseModel):
    """https://docs.curseforge.com/#tocS_FingerprintsMatchesResult"""

    is_cache_built: bool = Field(alias="isCacheBuilt")
    exact_matches: list[FingerprintMatch] = Field(alias="exactMatches")
    exact_fingerprints: list[int] = Field(alias="exactFingerprints")
    partial_matches: list[FingerprintMatch] = Field(alias="partialMatches")
    partial_match_fingerprints: dict[str, list[int]] = Field(
        alias="partialMatchFingerprints"
    )
    additional_properties: list[int] = Field(alias="additionalProperties")
    installed_fingerprints: list[int] = Field(alias="installedFingerprints")
    unmatched_fingerprints: list[int] = Field(alias="unmatchedFingerprints")


class FolderFingerprint(BaseModel):
    """https://docs.curseforge.com/#tocS_FolderFingerprint"""

    foldername: str = Field(alias="foldername")
    fingerprints: list[int] = Field(alias="fingerprints")


class FingerprintFuzzyMatch(BaseModel):
    """https://docs.curseforge.com/#tocS_FingerprintFuzzyMatch"""

    id: int = Field(alias="id")
    file: File = Field(alias="file")
    latest_files: list[File] = Field(alias="latestFiles")
    fingerprints: list[int] = Field(alias="fingerprints")


class FingerprintFuzzyMatchResult(BaseModel):
    """https://docs.curseforge.com/#tocS_FingerprintFuzzyMatchResult"""

    fuzzyMatches: list[FingerprintMatch] = Field(alias="fuzzyMatches")
