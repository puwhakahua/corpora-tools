import argparse
import traceback

from puwhakahua.utils import save_corpus

# special markups to replace
MARKUPS = [
    "[ARB]",
    "[FIGURE]",
    "[FORMULA]",
    "[FORMULAE]",
    "[ILLUSTRATION]",
    "[ILLUSTRATIONS]",
    "[LIST]",
    "[LONG PASSAGE IN MAORI]",
    "[LONG QUOTATION]",
    "[LONG QUOTATIONS]",
    "[PLATE]",
    "[PLATES]",
    "[POEM]",
    "[SHORTHAND CHARACTER]",
    "[SHORTHAND CHARACTERS]",
    "[SIC]",
    "[SIGNATURE]",
    "[SONG]",
    "[TABLE]",
]


def import_wwc(input_file: str, output_file: str = None):
    """
    Imports the sentences from the untagged WWC text file and stores in standard corpus file format.

    :param input_file: the WWC corpus text file to load and process
    :type input_file: str
    :param output_file: the corpus file to store the result in
    :type output_file: str
    """
    print("Loading WWC data from: %s" % input_file)
    with open(input_file, "r") as fp:
        lines = [x.strip() for x in fp.readlines()]
    print("Loaded %d lines" % len(lines))

    # remove prefix and meta-data lines
    clean = []
    for line in lines:
        if len(line) > 9:
            line = line[8:].strip()
            # skip meta-data
            if line.startswith("**") or line.startswith("*#"):
                continue
            clean.append(line)
    lines = clean

    # remove *N and \N (with N=0-9), remove **
    clean = []
    for line in lines:
        if "*" in line:
            for i in range(10):
                line = line.replace("*%d" % i, "")
            line = line.replace("**", "")
        if "\\" in line:
            for i in range(10):
                line = line.replace("\\%d" % i, "")
        if "{" in line:
            for i in range(10):
                line = line.replace("{%d" % i, "")
        clean.append(line)
    lines = clean

    # group lines
    groups = dict()
    group_id = 0
    for line in lines:
        if line.startswith("*<"):
            group_id += 1
            continue
        if group_id not in groups:
            groups[group_id] = []
        groups[group_id].append(line)

    # turn into corpus
    corpus = []
    sentence_id = 0
    for group_id, group in groups.items():
        text = " ".join(group)
        sentences = text.replace("|", "").split("^")
        for sentence in sentences:
            # final clean
            sentence = sentence.replace("*", "").replace("}", "")
            if "[" in sentence:
                for markup in MARKUPS:
                    sentence = sentence.replace(markup, "")
            sentence = sentence.strip()
            if len(sentence) == 0:
                continue
            sentence_id += 1
            corpus.append((sentence_id, group_id, sentence))
    print("Split into %d groups and %d sentences" % (len(groups), sentence_id))

    # save corpus
    save_corpus(corpus, output_file)


def main(args=None):
    """
    The main method for parsing command-line arguments.

    :param args: the commandline arguments, uses sys.argv if not supplied
    :type args: list
    """
    parser = argparse.ArgumentParser(
        description='Imports the untagged text from the WWC corpus and outputs the cleaned up sentences in standard corpus format.',
        prog="import-wwc",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-i", "--input", metavar="FILE", help="The WWC text file to process.", default=None, type=str, required=True)
    parser.add_argument("-o", "--output", metavar="FILE", help="The corpus file to store the output in.", default=None, type=str, required=True)
    parsed = parser.parse_args(args=args)
    import_wwc(parsed.input, output_file=parsed.output)


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
