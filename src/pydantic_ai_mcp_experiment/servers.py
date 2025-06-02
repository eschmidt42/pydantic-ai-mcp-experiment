from pydantic_ai.mcp import MCPServerHTTP, MCPServerStdio

PORT = 3001


def get_stdio_mcp_server() -> MCPServerStdio:
    return MCPServerStdio("uv", args=["run", "server.py", "server"])


def get_http_mcp_server(port: int = PORT) -> MCPServerHTTP:
    return MCPServerHTTP(url=f"http://localhost:{port}/mcp")
