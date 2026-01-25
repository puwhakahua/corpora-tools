import argparse
import traceback

from puwhakahua.utils import load_corpus, load_document


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
            if word in entry[2]:
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

