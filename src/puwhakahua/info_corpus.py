import argparse
import sys
import traceback

from puwhakahua.utils import load_corpus, clean


def generate(corpus: str, output: str = None, word_list: str = None):
    """
    Outputs some information on the corpus.

    :param corpus: the corpus to load
    :type corpus: str
    :param output: the CSV file to store the output in, uses stdout out if None
    :type output: str
    :param word_list: the text file to store the unique words in, ignored if None
    :type word_list: str
    """
    corp = load_corpus(corpus, quiet=True, raw=True)
    groups = set()
    for item in corp:
        groups.add(item[1])

    # compute some stats
    sent_min = sys.maxsize
    sent_max = 0
    sent_mean = 0.0
    for item in corp:
        sent_len = len(item[2])
        sent_min = min(sent_min, sent_len)
        sent_max = max(sent_max, sent_len)
        sent_mean += sent_len
    sent_mean /= len(corp)

    # output stats
    if output is None:
        print("name,value")
        print("# sentences,%d" % len(corp))
        print("# groups,%d" % len(groups))
        print("# min sentence length,%d" % sent_min)
        print("# max sentence length,%d" % sent_max)
        print("# mean sentence length,%f" % sent_mean)
    else:
        print("Writing output to: %s" % output)
        with open(output, "w") as fp:
            fp.write("name,value\n")
            fp.write("# sentences,%d\n" % len(corp))
            fp.write("# groups,%d\n" % len(groups))
            fp.write("# min sentence length,%d\n" % sent_min)
            fp.write("# max sentence length,%d\n" % sent_max)
            fp.write("# mean sentence length,%f\n" % sent_mean)

    if word_list is not None:
        if output is not None:
            print("Writing word list to: %s" % word_list)
        corp = load_corpus(corpus, quiet=True, raw=False)
        words = set()
        for item in corp:
            for w in item[2]:
                try:
                    float(w)
                except:
                    words.add(clean(w))

        with open(word_list, "w") as fp:
            for word in sorted(words):
                fp.write("%s\n" % word)


def main(args=None):
    """
    The main method for parsing command-line arguments.

    :param args: the commandline arguments, uses sys.argv if not supplied
    :type args: list
    """
    parser = argparse.ArgumentParser(
        description='Outputs some information on the corpus.',
        prog="info-corpus",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-c", "--corpus", metavar="FILE", help="The corpus to load (format: NUM: SENTENCE).", default=None, type=str, required=True)
    parser.add_argument("-o", "--output", metavar="FILE", help="The CSV file to store the output in.", default=None, type=str, required=False)
    parser.add_argument("-w", "--word_list", metavar="FILE", help="The text file to store the unique, clean words in.", default=None, type=str, required=False)
    parsed = parser.parse_args(args=args)
    generate(parsed.corpus, output=parsed.output, word_list=parsed.word_list)


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
