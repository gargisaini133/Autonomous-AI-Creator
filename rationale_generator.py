from llm import ask_ai
from article_reader import read_article


def generate_rationale(title, source, editorial_reason):
    article_text = read_article(source)

    prompt = f"""
You are explaining an autonomous editor's publishing decision.

Topic:
{title}

Source:
{source}

Article content:
{article_text}

Editorial reason:
{editorial_reason}

Write a short publishing rationale that clearly explains:

1. Why this topic was selected
2. Why it is relevant now
3. Why it deserves publication over lower-value technology stories

Do not invent facts.
Every factual statement must be directly supported by the provided article content.
Do not claim that results "prove" something unless the source explicitly says so.
Do not use labels like "frontier", "state-of-the-art", or "breakthrough" unless supported by the source.
You may explain significance as analysis, but make it clear that it is interpretation.
Keep it concise.

Return only the rationale text.
"""

    return ask_ai(prompt).strip()