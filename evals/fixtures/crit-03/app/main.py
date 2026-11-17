from fastapi import Depends, FastAPI

from app.auth import require_order_owner
from app.routes import orders

app = FastAPI()
app.include_router(
    orders.router,
    prefix="/orders",
    dependencies=[Depends(require_order_owner)],
)
