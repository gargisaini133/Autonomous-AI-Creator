import json

from llm import ask_ai
from article_reader import read_article


def judge_topic(title, source):
    article_text = read_article(source)

    prompt = f"""
You are Nexus, an autonomous AI and emerging technology analyst.

Your audience follows:
- Artificial intelligence
- Machine learning
- AI models
- AI agents
- AI security
- Robotics
- Open-source technology
- Developer tools

You are selective. You DO NOT publish something just because it involves technology.

Reject:
- Funny or novelty stories
- Lifestyle stories
- Celebrity stories
- Clickbait
- Minor product changes
- Topics with no meaningful AI or technical importance
- Stories that would not matter to AI/technology professionals

Publish only if the topic has meaningful relevance to AI, software, computing,
security, robotics, machine learning, open source, or important developer technology.

Candidate title:
{title}

Source:
{source}

Article content:
{article_text}

Give scores from 0 to 10 for:
1. AI/technology relevance
2. Technical significance
3. Professional usefulness
4. Novelty

If AI/technology relevance is below 6, you MUST reject it.

Base your judgment only on the title and article content provided.
Do not invent facts that are not present in the source.

Return ONLY valid JSON like this:

{{
    "decision": "PUBLISH",
    "score": 8,
    "reason": "Brief explanation based on the source"
}}
"""

    result = ask_ai(prompt)

    result = result.replace("```json", "").replace("```", "").strip()

    return json.loads(result)