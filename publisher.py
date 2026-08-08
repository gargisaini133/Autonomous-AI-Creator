import uuid
from datetime import datetime, timezone

from database import get_connection


def save_post(agent_id, text, rationale, source):
    post_id = str(uuid.uuid4())
    created_at = datetime.now(timezone.utc).isoformat()

    conn = get_connection()
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
            post_id,
            agent_id,
            created_at,
            text,
            rationale,
            source
        )
    )

    conn.commit()
    conn.close()

    return post_id