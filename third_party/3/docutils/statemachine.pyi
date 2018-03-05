# Stubs for docutils.statemachine (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Callable, Dict, Generator, List, Match, Optional, Pattern, Tuple, Type, Union
from docutils import statemachine

__docformat__: str

class StateMachine:
    input_lines: statemachine.StringList = ...
    input_offset: int = ...
    line: str = ...
    line_offset: int = ...
    debug: bool = ...
    initial_state: str = ...
    current_state: List[statemachine.State] = ...
    states: Any = ...
    observers: Any = ...
    def __init__(self, state_classes: List[Type[statemachine.State]], initial_state: str, debug: bool = ...) -> None: ...
    def unlink(self) -> None: ...
    def run(self, input_lines: Union[List[str], statemachine.StringList], input_offset: int = ..., context: Optional[Any] = ..., input_source: Optional[str] = ..., initial_state: Optional[str] = ...): ...
    def get_state(self, next_state: Optional[str] = ...) -> statemachine.State: ...
    def next_line(self, n: int = ...) -> str: ...
    def is_next_line_blank(self) -> bool: ...
    def at_eof(self) -> bool: ...
    def at_bof(self) -> bool: ...
    def previous_line(self, n: int = ...) -> str: ...
    def goto_line(self, line_offset) -> None: ...
    def get_source(self, line_offset) -> str: ...
    def abs_line_offset(self) -> int: ...
    def abs_line_number(self) -> int: ...
    def get_source_and_line(self, lineno: Optional[int] = ...) -> Tuple[str, int]: ...
    def insert_input(self, input_lines: Union[List[str], statemachine.StringList], source: str) -> None: ...
    def get_text_block(self, flush_left: bool = ...) -> statemachine.StringList: ...
    def check_line(self, context: Any, state: statemachine.State, transitions: Optional[List[str]] = ...) -> Any: ...
    def add_state(self, state_class: Type[statemachine.State]) -> None: ...
    def add_states(self, state_classes: List[Type[statemachine.State]]) -> None: ...
    def runtime_init(self) -> None: ...
    def error(self) -> None: ...
    def attach_observer(self, observer) -> None: ...
    def detach_observer(self, observer) -> None: ...
    def notify_observers(self) -> None: ...

class State:
    patterns: Dict[str, str] = ...
    initial_transitions: List[Union[str, Tuple[str, str]]] = ...
    nested_sm: Type[StateMachine] = ...
    nested_sm_kwargs: Dict[str, Any] = ...
    transition_order: List[str] = ...
    transitions: Dict[str, Tuple[Pattern, Callable, str]] = ...
    state_machine: StateMachine = ...
    debug: bool = ...
    def __init__(self, state_machine: StateMachine, debug: bool = ...) -> None: ...
    def runtime_init(self) -> None: ...
    def unlink(self) -> None: ...
    def add_initial_transitions(self) -> None: ...
    def add_transitions(self, names: List[str], transitions) -> None: ...
    def add_transition(self, name: str, transition: Tuple[Pattern, str, str]) -> None: ...
    def remove_transition(self, name: str) -> None: ...
    def make_transition(self, name: str, next_state: Optional[str] = ...) -> Tuple[Pattern, Callable, str]: ...
    def make_transitions(self, name_list: List[Union[str, Tuple[str], Tuple[str, str]]]) -> Tuple[List[str], Dict[str, Tuple[Pattern, Callable, str]]]: ...
    def no_match(self, context, transitions: Tuple[List[str], Dict[str, Tuple[Pattern, Callable, str]]]) -> Tuple[Any, str, List]: ...
    def bof(self, context) -> Tuple[Any, List]: ...
    def eof(self, context) -> List: ...
    def nop(self, match, context, next_state: str) -> Tuple[Any, str, List]: ...

class StateMachineWS(StateMachine):
    def get_indented(self, until_blank: bool = ..., strip_indent: bool = ...) -> Tuple[List[str], int, int, bool]: ...
    def get_known_indented(self, indent: int, until_blank: bool = ..., strip_indent: bool = ...) -> Tuple[List[str], int, bool]: ...
    def get_first_known_indented(self, indent: int, until_blank: bool = ..., strip_indent: bool = ..., strip_top: bool = ...) -> Tuple[List[str], int, int, bool]: ...

class StateWS(State):
    indent_sm: Type[StateMachine] = ...
    indent_sm_kwargs: Dict[str, Any] = ...
    known_indent_sm: Type[StateMachine] = ...
    known_indent_sm_kwargs: Dict[str, Any] = ...
    ws_patterns: Dict[str, str] = ...
    ws_initial_transitions: Tuple[str, ...] = ...
    def __init__(self, state_machine: StateMachine, debug: bool = ...) -> None: ...
    patterns: Dict[str, str] = ...
    def add_initial_transitions(self) -> None: ...
    def blank(self, match: Match, context, next_state: str) -> Tuple[Any, str, Any]: ...
    def indent(self, match: Match, context, next_state: str) -> Tuple[Any, str, Any]: ...
    def known_indent(self, match: Match, context, next_state: str) -> Tuple[Any, str, Any]: ...
    def first_known_indent(self, match: Match, context, next_state: str) -> Tuple[Any, str, Any]: ...

class _SearchOverride:
    def match(self, pattern: Pattern) -> Match: ...

class SearchStateMachine(_SearchOverride, StateMachine): ...
class SearchStateMachineWS(_SearchOverride, StateMachineWS): ...

class ViewList:
    data: List = ...
    items: List[Tuple[str, int]] = ...
    parent: statemachine.ViewList = ...
    parent_offset: int = ...
    def __init__(self, initlist: Optional[Union[statemachine.ViewList, List]] = ..., source: Optional[str] = ..., items: Optional[List[Tuple[str, int]]] = ..., parent: Optional[statemachine.ViewList] = ..., parent_offset: Optional[int] = ...) -> None: ...
    def __lt__(self, other: Any) -> bool: ...
    def __le__(self, other: Any) -> bool: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def __gt__(self, other: Any) -> bool: ...
    def __ge__(self, other: Any) -> bool: ...
    def __cmp__(self, other: Any) -> int: ...
    def __contains__(self, item: statemachine.ViewList) -> bool: ...
    def __len__(self) -> int: ...
    def __getitem__(self, i: Union[int, slice]) -> Union[str, statemachine.ViewList]: ...
    def __setitem__(self, i: Union[str, slice], item: Union[str, statemachine.ViewList]) -> None: ...
    def __delitem__(self, i: int) -> None: ...
    def __add__(self, other: statemachine.ViewList) -> None: ...
    def __radd__(self, other: statemachine.ViewList) -> None: ...
    def __iadd__(self, other: statemachine.ViewList) -> statemachine.ViewList: ...
    def __mul__(self, n: int) -> statemachine.ViewList: ...
    __rmul__: Any = ...
    def __imul__(self, n: int) -> statemachine.ViewList: ...
    def extend(self, other: statemachine.ViewList) -> None: ...
    def append(self, item: Any, source: Optional[str] = ..., offset: int = ...) -> None: ...
    def insert(self, i: int, item: Any, source: Optional[str] = ..., offset: int = ...) -> None: ...
    def pop(self, i: int = ...) -> Any: ...
    def trim_start(self, n: int = ...) -> None: ...
    def trim_end(self, n: int = ...) -> None: ...
    def remove(self, item: Any) -> None: ...
    def count(self, item: Any) -> int: ...
    def index(self, item: Any) -> int: ...
    def reverse(self) -> None: ...
    def sort(self, *args: Any) -> None: ...
    def info(self, i: int) -> Tuple[str, int]: ...
    def source(self, i: int) -> str: ...
    def offset(self, i: int) -> int: ...
    def disconnect(self) -> None: ...
    def xitems(self) -> Generator[Tuple[str, int, str], None, None]: ...
    def pprint(self) -> None: ...

class StringList(ViewList):
    def trim_left(self, length: int, start: int = ..., end: int = ...) -> None: ...
    def get_text_block(self, start: int, flush_left: bool = ...) -> statemachine.StringList: ...
    def get_indented(self, start: int = ..., until_blank: bool = ..., strip_indent: bool = ..., block_indent: Optional[int] = ..., first_indent: Optional[int] = ...) -> Tuple[statemachine.StringList, int, bool]: ...
    def get_2D_block(self, top: int, left: int, bottom: int, right: int, strip_indent: bool = ...) -> statemachine.StringList: ...
    def pad_double_width(self, pad_char: str) -> None: ...
    def replace(self, old: str, new: str) -> None: ...

class StateMachineError(Exception): ...
class UnknownStateError(StateMachineError): ...
class DuplicateStateError(StateMachineError): ...
class UnknownTransitionError(StateMachineError): ...
class DuplicateTransitionError(StateMachineError): ...
class TransitionPatternNotFound(StateMachineError): ...
class TransitionMethodNotFound(StateMachineError): ...
class UnexpectedIndentationError(StateMachineError): ...
class TransitionCorrection(Exception): ...
class StateCorrection(Exception): ...

def string2lines(astring: str, tab_width: int = ..., convert_whitespace: bool = ..., whitespace: Pattern = ...) -> List[str]: ...
