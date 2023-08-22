from datetime import datetime


def now() -> datetime.date:
  return datetime.utcnow()


def now_iso() -> str:
  return to_iso(now())


def to_iso(date: datetime.date):
  return date.replace(microsecond=0).isoformat() + "Z"


def iso_to_iso_safe(iso: str):
  return iso.replace(":", "-").replace("T", "--")
