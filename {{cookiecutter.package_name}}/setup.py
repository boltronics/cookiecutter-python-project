import re
from pathlib import PurePath
from setuptools import setup

regexp = re.compile(r".*__version__ = [\'\"](.*?)[\'\"]", re.S)

base_package = "{{cookiecutter.package_name}}"
base_path = PurePath(__file__).parent

init_file = PurePath(base_path).joinpath(
    "{{cookiecutter.package_name}}", "__init__.py"
)
with open(init_file, "r", encoding="utf-8") as f:
    module_content = f.read()

    match = regexp.match(module_content)
    if match:
        version = match.group(1)
    else:
        raise RuntimeError(f"Cannot find __version__ in {init_file}")

with open("README.rst", "r", encoding="utf-8") as f:
    readme = f.read()

with open("CHANGELOG.rst", "r", encoding="utf-8") as f:
    changes = f.read()


def parse_requirements(filename):
    """Load requirements from a pip requirements file"""
    with open(filename, "r", encoding="utf-8") as fd:
        lines = []
        for line in fd:
            line.strip()
            if line and not line.startswith("#"):
                lines.append(line)
    return lines


requirements = parse_requirements("requirements.txt")


if __name__ == "__main__":
    setup(
        name="{{cookiecutter.package_name}}",
        description="{{cookiecutter.package_short_description}}",
        long_description="\n\n".join([readme, changes]),
        license="{{cookiecutter.license}}",
        url="https://github.com/{{cookiecutter.github_user_name}}/{{cookiecutter.github_repo_name}}",
        version=version,
        author="{{cookiecutter.full_name}}",
        author_email="{{cookiecutter.email}}",
        maintainer="{{cookiecutter.full_name}}",
        maintainer_email="{{cookiecutter.email}}",
        install_requires=requirements,
        keywords=["{{cookiecutter.package_name}}"],
        packages=["{{cookiecutter.package_name}}"],
        zip_safe=False,
        # https://pypi.org/classifiers/
        classifiers=[
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
        ],
    )
