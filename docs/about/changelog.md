# Changelog

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
