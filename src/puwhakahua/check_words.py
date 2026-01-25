import argparse
import traceback

from typing import List, Dict, Tuple, Set


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


def load_corpus(path: str) -> List[Tuple[int, str]]:
    """
    Loads the corpus. Blank lines get ignored. 
    Line format: NUM: SENTENCE
    Sentences get split into words using blanks as separator.
    
    :param path: the path of the corpus to load
    :type path: str
    :return: the corpus (tuple of sentence ID and set of words)
    :rtype: list
    """
    result = []

    print("Loading corpus: %s" % path)

    with open(path, "r") as fp:
        for line in fp.readlines():
            line = line.strip()
            if len(line) == 0:
                continue
            parts = line.split(":  ")
            if len(parts) == 2:
                result.append((int(parts[0]), set(clean(parts[1]).split(" "))))

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


def check(corpus: str, document: str, min_length: int):
    """
    Checks the document against the corpus and outputs the results.

    :param corpus: the corpus to load
    :type corpus: str
    :param document: the document to check against the corpus
    :type document: str
    :param min_length: the minimum length that words have to have
    :type min_length: int
    """
    stats = dict()
    corp = load_corpus(corpus)
    doc = load_document(document, min_length)

    # count occurrences
    for word in doc:
        stats[word] = 0
        for entry in corp:
            if word in entry[1]:
                stats[word] = stats[word] + 1

    # output stats
    print("word,count,percentage")
    for word in doc:
        print("%s,%d,%f" % (word, stats[word], stats[word]/len(corp)*100))


def main(args=None):
    """
    The main method for parsing command-line arguments.

    :param args: the commandline arguments, uses sys.argv if not supplied
    :type args: list
    """
    parser = argparse.ArgumentParser(
        description='Checks in how many sentences of the corpus the words from the supplied document appear.',
        prog="check-words",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-c", "--corpus", help="The corpus to load (format: NUM: SENTENCE).", default=None, type=str, required=True)
    parser.add_argument("-d", "--document", help="The text document to load and check its words.", default=None, type=str, required=True)
    parser.add_argument("-m", "--min_length", help="The minimum length that words need to meet in order to be checked.", default=1, type=int, required=False)
    parsed = parser.parse_args(args=args)
    check(parsed.corpus, parsed.document, parsed.min_length)


def sys_main() -> int:
    """
    Runs the main function using the system cli arguments, and
    returns a system error code.

    :return: 0 for success, 1 for failure.
    """
    try:
        main()
        return 0
    except Exception:
        traceback.print_exc()
        return 1


if __name__ == '__main__':
    main()

