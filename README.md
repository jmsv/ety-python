# ety-python
Python module to find the etymological origins of a word

[![Build Status](https://travis-ci.org/jmsv/ety-python.svg?branch=master)](https://travis-ci.org/jmsv/ety-python)
[![PyPI version](https://badge.fury.io/py/ety.svg)](https://badge.fury.io/py/ety)
[![Python versions](https://img.shields.io/pypi/pyversions/ety.svg)](https://pypi.python.org/pypi/ety)
[![Wheel Support](https://img.shields.io/pypi/wheel/ety.svg)](https://pypi.python.org/pypi/ety)

## Install

### [pip](https://pypi.org/project/ety)

```bash
pip install ety
```

### Development

In a virtual environment: (Pipenv is recommended)

```bash
python setup.py install
```

## Usage

### Module

```
>>> import ety

>>> ety.origins("potato")
[{'word': 'batata', 'lang': {'code': 'tnq', 'name': 'Taino'}}]

>>> ety.origins('drink', recursive=True)
[{'word': 'drync', 'lang': {'code': 'ang', 'name': 'Old English (ca. 450-1100)'}}, {'word': 'drinken', 'lang': {'code': 'enm', 'name': 'Middle English (1100-1500)'}}, {'word': 'drincan', 'lang': {'code': 'ang', 'name': 'Old English (ca. 450-1100)'}}]

>>> print(ety.tree('aerodynamically'))
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
usage: ety [-h] [-r] [-t] word

positional arguments:
  word             the search word

optional arguments:
  -h, --help       show this help message and exit
  -r, --recursive  search origins recursively
  -t, --tree       display etymology tree
```

#### Examples:

```
$ ety drink   # List direct origins of a word
drync (Old English (ca. 450-1100))
drinken (Middle English (1100-1500))

$ ety drink -r  # Recursive argument
drync (Old English (ca. 450-1100))
drinken (Middle English (1100-1500))
drincan (Old English (ca. 450-1100))

$ ety drink -t  # Output tree argument
drink (English)
├── drinken (Middle English (1100-1500))
│   └── drincan (Old English (ca. 450-1100))
└── drync (Old English (ca. 450-1100))
```
