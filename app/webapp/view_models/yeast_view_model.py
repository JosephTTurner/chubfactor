from view_models.base_view_model import BaseViewModel
from webapp.models.yeast_model import TempMatchEnum

class YeastMatchResultsViewModel(BaseViewModel):
    match_enum = None
    min_temp = None
    max_temp = None

    def __init__(
        self,
        match_enum: TempMatchEnum,
        min_temp: int,
        max_temp: int):

        self.match_enum=match_enum
        self.min_temp=min_temp
        self.max_temp=max_temp

