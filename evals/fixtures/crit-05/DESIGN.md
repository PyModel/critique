# Stockroom — internal inventory tool

## Context

Used by the 12 people in our one warehouse to record stock counts and transfers between shelves. About 200 requests a day, office hours only. If it is down for an afternoon, staff write counts on paper and enter them later.

## Design

- One FastAPI process behind the company SSO proxy (the proxy authenticates; the app reads the `X-User` header it sets and rejects requests without it; the VM firewall only accepts traffic from the proxy).
- SQLite database file on the VM's disk, WAL mode. Tables: `items(sku PRIMARY KEY, name)`, `stock(sku REFERENCES items, shelf, qty CHECK (qty >= 0), PRIMARY KEY (sku, shelf))`, `transfers(id, sku, from_shelf, to_shelf, qty, user, at)`.
- A transfer runs in one transaction: decrement the source shelf, increment the destination, insert the transfer row.
- Server-rendered HTML forms; every form post carries a hidden one-time token stored with a unique constraint, so a double submit is rejected.
- Nightly `sqlite3 .backup` copied to the company file server; restore was tested last month (15 minutes).
- Deployed with a systemd unit; `git pull && systemctl restart stockroom` to release. Logs go to journald.
