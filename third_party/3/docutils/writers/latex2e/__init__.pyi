# Stubs for docutils.writers.latex2e (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from docutils import nodes, writers
from typing import Any, Optional

__docformat__: str

class Writer(writers.Writer):
    supported: Any = ...
    default_template: str = ...
    default_template_path: Any = ...
    default_preamble: Any = ...
    table_style_values: Any = ...
    settings_spec: Any = ...
    settings_defaults: Any = ...
    config_section: str = ...
    config_section_dependencies: Any = ...
    head_parts: Any = ...
    visitor_attributes: Any = ...
    output: Any = ...
    translator_class: Any = ...
    def __init__(self) -> None: ...
    def get_transforms(self): ...
    def translate(self): ...
    def assemble_parts(self): ...

class Babel:
    language_codes: Any = ...
    warn_msg: str = ...
    active_chars: Any = ...
    reporter: Any = ...
    language: Any = ...
    otherlanguages: Any = ...
    def __init__(self, language_code, reporter: Optional[Any] = ...) -> None: ...
    setup: Any = ...
    def __call__(self): ...
    def language_name(self, language_code): ...
    def get_language(self): ...

class SortableDict(dict):
    def sortedkeys(self): ...
    def sortedvalues(self): ...

class PreambleCmds: ...

class CharMaps:
    alltt: Any = ...
    special: Any = ...
    unsupported_unicode: Any = ...
    utf8_supported_unicode: Any = ...
    textcomp: Any = ...
    pifont: Any = ...

class DocumentClass:
    document_class: Any = ...
    sections: Any = ...
    def __init__(self, document_class, with_part: bool = ...) -> None: ...
    def section(self, level): ...

class Table:
    stubs: Any = ...
    colwidths_auto: bool = ...
    def __init__(self, translator, latex_type) -> None: ...
    caption: Any = ...
    def open(self): ...
    def close(self): ...
    def is_open(self): ...
    borders: Any = ...
    def set_table_style(self, table_style, classes): ...
    def get_latex_type(self): ...
    def set(self, attr, value): ...
    def get(self, attr): ...
    def get_vertical_bar(self): ...
    def get_opening(self): ...
    def get_closing(self): ...
    def visit_colspec(self, node): ...
    def get_colspecs(self, node): ...
    def get_column_width(self): ...
    def get_multicolumn_width(self, start, len_): ...
    def get_caption(self): ...
    def need_recurse(self): ...
    def visit_thead(self): ...
    def depart_thead(self): ...
    def visit_row(self): ...
    def depart_row(self): ...
    def set_rowspan(self, cell, value): ...
    def get_rowspan(self, cell): ...
    def get_entry_number(self): ...
    def visit_entry(self): ...
    def is_stub_column(self): ...

class LaTeXTranslator(nodes.NodeVisitor):
    is_xetex: bool = ...
    compound_enumerators: bool = ...
    section_prefix_for_enumerators: bool = ...
    section_enumerator_separator: str = ...
    has_latex_toc: bool = ...
    is_toc_list: bool = ...
    section_level: int = ...
    inside_citation_reference_label: bool = ...
    verbatim: bool = ...
    insert_non_breaking_blanks: bool = ...
    insert_newline: bool = ...
    literal: bool = ...
    alltt: bool = ...
    warn: Any = ...
    error: Any = ...
    settings: Any = ...
    latex_encoding: Any = ...
    use_latex_toc: Any = ...
    use_latex_docinfo: Any = ...
    hyperlink_color: Any = ...
    font_encoding: Any = ...
    literal_block_env: str = ...
    literal_block_options: str = ...
    bibtex: Any = ...
    language_module: Any = ...
    babel: Any = ...
    author_separator: Any = ...
    documentoptions: Any = ...
    d_class: Any = ...
    graphicx_package: str = ...
    docutils_footnotes: Any = ...
    head_prefix: Any = ...
    requirements: Any = ...
    latex_preamble: Any = ...
    fallbacks: Any = ...
    pdfsetup: Any = ...
    title: Any = ...
    subtitle: Any = ...
    titledata: Any = ...
    body_pre_docinfo: Any = ...
    docinfo: Any = ...
    dedication: Any = ...
    abstract: Any = ...
    body: Any = ...
    context: Any = ...
    title_labels: Any = ...
    subtitle_labels: Any = ...
    author_stack: Any = ...
    date: Any = ...
    pdfinfo: Any = ...
    pdfauthor: Any = ...
    table_stack: Any = ...
    active_table: Any = ...
    out: Any = ...
    out_stack: Any = ...
    stylesheet: Any = ...
    hyperref_options: str = ...
    def __init__(self, document, babel_class: Any = ...) -> None: ...
    def stylesheet_call(self, path): ...
    def to_latex_encoding(self, docutils_encoding): ...
    def language_label(self, docutil_label): ...
    def encode(self, text): ...
    def attval(self, text, whitespace: Any = ...): ...
    def is_inline(self, node): ...
    def append_hypertargets(self, node): ...
    def ids_to_labels(self, node, set_anchor: bool = ...): ...
    def set_align_from_classes(self, node): ...
    def insert_align_declaration(self, node, default: Optional[Any] = ...): ...
    def duclass_open(self, node): ...
    def duclass_close(self, node): ...
    def push_output_collector(self, new_out): ...
    def pop_output_collector(self): ...
    def visit_Text(self, node): ...
    def depart_Text(self, node): ...
    def visit_abbreviation(self, node): ...
    def depart_abbreviation(self, node): ...
    def visit_acronym(self, node): ...
    def depart_acronym(self, node): ...
    def visit_address(self, node): ...
    def depart_address(self, node): ...
    def visit_admonition(self, node): ...
    def depart_admonition(self, node: Optional[Any] = ...): ...
    def visit_author(self, node): ...
    def depart_author(self, node): ...
    def visit_authors(self, node): ...
    def depart_authors(self, node): ...
    def visit_block_quote(self, node): ...
    def depart_block_quote(self, node): ...
    def visit_bullet_list(self, node): ...
    def depart_bullet_list(self, node): ...
    def visit_superscript(self, node): ...
    def depart_superscript(self, node): ...
    def visit_subscript(self, node): ...
    def depart_subscript(self, node): ...
    def visit_caption(self, node): ...
    def depart_caption(self, node): ...
    def visit_title_reference(self, node): ...
    def depart_title_reference(self, node): ...
    def visit_citation(self, node): ...
    def depart_citation(self, node): ...
    def visit_citation_reference(self, node): ...
    def depart_citation_reference(self, node): ...
    def visit_classifier(self, node): ...
    def depart_classifier(self, node): ...
    def visit_colspec(self, node): ...
    def depart_colspec(self, node): ...
    def visit_comment(self, node): ...
    def depart_comment(self, node): ...
    def visit_compound(self, node): ...
    def depart_compound(self, node): ...
    def visit_contact(self, node): ...
    def depart_contact(self, node): ...
    def visit_container(self, node): ...
    def depart_container(self, node): ...
    def visit_copyright(self, node): ...
    def depart_copyright(self, node): ...
    def visit_date(self, node): ...
    def depart_date(self, node): ...
    def visit_decoration(self, node): ...
    def depart_decoration(self, node): ...
    def visit_definition(self, node): ...
    def depart_definition(self, node): ...
    def visit_definition_list(self, node): ...
    def depart_definition_list(self, node): ...
    def visit_definition_list_item(self, node): ...
    def depart_definition_list_item(self, node): ...
    def visit_description(self, node): ...
    def depart_description(self, node): ...
    def visit_docinfo(self, node): ...
    def depart_docinfo(self, node): ...
    def visit_docinfo_item(self, node, name): ...
    def depart_docinfo_item(self, node): ...
    def visit_doctest_block(self, node): ...
    def depart_doctest_block(self, node): ...
    def visit_document(self, node): ...
    def depart_document(self, node): ...
    def visit_emphasis(self, node): ...
    def depart_emphasis(self, node): ...
    def insert_additional_table_colum_delimiters(self): ...
    def visit_entry(self, node): ...
    def depart_entry(self, node): ...
    def visit_row(self, node): ...
    def depart_row(self, node): ...
    def visit_enumerated_list(self, node): ...
    def depart_enumerated_list(self, node): ...
    def visit_field(self, node): ...
    def depart_field(self, node): ...
    def visit_field_argument(self, node): ...
    def depart_field_argument(self, node): ...
    def visit_field_body(self, node): ...
    def depart_field_body(self, node): ...
    def visit_field_list(self, node): ...
    def depart_field_list(self, node): ...
    def visit_field_name(self, node): ...
    def depart_field_name(self, node): ...
    def visit_figure(self, node): ...
    def depart_figure(self, node): ...
    def visit_footer(self, node): ...
    def depart_footer(self, node): ...
    def visit_footnote(self, node): ...
    def depart_footnote(self, node): ...
    def visit_footnote_reference(self, node): ...
    def depart_footnote_reference(self, node): ...
    def label_delim(self, node, bracket, superscript): ...
    def visit_label(self, node): ...
    def depart_label(self, node): ...
    def visit_generated(self, node): ...
    def depart_generated(self, node): ...
    def visit_header(self, node): ...
    def depart_header(self, node): ...
    def to_latex_length(self, length_str, pxunit: Optional[Any] = ...): ...
    def visit_image(self, node): ...
    def depart_image(self, node): ...
    def visit_inline(self, node): ...
    def depart_inline(self, node): ...
    def visit_interpreted(self, node): ...
    def depart_interpreted(self, node): ...
    def visit_legend(self, node): ...
    def depart_legend(self, node): ...
    def visit_line(self, node): ...
    def depart_line(self, node): ...
    def visit_line_block(self, node): ...
    def depart_line_block(self, node): ...
    def visit_list_item(self, node): ...
    def depart_list_item(self, node): ...
    def visit_literal(self, node): ...
    def depart_literal(self, node): ...
    def is_plaintext(self, node): ...
    def visit_literal_block(self, node): ...
    def depart_literal_block(self, node): ...
    def visit_math(self, node, math_env: str = ...): ...
    def depart_math(self, node): ...
    def visit_math_block(self, node): ...
    def depart_math_block(self, node): ...
    def visit_option(self, node): ...
    def depart_option(self, node): ...
    def visit_option_argument(self, node): ...
    def depart_option_argument(self, node): ...
    def visit_option_group(self, node): ...
    def depart_option_group(self, node): ...
    def visit_option_list(self, node): ...
    def depart_option_list(self, node): ...
    def visit_option_list_item(self, node): ...
    def depart_option_list_item(self, node): ...
    def visit_option_string(self, node): ...
    def depart_option_string(self, node): ...
    def visit_organization(self, node): ...
    def depart_organization(self, node): ...
    def visit_paragraph(self, node): ...
    def depart_paragraph(self, node): ...
    def visit_problematic(self, node): ...
    def depart_problematic(self, node): ...
    def visit_raw(self, node): ...
    def depart_raw(self, node): ...
    def has_unbalanced_braces(self, string): ...
    def visit_reference(self, node): ...
    def depart_reference(self, node): ...
    def visit_revision(self, node): ...
    def depart_revision(self, node): ...
    def visit_rubric(self, node): ...
    def depart_rubric(self, node): ...
    def visit_section(self, node): ...
    def depart_section(self, node): ...
    def visit_sidebar(self, node): ...
    def depart_sidebar(self, node): ...
    attribution_formats: Any = ...
    def visit_attribution(self, node): ...
    def depart_attribution(self, node): ...
    def visit_status(self, node): ...
    def depart_status(self, node): ...
    def visit_strong(self, node): ...
    def depart_strong(self, node): ...
    def visit_substitution_definition(self, node): ...
    def visit_substitution_reference(self, node): ...
    def visit_subtitle(self, node): ...
    def depart_subtitle(self, node): ...
    def visit_system_message(self, node): ...
    def depart_system_message(self, node): ...
    def visit_table(self, node): ...
    def depart_table(self, node): ...
    def visit_target(self, node): ...
    def depart_target(self, node): ...
    def visit_tbody(self, node): ...
    def depart_tbody(self, node): ...
    def visit_term(self, node): ...
    def depart_term(self, node): ...
    def visit_tgroup(self, node): ...
    def depart_tgroup(self, node): ...
    def thead_depth(self): ...
    def visit_thead(self, node): ...
    def depart_thead(self, node): ...
    def visit_title(self, node): ...
    def depart_title(self, node): ...
    def minitoc(self, node, title, depth): ...
    def visit_topic(self, node): ...
    def depart_topic(self, node): ...
    def visit_transition(self, node): ...
    def depart_transition(self, node): ...
    def visit_version(self, node): ...
    def depart_version(self, node): ...
    def unimplemented_visit(self, node): ...
