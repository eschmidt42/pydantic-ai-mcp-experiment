from typing import Literal

from mcp.server.fastmcp import FastMCP

server = FastMCP("Best City Server")


@server.tool()
async def get_best_city() -> str:
    """Source for the best city"""
    return "Berlin, Germany"


Musicals = Literal["book of mormon", "cabaret"]


@server.tool()
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
    server.run()
