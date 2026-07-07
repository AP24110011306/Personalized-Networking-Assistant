from transformers import pipeline

classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)

LABELS = [
    "Artificial Intelligence",
    "Healthcare",
    "Business",
    "Education",
    "Technology",
    "Networking",
    "Finance",
    "Sustainability",
]

def classify_theme(event_description):
    result = classifier(event_description, LABELS)
    return result["labels"][:3]
