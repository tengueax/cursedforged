from datetime import datetime

from pydantic import BaseModel, Field


class Category(BaseModel):
    """https://docs.curseforge.com/#tocS_Category"""

    id: int = Field(alias="id", description="The category id")
    game_id: int = Field(
        alias="gameId", description="The game id related to the category"
    )
    name: str = Field(alias="name", description="Category name")
    slug: str = Field(
        alias="slug", description="The category slug as it appears in the URL"
    )
    url: str = Field(alias="url", description="The category URL")
    icon_url: str = Field(alias="iconUrl", description="URL for the category icon")
    date_modified: datetime = Field(
        alias="dateModified", description="Last modified date of the category"
    )
    is_class: bool | None = Field(
        alias="isClass",
        description="A top level category for other categories",
        default=None,
    )
    class_id: int | None = Field(
        alias="classId",
        description="The class id of the category, meaning - the class of which this category is under",
        default=None,
    )
    parent_category_id: int | None = Field(
        alias="parentCategoryId",
        description="The parent category for this category",
        default=None,
    )
    display_index: int | None = Field(
        alias="displayIndex",
        description="The display index for this category",
        default=None,
    )
