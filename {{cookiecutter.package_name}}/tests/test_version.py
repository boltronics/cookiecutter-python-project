"""Version unit tests"""

import unittest

import {{cookiecutter.package_name}}


class VersionTestCase(unittest.TestCase):
    """Version tests"""

    def test_version(self) -> None:
        """check {{cookiecutter.package_name}} exposes a version attribute"""
        self.assertTrue(hasattr({{cookiecutter.package_name}}, "__version__"))
        self.assertIsInstance({{cookiecutter.package_name}}.__version__, str)


if __name__ == "__main__":
    unittest.main()
