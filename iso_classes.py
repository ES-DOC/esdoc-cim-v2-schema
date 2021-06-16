# -*- coding: utf-8 -*-

"""
.. module:: iso_classes.py
   :synopsis: Set of CIM v2 ontology type definitions.
   applying to the description of CMIP6 Data Reference Syntax quantities.

This package is based on DQ_Lineage (ISO19115-2) as documented at
http://wiki.esipfed.org/index.php/File:LI_Lineage-2.png.

It provides a complete and extended implementation of _one_ possible way
of implementing LI_Lineage (i.e. some optional associations are ommitted, and
some additional associations are included, and where necessary, some
associations are to CIM entities, rather than other ISO implementations
(e.g. to shared.citation, rather than CI_Citation, although the CIM
shared.citation is itself an extension of CI_Citation).

The key omission is the use of LE_Source, where instead process_step is
preferred, and process_step itself uses CIM data.dataset for source inputs.

"""


def lineage():
    """Representation of the ISO19115 lineage provenance description.

    Information about the events or source data used in constructing a
    dataset

    """
    return {
        "type": "class",
        "base": None,
        "is_abstract": False,
        "is_document": True,
        "pstr": ("{}", ("statement",)),
        "properties": [
            (
                "statement",
                "str",
                "0.1",
                "General explanation of the level of knowledge or lack "
                "thereof about the lineage",
            ),
            (
                "process_step",
                "iso.process_step",
                "0.N",
                "How the resource was developed or set of events associated "
                "with production.",
            ),
            (
                "source",
                "linked_to(data.dataset)",
                "0.N",
                "Input(s) used in production of resource",
            ),
        ],
        "constraints": [],
    }


def process_step():
    """Representation of the ISO19115 LE_ProcessStep and parent
    LI_ProcessStep classes."""

    return {
        "type": "class",
        "base": None,
        "is_abstract": False,
        "is_document": False,
        "pstr": ("{}", ("description",)),
        "properties": [
            (
                "description",
                "str",
                "1.1",
                "General description of the events in the development of the "
                "resource.",
            ),
            (
                "rationale",
                "str",
                "0.1",
                "Purpose for performing the process on the resource",
            ),
            (
                "execution_date_time",
                "time.date_time",
                "0.1",
                "The date and time when the process was completed.",
            ),
            (
                "processor",
                "shared.responsibility",
                "0.1",
                "Individual or organisation responsible for the process step. "
                "Use roleCode='processor'. Contact information is not "
                "necessary.",
            ),
            (
                "reference",
                "linked_to(shared.citation)",
                "0.N",
                "Process step documentation",
            ),
            (
                "source",
                "linked_to(data.dataset)",
                "0.N",
                "Information on the inputs used in the process step.",
            ),
            (
                "processing_information",
                "iso.processing",
                "0.N",
                "Comprehensive information on the processing carried out",
            ),
            (
                "report",
                "iso.process_step_report",
                "0.N",
                "Report generated by the process step",
            ),
        ],
    }


def processing():
    """Representation of the ISO19115 LE_Processing class Note that the
    algorithm definition has been adjusted to be more generic and less
    "instrument obsessed" than ISO19115.

    Name is an extension, and the identifier is simply a code string
    (id) ... but given there may be no identifier space for this
    processing step, it is made optional, rather than mandatory as in
    ISO. For export to ISO, the recommendation is to use the identifier
    of the CIM document which uses this class.

    """

    return {
        "type": "class",
        "base": None,
        "is_abstract": False,
        "is_document": False,
        "pstr": ("{}", ("name",)),
        "properties": [
            (
                "name",
                "str",
                "1.1",
                "Name of the processing action (ISO extension)",
            ),
            (
                "identifier",
                "str",
                "0.1",
                "Identifier (strictly, a code which can be used in an "
                "MD_Identifier",
            ),
            (
                "softwareReference",
                "linked_to(shared.citation)",
                "0.N",
                "Reference to document describing processing software",
            ),
            (
                "procedureDescription",
                "str",
                "0.1",
                "additional details about the processing procedures",
            ),
            (
                "documentation",
                "linked_to(shared.citation)",
                "0.1",
                "reference to documentation describing the processing",
            ),
            (
                "runTimeParameters",
                "str",
                "0.1",
                "parameters to control the processing operations, entered at "
                "run time",
            ),
            (
                "algorithm",
                "iso.algorithm",
                "0.N",
                "details of the methodology carried out in this processing",
            ),
        ],
    }


def process_step_report():
    """Report of what happened during a processing step.

    Representation of ISO LE_ProcessStepReport, modified to use links or
    body text, rather than files.

    """
    return {
        "type": "class",
        "base": None,
        "is_abstract": False,
        "is_document": False,
        "pstr": ("{}", ("name",)),
        "properties": [
            ("name", "str", "1.1", "Name of the processing report"),
            (
                "description",
                "str",
                "1.1",
                "Summary textual description of what occurred during the "
                "process step",
            ),
            (
                "link",
                "shared.online_resource",
                "0.1",
                "Link to actual report documents, if any",
            ),
        ],
    }


def algorithm():
    """Representation of the LE_Algorithm Class."""
    return {
        "type": "class",
        "base": None,
        "is_abstract": False,
        "is_document": False,
        "pstr": ("{}", ("description",)),
        "properties": [
            ("description", "str", "0.1", "Textural description of algorithm"),
            (
                "citation",
                "linked_to(shared.citation)",
                "0.1",
                "Formal documentation for the algorithm used.",
            ),
        ],
    }


def quality_report():
    """"""
    return {
        "type": "class",
        "base": None,
        "is_abstract": False,
        "is_document": True,
        "properties": [
            (
                "target",
                "shared.online_resource",
                "1.1",
                "Document about to which this quality report applies",
            ),
            (
                "issues",
                "iso.quality_issue",
                "0.N",
                "Issues with this resource",
            ),
            (
                "reports",
                "iso.quality_evaluation_result",
                "0.N",
                "Reports against quality measures for this resource",
            ),
        ],
    }


def quality_issue():
    """A description of some scientific quality issue known about a
    resource described by this ontology.

    E.g. if a model is known to have a particular problem, or there has
    been a problem found with a dataset. Expect that most such detail
    should be managed in an external (and formal) issue tracker.

    """

    return {
        "type": "class",
        "base": None,
        "is_abstract": False,
        "properties": [
            ("summary", "str", "1.1", "Brief (one-line) description of issue"),
            (
                "reporter",
                "linked_to(shared.party)",
                "0.1",
                "Person or entity responsible for reporting/describing issue",
            ),
            ("description", "str", "0.1", "Description of issue"),
            (
                "tracked_issue",
                "shared.online_resource",
                "0.1",
                "Issue as lodged in an external issue tracker",
            ),
        ],
    }


def quality_evaluation_result():
    """The output of some quality evaluation against a specific measure
    for evaluation quality.

    This flattens several ISO classes, including DQ_Result,
    DQ_ConformanceResult, DQ_QuantativeResult, DQ_Element.

    """

    return {
        "type": "class",
        "base": None,
        "is_abstract": False,
        "properties": [
            ("name", "str", "1.1", "Name of measure being evaluated"),
            (
                "evaluation_procedure",
                "str",
                "0.1",
                "Brief description of the evaluation method",
            ),
            (
                "specification",
                "linked_to(shared.citation)",
                "0.1",
                "Formal specification of the evaluation method",
            ),
            (
                "evaluator",
                "linked_to(shared.party)",
                "0.1",
                "Person or entity reesponsible for evaluation",
            ),
            ("date", "time.date_time", "0.1", "Date of quality evaluation"),
            (
                "summary_result",
                "str",
                "0.1",
                "Summary description of evaluation outcome",
            ),
            (
                "passed",
                "bool",
                "0.1",
                "Success or failure of the evaluation, if boolean concept is "
                "appropriate",
            ),
            (
                "results",
                "iso.quality_evaluation_output",
                "0.N",
                "Evaluation outputs, including log files, plots, or datasets",
            ),
        ],
    }


def quality_evaluation_output():
    """A specific evaluation output."""
    return {
        "type": "class",
        "base": "shared.online_resource",
        "is_abstract": False,
        "properties": [
            (
                "output_type",
                "iso.dq_evaluation_result_type",
                "1.1",
                "Type of evaluation resource",
            )
        ],
    }
