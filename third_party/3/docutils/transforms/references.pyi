# Stubs for docutils.transforms.references (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from docutils import nodes
from docutils.transforms import Transform
from typing import Callable, Dict, List, Text, Type, Union

__docformat__: str

class PropagateTargets(Transform):
    default_priority: int = ...
    def apply(self) -> None: ...  # type: ignore

class AnonymousHyperlinks(Transform):
    default_priority: int = ...
    def apply(self) -> None: ...  # type: ignore

class IndirectHyperlinks(Transform):
    default_priority: int = ...
    def apply(self) -> None: ...  # type: ignore
    def resolve_indirect_target(self, target: nodes.target) -> None: ...
    def nonexistent_indirect_target(self, target: nodes.target) -> None: ...
    def circular_indirect_reference(self, target: nodes.target) -> None: ...
    def indirect_target_error(self, target: nodes.target, explanation: str) -> None: ...
    def resolve_indirect_references(self, target: nodes.target) -> None: ...

class ExternalTargets(Transform):
    default_priority: int = ...
    def apply(self) -> None: ...  # type: ignore

class InternalTargets(Transform):
    default_priority: int = ...
    def apply(self) -> None: ...  # type: ignore
    def resolve_reference_ids(self, target: nodes.target): ...

class Footnotes(Transform):
    default_priority: int = ...
    autofootnote_labels: List[str] = ...
    symbols: List[Text] = ...
    def apply(self) -> None: ...  # type: ignore
    def number_footnotes(self, startnum: int) -> int: ...
    def number_footnote_references(self, startnum: int) -> None: ...
    def symbolize_footnotes(self) -> None: ...
    def resolve_footnotes_and_citations(self) -> None: ...
    def resolve_references(self, note: Union[nodes.footnote, nodes.citation], reflist: Union[nodes.footnote_reference, nodes.citation_reference]) -> None: ...

class CircularSubstitutionDefinitionError(Exception): ...

class Substitutions(Transform):
    default_priority: int = ...
    def apply(self) -> None: ...  # type: ignore

class TargetNotes(Transform):
    default_priority: int = ...
    classes: List[Type] = ...
    def __init__(self, document: nodes.document, startnode: nodes.Node) -> None: ...
    def apply(self) -> None: ...  # type: ignore
    def make_target_footnote(self, refuri, refs: List[str], notes: Dict[str, nodes.footnote]) -> nodes.footnote: ...

class DanglingReferences(Transform):
    default_priority: int = ...
    def apply(self) -> None: ...  # type: ignore

class DanglingReferencesVisitor(nodes.SparseNodeVisitor):
    document: nodes.document = ...
    unknown_reference_resolvers: List[Callable[[nodes.Node], bool]] = ...
    def __init__(self, document: nodes.document, unknown_reference_resolvers: List[Callable[[nodes.Node], bool]]) -> None: ...
    def unknown_visit(self, node: nodes.Node) -> None: ...
    def visit_reference(self, node: nodes.Node) -> None: ...
    visit_footnote_reference: Callable[[DanglingReferencesVisitor, nodes.Node], None] = ...
    visit_citation_reference: Callable[[DanglingReferencesVisitor, nodes.Node], None] = ...
