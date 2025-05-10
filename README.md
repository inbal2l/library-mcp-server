# Library MCP Server

A basic MCP server for fixing library wording for the C++ standards committee.

## Installation

### Environment setup
The python MCP server SDK is based on FastMCP package.

The project is provided with a "requirements.txt" file (used in pip package manager (pipreqs) to define dependencies). You can use any package and virtual environment tool (they can use the "requirements.txt" file to generate their own configs).

Described below installation on windows OS using "Power Shell", "python3" and "pip" package manager, search the web for equivalnts for other environments.

#### Virtual Environment Installation

1. Create virtual environment
```bash
python -m venv .venv
```

1. Activate the virtual environment
```bash
.\.venv\Scripts\activate
```

1. Install dependencies from "requirements.txt" file:
```bash
python -m pip install -r requirements.txt
```

## Development (WIP)

### Installing Development Dependencies

In order to debug the server you'll need to install the "mcp[cli]" python package (and possibly node, npx and uv).

Once installed, the server can be run on localhost using:
```bash
mcp dev src\server.py
```

```bash
# Install the package and its dependencies
pip install -e .
```

```bash
# Install development dependencies
pip install -e ".[test]"
```

### Running Tests

To run the unit tests, you can use pytest directly:

```bash
# Run all tests
pytest tests/

# Run only unit tests
pytest tests/unit/

# Run with verbose output
pytest -v tests/unit/
```

Alternatively, you can use the provided test runner script:

```bash
# Run all tests
python run_tests.py

# Run only unit tests
python run_tests.py --unit

# Run only functional tests
python run_tests.py --functional

# Run with verbose output
python run_tests.py -v
```

## Usage

#### Step I: Verify Environment is set

1. Follow instructions under: "Virtual Environment Installation" to set up venv.
2. From within venv, run the "src\server.py" file to verify env set up correctly:
```bash
python -m src.server
```
You should see in terminal:
```bash
Init library-mcp-server module...
Running library wording MCP server...
```

#### Step II: Set up MCP server using Cline VSCode extension

Clone the project and follow instractions for configuring "installed" (local) MCP Servers, described here: https://docs.cline.bot/mcp-servers/configuring-mcp-servers
