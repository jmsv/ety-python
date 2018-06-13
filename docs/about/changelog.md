# Changelog

## [1.1.0] - 2018/03/13

### Added

- Support for running CLI as module: `python -m ety words` [#18](https://github.com/jmsv/ety-python/pull/18)
- `Word`s have `__eq__` and `__lt__` methods
- Proto language support [#32](https://github.com/jmsv/ety-python/issues/32)

### Changed

- `origins` returns a list of `Word` objects (e.g. `[Word(potato, language=English), ...]`), rather than a list of dictionaries
- `random_word` returns a `Word` object, rather than a string
- `tree` returns a [treelib](https://github.com/caesar0301/treelib) tree, rather than its string representation. A string can be obtained using `str()`
- Origins cli search bullet points origin lists, reducing ambiguity when searching for multiple words

### Bug fixes

- Fixed circular origin bug [#20](https://github.com/jmsv/ety-python/issues/20)

## [1.0.2] - 2018/06/06

### Bug Fixes

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

## [0.2.0] - 2018/05/16

### Added

- `ety.words` method. This acts as a reverse search: given an origin, it will return all of the words from (or partially from) that origin
- `ety.random_word` method returns a random word from the origins data set

## [0.1.0] - 2018/05/15

- `ety.origins` method takes a word and returns a list of the etymological origins of the word
- Command line tool: `ety word` lists the origins of 'word'
