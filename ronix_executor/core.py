"""Core logic for managing Roblox executor scripts.

This module does not perform any injection into Roblox; it simply tracks and
executes Lua scripts locally so users can organize their library before using
an external injector.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List


@dataclass
class Script:
    """Represents a Roblox Lua script on disk."""

    name: str
    path: Path

    def load(self) -> str:
        """Return the contents of the script."""
        return self.path.read_text(encoding="utf-8")


class ScriptManager:
    """Manage a collection of Lua scripts for Roblox executors."""

    def __init__(self, scripts_dir: Path | str = "ronix_executor/scripts") -> None:
        self.scripts_dir = Path(scripts_dir)
        self.scripts_dir.mkdir(parents=True, exist_ok=True)

    def list_scripts(self) -> List[Script]:
        """Return all scripts available in the scripts directory."""
        scripts: Iterable[Path] = sorted(self.scripts_dir.glob("*.lua"))
        return [Script(path.stem, path) for path in scripts]

    def add_script(self, name: str, content: str) -> Script:
        """Create a new script with the provided name and content."""
        sanitized = name.replace(" ", "_")
        target = self.scripts_dir / f"{sanitized}.lua"
        target.write_text(content, encoding="utf-8")
        return Script(sanitized, target)

    def run_script(self, name: str) -> str:
        """Return the script contents to be executed by an external injector.

        This method does not interact with Roblox directly; instead it returns
        the script body so callers can pipe it into their preferred injector.
        """

        script = next((s for s in self.list_scripts() if s.name == name), None)
        if script is None:
            available = ", ".join(s.name for s in self.list_scripts()) or "none"
            raise FileNotFoundError(
                f"Script '{name}' not found. Available scripts: {available}"
            )
        return script.load()

    def ensure_sample(self) -> Script:
        """Create a sample script if the folder is empty and return it."""
        scripts = self.list_scripts()
        if scripts:
            return scripts[0]
        return self.add_script(
            "hello_world",
            """-- Ronix sample script\nprint("Hello from Ronix executor!")\n""",
        )
