# corpora-tools
Tools for evaluating text corpora.

## Installation

```bash
pip install git+https://github.com/puwhakahua/corpora-tools.git
```

## Tools

### check-words

```
usage: check-words [-h] -c CORPUS -d DOCUMENT [-m MIN_LENGTH]

Checks in how many sentences of the corpus the words from the supplied
document appear.

options:
  -h, --help            show this help message and exit
  -c CORPUS, --corpus CORPUS
                        The corpus to load (format: NUM: SENTENCE). (default:
                        None)
  -d DOCUMENT, --document DOCUMENT
                        The text document to load and check its words.
                        (default: None)
  -m MIN_LENGTH, --min_length MIN_LENGTH
                        The minimum length that words need to meet in order to
                        be checked. (default: 1)
```
