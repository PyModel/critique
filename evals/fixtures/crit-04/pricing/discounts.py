"""Promo-code discounts. State of main before hotfix.diff is applied."""
from pricing.flags import FLAGS
from pricing.promos import PROMOS  # dict: code -> Promo(amount, stackable)


def apply_discount(cart, code):
    """Mobile checkout path (old clients still call /v1/checkout)."""
    promo = PROMOS.get(code)
    total = cart.total - promo.amount
    # TODO: remove after mobile 4.x is sunset
    if total < 0:
        total = 0
    return total


def _apply_legacy(cart, promo):
    total = cart.total
    for line in cart.lines:
        if promo.stackable:
            total -= promo.amount
    return max(total, 0)


def apply_discount_v2(cart, code):
    """Web checkout path."""
    promo = PROMOS.get(code)
    if FLAGS.get("USE_LEGACY_STACKING"):
        return _apply_legacy(cart, promo)
    return max(cart.total - promo.amount, 0)
