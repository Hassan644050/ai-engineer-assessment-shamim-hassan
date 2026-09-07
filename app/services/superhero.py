import httpx
from app.config import get_env_meta_info


def search_superhero(name: str):
    env_meta_info = get_env_meta_info()

    url = (
        f"https://superheroapi.com/api/"
        f"{env_meta_info.super_hero_api_token}/search/{name}"
    )

    response = httpx.get(url, timeout=10,follow_redirects=True)
    response.raise_for_status()
    return response.json()

def format_superhero_response(data: dict) -> str:
    if data.get("response") != "success":
        return "I couldn't find that superhero."

    results = data.get("results", [])

    if not results:
        return "I couldn't find that superhero."

    superhero = results[0]
    for result in results:
        full_name = result.get("biography", {}).get("full-name", "")

        if full_name == "Bruce Wayne":
            superhero = result
            break

    name = superhero.get("name", "Unknown")
    biography = superhero.get("biography", {})
    powerstats = superhero.get("powerstats", {})

    full_name = biography.get("full-name", "Unknown")
    alignment = biography.get("alignment", "Unknown")

    intelligence = powerstats.get("intelligence", "Unknown")
    strength = powerstats.get("strength", "Unknown")
    speed = powerstats.get("speed", "Unknown")

    return (
        f"{name} ({full_name}) is a {alignment} superhero. "
        f"Powerstats: intelligence={intelligence}, "
        f"strength={strength}, speed={speed}."
    )