from datetime import datetime


def today() -> str:
    """Returns today's date YYYY-MM-DD"""
    today = datetime.now()
    return f"{today.year}-{today.month:02d}-{today.day:02d}"
