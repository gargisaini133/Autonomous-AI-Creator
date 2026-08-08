import uuid

from discovery import get_hacker_news_topics
from ai_editorial import judge_topic
from post_generator import generate_post
from rationale_generator import generate_rationale
from publisher import save_post
from memory import has_similar_memory, remember_post
from database import get_connection


def run_agent_cycle(agent_id, name, domain):
    print("Nexus is starting a new autonomous cycle...")

    topics = get_hacker_news_topics()

    publish_candidates = []

    for topic in topics:
        title = topic["title"]
        source = topic["url"]

        print()
        print("Checking:", title)

        # STEP 1: Check memory
        try:
            if has_similar_memory(agent_id, title):
                print("Already covered this story. Skipping.")
                continue
        except Exception as error:
            print("Memory error. Skipping this topic.")
            print("Error:", error)
            continue

        # STEP 2: Let AI judge it
        try:
            result = judge_topic(title, source)
        except Exception as error:
            print("AI error. Skipping this topic.")
            print("Error:", error)
            continue

        print("Decision:", result["decision"])
        print("Score:", result["score"])
        print("Reason:", result["reason"])

        # STEP 3: Save editorial decision
        conn = get_connection()
        cursor = conn.cursor()

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
                title,
                source,
                result["score"],
                result["decision"],
                result["reason"]
            )
        )

        conn.commit()
        conn.close()

        # STEP 4: Keep good candidates
        if result["decision"] == "PUBLISH":
            publish_candidates.append({
                "title": title,
                "source": source,
                "score": result["score"],
                "reason": result["reason"]
            })

    # Nothing worth publishing
    if not publish_candidates:
        print()
        print("Nothing worth publishing this cycle.")
        print("Autonomous cycle complete.")
        return

    # STEP 5: Pick only the highest-scoring story
    best_topic = max(
        publish_candidates,
        key=lambda item: item["score"]
    )

    print()
    print("Best topic selected:")
    print(best_topic["title"])
    print("Score:", best_topic["score"])

    # STEP 6: Write the post
    post = generate_post(
        name,
        domain,
        best_topic["title"],
        best_topic["source"]
    )

    # STEP 7: Generate rationale
    rationale = generate_rationale(
        best_topic["title"],
        best_topic["source"],
        best_topic["reason"]
    )

    # STEP 8: Save the post
    post_id = save_post(
        agent_id,
        post,
        rationale,
        best_topic["source"]
    )

    # STEP 9: Remember the post using Breeth
    remember_post(
        agent_id,
        best_topic["title"],
        post
    )

    print()
    print("Published!")
    print("Post ID:", post_id)

    print()
    print("Autonomous cycle complete.")