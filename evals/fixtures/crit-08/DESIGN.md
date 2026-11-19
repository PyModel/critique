# Directory release and recovery
Employees' display names reside in the primary directory, a search projection, and daily backup snapshots. Contract: once deletion has been acknowledged, the name must not reappear in any served view, including after a restore. Cold offline snapshots may be retained for 30 days. A separate durable erasure journal is available to recovery operators.

Deletion writes the journal and removes the primary and search entries before acknowledging. Recovery restores last night's database, rebuilds search, opens traffic and then asynchronously replays the erasure journal. Backups restore successfully in a timed 12-minute drill. Its measured interval ends before journal replay. Service target: resume compliant traffic within 20 minutes.

CI tests immutable build digest D. Promotion selects tag 'candidate' at deployment time. A later successful build may move the tag between review and promotion. Rollback uses the recorded previous digest. The manifest validation command requires a real vendor credential and sends the manifest to its external service. The only available third-party review service has no approval to receive this design.
