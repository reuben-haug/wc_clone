# ccwc.py

This is a Python script that mimics the functionality of the `wc` command in Unix/Linux. It reads the contents of a text file or standard input and counts the number of lines, words, and characters. It can also count the number of bytes in the file.

## Usage

Run the script with the name of the file to be processed as an argument. If no file is provided, the script will read from standard input. You can also pass the following options:

- `-c`: Count the number of bytes in the file.
- `-l`: Count the number of lines in the file.
- `-w`: Count the number of words in the file.
- `-m`: Count the number of characters in the file.

## Examples

```bash
python ccwc.py myfile.txt -l
cat myfile.txt | python ccwc.py -c