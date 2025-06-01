# PydanticAI MCP Experiment

Under `examples/` are different configurations providing an MCP client and server using `pydantic_ai` and local models / ollama to get your hands dirty and tinker.

## Setup

    uv sync

## Examples

### `examples/subprocess

Run using (with your venv active)

    cd examples/subprocess
    python client.py

This will prompt you to authenticate with logfire. If you want to use another backend, e.g. `otel-tui`, you can with a caveat, see the references below.



## References

* pydantic + ollama: https://ai.pydantic.dev/models/openai/#example-local-usage
* pydantic ai + mcp + "stdio" server: https://ai.pydantic.dev/mcp/client/#mcp-stdio-server
* logfire setup: https://logfire.pydantic.dev/docs/#logfire - requires account creation
* logfire with otel-tui backend: https://ai.pydantic.dev/logfire/#logfire-with-an-alternative-otel-backend -> does not show the prompts and responses (despite them being present in the screenshots in the docs)
