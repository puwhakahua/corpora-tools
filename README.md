# corpora-tools
Tools for evaluating text corpora.

## Installation

```bash
pip install git+https://github.com/puwhakahua/corpora-tools.git
```

## Tools

### check-words

```
usage: check-words [-h] -c FILE -d FILE [-m NUM] [-o FILE]

Checks in how many sentences of the corpus the words from the supplied
document appear.

options:
  -h, --help            show this help message and exit
  -c FILE, --corpus FILE
                        The corpus to load (format: NUM: SENTENCE). (default:
                        None)
  -d FILE, --document FILE
                        The text document to load and check its words.
                        (default: None)
  -m NUM, --min_length NUM
                        The minimum length that words need to meet in order to
                        be checked. (default: 1)
  -o FILE, --output FILE
                        The CSV file to store the output in. (default: None)
```

### check-groups

```
usage: check-groups [-h] -c FILE -d FILE [-m NUM] [-o FILE]

Checks how many unique words from the document appear in each group of the
corpus.

options:
  -h, --help            show this help message and exit
  -c FILE, --corpus FILE
                        The corpus to load (format: NUM: SENTENCE). (default:
                        None)
  -d FILE, --document FILE
                        The text document to load and check its words.
                        (default: None)
  -m NUM, --min_length NUM
                        The minimum length that words need to meet in order to
                        be checked. (default: 1)
  -o FILE, --output FILE
                        The CSV file to store the output in. (default: None)
```
