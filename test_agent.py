import pytest
from unittest.mock import AsyncMock, patch
import httpx
from agent import web_search_agent, perform_web_search, Deps
from dataclasses import dataclass
from typing import Any
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

@dataclass
class RunContext:
    deps: Any
    other_context: Any = None

@pytest.fixture
def mock_deps():
    return Deps(client=AsyncMock(), brave_api_key="test_key")

@pytest.mark.asyncio
async def test_perform_web_search_missing_key():
    deps = Deps(client=AsyncMock(), brave_api_key=None)
    with pytest.raises(ValueError, match="Your Brave API key is missing."):
        await perform_web_search(
            ctx=RunContext(deps=deps),
            query="test"
        )

@pytest.mark.asyncio
async def test_perform_web_search_success(mock_deps):
    mock_response = {"web": {"results": [{"title": "Test Result"}]}}
    mock_deps.client.get.return_value = httpx.Response(
        200,
        json=mock_response
    )
    
    results = await perform_web_search(
        ctx=RunContext(deps=mock_deps),
        query="test query"
    )
    
    mock_deps.client.get.assert_awaited_once_with(
        "https://api.brave.com/v1/search?q=test%20query",
        headers={"Authorization": "Bearer test_key"}
    )
    assert results == mock_response

@pytest.mark.asyncio
async def test_agent_execution(mock_deps):
    mock_response = {"web": {"results": [{"title": "Spain Capital Result"}]}}
    mock_deps.client.get.return_value = httpx.Response(
        200,
        json=mock_response
    )
    
    result = await web_search_agent.run(
        "What is the capital of Spain",
        deps=mock_deps
    )
    
    assert "Spain" in str(result.data)
    assert "capital" in str(result.data)