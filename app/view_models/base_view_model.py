'''
Base view model for compiling data model info to pass to view.
It may be easier to just explicitly define all the attributes,
but this base class can provide a lot of convenience.
Especially when interfacing with table view models.
'''
from models.base_model import Base

class BaseViewModel():
    def __init__(self, model: Base = None, **kwargs) -> 'BaseViewModel':

        # If a sub class of declarative base is passed,
        # pull attributes of data model class into view model class.
        # This may be redundant if you can just call model.clone(),
        # but combining this with the kwargs allows for a more customized view model.
        if model is not None:
            for key, value in model.as_dict().items():
                setattr(self, key, value)

        # By calling this aftwer copying attributes from the data model,
        # we have the opportunity to overwrite some attributes if needed.
        # For example, we may need another model class instead of a relationship.
        for key, value in kwargs.items():
            setattr(self, key, value)

    @classmethod
    def get_fields(cls):
        return {
            name: name.title().replace('_',' ')
            for name in cls.__dict__.keys()
            if not name.startswith('__')
        }
