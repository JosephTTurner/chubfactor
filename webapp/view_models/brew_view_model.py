"""
A model that builds the values to display for a brew.
"""
from core.view_models.base_view_model import BaseViewModel
from webapp.models.brew_model import Brew


class BrewViewModel(BaseViewModel):
    brewer = ""
    style = ""
    shade = ""
    color = ""

    def __init__(self, brew: Brew):
        self.brewer = brew.brewer.nick_name if brew.brewer is not None else ""
        self.style = brew.style.name if brew.style is not None else ""
        self.shade = brew.style.shade.name if brew.style is not None else ""
        self.color = brew.style.color.name if brew.style is not None else ""
