VERSION=0.0.0

pyproject:
	python update_pyproject.py

init:
	python -m venv venv
	source venv/bin/activate
	pip install -r requirements.txt

test:
	pytest
#	@if [ $$? -eq 0 ]; then \
#		$(MAKE) -s build; \
#	fi

format:
	black .

pre-commit: format
	@if [ $(VERSION) != "0.0.0" ]; then \
		$(MAKE) -s release; \
	fi

install_black:
	pip install black
	echo -e '#!/bin/bash\nmake pre-commit' > test

doc:
	sphinx-build -b html docs docs/_build

clean_doc:
	rm -rf docs/_build

docx: clean_doc doc
	firefox docs/_build/index.html

build:
	python -m build

release: test build
	git tag -a v$(VERSION) -m "Release version $(VERSION)"
	git push --tags