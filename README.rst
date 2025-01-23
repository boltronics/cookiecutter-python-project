Cookiecutter Python Project
###########################

This project contains a Cookiecutter template that helps you create new Python
3.11+ package projects by automatically generating most of the boiler plate
content for you.

Cookiecutter is a command-line utility that creates projects from templates.
Cookiecutter lets you to easily and quickly bootstrap a new project from a
template which allows you to skip all manual setup and common mistakes when
starting a new project.

Cookiecutter takes a source directory tree and copies it into your new project.
It replaces all the names that it finds surrounded by templating tags ``{{``
and ``}}`` with names that it finds in the file ``cookiecutter.json``.

The Python project structure produced by this Cookiecutter template contains
the following items:

- A minimal README.rst file.
- A (non-essential) Makefile that taps into a Hatch project manager
  setup to automate many common developer tasks, such as:

  - The usage of virtual environments.
  - Checking and formatting code style with ``black`` and ``isort``.
  - Performing static analysis checks with ``pylint``.
  - Performing type checking with ``mypy``.
  - Running unit tests with ``pytest``/``unittest``.
  - Checking code coverage with ``coverage``.
  - Generating documentation with ``Sphinx``.
  - Generating, testing and uploading a project release to PyPI.

- A ``pyproject.toml`` file used to manage nearly all project configuration.
- A ``CONTRIBUTING.rst`` guide. On GitHub this file is shown when sending
  a pull request or an issue. This file also gets included in the generated
  developer documentation.
- An empty ``CHANGELOG.rst`` file. This file gets included in the user
  documentation.
- An optional ``LICENSE`` file (or ``COPYING`` for GNU licenses).
- An ``examples`` directory with a minimal quickstart example script. This
  script imports the package and prints the package version. It is also
  called by the unit test suite to ensure it always works.
- A ``tests`` directory containing a basic unit test and a shell
  script that can be used to test a wheel distribution of the package.
- A GitHub Actions continuous integration configuration.
- A ``docs`` directory with pre-configured Sphinx documentation containing:

  - A minimal ``index.rst`` page

  - A user focused page containing information such as installation
    instructions, API docs, a link to the change log and instructions
    about how to raise a bug.

  - A developer focused page containing information such as contributing,
    testing, code coverage, style compliance, type annotations and
    documentation.

It is assumed that the new Python package will eventually be:

- hosted on GitHub (or perhaps GitLab)
- published to PyPI
- linked to ReadTheDocs.

The generated docs have some references and links to those sites.


Getting Started
===============

One Time Setup Steps
--------------------

The process for using Cookiecutter to create a new Python package project
starts with installing Cookiecutter. This is best done by creating a new
virtual environment specifically for cookiecutter and then installing
cookiecutter using ``pip``. The example below shows how to do this.

.. code-block:: console

    $ python -m venv --prompt cc ccvenv
    $
    $ source ccvenv/bin/activate
    $ # or for cmd.exe:
    $ # ccvenv\Scripts\activate.bat
    $ # or for PowerShell:
    $ # ccvenv\Scripts\Activate.ps1
    $
    (cc) $ pip install -U pip  # update pip to avoid any warnings
    (cc) $ pip install cookiecutter

If you do not yet have Hatch installed, now would be a good time to do
so. Refer to the installation instructions for your operating system
`here <https://hatch.pypa.io/latest/install/>`_.

It may also be a good idea to ensure you have ``git`` installed (and
it may be required for cookiecutter to function if using it to clone
this template). Under Windows, you can use `winget
<https://learn.microsoft.com/en-us/windows/package-manager/winget/>`_.

.. code-block:: console

    (cc) $ winget install --id Git.Git --exact --source winget

Under macOS you can use `brew <https://brew.sh/>`_.

.. code-block:: console

    (cc) $ brew install git

Users of other operating systems likely already have it installed or
will be able to install it via their operating system's package
manager.

If you wish to use the fancy Makefile included in this project, which
is entirely optional, you may wish to install the ``make``
command. Under Windows, again using winget:

.. code-block:: console

    (cc) $ winget install --id GnuWin32.Make --exact --source winget

Unlike with git, you will need to `manually add
<https://stackoverflow.com/a/44272417/8243194>`_ the directory
containing ``make.exe`` to your PATH, which is typically something like:
``C:\Program Files(x86)\GnuWin32\bin\``.

Under macOS you can again use brew.

.. code-block:: console

    (cc) $ brew install make

Users of other operating systems should again have no trouble finding
it in their operating system's package manager.

You are now ready to create a new Python project from the Cookiecutter
template provided by this project.


Create a new project
--------------------

To create a new Python package project based on this cookiecutter template
simply navigate to a directory where you want to create the new project, then
run the ``cookiecutter`` command with a command line argument referencing this
template.

The easiest method is to reference this template via its GitHub URL (where 'gh'
is a shortened form for GitHub):

.. code-block:: console

    (cc) $ cookiecutter gh:boltronics/cookiecutter-python-project

Alternatively, if you have cloned a local copy of this template you can
reference it directly:

.. code-block:: console

    (cc) $ cookiecutter path/to/cookiecutter-python-project

You will be prompted for user input to configure the project. Prompts are the
keys in 'cookiecutter.json' and default responses are the values. Prompts are
shown in order.

Once you have generated your new Python package project you can exit the
cookiecutter virtual environment as it is no longer required.

.. code-block:: console

    (cc) $ deactivate
    $


Manual Modifications
--------------------

Some aspects of generating a project in a generic approach are not practical
to completely automate so there may be a few steps remaining before you begin
using the new project.

- If you do not plan to publish project artifacts at GitHub, PyPI or
  ReadTheDocs then remove any links to those sites. Affected files are:

  - README.rst (references to PyPI and ReadTheDocs)
  - docs/source/index.rst (references to PyPI)
  - pyproject.toml (references to GitHub and ReadTheDocs under
    the `[project.urls]` section)

- Update any additional useful classifiers in ``pyproject.toml``. The
  list of available classifiers can be found `here
  <https://pypi.python.org/pypi?:action=list_classifiers>`_.


Example
=======

Below is an example showing exactly how to create a new Python project using
the template in this project. In this scenario the project is called
``abc 123`` and the Python package is called ``abc_123``.

It is assumed that you have performed the actions outlined in the One Time
Setup Steps section above which provides a virtual environment with
cookiecutter installed into it.

After running the cookiecutter command and passing it a reference to this
template, the first question it asks for is the package display name. This is
the human friendly label that will be used in docs to refer to the project. It
is also used to create the package name so it should not contain special
characters that are invalid when used in a Python attribute. It can have spaces
and hyphens in it. The package display name is first converted to lowercase
text and then any spaces or hyphens are converted to underscores to produce a
Python package name.

.. code-block:: console

    (cc) $ cookiecutter gh:boltronics/cookiecutter-python-project
    [1/10] package_display_name (Package-Name): abc 123
    [2/10] package_name (abc_123):
    [3/10] package_short_description (A description of the package): This is my abc 123 package.
    [4/10] version (0.0.1):
    [5/10] full_name (Your Name): First Last
    [6/10] email ():
    [7/10] github_user_name (GithubUserName): flast
    [8/10] github_repo_name (abc_123):
    [9/10] Select license
      1 - Not licensed for distribution (no license)
      2 - AGPL-3.0-only
      3 - AGPL-3.0-or-later
      4 - Apache-2.0
      5 - BSD-3-Clause
      6 - GPL-2.0-only
      7 - GPL-2.0-or-later
      8 - GPL-3.0-only
      9 - GPL-3.0-or-later
      Choose from [1/2/3/4/5/6/7/8/9] (1): 9
    [10/10] year (2025):

The project has been created in the ``abc_123`` directory.

.. code-block:: console

    $ cd abc_123

If you are planning to use git, it might be a good idea to create a
new repository at this point.

.. code-block:: console

    $ git init
    $ git add .
    $ git commit -m 'Initial cookiecutter-python-project setup'

With that out of the way, it will be easy to use git to undo any
potential mistakes made while experimenting.

We can now kick the tires of this new project by performing some initial
project checks.

First, let's enter a project-specific virtual environment. Hatch
will install any of the project's dependencies (if added to pyproject.toml) as well as
the project itself as an editable package.

.. code-block:: console

    $ hatch shell
    (abc_123) $

You can exit the environment by typing `exit` or using the Ctrl+d shortcut.

Now that we have a virtual environment we can check the remaining convenience
functions provided by the Makefile.

There are a number of other virtual environments available to you, and
most of these have their own packages and scripts to ease
development. You can bring up a summary like so:

.. code-block:: console

    $ hatch env show
                            Standalone
    ┏━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
    ┃ Name     ┃ Type    ┃ Dependencies ┃ Scripts              ┃
    ┡━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
    │ default  │ virtual │              │                      │
    ├──────────┼─────────┼──────────────┼──────────────────────┤
    │ coverage │ virtual │ coverage     │ run-coverage         │
    │          │         │              │ run-coverage-erase   │
    │          │         │              │ run-coverage-html    │
    │          │         │              │ run-coverage-report  │
    │          │         │              │ run-coverage-tests   │
    │          │         │              │ run-coverage-verbose │
    │          │         │              │ run-new-reports      │
    │          │         │              │ run-reports          │
    ├──────────┼─────────┼──────────────┼──────────────────────┤
    │ docs     │ virtual │ sphinx       │ build                │
    │          │         │              │ build-dummy          │
    ├──────────┼─────────┼──────────────┼──────────────────────┤
    │ lint     │ virtual │ pylint       │ check                │
    ├──────────┼─────────┼──────────────┼──────────────────────┤
    │ style    │ virtual │ black        │ check                │
    │          │         │ flake8       │ format               │
    │          │         │ isort        │ run-black            │
    │          │         │              │ run-black-check      │
    │          │         │              │ run-flake8           │
    │          │         │              │ run-isort            │
    │          │         │              │ run-isort-check      │
    ├──────────┼─────────┼──────────────┼──────────────────────┤
    │ types    │ virtual │ mypy         │ check                │
    └──────────┴─────────┴──────────────┴──────────────────────┘
    $

You can enter use these virtual environments like so:

.. code-block:: console

    $ hatch shell types
    (types) $ pip freeze
    # Editable Git install with no remote (abc_123==0.0.1)
    -e /home/abolte/tmp/cookiecutter-testing/abc_123
    mypy==1.14.1
    mypy-extensions==1.0.0
    typing_extensions==4.12.2
    (types) $ exit
    $ hatch run types:check
    Success: no issues found in 4 source files
    $

In other words, `hatch run ENV:SCRIPT` (replacing *ENV* with something
from the Name column in the above table, and *SCRIPT* likewise with
something from the Scripts column) will allow various tools to be
executed in a clean environment.

By splitting the tools out into separate environments, we save time by
only installing packages that we actually need.

Take a look at the pyproject.toml configuration file to see precisely
what each script does, and make any adjustments as desired. You can
also define environments with one or more different versions of Python
to run tests or for development. See the Hatch documentation on
`matrices <https://hatch.pypa.io/1.9/environment/#matrix>`_ for
details.

If you have make installed, the included Makefile provides handy
shortcuts for various Hatch commands and the configured scripts. You
can print a summary of options via the `make help` command, like so:

.. code-block:: console

    $ make help

    abc 123 Makefile help

    help                           - display makefile help information
    venv                           - enter a dev virtual environment
    clean                          - clean all files using .gitignore rules
    scrub                          - clean all files, even untracked files
    test                           - run tests
    test-verbose                   - run tests [verbosely]
    coverage                       - perform test coverage checks
    format                         - perform code style format
    check-format                   - check code format compliance
    sort-imports                   - apply import sort ordering
    check-sort-imports             - check imports are sorted
    style                          - perform code style format
    check-style                    - check code style compliance
    check-types                    - check type hint annotations
    check-lint                     - run static analysis checks
    check-static-analysis          - check code style compliance
    docs                           - generate project documentation
    check-docs                     - quick check docs consistency
    serve-docs                     - serve project html documentation
    dist                           - create a wheel distribution package
    dist-test                      - test a wheel distribution package
    dist-upload                    - upload a wheel distribution package


Here is an example of one in action:

.. code-block:: console

    $ make test-verbose
    ────────────────────────────── hatch-test.py3.13 ───────────────────────────────
    ============================= test session starts ==============================
    platform linux -- Python 3.13.1, pytest-8.3.4, pluggy-1.5.0 -- venvs/hatch-test.py3.13/bin/python3
    cachedir: .pytest_cache
    rootdir: /abc_123
    configfile: pyproject.toml
    plugins: mock-3.14.0, rerunfailures-14.0, xdist-3.6.1
    collected 2 items

    tests/test_examples.py::ExamplesTestCase::test_quickstart_example PASSED [ 50%]
    tests/test_version.py::VersionTestCase::test_version PASSED              [100%]

    ============================== 2 passed in 0.09s ===============================
    ────────────────────────────── hatch-test.py3.12 ───────────────────────────────
    ============================= test session starts ==============================
    platform linux -- Python 3.12.8, pytest-8.3.4, pluggy-1.5.0 -- venvs/hatch-test.py3.12/bin/python3
    cachedir: .pytest_cache
    rootdir: /abc_123
    configfile: pyproject.toml
    plugins: mock-3.14.0, rerunfailures-14.0, xdist-3.6.1
    collected 2 items

    tests/test_examples.py::ExamplesTestCase::test_quickstart_example PASSED [ 50%]
    tests/test_version.py::VersionTestCase::test_version PASSED              [100%]

    ============================== 2 passed in 0.09s ===============================
    ────────────────────────────── hatch-test.py3.11 ───────────────────────────────
    ============================= test session starts ==============================
    platform linux -- Python 3.11.11, pytest-8.3.4, pluggy-1.5.0 -- venvs/hatch-test.py3.11/bin/python3
    cachedir: .pytest_cache
    rootdir: /abc_123
    configfile: pyproject.toml
    plugins: mock-3.14.0, rerunfailures-14.0, xdist-3.6.1
    collected 2 items

    tests/test_examples.py::ExamplesTestCase::test_quickstart_example PASSED [ 50%]
    tests/test_version.py::VersionTestCase::test_version PASSED              [100%]

    ============================== 2 passed in 0.08s ===============================

    Skipped 3 incompatible environments:
    hatch-test.py3.10 -> cannot locate Python: 3.10
    hatch-test.py3.9 -> cannot locate Python: 3.9
    hatch-test.py3.8 -> cannot locate Python: 3.8
    Combined data file .coverage.dragon.311786.XZHVzPhx
    Combined data file .coverage.dragon.311791.XRWZtnFx
    Skipping duplicate data .coverage.dragon.311797.XTgleYIx
    Name                      Stmts   Miss Branch BrPart  Cover
    -----------------------------------------------------------
    src/abc_123/__init__.py       1      0      0      0   100%
    -----------------------------------------------------------
    TOTAL                         1      0      0      0   100%
    $


Suggestions? Contributions? Problems?
=====================================

Please open an Issue or a Pull Request! I'm open to hearing any
suggestions.
