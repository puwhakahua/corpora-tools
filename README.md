# corpora-tools
Tools for working with text corpora.

## Installation

```bash
pip install git+https://github.com/puwhakahua/corpora-tools.git
```

## Tools

### check-words

```
usage: check-words [-h] -c FILE -d FILE [-m NUM] [-o FILE] [-p] [-P FILE]

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
  -p, --plot            Whether to visualize the data. (default: False)
  -P FILE, --plot_output FILE
                        The file to store the plot in, does not require
                        visualization (-p). (default: None)
```

### check-groups

```
usage: check-groups [-h] -c FILE -d FILE [-m NUM] [-o FILE] [-p] [-P FILE]

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
  -p, --plot            Whether to visualize the data. (default: False)
  -P FILE, --plot_output FILE
                        The file to store the plot in, does not require
                        visualization (-p). (default: None)
```

### export-corpus

```
usage: export-corpus [-h] -c FILE -o DIR

Exports the sentences of the corpus into individual text files, using the ID
as file name.

options:
  -h, --help            show this help message and exit
  -c FILE, --corpus FILE
                        The corpus to load (format: NUM: SENTENCE). (default:
                        None)
  -o DIR, --output DIR  The directory to store the output in. (default: None)
```


### info-corpus

```
usage: info-corpus [-h] -c FILE [-o FILE] [-w FILE]

Outputs some information on the corpus.

options:
  -h, --help            show this help message and exit
  -c FILE, --corpus FILE
                        The corpus to load (format: NUM: SENTENCE). (default:
                        None)
  -o FILE, --output FILE
                        The CSV file to store the output in. (default: None)
  -w FILE, --word_list FILE
                        The text file to store the unique, clean words in.
                        (default: None)
```


### info-doc

```
usage: info-doc [-h] -d FILE [-o FILE]

Outputs some information on the text document.

options:
  -h, --help            show this help message and exit
  -d FILE, --document FILE
                        The text document to load. (default: None)
  -o FILE, --output FILE
                        The CSV file to store the output in. (default: None)
```


### rare-word-groups

```
usage: rare-word-groups [-h] -c FILE -d FILE [-m NUM] [-r NUM] [-R NUM]
                        [-o FILE]

Determines the corpus groups which have occurrences of rare words from the
document.

options:
  -h, --help            show this help message and exit
  -c FILE, --corpus FILE
                        The corpus to load (format: NUM: SENTENCE). (default:
                        None)
  -d FILE, --document FILE
                        The text document to load and use for determining
                        groups of rare words. (default: None)
  -m NUM, --min_length NUM
                        The minimum length that words need to meet in order to
                        be checked. (default: 1)
  -r NUM, --min_occurrence NUM
                        The minimum occurrence for a word in the corpus in
                        order to be considered rare. (default: 1)
  -R NUM, --max_occurrence NUM
                        The maximum occurrence for a word in the corpus in
                        order to be considered rare. (default: 1)
  -o FILE, --output FILE
                        The text file to store the corpus subset in, uses
                        stdout if not provided. (default: None)
```

### split-corpus

```
usage: split-corpus [-h] -c FILE [-o DIR] [-r] [-s SEED] [-n NUM]

Splits the corpus into subsets.

options:
  -h, --help            show this help message and exit
  -c FILE, --corpus FILE
                        The corpus to split (format: NUM: SENTENCE). (default:
                        None)
  -o DIR, --output DIR  The directory to store the splits in. (default: None)
  -r, --randomize       Whether to randomize the group order. (default: False)
  -s SEED, --seed SEED  The seed value for the randomization, default uses no
                        seed. (default: None)
  -n NUM, --split_size NUM
                        The number of groups within a split. (default: 100)
```


## Documentation

See [here](doc/README.md) for some documentation and examples.
