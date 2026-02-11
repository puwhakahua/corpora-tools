import argparse
import os.path
import traceback
import matplotlib.pyplot as plt

from puwhakahua.utils import load_document


def generate(doc: str, output: str = None, plot: bool = False, plot_output: str = None):
    """
    Outputs some information on the corpus.

    :param doc: the corpus to load
    :type doc: str
    :param output: the CSV file to store the output in, uses stdout out if None
    :type output: str
    :param plot: whether to plot the data
    :type plot: bool
    :param plot_output: the file to store the plot in
    :type plot_output: str
    """
    words = load_document(doc, min_length=1, quiet=True)
    max_len = 0
    lengths = dict()
    for word in words:
        l = len(word)
        max_len = max(max_len, l)
        if l not in lengths:
            lengths[l] = 0
        lengths[l] += 1

    # output stats
    if output is None:
        print("name,value")
        print("# unique words,%d" % len(words))
        print("max word length,%d" % max_len)
        for l in sorted(lengths.keys()):
            print("# words of length %d,%d" % (l, lengths[l]))
    else:
        print("Writing output to: %s" % output)
        with open(output, "w") as fp:
            fp.write("name,value\n")
            fp.write("# unique words,%d\n" % len(words))
            fp.write("max word length,%d\n" % max_len)
            for l in sorted(lengths.keys()):
                fp.write("# words of length %d,%d\n" % (l, lengths[l]))

    if plot or (plot_output is not None):
        x = []
        y = []
        for l in sorted(lengths.keys()):
            x.append(l)
            y.append(lengths[l])
        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.set(ylabel='# words', xlabel='word length',
               title='%s: # words = %d' % (os.path.basename(doc), len(words)))
        if plot_output is not None:
            fig.savefig(plot_output)
        if plot:
            plt.show()


def main(args=None):
    """
    The main method for parsing command-line arguments.

    :param args: the commandline arguments, uses sys.argv if not supplied
    :type args: list
    """
    parser = argparse.ArgumentParser(
        description='Outputs some information on the text document.',
        prog="doc-info",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-d", "--document", metavar="FILE", help="The text document to load.", default=None, type=str, required=True)
    parser.add_argument("-o", "--output", metavar="FILE", help="The CSV file to store the output in.", default=None, type=str, required=False)
    parser.add_argument("-p", "--plot", action="store_true", help="Whether to visualize the data.")
    parser.add_argument("-P", "--plot_output", metavar="FILE", help="The file to store the plot in, does not require visualization (-p).", default=None, type=str, required=False)
    parsed = parser.parse_args(args=args)
    generate(parsed.document, output=parsed.output,
             plot=parsed.plot, plot_output=parsed.plot_output)


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
