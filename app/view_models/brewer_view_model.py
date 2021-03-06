"""
A model that builds the values to display for a brewer.
"""
from core.view_models.base_view_model import BaseViewModel
from data.models.brewer_model import Brewer


class BrewerViewModel(BaseViewModel):
    def __init__(self, brewer: Brewer, **kwargs):
        super.__init__(brewer)
