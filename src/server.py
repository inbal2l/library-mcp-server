#!/usr/bin/env python3
"""
Basic MCP server for fixing library wording for the C++ standards committee.
"""

import asyncio
import logging
from typing import Dict, Any, List

from mcp.server.fastmcp import FastMCP
from mcp.types import TextContent, CallToolResult

# Set up a logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Initialize FastMCP server
mcp = FastMCP("library-mcp-server")

@mcp.tool()
async def hello(name: str = "World") -> str:
    """Sanity check: Say hello to someone or something.
    
    Args:
        name: The name to greet (defaults to "World")
    
    Returns:
        A greeting message
    """
    logger.info(f"was called with: {name}")
    return f"Hello, {name}!"

def main():
    """Run the MCP server."""
    print("Running library wording MCP server...")
    mcp.run(transport="stdio")

if __name__ == "__main__":
    main()
