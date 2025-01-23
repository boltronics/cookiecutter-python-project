"""
To avoid bit-rot in the examples they are tested as part of the unit tests
suite.
"""

import logging
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

        if os.name == "nt":
            # Windows
            activate_cmd = f"{VENV_DIR}\\Scripts\\activate"
            args = shlex.split(
                f'cmd.exe /c "{activate_cmd} && python {filename}"'
            )
        else:
            # Unix-like systems
            activate_cmd = f"source {VENV_DIR}/bin/activate"
            args = shlex.split(
                f'sh -c "{activate_cmd} && python {filename}"'
            )

        env: dict[str, str] = {}
        if os.environ.get("PATH"):
            env["PATH"] = os.environ["PATH"]
        if "LD_LIBRARY_PATH" in os.environ:
            env["LD_LIBRARY_PATH"] = os.environ["LD_LIBRARY_PATH"]

        if popen_kwargs is None:
            popen_kwargs = {}

        popen_default_kwargs: dict[str, Any] = {
            "env": env,
            "cwd": script_dir,
            "timeout": timeout,
            "stdout": subprocess.PIPE,
            "stderr": subprocess.PIPE,
        }
        popen_default_kwargs.update(popen_kwargs)

        try:
            subprocess.run(args, **popen_default_kwargs, check=True)
            return True
        except subprocess.CalledProcessError as error:
            logging.error("Error: %s", error)
            if error.stdout:
                logging.error("stdout: %s", error.stdout.decode())
            if error.stderr:
                logging.error("stderr: %s", error.stderr.decode())
            return False
        finally:
            os.chdir(original_cwd)

    def test_quickstart_example(self) -> None:
        """check quickstart example"""
        assert (
            self.run_in_venv(os.path.join("examples", "quickstart.py")) is True
        )


if __name__ == "__main__":
    unittest.main()
