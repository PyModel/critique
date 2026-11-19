def run_one(db, queue):
    member, label, job_id = queue.receive()
    db.execute("UPDATE published SET label=?", (label,))
    db.commit()
    queue.ack(job_id)
