from rationale_generator import generate_rationale

rationale = generate_rationale(
    "DeepSeek V4 Flash 0731",
    "https://arcprize.org/results/deepseek-v4-flash-0731",
    "The benchmark results show strong reasoning performance at very low per-task cost, making the topic relevant to AI professionals tracking model capability and efficiency."
)

print(rationale)