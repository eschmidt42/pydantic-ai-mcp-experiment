from typing import Literal, Sequence

from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServer
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider

from pydantic_ai_mcp_experiment.data import CityLocation

LocalToolModels = Literal["qwen3:32b", "llama3.1:8b"]


def get_agents(
    model_name: LocalToolModels, servers: Sequence[MCPServer]
) -> tuple[Agent[None, CityLocation], Agent]:
    """
    Note: you need a model with name `model_name` available in ollama on your machine.
    """

    ollama_model = OpenAIModel(
        model_name=model_name,
        provider=OpenAIProvider(base_url="http://localhost:11434/v1"),
    )

    city_agent = Agent(ollama_model, output_type=CityLocation, mcp_servers=servers)
    music_agent = Agent(ollama_model, mcp_servers=servers)
    return city_agent, music_agent
