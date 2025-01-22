"""
To avoid bit-rot in the examples they are tested as part of the unit tests
suite.
"""

import os
import shlex
import subprocess
import unittest
from typing import Any

# Use the current virtual environment when executing the example scripts.
VENV_DIR = os.environ.get("VIRTUAL_ENV")

REPO_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


@unittest.skipIf(
    VENV_DIR is None, "VIRTUAL_ENV environment variable is not set"
)
class ExamplesTestCase(unittest.TestCase):
    """Check example scripts function.

    This test case assumes it is running in a virtual environment. The same
    virtual environment is activated prior to running the example script
    in a subprocess.
    """

    def run_in_venv(
        self,
        filepath: str,
        timeout: float = 5,
        popen_kwargs: dict[str, Any] | None = None,
    ) -> bool:
        """Run a Python script in a virtual env in a subprocess.

        filepath references must be relative to the repo root directory.
        """
        original_cwd = os.getcwd()
        script_dir = os.path.join(REPO_DIR, os.path.dirname(filepath))
        filename = os.path.basename(filepath)
        args = shlex.split(
            (
                f'/bin/bash -c "source {VENV_DIR}/bin/activate '
                f'&& python {filename}"'
            )
        )

        env = {}
        if os.environ["PATH"]:
            env["PATH"] = os.environ["PATH"]
        if "LD_LIBRARY_PATH" in os.environ:
            env["LD_LIBRARY_PATH"] = os.environ["LD_LIBRARY_PATH"]

        if popen_kwargs is None:
            popen_kwargs = {}

        popen_default_kwargs = {
            "env": env,
            "stdout": subprocess.PIPE,
            "stderr": subprocess.PIPE,
            "shell": False,
        }

        try:
            os.chdir(script_dir)
            with subprocess.Popen(
                args=args,
                **{**popen_default_kwargs, **popen_kwargs},
            ) as proc:
                _out, _err = proc.communicate(timeout=timeout)
                returncode = proc.returncode
        finally:
            os.chdir(original_cwd)

        return returncode == 0

    def test_quickstart_example(self) -> None:
        """check quickstart example"""
        assert (
            self.run_in_venv(os.path.join("examples", "quickstart.py")) is True
        )


if __name__ == "__main__":
    unittest.main()
