# Seller payouts — design

Sellers are paid nightly for the previous day's settled orders. An accepted bank transfer is irreversible: the payout service cannot recall it.

## Flow

1. At 02:00 a cron job starts two payout workers (two for speed; the run must finish before 06:00).
2. Each worker runs `SELECT * FROM payouts WHERE status = 'pending' LIMIT 500` and loops over the rows.
3. For each row the worker calls the bank's `POST /transfers` with the seller's account and the amount.
4. On HTTP 200 the worker sets `status = 'paid'` and stores the bank's transfer id.
5. On a timeout (10 s) or a 5xx the worker retries up to 3 times, then leaves the row `pending` for the next night.

## Notes

- Amounts are stored as floats in dollars.
- The bank API accepts an optional `Idempotency-Key` header; we do not send it yet.
- Finance reconciles against the bank statement at month end.
- Expected volume: about 4,000 payouts per night.
