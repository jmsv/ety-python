.PHONY: dist

install:
	python setup.py install

test:
	python -m pytest test_ety.py
	timeout 30s python -c "import test_ety; test_ety.test_circular_etymology()"

data:
	PYTHONIOENCODING=utf-8 python ety/data/generate.py

clean:
	rm -rf build/ dist/ ety.egg-info/ _trial_temp/ __pycache__/ */__pycache__/ htmlcov/
	rm -f *.pyc */*.pyc

format:
	black .

dist:
	python3 setup.py sdist bdist_wheel

upload:
	twine upload dist/*

