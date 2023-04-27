PROJECT = euler_problems
SRC_DIR := app
VENV_DIR = .venv
PYTHON := python3
RUN := . $(VENV_DIR)/bin/activate;

venv_init:
	@if [ ! -f "$(VENV_DIR)" ]; then \
		$(PYTHON) -m venv $(VENV_DIR) --prompt $(PROJECT); \
	fi
	$(RUN) pip install -r requirements.txt

venv: venv_init

clean:
	rm -rf $(VENV_DIR)