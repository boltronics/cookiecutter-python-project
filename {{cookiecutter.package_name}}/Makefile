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


# help: venv                           - enter a dev virtual environment
.PHONY: venv
venv:
	@hatch shell


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
	@hatch test --all --cover


# help: test-verbose                   - run tests [verbosely]
.PHONY: test-verbose
test-verbose:
	@hatch test -v --all --cover


# help: coverage                       - perform test coverage checks
.PHONY: coverage
coverage:
	@hatch run coverage:run-new-reports


# help: format                         - perform code style format
.PHONY: format
format:
	@hatch run style:run-black


# help: check-format                   - check code format compliance
.PHONY: check-format
check-format:
	@hatch run style:run-black-check


# help: sort-imports                   - apply import sort ordering
.PHONY: sort-imports
sort-imports:
	@hatch run style:run-isort


# help: check-sort-imports             - check imports are sorted
.PHONY: check-sort-imports
check-sort-imports:
	@hatch run style:run-isort-check


# help: style                          - perform code style format
.PHONY: style
style: sort-imports format


# help: check-style                    - check code style compliance
.PHONY: check-style
check-style: check-sort-imports check-format


# help: check-types                    - check type hint annotations
.PHONY: check-types
check-types:
	@hatch run types:check


# help: check-lint                     - run static analysis checks
.PHONY: check-lint
check-lint:
	@hatch run lint:check


# help: check-static-analysis          - check code style compliance
.PHONY: check-static-analysis
check-static-analysis: check-lint check-types


# help: docs                           - generate project documentation
.PHONY: docs
docs: coverage
	@hatch run docs:build


# help: check-docs                     - quick check docs consistency
.PHONY: check-docs
check-docs:
	@hatch run docs:build-dummy


# help: serve-docs                     - serve project html documentation
.PHONY: serve-docs
serve-docs:
	@hatch run python -m http.server -b 127.0.0.1 -d docs/build/html


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
	@hatch publish


# Keep these lines at the end of the file to retain nice help
# output formatting.
# help:
