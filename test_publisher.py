from post_generator import generate_post
from rationale_generator import generate_rationale
from publisher import save_post

agent_id = "a2e9bd76-dd03-4912-bdfa-6a0d97a38c2d"

title = "DeepSeek V4 Flash 0731"
source = "https://arcprize.org/results/deepseek-v4-flash-0731"

editorial_reason = (
    "The benchmark results show strong reasoning performance "
    "at very low per-task cost."
)

post = generate_post(
    "Nexus",
    "AI and Emerging Technology",
    title,
    source
)

rationale = generate_rationale(
    title,
    source,
    editorial_reason
)

post_id = save_post(
    agent_id,
    post,
    rationale,
    source
)

print("Post saved!")
print("Post ID:", post_id)