import re


def score_topic(title):
    title_lower = title.lower()

    important_words = [
        "ai",
        "model",
        "deepseek",
        "open source",
        "security",
        "robotics",
        "machine learning",
        "llm"
    ]

    score = 0

    for word in important_words:
        pattern = r"\b" + re.escape(word) + r"\b"

        if re.search(pattern, title_lower):
            score += 1

    return score


def decide_topic(title):
    score = score_topic(title)

    if score >= 1:
        return {
            "decision": "PUBLISH",
            "score": score
        }

    return {
        "decision": "REJECT",
        "score": score
    }