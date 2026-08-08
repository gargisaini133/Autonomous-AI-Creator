from ai_editorial import judge_topic

topic = {
    "title": "A Physicist Rigged His Pet Hamster’s Wheel to Upload to Strava",
    "source": "https://www.runnersworld.com/"
}

print("Starting test...")

result = judge_topic(
    topic["title"],
    topic["source"]
)

print(result)