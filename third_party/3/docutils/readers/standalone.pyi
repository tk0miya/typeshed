# Stubs for docutils.readers.standalone (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from docutils import readers
from docutils.nodes import document
from docutils.transforms import Transform
from typing import Any, Dict, List, Tuple, Type

__docformat__: str

class Reader(readers.Reader):
    supported: Tuple[str, ...] = ...
    document: document = ...
    settings_spec: Tuple[str, str, Tuple[str, List[str], Dict[str, Any]]] = ...
    config_section: str = ...
    config_section_dependencies: Tuple[str, ...] = ...
    def get_transforms(self) -> List[Type[Transform]]: ...