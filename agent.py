from __future__ import annotations as _annotations
from dotenv import load_dotenv

import os
from dataclasses import dataclass
import httpx
from typing import Any, Dict, List

from pydantic_ai import Agent, RunContext

load_dotenv()  # Load environment variables from .env file

openai_api_key = os.getenv("OPENAI_API_KEY")  # Retrieve OpenAI API key

@dataclass
class Deps:
    client: httpx.AsyncClient
    brave_api_key: str | None

# Create the web search agent
web_search_agent = Agent(
    model='openai:gpt-4o',
    system_prompt="Use the Brave API to perform web searches and return results succinctly.",
    deps_type=Deps,
    retries=2
)

@web_search_agent.tool
async def perform_web_search(ctx: RunContext[Deps], query: str) -> List[Dict[str, Any]]:
    """Search the web using the Brave API.

    Args:
        ctx: The context.
        query: The search query string.

    Returns:
        A list of search results.
    """
    if ctx.deps.brave_api_key is None:
        raise ValueError("Brave API key is missing.")

    headers = {"Authorization": f"Bearer {ctx.deps.brave_api_key}"}
    search_url = f"https://api.brave.com/v1/search?q={query}"

    async with ctx.deps.client.get(search_url, headers=headers) as response:
        response.raise_for_status()
        return await response.json()

async def main():
    async with httpx.AsyncClient() as client:
        brave_api_key = os.getenv("BRAVE_API_KEY")  # Assuming you set your Brave API key in environment var
        deps = Deps(client=client, brave_api_key=brave_api_key)

        # Example usage
        results = await web_search_agent.run("What is the capital of France?", deps=deps)
        print("Search Results:", results.data)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())