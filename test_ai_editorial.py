from ai_editorial import judge_topic

topic = {
    "title": "DeepSeek V4 Flash 0731",
    "source": "https://arcprize.org/results/deepseek-v4-flash-0731"
}

print("Reading source and judging topic...")

result = judge_topic(
    topic["title"],
    topic["source"]
)

print(result)