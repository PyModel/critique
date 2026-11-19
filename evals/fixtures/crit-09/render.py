"""Offline renderer. order_ids is a list of integer IDs, including repeats and misses.
On a single consistent snapshot, db.items(id) returns a fresh list of approved
items for that order in position order; db.items_many(ids) makes one read and
returns (order_id, item) pairs with the SAME approval filter and within-order
ordering. It accepts up to 100 distinct IDs per call. A typical logged run made
501 reads for 501 positions (240 unique IDs). Each output list is independently editable.
"""


def render(db, order_ids):
    return [db.items(order_id) for order_id in order_ids]
