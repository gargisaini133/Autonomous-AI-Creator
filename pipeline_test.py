from discovery import get_hacker_news_topics
from editorial import decide_topic

topics = get_hacker_news_topics()

for topic in topics:
    result = decide_topic(topic["title"])

    print("TITLE:", topic["title"])
    print("DECISION:", result["decision"])
    print("SCORE:", result["score"])
    print("SOURCE:", topic["url"])
    print("--------------------------")