# Stubs for docutils.writers.null (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from docutils import writers
from typing import Any

class Writer(writers.UnfilteredWriter):
    supported: Any = ...
    config_section: str = ...
    config_section_dependencies: Any = ...
    def translate(self): ...