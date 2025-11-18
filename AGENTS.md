# Repository Guidelines

This repository contains the `data_storage` MCP server. Keep changes minimal, well-tested, and aligned with the existing CLI and process-management behavior.

## Project Structure & Modules
- Core server logic: `server.py` (CLI commands, protocol handling, MCP tools).
- Tests: `test_server.py` using `unittest`.
- Dependency and tooling files: `requirements.txt`, `data_storage_server.spec`.
- Scripts: `setup.ps1`, `build.ps1`, `run.ps1`, `manage-server.ps1`, plus `.bat` equivalents for Windows.

## Build, Test, and Development Commands
- Setup environment: `.\setup.ps1` (installs dependencies and configures a venv).
- Run server for development: `python server.py start` (default stdio protocol).
- Build executable: `.\build.ps1` (creates `dist\data_storage-mcp-server.exe`).
- Run tests: `python test_server.py` or `python -m unittest`.

## Coding Style & Naming
- Python: 4-space indentation, type hints where practical, and concise docstrings.
- Keep CLI entrypoints and process management in `server.py`; add new MCP tools using the `@mcp.tool()` pattern already present.
- Name files and classes descriptively (e.g., `TestDataStorageServer`, `start_server`, `stop_server`).

## Testing Guidelines
- Add or update tests in `test_server.py` (or new `test_*.py` files) for any new behavior.
- Prefer small, focused test methods with descriptive names (e.g., `test_start_creates_pid_file`).
- Before opening a PR, run `python test_server.py` and ensure all tests pass.

## Commit & Pull Request Guidelines
- Use clear, imperative commit messages (e.g., `Add SSE protocol health check`).
- PRs should describe the change, motivation, and any protocol/CLI impact.
- Include how you tested the change and any relevant command examples (`python server.py ...`).

## Agent-Specific Instructions
- Preserve existing behavior and public CLI (`start`, `stop`, `status`, `ping`, `version`, `help`).
- Do not change script interfaces (`setup.ps1`, `build.ps1`, `manage-server.ps1`) unless explicitly required.
- When in doubt, mirror patterns already used in `server.py` and `test_server.py`.

