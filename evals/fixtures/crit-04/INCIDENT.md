# INC-2291 — checkout 500s on expired promo codes

- Since the 14:02 deploy, web checkout returns 500 when the cart carries a promo code that is no longer in `PROMOS` (expired codes were pruned from the table in that deploy).
- 8% of web checkouts are failing. Stack trace: `AttributeError: 'NoneType' object has no attribute 'amount'` in `apply_discount_v2`.
- Proposed hotfix: `hotfix.diff`. Ship tonight; release freeze starts tomorrow 09:00.
