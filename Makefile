install:
	python setup.py install

test:
	python tests.py

clean:
	rm -rf build dist ety.egg-info
	rm -f *.pyc */*.pyc
	pipenv --rm

