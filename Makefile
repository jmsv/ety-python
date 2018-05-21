install:
	python setup.py install

test:
	flake8
	python tests.py

clean:
	rm -rf build dist ety.egg-info _trial_temp __pycache__
	rm -f *.pyc */*.pyc
	pipenv --rm

