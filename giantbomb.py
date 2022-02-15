from dataclasses import dataclass
from typing import Optional


@dataclass
class NestedImage:
    """
    Class to map fields from GiantBomb API Image list
    """
    icon_url: str
    medium_url: str
    screen_url: str
    screen_large_url: str
    small_url: str
    super_url: str
    thumb_url: str
    tiny_url: str
    original_url: str
    image_tags: str


@dataclass
class GiantBomb:
    """
    Class to map fields from GiantBomb API game data list
    """
    aliases: str
    name: str
    id: int
    description: str
    image: NestedImage
    site_detail_url: str
    api_detail_url: Optional[str]
    date_added: Optional[str]
    date_last_updated: Optional[str]
    deck: Optional[str]
    expected_release_day: Optional[str]
    expected_release_month: Optional[int]
    expected_release_quarter: Optional[int]
    expected_release_year: Optional[int]
    guid: Optional[str]
    image_tags: list
    number_of_user_reviews: int
    original_game_rating: Optional[list]
    original_release_date: Optional[str]
    platforms: Optional[list]
    term_frequencies: Optional[str]

    def __init__(self, id, aliases='', name='', description='', image=None, site_detail_url='', **kwargs):
        self.aliases = aliases
        self. id = id
        self.name = name
        self.description = description
        self.image = image
        self.site_detail_url = site_detail_url

    @property
    def fulltext(self) -> str:
        if self.name and self.aliases:
            return ' '.join([self.name, self.aliases])
        else:
            if self.name:
                return ' '.join([self.name])
