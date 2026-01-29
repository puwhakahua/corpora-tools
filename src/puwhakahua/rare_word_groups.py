import argparse
import traceback

from puwhakahua.utils import load_corpus, load_document, word_occurrences


def check(corpus: str, document: str, min_length: int, min_occurrence: int, max_occurrence: int, output: str = None):
    """
    Checks the document against the corpus and outputs the results.

    :param corpus: the corpus to load
    :type corpus: str
    :param document: the document to check against the corpus
    :type document: str
    :param min_length: the minimum length that words have to have
    :type min_length: int
    :param min_occurrence: the minimum occurrence for a word in the corpus in order to be considered rare
    :type min_occurrence: int
    :param max_occurrence: the maximum occurrence for a word in the corpus in order to be considered rare
    :type max_occurrence: int
    :param output: the text file to store the corpus subset in, uses stdout if None
    :type output: str
    """
    if min_occurrence > max_occurrence:
        raise Exception("Min occurrence must be smaller than max one: min=%d, max=%d" % (min_occurrence, max_occurrence))

    corp = load_corpus(corpus)
    doc = load_document(document, min_length)
    stats = word_occurrences(corp, doc)

    # determine rare words
    rare_words = []
    for word in stats:
        if (stats[word] >= min_occurrence) and (stats[word] <= max_occurrence):
            rare_words.append(word)
    print("# rare words: %d" % len(rare_words))

    # determine groups with these rare words
    rare_groups = set()
    for word in rare_words:
        for entry in corp:
            if word in entry[2]:
                rare_groups.add(entry[1])

    # output updated corpus
    corp_raw = load_corpus(corpus, raw=True)
    last_group = -1
    if output is not None:
        print("Generating corpus subset: %s" % output)
        with open(output, "w") as fp:
            for entry in corp_raw:
                if entry[1] in rare_groups:
                    if (last_group > -1) and (last_group != entry[1]):
                        fp.write("\n")
                    last_group = entry[1]
                    fp.write("%05d:  %s\n" % (entry[0], entry[2]))
    else:
        for entry in corp_raw:
            if entry[1] in rare_groups:
                if (last_group > -1) and (last_group != entry[1]):
                    print()
                last_group = entry[1]
                print("%05d:  %s" % (entry[0], entry[2]))


def main(args=None):
    """
    The main method for parsing command-line arguments.

    :param args: the commandline arguments, uses sys.argv if not supplied
    :type args: list
    """
    parser = argparse.ArgumentParser(
        description='Determines the corpus groups which have occurrences of rare words from the document.',
        prog="rare-word-groups",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-c", "--corpus", metavar="FILE", help="The corpus to load (format: NUM: SENTENCE).", default=None, type=str, required=True)
    parser.add_argument("-d", "--document", metavar="FILE", help="The text document to load and use for determining groups of rare words.", default=None, type=str, required=True)
    parser.add_argument("-m", "--min_length", metavar="NUM", help="The minimum length that words need to meet in order to be checked.", default=1, type=int, required=False)
    parser.add_argument("-r", "--min_occurrence", metavar="NUM", help="The minimum occurrence for a word in the corpus in order to be considered rare.", default=1, type=int, required=False)
    parser.add_argument("-R", "--max_occurrence", metavar="NUM", help="The maximum occurrence for a word in the corpus in order to be considered rare.", default=1, type=int, required=False)
    parser.add_argument("-o", "--output", metavar="FILE", help="The text file to store the corpus subset in, uses stdout if not provided.", default=None, type=str, required=False)
    parsed = parser.parse_args(args=args)
    check(parsed.corpus, parsed.document, parsed.min_length,
          parsed.min_occurrence, parsed.max_occurrence,
          output=parsed.output)


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
