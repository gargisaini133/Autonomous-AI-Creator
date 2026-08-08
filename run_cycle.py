import uuid

from discovery import get_hacker_news_topics
from ai_editorial import judge_topic
from database import get_connection

agent_id = "a2e9bd76-dd03-4912-bdfa-6a0d97a38c2d"

topics = get_hacker_news_topics()

conn = get_connection()
cursor = conn.cursor()

for topic in topics:
    result = judge_topic(
        topic["title"],
        topic["url"]
    )

    cursor.execute(
        """
        INSERT INTO candidates (
            candidate_id,
            agent_id,
            title,
            source,
            score,
            decision,
            reason
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            str(uuid.uuid4()),
            agent_id,
            topic["title"],
            topic["url"],
            result["score"],
            result["decision"],
            result["reason"]
        )
    )

    print()
    print("TITLE:", topic["title"])
    print("DECISION:", result["decision"])
    print("SCORE:", result["score"])
    print("REASON:", result["reason"])

conn.commit()
conn.close()

print()
print("AI editorial cycle complete!")