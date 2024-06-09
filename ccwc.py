"""
ccwc.py: A coding challenge copy of the wc command in Unix/Linux.

This script reads the contents of a text file or standard input and counts the number of lines, words, and characters. It can also count the number of bytes in the file. The file name is passed as an argument to the script.

Usage:
    python ccwc.py [file] [-c] [-l] [-w] [-m]

Arguments:
    file: The name of the file to be processed. If no file is provided, the script will read from standard input.
    -c: Count the number of bytes in the file.
    -l: Count the number of lines in the file.
    -w: Count the number of words in the file.
    -m: Count the number of characters in the file.

Examples:
    python ccwc.py myfile.txt -l
    cat myfile.txt | python ccwc.py -c
"""

import sys
import os
import argparse
import locale

def read_file(file_path):
    """Read the contents of a file at the given path."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()


def count_bytes(file_path):
    """Return the number of bytes in the file."""
    return os.path.getsize(file_path)


def count_lines(file_contents):
    """Return the number of lines in the text."""
    return file_contents.count('\n')


def count_words(file_contents):
    """Return the number of words in the text."""
    words = file_contents.split()
    return len(words)


def count_characters(file_contents):
    """Return the number of characters in the text."""
    encoding = locale.getpreferredencoding()
    return len(file_contents.encode(encoding))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='A coding challenge copy of the wc command in Unix/Linux.'
    )
    parser.add_argument('file', nargs='?', default=sys.stdin, type=argparse.FileType('r'), 
                        help='The file to be processed.')
    parser.add_argument('-c', '--bytes', action='store_true',
                        help='Count the number of bytes in the file.')
    parser.add_argument('-l', '--lines', action='store_true', 
                        help='Count the number of lines in the file.')
    parser.add_argument('-w', '--words', action='store_true', 
                        help='Count the number of words in the file.')
    parser.add_argument('-m', '--characters', action='store_true', 
                        help='Count the number of characters in the file. Locale dependant.')
    args = parser.parse_args()

    file_contents = args.file.read()
    # Check if file contents or standard input
    file_name = args.file.name if args.file is not sys.stdin else ''

    count_functions = {
        'bytes': count_bytes,
        'lines': count_lines,
        'words': count_words,
        'characters': count_characters
    }

    if not any([args.bytes, args.characters, args.words, args.lines]):
        # Default behavior: Count lines, words, and characters
        line_count = count_lines(file_contents)
        word_count = count_words(file_contents)
        char_count = count_characters(file_contents)
        print(f"{line_count} {word_count} {char_count} {file_name}")

    if args.bytes:
        byte_count = count_bytes(args.file)
        print(f"{byte_count} {file_name}")
    if args.characters:
        char_count = count_characters(file_contents)
        print(f"{char_count} {file_name}")
    if args.words:
        word_count = count_words(file_contents)
        print(f"{word_count} {file_name}")
    if args.lines:
        line_count = count_lines(file_contents)
        print(f"{line_count} {file_name}")