from dataclasses import dataclass

from fastapi import Header, HTTPException

from app.tokens import verify_session_token


@dataclass(frozen=True)
class User:
    id: int


def current_user(authorization: str = Header(...)) -> User:
    user_id = verify_session_token(authorization.removeprefix("Bearer "))
    if user_id is None:
        raise HTTPException(status_code=401)
    return User(id=user_id)
