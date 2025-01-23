#!/usr/bin/env python3
"""Pre-gen project hook script

Takes care of setting the correct license file in pyproject.toml.
"""

from pathlib import Path
from shutil import copy


PROJECT_DIR = Path(".")
LICENSE_DIR = PROJECT_DIR.joinpath("licenses")
LICENSES = {{cookiecutter._license_map | jsonify}}
LICENSE_SELECTED = "{{ cookiecutter.license }}"
SELECTED_LICENSE_SOURCE = "{{ cookiecutter.__license_src }}"
SELECTED_LICENSE_DESTINATION = "{{ cookiecutter.__license_dest }}"


def deploy_license() -> None:
    """Move the selected license file into the project root"""
    sources: set[Path] = set()
    for license_option, license_config in LICENSES.items():
        source_path = LICENSE_DIR.joinpath(license_config["source"])
        if license_option == LICENSE_SELECTED:
            destination_path = PROJECT_DIR.joinpath(
                SELECTED_LICENSE_DESTINATION
            )
            copy(source_path, destination_path)
        sources.add(source_path)
    for source in sources:
        source.unlink()
    LICENSE_DIR.rmdir()


if __name__ == "__main__":
    deploy_license()
