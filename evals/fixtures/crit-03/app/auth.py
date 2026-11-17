from fastapi import Depends, HTTPException, Request

from app.db import get_db
from app.session import current_user


def require_order_owner(request: Request, user=Depends(current_user), db=Depends(get_db)):
    """Router-level guard: any route with an order_id path parameter is owner-only."""
    order_id = request.path_params.get("order_id")
    if order_id is None:
        return
    owner = db.execute("SELECT user_id FROM orders WHERE id = ?", (order_id,)).fetchone()
    if owner is None or owner[0] != user.id:
        raise HTTPException(status_code=404)
