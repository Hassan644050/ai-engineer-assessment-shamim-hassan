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