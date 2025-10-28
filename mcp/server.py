from fastmcp import FastMCP

mcp = FastMCP("Test Server")

@mcp.tool
def greet(name: str) -> str:
	return f"Hello, {name}!"

if __name__ == "__main__":
	# mcp.run()
	mcp.run(transport="http", port = 8000)

