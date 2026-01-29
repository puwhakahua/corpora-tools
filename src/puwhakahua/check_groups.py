import argparse
import traceback

from puwhakahua.utils import load_corpus, load_document, group_occurrences


def check(corpus: str, document: str, min_length: int, output: str = None):
    """
    Checks the document against the corpus and outputs the results.

    :param corpus: the corpus to load
    :type corpus: str
    :param document: the document to check against the corpus
    :type document: str
    :param min_length: the minimum length that words have to have
    :type min_length: int
    :param output: the CSV file to store the output in, uses stdout out if None
    :type output: str
    """
    corp = load_corpus(corpus)
    doc = load_document(document, min_length)
    stats = group_occurrences(corp, doc)

    # output stats
    if output is None:
        print("group,count,percentage")
        for group in sorted(stats.keys()):
            print("%d,%d,%f" % (group, len(stats[group]), len(stats[group])/len(corp)*100))
    else:
        print("Writing output to: %s" % output)
        with open(output, "w") as fp:
            fp.write("group,count,percentage\n")
            for group in sorted(stats.keys()):
                fp.write("%d,%d,%f\n" % (group, len(stats[group]), len(stats[group]) / len(corp) * 100))


def main(args=None):
    """
    The main method for parsing command-line arguments.

    :param args: the commandline arguments, uses sys.argv if not supplied
    :type args: list
    """
    parser = argparse.ArgumentParser(
        description='Checks how many unique words from the document appear in each group of the corpus.',
        prog="check-groups",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-c", "--corpus", metavar="FILE", help="The corpus to load (format: NUM: SENTENCE).", default=None, type=str, required=True)
    parser.add_argument("-d", "--document", metavar="FILE", help="The text document to load and check its words.", default=None, type=str, required=True)
    parser.add_argument("-m", "--min_length", metavar="NUM", help="The minimum length that words need to meet in order to be checked.", default=1, type=int, required=False)
    parser.add_argument("-o", "--output", metavar="FILE", help="The CSV file to store the output in.", default=None, type=str, required=False)
    parsed = parser.parse_args(args=args)
    check(parsed.corpus, parsed.document, parsed.min_length, output=parsed.output)


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
