"""Script to be run that creates the mcp client and handles the mcp server in a subprocess.

Run using (with your venv active)

    python client.py

References

* pydantic + ollama: https://ai.pydantic.dev/models/openai/#example-local-usage
* pydantic ai + mcp + "stdio" server: https://ai.pydantic.dev/mcp/client/#mcp-stdio-server
* logfire setup: https://logfire.pydantic.dev/docs/#logfire - requires account creation
* logfire with otel-tui backend: https://ai.pydantic.dev/logfire/#logfire-with-an-alternative-otel-backend -> does not show the prompts and responses (despite them being present in the screenshots in the docs)
"""

import asyncio

import logfire

from pydantic_ai_mcp_experiment.agents import get_agents
from pydantic_ai_mcp_experiment.servers import get_http_mcp_server

logfire.configure()
logfire.instrument_pydantic_ai()

# server run with uvicorn and fastapi
server = get_http_mcp_server()

city_agent, music_agent = get_agents("qwen3:32b", [server])


async def main():
    async with city_agent.run_mcp_servers():
        result = await city_agent.run(
            "What's the best city? Please use available tools."
        )
    print(f"best city: {result.output}")

    async with music_agent.run_mcp_servers():
        result = await music_agent.run(
            "Please return a cabaret musical greeting. Please use available tools."
        )
    print(f"greeting: {result.output}")


if __name__ == "__main__":
    asyncio.run(main())
