from editorial import decide_topic

topics = [
    "DeepSeek V4 Flash",
    "A Hamster Uploaded to Strava",
    "New AI Security Model Released",
    "Assembly Hall of Shame"
]

for topic in topics:
    result = decide_topic(topic)

    print(topic)
    print("Decision:", result["decision"])
    print("Score:", result["score"])
    print()