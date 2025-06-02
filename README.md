# PydanticAI MCP Experiment
> Minimalist examples to provide your own MCP servers to your local llm models.

Under `examples/` are different configurations providing an MCP client and server using `pydantic_ai` and local models / ollama to get your hands dirty and tinker.

## Setup

This project is [uv](https://docs.astral.sh/uv/getting-started/) managed. So to set up run

    uv sync

## Examples

There are 4 different examples for running a MCP server (locally) via:

* Stdio -> `examples/0_subprocess`
* HTTP
  * `mcp.run` -> `examples/1_http_mcp_run`
  * FastAPI -> `examples/2_http_fastapi`
  * Starlette -> `examples/3_http_starlette`

Each folder contains a `client.py` and `server.py` file.

The servers should be started before running the `client.py` file.

The scripts are set up such that when you change into the respective example folder you can run each simply using

    python server.py

and

    python client.py

## Logging

Since `pydantic_ai` is used here the natural choice for logging is `logfire`. Hence upon running the `client.py` files you will be asked to authenticate with logfire. You can change the backend to something like [`otel-tui`](https://ai.pydantic.dev/logfire/#logfire-with-an-alternative-otel-backend), but I tried and failed to find the prompt and response messages I wanted to see.


## References

* pydantic + ollama: https://ai.pydantic.dev/models/openai/#example-local-usage
* pydantic ai + mcp + "stdio" server: https://ai.pydantic.dev/mcp/client/#mcp-stdio-server
* logfire setup: https://logfire.pydantic.dev/docs/#logfire - requires account creation
* logfire with otel-tui backend: https://ai.pydantic.dev/logfire/#logfire-with-an-alternative-otel-backend -> does not show the prompts and responses (despite them being present in the screenshots in the docs)
