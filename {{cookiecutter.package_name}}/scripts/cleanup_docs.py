"""Remove docs build files and generated API docs"""

import shutil
from pathlib import Path

paths = [
    "docs/build",
    "docs/source/api/modules.rst",
    "docs/source/api/{{cookiecutter.package_name}}*.rst",
]

for path in paths:
    p = Path(path)
    if p.exists():
        if p.is_dir():
            shutil.rmtree(p)
        else:
            p.unlink()
