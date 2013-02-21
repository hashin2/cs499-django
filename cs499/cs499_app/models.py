from django.db import models
from collections import OrderedDict
import json

from cs499.cs499_app.views.api.helpers import dejsonify


# Abstract Models #############################################################

class AbstractBaseModel(models.Model):
    class Meta:
        abstract = True

    # Returns the object represented as a dict.
    def to_dict(self, short=False, deep=False):
        """
        Returns the object represented as a dict. If short is set to true, an
        abbreviated version of the object will be returned (usually just id and
        a any other essential fields, the rest should be omitted).  If deep is
        set to true, the dict will contain child objects, and will assume this
        instance has been annotate with the children objects in a predefined
        attribute.  See the documentation for each model's to_dict() for what
        those attributes should be. Note that sometimes setting short to true
        will cause the attribute that deep enables to be skipped.
        """
        raise NotImplementedError("This model hasn't implemented to_dict().")

    # Returns the object represended as json (based on the value of to_dict())
    def to_json(self):
        return json.dumps(self.to_dict(), sort_keys=False, indent=4)

    # Returns an instance of this model populated with data from the json 
    # string passed in.
    @classmethod
    def create_from_json(cls, json_string, **kwargs):
        instance = cls()
        instance.update_from_json(json_string, **kwargs)
        return instance

    # Returns an instance of this model populated with data from the dict
    # passed in.
    @classmethod
    def create_from_dict(cls, d, **kwargs):
        instance = cls()
        instance.update_from_dict(d, **kwargs)
        return instance

    # Updates this object to match the data in the json passed in.
    def update_from_json(self, json_string, **kwargs):
        d = dejsonify(json_string)
        self.update_from_dict(d, **kwargs)

    # Updates this object to match the data in the dict passed in.
    # If full_clean is true, it'll automatically call self.full_clean() before
    # returning.  If false, validating the model before saving is up to the 
    # caller.
    def update_from_dict(self, d, **kwargs):
        raise NotImplementedError(
            "Ths model hasn't implemented update_from_dict()")