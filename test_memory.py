from memory import has_similar_memory

agent_id = "a2e9bd76-dd03-4912-bdfa-6a0d97a38c2d"

print("Known old topic:")
print(
    has_similar_memory(
        agent_id,
        "Memory Test Topic"
    )
)

print()

print("Completely different topic:")
print(
    has_similar_memory(
        agent_id,
        "New robotics foundation model released for warehouse automation"
    )
)