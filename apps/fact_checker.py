import requests

WIKIPEDIA_API = "https://en.wikipedia.org/api/rest_v1/page/summary/"

def fact_check(query):
    try:
        response = requests.get(
            WIKIPEDIA_API + query.replace(" ", "_"),
            timeout=5
        )

        if response.status_code == 200:
            data = response.json()
            return {
                "verified": True,
                "summary": data.get("extract", "No summary available."),
                "source": data.get("content_urls", {})
            }

        return {
            "verified": False,
            "summary": "No information found."
        }

    except Exception as e:
        return {
            "verified": False,
            "summary": str(e)
        }
