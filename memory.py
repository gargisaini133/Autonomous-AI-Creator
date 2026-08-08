import os

from dotenv import load_dotenv
from breeth import BreethClient

from llm import ask_ai


load_dotenv()

api_key = os.getenv("BREETH_API_KEY")

client = BreethClient(api_key=api_key)


def remember_post(agent_id, title, post_text):
    return client.write(
        content=f"""
Agent {agent_id} published a post.

Topic: {title}

Post:
{post_text}
""",
        group_id=agent_id,
        source_description="autonomous-ai-creator",
        extract_intent=False
    )


def search_memory(agent_id, topic):
    return client.retrieve(
        query=topic,
        group_id=agent_id,
        limit=5
    )


def has_similar_memory(agent_id, topic):
    results = search_memory(agent_id, topic)

    memory_facts = []

    if results.edges:
        for edge in results.edges:
            if edge.fact:
                memory_facts.append(edge.fact)

    if not memory_facts:
        return False

    memories_text = "\n".join(memory_facts)

    prompt = f"""
You are checking whether an autonomous technology creator
has already published about the SAME news story.

New topic:
{topic}

Previous memories:
{memories_text}

Return DUPLICATE only if the previous memory clearly refers to
the same event, announcement, release, benchmark, or story.

If it is merely related, about the same company, or represents
a new development, return NEW.

Return exactly one word:

DUPLICATE

or

NEW
"""

    decision = ask_ai(prompt).strip().upper()

    return decision == "DUPLICATE"