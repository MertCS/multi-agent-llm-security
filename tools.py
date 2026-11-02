
from pathlib import Path
from datetime import datetime, timezone
import json

DOCUMENTS_DIR = Path(__file__).parent / "documents"
EMAIL_LOG = Path(__file__).parent / "email_log.jsonl"


def read_document(id: str) -> str:
    """Read a document from the local documents directory."""
    if not id.isalnum():
        raise ValueError("Invalid document ID")

    path = DOCUMENTS_DIR / f"{id}.txt"

    if not path.is_file():
        raise FileNotFoundError(f"Document {id} not found")

    return path.read_text(encoding="utf-8")


def send_email(to: str, body: str) -> str:
    """Simulate sending an email by recording the call."""
    entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "to": to,
        "body": body,
    }

    with EMAIL_LOG.open("a", encoding="utf-8") as file:
        file.write(json.dumps(entry) + "\n")

    return "Email call logged (no email was sent)"
