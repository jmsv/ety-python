- etymwn-eng.tsv is the etymwn.tsv dataset filtered to lines starting with "eng:"
- iso-639-3.json contains country codes used by the etymwn dataset

Etymological Wordnet 2013-02-08
Gerard de Melo
http://icsi.berkeley.edu/~demelo/etymwn/


== DESCRIPTION ==

The Etymological Wordnet project provides information about how words in different languages
are etymologically related. The information is mostly mined from the English version of
Wiktionary, but also contains a number of manual additions.


== FORMAT ==

The package includes a Tab-separated values (TSV) file in UTF-8 format with three columns,
providing a word, a relation, and a target word. Words are given with ISO 639-3 codes
(additionally, there are some ISO 639-2 codes prefixed with "p_" to indicate proto-languages).
The most relevant relation is "rel:etymology". To see only etymological relations, run
  grep "rel:etymology" etymwn.tsv | less
on UNIX-based systems.


== CREDITS AND LICENSE ==

Gerard de Melo
http://icsi.berkeley.edy/~demelo/
Based on the contributions of the English Wiktionary community
http://en.wiktionary.org/

License: CC-BY-SA 3.0

In scientific works, please cite:
  Gerard de Melo, Gerhard Weikum. "Towards Universal Multilingual Knowledge Bases".
  In: Principles, Construction, and Applications of Multilingual Wordnets. Proceedings
  of the 5th Global Wordnet Conference (GWC 2010). Narosa Publishing 2010, New Delhi India.
