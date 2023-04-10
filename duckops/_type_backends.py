"""
This module allows you to check types (e.g. using isinstance) without importing them.
Note that this is copied from https://github.com/machow/databackend
"""

import sys
import importlib

from abc import ABCMeta


def _load_class(mod_name: str, cls_name: str):
    mod = importlib.import_module(mod_name)
    return getattr(mod, cls_name)


class _AbstractBackendMeta(ABCMeta):
    def register_backend(cls, mod_name: str, cls_name: str):
        cls._backends.append((mod_name, cls_name))
        cls._abc_caches_clear()


class AbstractBackend(metaclass=_AbstractBackendMeta):
    @classmethod
    def __init_subclass__(cls):
        if not hasattr(cls, "_backends"):
            cls._backends = []

    @classmethod
    def __subclasshook__(cls, subclass):
        for mod_name, cls_name in cls._backends:
            if mod_name not in sys.modules:
                # module isn't loaded, so it can't be the subclass
                # we don't want to import the module to explicitly run the check
                # so skip here.
                continue
            else:
                target_cls = _load_class(mod_name, cls_name)
                if issubclass(subclass, target_cls):
                    return True

        return NotImplemented


# Implementations -------

from typing import TYPE_CHECKING

#if TYPE_CHECKING:
import pandas as pd

class PlObject(AbstractBackend): pass
class PdArray(AbstractBackend): pass
class PdFrame(AbstractBackend): pass
class PdSeries(AbstractBackend): pass

PlObject.register_backend("polars", "DataFrame")
PlObject.register_backend("polars", "Series")
PdArray.register_backend("pandas.api.extensions", "ExtensionArray")
PdSeries.register_backend("pandas", "Series")
PdFrame.register_backend("pandas", "DataFrame")