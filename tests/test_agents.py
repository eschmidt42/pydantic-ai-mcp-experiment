"""Testing examples/subprocess flow.

Reference: https://ai.pydantic.dev/testing/#overriding-model-via-pytest-fixtures
"""

import pytest
from pydantic_ai import models
from pydantic_ai.models.test import TestModel

from pydantic_ai_mcp_experiment.agents import get_agents
from pydantic_ai_mcp_experiment.data import CityLocation

city_agent, music_agent = get_agents("qwen3:32b", [])

# -------------------
# Fixtures
# -------------------


@pytest.fixture(autouse=True)
def block_real_model_requests():
    """Globally block any real model requests during tests."""
    models.ALLOW_MODEL_REQUESTS = False
    yield
    # Restore for future tests (if needed)
    models.ALLOW_MODEL_REQUESTS = True


@pytest.fixture
def override_models():
    """Replace the model in both agents with TestModel."""
    with city_agent.override(model=TestModel()):
        with music_agent.override(model=TestModel()):
            yield


# -------------------
# Tests
# -------------------
@pytest.mark.asyncio
async def test_city_agent(override_models):
    result = await city_agent.run("What's the best city?")
    assert isinstance(result.output, CityLocation)


@pytest.mark.asyncio
async def test_music_agent(override_models):
    result = await music_agent.run("Please return a cabaret musical greeting.")
    assert isinstance(result.output, str)
