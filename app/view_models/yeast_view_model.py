from core.view_models.base_view_model import BaseViewModel
from data.models.yeast_model import TempMatchEnum


class YeastMatchResultsViewModel(BaseViewModel):
    match_enum = None
    match_description = None
    min_temp = None
    max_temp = None

    def __init__(
        self,
        match_enum: TempMatchEnum,
        match_description: str,
        min_temp: int,
        max_temp: int,
    ):

        self.match_enum = match_enum
        self.match_description = match_description
        self.min_temp = min_temp
        self.max_temp = max_temp
