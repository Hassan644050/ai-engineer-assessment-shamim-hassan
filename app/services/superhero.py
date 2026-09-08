import httpx
from app.config import get_env_meta_info
from app.exceptions.exceptions import SuperheroAPIException


def search_superhero(name: str):
    env_meta_info = get_env_meta_info()

    url = (
        f"https://superheroapi.com/api/"
        f"{env_meta_info.super_hero_api_token}/search/{name}"
    )

    try:
        response = httpx.get(url, timeout=10,follow_redirects=True)
        response.raise_for_status()
        return response.json()
    except httpx.TimeoutException as exc:
        raise SuperheroAPIException(
            "Superhero API request timed out."
        ) from exc
    
    except httpx.HTTPStatusError as exc:
        raise SuperheroAPIException(
            "Superhero API returned an HTTP error."
        ) from exc
    
    except ValueError as exc:
        raise SuperheroAPIException(
            "Superhero API returned invalid JSON."
        ) from exc
    
    except httpx.RequestError as exc:
        raise SuperheroAPIException(
            "Unable to connect to Superhero API."
        ) from exc
    

def format_superhero_response(data: dict) -> str:
    if data.get("response") != "success":
        return data.get(
            "error",
            "I couldn't retrieve superhero information."
        )

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