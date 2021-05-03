'''
A generic model for generating datatables on html pages.
Intended to build off of view models that are generated from SQLAlchemy classes.
Either a view model class, a list of view models, or both can be past to __init__().

'''

from typing import List
from flask.templating import render_template
from view_models.base_view_model import BaseViewModel

class BaseTableViewModel:
    model_list = None
    view_model_class = None
    display_names = None
    table_id = None
    ajax_endpoint = None

    def __init__(
        self,
        model_list:List[BaseViewModel]=None,
        view_model_class:BaseViewModel=None,
        display_names:dict=None,
        **kwargs
        ):

        self.data = model_list

        table_id = kwargs.get('table_id')
        if table_id is not None:
            self.table_id = table_id
        elif model_list is not None:
            self.table_id = f'{model_list[0].__class__.__name__.lower()}Table'

        if display_names is None and model_list is not None:
            # if there is no display names dictionary is based,
            # build one from the attributes of the first object in the list
            self.display_names = model_list[0].get_fields()
        elif display_names is None and view_model_class is not None:
            self.display_names = view_model_class.get_fields()
        else:
            self.display_names = display_names

        for key, value in kwargs.items():
            setattr(self, key, value)

    def render(self):
        '''
        Returns html of rendered datatable with necessary js.
        Doesn't necessarily put the datatables CDN's or javascript in a desirable place.
        Requires call to safe in jinja template:
            `{{ table_view.render()|safe }}`
        '''
        return render_template('partials/base_table_view.html', table_model=self)
