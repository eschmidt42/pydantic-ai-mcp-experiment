"""Uvicorn + FastAPI version of the MCP server.

Run using (with your venv active)

    python server.py

References

* https://github.com/modelcontextprotocol/python-sdk?tab=readme-ov-file#mounting-to-an-existing-asgi-server
* https://github.com/modelcontextprotocol/python-sdk?tab=readme-ov-file#streamable-http-transport
"""

import contextlib
from typing import Literal

import uvicorn
from fastapi import FastAPI
from mcp.server.fastmcp import FastMCP

from pydantic_ai_mcp_experiment.servers import PORT

mcp = FastMCP(
    "FastAPI MCP Server",
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


@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    async with contextlib.AsyncExitStack() as stack:
        await stack.enter_async_context(mcp.session_manager.run())
        yield


app = FastAPI(lifespan=lifespan)
app.mount("/", mcp.streamable_http_app())


if __name__ == "__main__":
    uvicorn.run(app, port=PORT)
