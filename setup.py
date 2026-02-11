from setuptools import setup, find_namespace_packages


def _read(f):
    """
    Reads in the content of the file.
    :param f: the file to read
    :type f: str
    :return: the content
    :rtype: str
    """
    return open(f, 'rb').read()


setup(
    name="corpora_tools",
    description="Python3 library for evaluating text corpora.",
    long_description=(
            _read('DESCRIPTION.rst') + b'\n' +
            _read('CHANGES.rst')).decode('utf-8'),
    url="https://github.com/puwhakahua/corpora-tools",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Utilities',
        'Programming Language :: Python :: 3',
    ],
    package_dir={
        '': 'src'
    },
    packages=find_namespace_packages(where='src'),
    install_requires=[
        "setuptools",
        "matplotlib",
    ],
    version="0.0.1",
    author='Peter Reutemann',
    author_email='fracpete@waikato.ac.nz',
    entry_points={
        "console_scripts": [
            "check-words=puwhakahua.check_words:sys_main",
            "check-groups=puwhakahua.check_groups:sys_main",
            "corpus-info=puwhakahua.corpus_info:sys_main",
            "doc-info=puwhakahua.doc_info:sys_main",
            "rare-word-groups=puwhakahua.rare_word_groups:sys_main",
        ],
    },
)
