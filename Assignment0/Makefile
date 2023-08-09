REQUIRED_VERSION := 3.7
PYTHON_VERSION := $(shell python3 --version | grep ^Python | sed 's/^.* //g')
PYTHON := python3
PIP := pip3
PYTHON_VERSION := $(filter $(REQUIRED_VERSION),$(firstword $(sort $(PYTHON_VERSION) $(REQUIRED_VERSION))))

MAX_LINE := 100

all: coverage

help:
	@echo "setup    - install correct dependencies and check for correct python version (3.7+)"
	@echo "clean    - remove all build, test, coverage and Python artifacts"
	@echo "format   - run autopep8 to auto format the code"
	@echo "style    - check style with pylint"
	@echo "test     - run all unit tests"
	@echo "coverage - check code coverage of unit tests"
	@echo "runner   - generate graphs for specific algorithms"

clean:
	rm -rf */__pycache__ # remove compiled python directory
	rm -rf fibonacci/fib/__pycache__ # remove compiled python directory
	rm -rf test/fib/__pycache__ # remove compiled python directory
	rm -f .coverage # clean up file associated with unit test coverage
	rm -f *.png # clean up pictures from runner

.python-check:
	@echo Current Python Version $(PYTHON_VERSION)
	@echo Required Minimum Python Version $(REQUIRED_VERSION)
	@[ "${PYTHON_VERSION}" ] && echo "Correct python version installed" || \
		( echo "Python $(REQUIRED_VERSION)+ not installed"; exit 1 )

setup: .python-check
	$(PIP) install -r requirements.txt

format:
	@echo "Auto Format to PEP-8 Standards"
	autopep8 --in-place --aggressive --experimental --max-line-length $(MAX_LINE) --recursive fibonacci/
	autopep8 --in-place --aggressive --experimental --max-line-length $(MAX_LINE) --recursive test/
	@echo "Auto Format to PEP-257 Standards"
	docformatter --in-place --wrap-summaries $(MAX_LINE) --wrap-descriptions $(MAX_LINE) \
		--pre-summary-newline --recursive fibonacci/
	docformatter --in-place --wrap-summaries $(MAX_LINE) --wrap-descriptions $(MAX_LINE) \
		--pre-summary-newline --recursive test/

style: .python-check
	@echo "Check if 'fibonacci' folder matches PEP-8 and PEP-257 guides"
	pydocstyle fibonacci/
	pycodestyle fibonacci/ --max-line-length=$(MAX_LINE)
	@echo "Check if 'test' folder matches PEP-8 and PEP-257 guides"
	pydocstyle test/
	pycodestyle test/ --max-line-length=$(MAX_LINE)
	@echo "Run pylint"
	pylint test/
	pylint fibonacci/

test: clean .python-check
	coverage run --source=fibonacci --omit=*"__init__.py" -m unittest -v

coverage: test
	coverage json
	coverage report -m

runner: .python-check
	$(PYTHON) runner.py
