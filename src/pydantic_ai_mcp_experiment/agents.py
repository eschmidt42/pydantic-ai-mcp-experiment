from typing import Sequence

from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServer, MCPServerStdio
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider

from pydantic_ai_mcp_experiment.data import CityLocation


def get_agents(servers: Sequence[MCPServer]) -> tuple[Agent[None, CityLocation], Agent]:
    model_name = "qwen3:32b"  # you need this on your machine
    ollama_model = OpenAIModel(
        model_name=model_name,
        provider=OpenAIProvider(base_url="http://localhost:11434/v1"),
    )

    city_agent = Agent(ollama_model, output_type=CityLocation, mcp_servers=servers)
    music_agent = Agent(ollama_model, mcp_servers=servers)
    return city_agent, music_agent


def get_stdio_mcp_server() -> MCPServerStdio:
    return MCPServerStdio("uv", args=["run", "server.py", "server"])
