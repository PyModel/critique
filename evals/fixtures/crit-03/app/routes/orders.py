from fastapi import APIRouter, Depends

from app.db import get_db
from app.session import current_user

router = APIRouter()
_FIELDS = ("id", "user_id", "total", "status")


@router.get("/{order_id}")
def get_order(order_id: int, db=Depends(get_db)):
    row = db.execute(
        "SELECT id, user_id, total, status FROM orders WHERE id = ?", (order_id,)
    ).fetchone()
    return dict(zip(_FIELDS, row))


@router.post("/{order_id}/cancel")
def cancel_order(order_id: int, db=Depends(get_db)):
    db.execute("UPDATE orders SET status = 'cancelled' WHERE id = ?", (order_id,))
    db.commit()
    return {"status": "cancelled"}


@router.get("")
def list_orders(limit: int = 50, offset: int = 0, user=Depends(current_user), db=Depends(get_db)):
    rows = db.execute(
        "SELECT id, user_id, total, status FROM orders WHERE user_id = ? LIMIT ? OFFSET ?",
        (user.id, limit, offset),
    ).fetchall()
    return [dict(zip(_FIELDS, r)) for r in rows]
