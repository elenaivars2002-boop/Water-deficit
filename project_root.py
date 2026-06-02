"""Find thesis project root from any notebook under notebooks/ (including subfolders)."""

from __future__ import annotations

from pathlib import Path


def find_project_root(start: Path | None = None) -> Path:
    """
    Walk upward from *start* (default: cwd) until ``data/csv_estream`` exists.
    Works from ``notebooks/``, ``notebooks/single_basin_running/``, etc.
    """
    start = (start or Path.cwd()).resolve()
    for path in [start, *start.parents]:
        if (path / "data" / "csv_estream").is_dir():
            return path
    raise FileNotFoundError(
        f"Project root not found (started at {start}). "
        "Open the notebook from the thesis project and run SETUP."
    )
