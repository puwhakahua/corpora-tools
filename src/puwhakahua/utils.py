from typing import List, Tuple, Set, Dict, Union


def clean(line: str) -> str:
    """
    Cleans up the sentence.

    :param line: the sentence to clean
    :type line: str
    :return: the clean sentence
    :rtype: str
    """
    line = line.strip().lower()
    line = line.replace(",", " ").replace(".", " ").replace("!", " ").replace("?", " ").replace(":", " ").replace(";", " ")
    return line


def load_corpus(path: str, raw: bool = False, quiet: bool = False) -> List[Tuple[int, int, Union[str, Set[str]]]]:
    """
    Loads the corpus. Blank lines get ignored.
    Line format: NUM:  SENTENCE  (double blank after colon!)
    Sentences get split into words using blanks as separator.

    :param path: the path of the corpus to load
    :type path: str
    :param raw: whether to load the corpus in raw format
    :type raw: bool
    :param quiet: whether to suppress logging info
    :type quiet: bool
    :return: the corpus (tuple of sentence ID, group index, set of words or sentence when raw)
    :rtype: list
    """
    result = []

    if not quiet:
        print("Loading corpus: %s" % path)

    group = 0
    with open(path, "r") as fp:
        for line in fp.readlines():
            line = line.strip()
            if len(line) == 0:
                group += 1
                continue
            parts = line.split(":  ")
            if len(parts) == 2:
                if raw:
                    result.append((int(parts[0]), group, parts[1]))
                else:
                    result.append((int(parts[0]), group, set(clean(parts[1]).split(" "))))

    if not quiet:
        print("# lines in corpus: %d" % len(result))

    return result


def load_document(path: str, min_length: int, quiet: bool = False) -> List[str]:
    """
    Loads the document and breaks it up into words.
    Words get converted into lower case. Words that fall below
    the minimum length get discarded. The result is a sorted list.

    :param path: the text document to load
    :type path: str
    :param min_length: the minium length for words
    :type min_length: int
    :return: the list of words to check
    :type: list
    :param quiet: whether to suppress logging info
    :type quiet: bool
    """
    if not quiet:
        print("Loading document: %s" % path)

    words = set()
    with open(path, "r") as fp:
        for line in fp.readlines():
            line = clean(line)
            for word in line.split(" "):
                if len(word) >= min_length:
                    words.add(word.lower())

    result = sorted(words)
    if not quiet:
        print("# words in document: %d" % len(result))
    return result


def word_occurrences(corpus: List[Tuple[int, int, Set[str]]], doc: List[str]) -> Dict[str, int]:
    """
    Counts the word occurrences in the corpus entries.

    :param corpus: the corpus to use for determining the occurrences
    :type corpus: list of tuples (sentence ID, group index, set of words)
    :param doc: the list of words to compute the occurrences for
    :type doc: list
    :return: the occurrences mapping (word -> count)
    :rtype: dict
    """
    result = dict()

    for word in doc:
        result[word] = 0
        for entry in corpus:
            if word in entry[2]:
                result[word] = result[word] + 1

    return result


def group_occurrences(corpus: List[Tuple[int, int, Set[str]]], doc: List[str]) -> Dict[int, Set]:
    """
    Records the occurrences of words in the groups of the corpus entries.

    :param corpus: the corpus to use for determining the occurrences
    :type corpus: list of tuples (sentence ID, group index, set of words)
    :param doc: the list of words to compute the occurrences for
    :type doc: list
    :return: the occurrences mapping (group -> set of words that occurred)
    :rtype: dict
    """
    result = dict()

    for word in doc:
        for entry in corpus:
            if word in entry[2]:
                if entry[1] not in result:
                    result[entry[1]] = set()
                result[entry[1]].add(word)

    return result
