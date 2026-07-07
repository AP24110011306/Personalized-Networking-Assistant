from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="gpt2"
)

def generate_conversation(event, interests, themes):
    prompt = (
        f"Generate three networking conversation starters.\n"
        f"Event: {event}\n"
        f"Interests: {interests}\n"
        f"Themes: {', '.join(themes)}\n\n"
        f"Conversation Starters:\n"
    )

    result = generator(
        prompt,
        max_length=100,
        num_return_sequences=1,
        do_sample=True,
        temperature=0.8
    )

    text = result[0]["generated_text"]

    starters = text.split("\n")

    return [
        line.strip("- ").strip()
        for line in starters
        if line.strip()
    ][:3]
