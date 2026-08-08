from discovery import get_hacker_news_topics

topics = get_hacker_news_topics()

for topic in topics:
    print(topic)