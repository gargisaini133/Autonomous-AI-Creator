from llm import ask_ai
from persona import build_persona
from article_reader import read_article


def generate_post(name, domain, title, source):
    persona = build_persona(name, domain)
    article_text = read_article(source)

    prompt = f"""
{persona}

You have selected this topic for publication.

Topic:
{title}

Source:
{source}

Article content:
{article_text}

Write one social media post about this topic.

Rules:
- Stay in the persona's voice
- Do not simply repeat the headline
- Explain why the development matters
- Every factual claim must be directly supported by the provided article content
- Do not add background facts from your own knowledge
- Do not invent statistics, events, capabilities, or claims
- You may give an opinion or interpretation, but make it clearly sound like analysis rather than fact
- If the source does not contain enough information for a claim, leave that claim out
- Keep it concise
- Do not use hashtags
- Do not mention that you are an AI
- Do not include the source URL in the post text

Return only the finished post text.
"""

    return ask_ai(prompt).strip()