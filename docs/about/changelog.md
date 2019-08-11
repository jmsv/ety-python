# Changelog

## [1.3.3] - 2019/08/12

### Fixed

- Replace deprecated Wintu ISO-639 code 'wit' with 'wnw'

## [1.3.2] - 2019/08/11

### Fixed

- Use ISO-639-2 language codes if 639-3 lookup fails

## [1.3.1] - 2018/07/28

### Fixed

- Incorrect README rendering on PyPI due to building with an old version of `wheel` (see [pypa/warehouse#3664](https://github.com/pypa/warehouse/issues/3664))

## [1.3.0] - 2018/07/28

### Added

- [`black`](https://github.com/ambv/black) code style

### Changed

- `lang` and `word_lang` params changed to `language` for uniformity

## [1.2.0] - 2018/07/17

### Added

- __Python 3.7 support!__
- Uses `colorful` for source word formatting in the command line
- `__dict__` method added to `EtyTree` for serialization
- Started monitoring [coverage](https://codecov.io/gh/jmsv/ety-python)

### Changed

- `EtyTree` takes an instance of `Word` [#13](https://github.com/jmsv/ety-python/issues/13)
- Data restructured for much better performance [#24](https://github.com/jmsv/ety-python/issues/24)
- `six` used to make Python 2/3 compatibility dev easier
- flake8 linting moved to Python tests, rather than cli tool

### Fixed

- Minor `Language` [`KeyError`](https://github.com/jmsv/ety-python/commit/086572f49899f918f395bdb8f867ae6a5702b1c8) bug

## [1.1.0] - 2018/06/13

### Added

- Support for running CLI as module: `python -m ety words` [#18](https://github.com/jmsv/ety-python/pull/18)
- `Word`s have `__eq__` and `__lt__` methods
- Proto language support [#32](https://github.com/jmsv/ety-python/issues/32)

### Changed

- `origins` returns a list of `Word` objects (e.g. `[Word(potato, language=English), ...]`), rather than a list of dictionaries
- `random_word` returns a `Word` object, rather than a string
- `tree` returns a [treelib](https://github.com/caesar0301/treelib) tree, rather than its string representation. A string can be obtained using `str()`
- Origins cli search bullet points origin lists, reducing ambiguity when searching for multiple words

### Fixed

- Fixed circular origin bug [#20](https://github.com/jmsv/ety-python/issues/20)

## [1.0.2] - 2018/06/06

### Fixed

- [@alxwrd](https://github.com/alxwrd) fixed unspecified encoding Windows bug, see [#16](https://github.com/jmsv/ety-python/pull/16)

## [1.0.1] - 2018/05/25

### Changed

- Improved command line interface
- `ety.origins` and `ety.tree` recursion fixes

## [1.0.0] - 2018/05/23

### Added

- `ety.tree` method takes a word and outputs the word's etymology in a tree format

### Changed

- Uses [Etymological Wordnet](http://www1.icsi.berkeley.edu/~demelo/etymwn) data instead of scraped Dictionary.com data
- `ety.origins` output structure changed

---

## [0.2.0] - 2018/05/16

### Added

- `ety.words` method. This acts as a reverse search: given an origin, it will return all of the words from (or partially from) that origin
- `ety.random_word` method returns a random word from the origins data set

## [0.1.0] - 2018/05/15

- `ety.origins` method takes a word and returns a list of the etymological origins of the word
- Command line tool: `ety word` lists the origins of 'word'
