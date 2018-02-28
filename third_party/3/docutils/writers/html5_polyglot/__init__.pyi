# Stubs for docutils.writers.html5_polyglot (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from docutils import writers
from typing import Any

__docformat__: str

class Writer(writers._html_base.Writer):
    supported: Any = ...
    default_stylesheets: Any = ...
    default_stylesheet_dirs: Any = ...
    default_template: str = ...
    default_template_path: Any = ...
    settings_spec: Any = ...
    config_section: str = ...
    parts: Any = ...
    translator_class: Any = ...
    def __init__(self) -> None: ...

class HTMLTranslator(writers._html_base.HTMLTranslator):
    def visit_acronym(self, node): ...
    def depart_acronym(self, node): ...
    def visit_authors(self, node): ...
    def depart_authors(self, node): ...
    def visit_copyright(self, node): ...
    def depart_copyright(self, node): ...
    def visit_date(self, node): ...
    def depart_date(self, node): ...
    def visit_meta(self, node): ...
    def depart_meta(self, node): ...
    def visit_organization(self, node): ...
    def depart_organization(self, node): ...
