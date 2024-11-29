#!/usr/bin/env python3
"""Pre-gen project hook script

Takes care of deploying the correct license file.
"""

import json
from pathlib import Path

PROJECT_DIR = Path(".")
LICENSE_DIR = PROJECT_DIR.joinpath("licenses")
LICENSE_CONFIG = LICENSE_DIR.joinpath("config.json")
LICENSE_SELECTED = "{{ cookiecutter.license }}"


def deploy_license() -> None:
    """Move the selected license file into the project root

    Licenses not selected for the project are removed.
    """
    sources: set[Path] = set()
    selected_source = None
    with LICENSE_CONFIG.open(mode="r", encoding="utf-8") as config_file:
        config = json.load(config_file)
        for license_option, license_data in config.items():
            source_path = LICENSE_DIR.joinpath(license_data["source"])
            if license_option == LICENSE_SELECTED:
                selected_source = source_path
                destination_path = PROJECT_DIR.joinpath(license_data["destination"])
                source_path.rename(destination_path)
                sources.discard(source_path)
            elif license_data["source"] != selected_source:
                sources.add(source_path)
        for source in sources:
            source.unlink()
    LICENSE_CONFIG.unlink()
    LICENSE_DIR.rmdir()


if __name__ == "__main__":
    deploy_license()
