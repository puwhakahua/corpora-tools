import argparse
import os
import random
import traceback
from typing import List

from puwhakahua.utils import load_corpus


def export(corpus: str, output: str = None, prefix: str = "", suffix: str = ".txt", left_pad: int = 5,
           ids: List[int] = None, seed: int = None, num_random: int = None, audio_companion_file: str = None):
    """
    Exports the corpus to the specified output directory.

    :param corpus: the corpus to load and export
    :type corpus: str
    :param output: the directory to store the output in
    :type output: str
    :param prefix: the prefix to use for the file name, before the ID
    :type prefix: str
    :param suffix: the suffix to use for the file name, after the ID
    :type suffix: str
    :param left_pad: the width to use for left-padding the ID with 0s, disabled if <=1
    :type  left_pad: int
    :param ids: the explicit list of IDs to export, ignored if None
    :type ids: list or None
    :param seed: the seed to use for randomized export, None for unseeded randomization
    :type seed: int or None
    :param num_random: the number of randomly selected sentences to export
    :type num_random: int
    :param audio_companion_file: the extension (incl dot) of the audio companion file that must be present for an ID, otherwise the ID gets skipped; ignored if None
    :type audio_companion_file: str
    """
    if (ids is not None) and (num_random is not None):
        raise Exception("You cannot list specific IDs and how many randomly selected sentences to export at the same time!")

    if prefix is None:
        prefix = ""
    if suffix is None:
        suffix = ""
    if (left_pad is None) or (left_pad < 1):
        left_pad = 1

    # generate file name format
    name_format = prefix
    if left_pad > 1:
        name_format += "%" + "0" * left_pad + "d"
    else:
        name_format += "%d"
    name_format += suffix

    corp = load_corpus(corpus, raw=True, quiet=True)
    processed = 0
    exported = 0

    # specific IDs
    ids_set = None
    max_items = len(corp)
    if ids is not None:
        ids_set = set(ids)
        max_items = len(ids)

    # randomly selected IDs
    if num_random is not None:
        rnd = random.Random(seed)
        max_items = num_random
        rnd.shuffle(corp)

    for item in corp:
        # specific IDs?
        if ids_set is not None:
            if item[0] not in ids_set:
                continue

        processed += 1

        # output sentence
        path = os.path.join(output, name_format % item[0])
        output_sentence = True

        # check for companion file?
        if audio_companion_file is not None:
            audio_path = os.path.splitext(path)[0] + audio_companion_file
            if not os.path.exists(audio_path):
                output_sentence = False

        # output text
        if output_sentence:
            with open(path, "w") as fp:
                fp.write(item[2])
                fp.write("\n")
            exported += 1

        # progress
        if processed % 100 == 0:
            print("Processed %d/%d, exported: %d" % (processed, max_items, exported))

        # finished?
        if processed >= max_items:
            break

    print("Processed %d sentences and exported %d!" % (max_items, exported))


def main(args=None):
    """
    The main method for parsing command-line arguments.

    :param args: the commandline arguments, uses sys.argv if not supplied
    :type args: list
    """
    parser = argparse.ArgumentParser(
        description='Exports the sentences of the corpus into individual text files, using the ID in conjunction with the prefix and suffix as file name.',
        prog="export-corpus",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-c", "--corpus", metavar="FILE", help="The corpus to load (format: NUM: SENTENCE).", default=None, type=str, required=True)
    parser.add_argument("-o", "--output", metavar="DIR", help="The directory to store the output in.", default=None, type=str, required=True)
    parser.add_argument("-P", "--prefix", metavar="PREFIX", help="The prefix to use for generating the file names, i.e., the string before the ID.", default="", type=str, required=False)
    parser.add_argument("-S", "--suffix", metavar="SUFFIX", help="The suffix to use for generating the file names, i.e., the string after the ID.", default=".txt", type=str, required=False)
    parser.add_argument("-L", "--left_pad", metavar="WIDTH", help="The width to use for left-padding the ID with 0s, disabled if <=1.", default=5, type=int, required=False)
    parser.add_argument("-i", "--ids", metavar="ID", help="The specific IDs of sentences to export rather than the whole corpus.", default=None, type=int, required=False, nargs="*")
    parser.add_argument("-s", "--seed", metavar="SEED", help="The seed value to use for the randomized export, uses unseeded randomization if none provided.", default=None, type=int, required=False)
    parser.add_argument("-r", "--num_random", metavar="NUM", help="The number of randomly selected sentences to export.", default=None, type=int, required=False)
    parser.add_argument("-a", "--audio_companion_file", metavar="EXT", help="The extension (incl dot) of the audio companion file that must be present for an ID, otherwise the ID gets skipped from the export.", default=None, type=str, required=False)
    parsed = parser.parse_args(args=args)
    export(parsed.corpus, output=parsed.output, prefix=parsed.prefix, suffix=parsed.suffix, left_pad=parsed.left_pad,
           ids=parsed.ids, seed=parsed.seed, num_random=parsed.num_random, audio_companion_file=parsed.audio_companion_file)


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
