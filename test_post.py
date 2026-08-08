import sqlite3
import uuid
from datetime import datetime, timezone

agent_id = "a2e9bd76-dd03-4912-bdfa-6a0d97a38c2d"

conn = sqlite3.connect("agent.db")
cursor = conn.cursor()

cursor.execute(
    """
    INSERT INTO posts (
        post_id,
        agent_id,
        created_at,
        text,
        rationale,
        sources
    )
    VALUES (?, ?, ?, ?, ?, ?)
    """,
    (
        str(uuid.uuid4()),
        agent_id,
        datetime.now(timezone.utc).isoformat(),
        "This is Nexus's first test post.",
        "This is a temporary test to check whether the feed works.",
        "https://example.com"
    )
)

conn.commit()
conn.close()

print("Test post added!")