"""mcp.run HTTP version of the MCP server.

Run using

    python server.py
"""

from typing import Literal

from mcp.server.fastmcp import FastMCP

from pydantic_ai_mcp_experiment.servers import PORT

mcp = FastMCP(
    "MCP Run Server",
    port=PORT,  # set this here if mcp.run used below instead of uvicorn
)


@mcp.tool()
async def get_best_city() -> str:
    """Source for the best city"""
    return "Berlin, Germany"


Musicals = Literal["book of mormon", "cabaret"]


@mcp.tool()
async def get_musical_greeting(musical: Musicals) -> str:
    """Source for a musical greeting"""
    match musical:
        case "book of mormon":
            return "Hello! My name is Elder Price And I would like to share with you The most amazing book."
        case "cabaret":
            return "Willkommen, bienvenue, welcome! Fremde, étranger, stranger. Glücklich zu sehen, je suis enchanté, Happy to see you, bleibe reste, stay."
        case _:
            raise ValueError


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
