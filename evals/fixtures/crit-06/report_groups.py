"""Offline report builder. Inputs are in-memory lists of strings and (string, string) tuples.
Typical full report: 2,000 requested groups, 40,000 event rows. The output is consumed
in requested order. Each output row is independently editable by the caller.
"""


def report_groups(requested, events):
    return [[value for tag, value in events if tag == group] for group in requested]
