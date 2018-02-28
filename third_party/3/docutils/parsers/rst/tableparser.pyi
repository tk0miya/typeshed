# Stubs for docutils.parsers.rst.tableparser (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from docutils import DataError
from docutils.statemachine import StringList
from typing import Any, Dict, List, Optional, Pattern, Tuple

Cell = Tuple[int, int, int, List[str]]
Row = List[Optional[Cell]]
Colspecs = List[int]

__docformat__: str

class TableMarkupError(DataError):
    offset: Any = ...
    def __init__(self, *args, **kwargs) -> None: ...

class TableParser:
    head_body_separator_pat: Pattern = ...
    double_width_pad_char: str = ...
    def parse(self, block: StringList) -> Tuple[Colspecs, List[Row], List[Row]]: ...
    head_body_sep: int = ...
    def find_head_body_sep(self) -> None: ...

class GridTableParser(TableParser):
    head_body_separator_pat: Pattern = ...
    block: StringList = ...
    bottom: int = ...
    right: int = ...
    head_body_sep: int = ...
    done: List[int] = ...
    cells: List[Cell] = ...
    rowseps: Dict[int, List[int]] = ...
    colseps: Dict[int, List[int]] = ...
    def setup(self, block: StringList) -> None: ...
    def parse_table(self) -> None: ...
    def mark_done(self, top: int, left: int, bottom: int, right: int) -> None: ...
    def check_parse_complete(self) -> bool: ...
    def scan_cell(self, top: int, left: int) -> Tuple[int, int, Dict[int, List[int]], Dict[int, List[int]]]: ...
    def scan_right(self, top: int, left: int) -> Tuple[int, int, Dict[int, List[int]], Dict[int, List[int]]]: ...
    def scan_down(self, top: int, left: int, right: int) -> Tuple[int, Dict[int, List[int]], Dict[int, List[int]]]: ...
    def scan_left(self, top: int, left: int, bottom: int, right: int) -> Tuple[Dict[int, List[int]], Dict[int, List[int]]]: ...
    def scan_up(self, top: int, left: int, bottom: int, right: int) -> Dict[int, List[int]]: ...
    def structure_from_cells(self) -> Tuple[Colspecs, List[Row], List[Row]]: ...

class SimpleTableParser(TableParser):
    head_body_separator_pat: Pattern = ...
    span_pat: Pattern = ...
    block: StringList = ...
    head_body_sep: int = ...
    columns: List[Tuple[int, int]] = ...
    border_end: int = ...
    table: Tuple[List[int], List[Row], List[Row]] = ...
    done: List[int] = ...
    rowseps: Dict[int, Tuple[int]] = ...
    colseps: Dict[int, Tuple[int]] = ...
    def setup(self, block: StringList) -> None: ...
    def parse_table(self) -> None: ...
    def parse_columns(self, line: str, offset: int) -> List[Tuple[int, int]]: ...
    def init_row(self, colspec: List[Tuple[int, int]], offset: int) -> List[Cell]: ...
    def parse_row(self, lines: List[str], start: int, spanline: Optional[Tuple[str, int]] = ...) -> None: ...
    def check_columns(self, lines: List[str], first_line: int, columns: List[Tuple[int, int]]): ...
    def structure_from_cells(self) -> Tuple[Colspecs, List[Row], List[Row]]: ...

def update_dict_of_lists(master: Dict[int, List[int]], newdata: Dict[int, List[int]]) -> None: ...
