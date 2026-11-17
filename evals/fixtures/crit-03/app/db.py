import sqlite3


def get_db():
    conn = sqlite3.connect("orders.db")
    try:
        yield conn
    finally:
        conn.close()
