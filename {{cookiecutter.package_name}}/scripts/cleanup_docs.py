"""Remove docs build files and generated API docs"""

import shutil
from pathlib import Path

_LITERAL_PATHS = [
    Path("docs/build"),
    Path("docs/source/api/modules.rst"),
]
_GLOB_PATTERNS = [
    ("docs/source/api", "reposcan*.rst"),
]


def clean() -> None:
    """Delete build artefacts and generated API documentation files."""
    for path in _LITERAL_PATHS:
        if path.exists():
            if path.is_dir():
                shutil.rmtree(path)
            else:
                path.unlink()

    for parent_str, pattern in _GLOB_PATTERNS:
        for match in Path(parent_str).glob(pattern):
            match.unlink()


if __name__ == "__main__":
    clean()
