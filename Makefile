compile-requirements:
	@pip-compile-multi --live

sync-requirements:
	@pip-sync requirements/*.txt

run:
	@source venv/bin/activate && python main.py