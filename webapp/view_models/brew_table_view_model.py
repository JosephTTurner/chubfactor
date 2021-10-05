from typing import List
from core.view_models.base_table_view_model import BaseTableViewModel
from webapp.view_models.brew_view_model import BrewViewModel


class BrewTableViewModel(BaseTableViewModel):
    def __init__(self, brew_view_models: List[BrewViewModel] = None, **kwargs):
        super(BrewTableViewModel, self).__init__(
            brew_view_models,
            view_model_class=BrewViewModel,
            table_id="brewTable",
            ajax_endpoint="/brew_table_data",
            **kwargs
        )
