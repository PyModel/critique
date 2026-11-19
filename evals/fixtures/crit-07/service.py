def enqueue_refresh(db, queue, member, label, job_id):
    if db.active_member(member):
        queue.put((member, label, job_id))


def disable_reminders(db):
    db.execute("UPDATE preferences SET enabled=0 WHERE enabled<>0")
