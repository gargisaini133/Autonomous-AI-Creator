import uuid

from discovery import get_hacker_news_topics
from editorial import decide_topic
from database import get_connection

agent_id = "a2e9bd76-dd03-4912-bdfa-6a0d97a38c2d"

topics = get_hacker_news_topics()

conn = get_connection()
cursor = conn.cursor()

for topic in topics:
    result = decide_topic(topic["title"])

    cursor.execute(
        """
        INSERT INTO candidates (
            candidate_id,
            agent_id,
            title,
            source,
            score,
            decision
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            str(uuid.uuid4()),
            agent_id,
            topic["title"],
            topic["url"],
            result["score"],
            result["decision"]
        )
    )

    print(topic["title"], "->", result["decision"])

conn.commit()
conn.close()

print("Candidates saved!")