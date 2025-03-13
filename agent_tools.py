from httpx import AsyncClient
from .agent import perform_web_search

async def create_client() -> AsyncClient:
    """Creates an async HTTP client for making API requests."""
    return AsyncClient()