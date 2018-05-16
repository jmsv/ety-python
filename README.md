# ety-python
Python module to find the etymological origins of a word

> ___Note:__ this module is under construction and doesn't yet have a large enough dataset to be useful_

## Install

### [pip](https://pypi.org/project/ety)

```bash
pip install ety
```

### Development

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

## Changelog

### [0.2.0] - 2018/05/16
#### Added
- `ety.words` method. This acts as a reverse search: given an origin, it will return all of the words from (or partially from) that origin
- `ety.random_word` method returns a random word from the origins data set

### [0.1.0] - 2018/05/15
- `ety.origins` method takes a word and returns a list of the etymological origins of the word
- Command line tool: `ety word` lists the origins of 'word'
