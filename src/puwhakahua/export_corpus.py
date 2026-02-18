import argparse
import os
import traceback

from puwhakahua.utils import load_corpus, clean


def export(corpus: str, output: str = None):
    """
    Exports the corpus to the specified output directory.

    :param corpus: the corpus to load and export
    :type corpus: str
    :param output: the directory to store the output in
    :type output: str
    """
    corp = load_corpus(corpus, raw=True, quiet=True)

    count = 0
    for item in corp:
        path = os.path.join(output, "%05d.txt" % item[0])
        with open(path, "w") as fp:
            fp.write(item[2])
            fp.write("\n")
        # progress
        count += 1
        if count % 100 == 0:
            print("Processing %d/%d..." % (count, len(corp)))
    print("Processed %d sentences!" % len(corp))


def main(args=None):
    """
    The main method for parsing command-line arguments.

    :param args: the commandline arguments, uses sys.argv if not supplied
    :type args: list
    """
    parser = argparse.ArgumentParser(
        description='Exports the sentences of the corpus into individual text files, using the ID as file name.',
        prog="export-corpus",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-c", "--corpus", metavar="FILE", help="The corpus to load (format: NUM: SENTENCE).", default=None, type=str, required=True)
    parser.add_argument("-o", "--output", metavar="DIR", help="The directory to store the output in.", default=None, type=str, required=True)
    parsed = parser.parse_args(args=args)
    export(parsed.corpus, output=parsed.output)


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
