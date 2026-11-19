# Label refresh service
Each workspace has its own database and its own single worker. DB selection is made by the runtime, not from message fields. Each database contains one preference row; no triggers, events or other side effects. Turning reminders off is a set operation.

A refresh may update the published label only while the requester's membership is active, including when the queued change commits. Membership can end while a job waits. The queue redelivers an unacknowledged job after worker restart. A job carries its requester's ID, original label, and job ID. No other component checks membership for this operation.
