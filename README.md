# ety-python
Python module to find the etymological origins of a word

> ___Note:__ this module is under construction and doesn't yet have a large enough dataset to be useful_

## Install

```bash
pipenv shell
python setup.py install
```

## Usage

### Module

```
>>> import ety

>>> ety.origins("potato")
['Spanish', 'Taino']

>>> ety.origins("abandon")
['Middle English', 'Middle French', 'Old French']
```

### CLI

After installing, a command-line tool is also available

```
Usage:
  $ ety <word>

Example:
  $ ety potato
  Spanish, Taino
```

