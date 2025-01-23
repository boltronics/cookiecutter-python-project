"""Quickstart example

This example script imports the {{cookiecutter.package_name}} package and prints out
the version.
"""

import logging

import {{cookiecutter.package_name}}

FORMAT = "%(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)


def main() -> None:
    """Begin execution"""
    logging.info("{{cookiecutter.package_name}} version: %s", {{cookiecutter.package_name}}.__version__)


if __name__ == "__main__":
    main()
