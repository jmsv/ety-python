![ety](https://user-images.githubusercontent.com/14852491/52982538-880fbd80-33de-11e9-8101-6fa24c3b697d.png)

<p align="center">
<a href="https://badge.fury.io/py/ety"><img src="https://badge.fury.io/py/ety.svg" alt="PyPI version"></a>
<a href="https://pypi.python.org/pypi/ety"><img src="https://img.shields.io/pypi/pyversions/ety.svg" alt="Python versions"></a>
<a href="https://pypi.python.org/pypi/ety"><img src="https://img.shields.io/pypi/wheel/ety.svg" alt="Wheel Support"></a>
<a href="https://ety-python.readthedocs.io/en/latest/?badge=latest"><img src="https://readthedocs.org/projects/ety-python/badge/?version=latest" alt="Documentation Status"></a><br>
<a href="https://travis-ci.org/jmsv/ety-python"><img src="https://travis-ci.org/jmsv/ety-python.svg?branch=master" alt="Build Status"></a>
<a href="https://github.com/ambv/black"><img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Code style: black"></a>
</p>

---

## Intro

Recently, [@jmsv](https://github.com/jmsv) and [@parker57](https://github.com/parker57) started a side project to analyse etymologies of text written by various historical authors, expecting there to already be a library for retrieving etymological data. On discovering that this wasn't the case, [ety](https://github.com/jmsv/ety-python) was created!

There isn't a single source of truth for etymologies; words' origins can be heavily disputed. This package's source data, Gerard de Melo's [Etymological Wordnet](http://www1.icsi.berkeley.edu/~demelo/etymwn/), is mostly mined from Wiktionary. Since this is a collaboratively edited dictionary, its data could be seen as the closest we can get to a public consensus.

## Install

### [pip](https://pypi.org/project/ety)

```bash
pip install ety
```

### Development

In a virtual environment - [Pipenv](https://docs.pipenv.org) is recommended:

```bash
python setup.py install
```

## Usage

### Module

```python
>>> import ety

>>> ety.origins("potato")
[Word(batata, language=Taino)]

>>> ety.origins("drink", recursive=True)
[Word(drync, language=Old English (ca. 450-1100)), Word(drinken, language=Middle English (1100-1500)), Word(drincan, language=Old English (ca. 450-1100))]

>>> print(ety.tree("aerodynamically"))
aerodynamically (English)
├── -ally (English)
└── aerodynamic (English)
    ├── aero- (English)
    │   └── ἀήρ (Ancient Greek (to 1453))
    └── dynamic (English)
        └── dynamique (French)
            └── δυναμικός (Ancient Greek (to 1453))
                └── δύναμις (Ancient Greek (to 1453))
                    └── δύναμαι (Ancient Greek (to 1453))
```

### CLI

After installing, a command-line tool is also available. `ety -h` outputs the following help text describing arguments:

```
usage: ety [-h] [-r] [-t] words [words ...]

positional arguments:
  words            the search word(s)

optional arguments:
  -h, --help       show this help message and exit
  -r, --recursive  search origins recursively
  -t, --tree       display etymology tree
```

#### Examples

```bash
$ ety drink
drink   # List direct origins
 • drync (Old English (ca. 450-1100))
 • drinken (Middle English (1100-1500))

$ ety drink -r   # Recursive search
drink 
 • drync (Old English (ca. 450-1100))
 • drinken (Middle English (1100-1500))
 • drincan (Old English (ca. 450-1100))

$ ety drink -t   # Etymology tree
drink (English)
├── drinken (Middle English (1100-1500))
│   └── drincan (Old English (ca. 450-1100))
└── drync (Old English (ca. 450-1100))
```
