# Contributing to the CIM

Dear ES-DOC community member,

Thank you for taking the time to consider making a contribution to the
CIM.

This set of guidelines provides a overview of the practices and
procedures that should be used in fixing, updating, or adding to the
CIM.

The ES-DOC community takes great pride in respectful and collegial
discourse. Any disrespectful or otherwise derogatory communication
will not be tolerated.

## General Guidelines

* All changes to the CIM should be done as git pull requests, since
  each pull request comes with documentation as to why the change is
  necessary.

* Changes to the CIM should be classified as trivial, minor or major
  as follows

  * **Major**: A change to any part of the schema layout, base metadata or
    constraint & reference structure.

  * **Minor**: Adding a new document class or a new extension package.

  * **Trivial**: A change to any other properties (including adding new
    classes or enumerations).

* For trivial and minor changes, the ES-DOC development team will have
  the authority to review and sign off. This can be done using slack
  or on a weekly telco. The team should have at least 2 days to
  review.

* Major changes should be approved by the PIs. Those requesting the
  change should contact the PIs with a summary of the changes with a
  justification for them. The PIs and ES-DOC development team should
  have at least 1 week to review the changes. If there is no response
  from the PIs for 1 week from the request being made, the changes may
  accepted by default.


## Version strategy for the CIM

Use a three-level **major.minor.trivial** numeric version scheme,
e.g 2.11.13. Major, minor and trivial changes to the CIM, as defined
above, require an increment to appropriate field of the version.

## History

These guidelines were originally conceived by the ES-DOC PIs on 30th
November 2016.
