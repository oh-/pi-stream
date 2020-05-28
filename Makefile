webapp_files='webapp/**/*/*.py'


serve: .PHONY
	python3 webapp/app.py

test: $(webapp_files)
	pytest

.PHONY:
