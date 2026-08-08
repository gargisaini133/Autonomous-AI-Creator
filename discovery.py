import requests


def get_hacker_news_topics():
    top_stories_url = "https://hacker-news.firebaseio.com/v0/topstories.json"

    story_ids = requests.get(top_stories_url).json()

    topics = []

    for story_id in story_ids[:5]:
        story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
        story = requests.get(story_url).json()

        topics.append({
            "title": story.get("title"),
            "url": story.get(
                "url",
                f"https://news.ycombinator.com/item?id={story_id}"
            )
        })

    return topics