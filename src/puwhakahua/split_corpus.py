import argparse
import os
import random
import traceback
from typing import Dict, List

from puwhakahua.utils import load_corpus, clean


def save_split(grouped: Dict, subset: List[int], path: str):
    """
    Saves the split in the specified file.

    :param grouped: the grouped corpus tuples (key is group index)
    :type grouped: dict
    :param subset: the list of group indices to save in split
    :type subset: list
    :param path: the file to store the subset in
    :type path: str
    """
    with open(path, "w") as fp:
        for group_index in subset:
            for item in grouped[group_index]:
                fp.write("%05d:  %s\n" % (item[0], item[2]))
            fp.write("\n")


def generate(corpus: str, output: str = None, randomize: bool = False, seed: int = None, split_size: int = 100):
    """
    Generates the splits of the corpus.

    :param corpus: the corpus to split
    :type corpus: str
    :param output: the directory to store the splits in
    :type output: str
    :param randomize: whether to randomize the order of groups
    :type randomize: bool
    :param seed: the seed value to use, unseeded if None
    :type seed: int
    :param split_size: the number of groups within a split
    :type split_size: int
    """
    if output is None:
        raise Exception("No output directory provided!")

    corp = load_corpus(corpus, raw=True, quiet=True)

    # determine groups
    groups = set()
    groups_list = []
    grouped = dict()
    for item in corp:
        if item[1] not in groups:
            groups.add(item[1])
            groups_list.append(item[1])
            grouped[item[1]] = []
        grouped[item[1]].append(item)

    # randomize order?
    if randomize:
        r = random.Random(seed)
        r.shuffle(groups_list)

    # generate splits
    count = 0
    split_num = 0
    prefix, suffix = os.path.splitext(os.path.basename(corpus))
    subset = []
    for group in groups_list:
        count += 1

        if count > split_size:
            split_num += 1
            path = os.path.join(output, "%s-%d%s" % (prefix, split_num, suffix))
            save_split(grouped, subset, path)
            subset.clear()
            count = 1

        subset.append(group)

    if len(subset) > 0:
        split_num += 1
        path = os.path.join(output, "%s-%d%s" % (prefix, split_num, suffix))
        save_split(grouped, subset, path)


def main(args=None):
    """
    The main method for parsing command-line arguments.

    :param args: the commandline arguments, uses sys.argv if not supplied
    :type args: list
    """
    parser = argparse.ArgumentParser(
        description='Splits the corpus into subsets.',
        prog="split-corpus",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-c", "--corpus", metavar="FILE", help="The corpus to split (format: NUM: SENTENCE).", default=None, type=str, required=True)
    parser.add_argument("-o", "--output", metavar="DIR", help="The directory to store the splits in.", default=None, type=str, required=False)
    parser.add_argument("-r", "--randomize", action="store_true", help="Whether to randomize the group order.", required=False)
    parser.add_argument("-s", "--seed", metavar="SEED", help="The seed value for the randomization, default uses no seed.", default=None, type=int, required=False)
    parser.add_argument("-n", "--split_size", metavar="NUM", help="The number of groups within a split.", default=100, type=int, required=False)
    parsed = parser.parse_args(args=args)
    generate(parsed.corpus, output=parsed.output, randomize=parsed.randomize, seed=parsed.seed, split_size=parsed.split_size)


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
