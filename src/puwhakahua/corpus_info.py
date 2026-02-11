import argparse
import traceback

from puwhakahua.utils import load_corpus


def generate(corpus: str, output: str = None):
    """
    Outputs some information on the corpus.

    :param corpus: the corpus to load
    :type corpus: str
    :param output: the CSV file to store the output in, uses stdout out if None
    :type output: str
    """
    corp = load_corpus(corpus, quiet=True)
    groups = set()
    for item in corp:
        groups.add(item[1])

    # output stats
    if output is None:
        print("name,value")
        print("# sentences,%d" % len(corp))
        print("# groups,%d" % len(groups))
    else:
        print("Writing output to: %s" % output)
        with open(output, "w") as fp:
            fp.write("name,value\n")
            fp.write("# sentences,%d\n" % len(corp))
            fp.write("# groups,%d\n" % len(groups))


def main(args=None):
    """
    The main method for parsing command-line arguments.

    :param args: the commandline arguments, uses sys.argv if not supplied
    :type args: list
    """
    parser = argparse.ArgumentParser(
        description='Outputs some information on the corpus.',
        prog="corpus-info",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-c", "--corpus", metavar="FILE", help="The corpus to load (format: NUM: SENTENCE).", default=None, type=str, required=True)
    parser.add_argument("-o", "--output", metavar="FILE", help="The CSV file to store the output in.", default=None, type=str, required=False)
    parsed = parser.parse_args(args=args)
    generate(parsed.corpus, output=parsed.output)


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
