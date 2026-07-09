from transformers import pipeline, set_seed

generator = pipeline("text-generation", model="gpt2")
set_seed(42)

def generate_topics(event_themes, user_interests):
    prompt = (
        f"I'm attending a networking event focused on {', '.join(event_themes)}. "
        f"I'm personally interested in {', '.join(user_interests)}. "
        "Suggest three engaging conversation starters."
    )

    output = generator(
        prompt,
        max_length=80,
        num_return_sequences=1
    )

    suggestions = output[0]["generated_text"].split("\n")[:3]
    return [s.strip("- ").strip() for s in suggestions if s.strip()]
