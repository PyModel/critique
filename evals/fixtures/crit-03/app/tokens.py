import hashlib
import hmac
import os

_KEY = os.environ["SESSION_SIGNING_KEY"].encode()


def verify_session_token(token: str) -> int | None:
    user_id, _, signature = token.partition(".")
    expected = hmac.new(_KEY, user_id.encode(), hashlib.sha256).hexdigest()
    if not user_id.isdigit() or not hmac.compare_digest(signature, expected):
        return None
    return int(user_id)
