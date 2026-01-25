from typing import List, Tuple, Set


def clean(line: str) -> str:
    """
    Cleans up the sentence.

    :param line: the sentence to clean
    :type line: str
    :return: the clean sentence
    :rtype: str
    """
    line = line.strip().lower()
    line = line.replace(",", " ").replace(".", " ").replace("!", " ").replace("?", " ").replace(":", " ").replace(";",
                                                                                                                  " ")
    return line


def load_corpus(path: str) -> List[Tuple[int, int, Set[str]]]:
    """
    Loads the corpus. Blank lines get ignored.
    Line format: NUM: SENTENCE
    Sentences get split into words using blanks as separator.

    :param path: the path of the corpus to load
    :type path: str
    :return: the corpus (tuple of sentence ID, group index, set of words)
    :rtype: list
    """
    result = []

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
                result.append((int(parts[0]), group, set(clean(parts[1]).split(" "))))

    print("# lines in corpus: %d" % len(result))

    return result


def load_document(path: str, min_length: int) -> List[str]:
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
    """
    print("Loading document: %s" % path)

    words = set()
    with open(path, "r") as fp:
        for line in fp.readlines():
            line = clean(line)
            for word in line.split(" "):
                if len(word) >= min_length:
                    words.add(word.lower())

    result = sorted(words)
    print("# words in document: %d" % len(result))
    return result
