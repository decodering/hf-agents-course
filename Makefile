# HARDCODED
VENV_BIN="venv/bin/activate"

compile-requirements:
	@pip-compile-multi --live

sync-requirements:
	@source ${VENV_BIN} && pip-sync requirements/*.txt

run:
	@source venv/bin/activate && python main.py