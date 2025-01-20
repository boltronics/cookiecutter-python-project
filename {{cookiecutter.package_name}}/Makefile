# This makefile has been created to help developers perform common actions.
# Most actions assume it is operating in a virtual environment where the
# python command links to the appropriate virtual environment Python.

MAKEFLAGS += --no-print-directory
GIT := $(shell command -v git)


define CHECK_GIT
$(if $(GIT),,$(error "git command not available."))
$(if $(wildcard .git),,$(error "Not a git repository."))
endef


# Do not remove this block. It is used by the 'help' rule when
# constructing the help output.
# help:
# help: {{cookiecutter.package_display_name}} Makefile help
# help:


# help: help                           - display makefile help information
.PHONY: help
help:
	@grep "^#\shelp:" Makefile | \
		grep -v grep | \
		sed 's/\# help\: //' | \
		sed 's/\# help\://'


# help: venv                           - create a dev virtual environment
PIP_CMDS = \
	source venv/bin/activate && \
	pip install -U pip && \
	pip install -e .[dev]
.PHONY: venv
venv:
	@rm -Rf venv
	@python3 -m venv venv --prompt {{cookiecutter.package_name}}
	/bin/bash -c "${PIP_CMDS}"
	@echo -e "Enter virtual environment using:" \
		"\n\n\t$ source venv/bin/activate\n"


# help: clean                          - clean all files using .gitignore rules
.PHONY: clean
clean:
	$(call CHECK_GIT)
	@$(GIT) clean -X -f -d


# help: scrub                          - clean all files, even untracked files
.PHONY: scrub
scrub:
	$(call CHECK_GIT)
	@$(GIT) clean -x -f -d


# help: test                           - run tests
.PHONY: test
test:
	@python -m unittest discover -s tests


# help: test-verbose                   - run tests [verbosely]
.PHONY: test-verbose
test-verbose:
	@python -m unittest discover -s tests -v


# help: coverage                       - perform test coverage checks
.PHONY: coverage
coverage:
	@coverage erase
	@PYTHONPATH=src coverage run -m unittest discover -s tests -v
	@coverage html
	@coverage report


# help: format                         - perform code style format
.PHONY: format
format:
	@black src/{{cookiecutter.package_name}} tests examples


# help: check-format                   - check code format compliance
.PHONY: check-format
check-format:
	@black --check src/{{cookiecutter.package_name}} tests examples


# help: sort-imports                   - apply import sort ordering
.PHONY: sort-imports
sort-imports:
	@isort . --profile black


# help: check-sort-imports             - check imports are sorted
.PHONY: check-sort-imports
check-sort-imports:
	@isort . --check-only --profile black


# help: style                          - perform code style format
.PHONY: style
style: sort-imports format


# help: check-style                    - check code style compliance
.PHONY: check-style
check-style: check-sort-imports check-format


# help: check-types                    - check type hint annotations
.PHONY: check-types
check-types:
	@cd src; mypy -p {{cookiecutter.package_name}} --ignore-missing-imports


# help: check-lint                     - run static analysis checks
.PHONY: check-lint
check-lint:
	@pylint {{cookiecutter.package_name}} \
		examples \
		tests


# help: check-static-analysis          - check code style compliance
.PHONY: check-static-analysis
check-static-analysis: check-lint check-types


# help: docs                           - generate project documentation
.PHONY: docs
docs: coverage
	@cd docs && \
	rm -rf \
		source/api/{{cookiecutter.package_name}}*.rst \
		source/api/modules.rst \
		build/*
	@cd docs && make html


# help: check-docs                     - quick check docs consistency
.PHONY: check-docs
check-docs:
	@cd docs; make dummy


# help: serve-docs                     - serve project html documentation
.PHONY: serve-docs
serve-docs:
	@cd docs/build/html; python -m http.server --bind 127.0.0.1


# help: dist                           - create a wheel distribution package
.PHONY: dist
dist:
	@hatch build


# help: dist-test                      - test a wheel distribution package
.PHONY: dist-test
dist-test: dist
	@cd dist && \
	../tests/test-dist.bash \
		./{{cookiecutter.package_name}}-*-py3-none-any.whl


# help: dist-upload                    - upload a wheel distribution package
.PHONY: dist-upload
dist-upload:
	@twine upload dist/{{cookiecutter.package_name}}-*-py3-none-any.whl


# Keep these lines at the end of the file to retain nice help
# output formatting.
# help:
