# wc_python

A recreation of Unix WC utility in python

## Install

```bash
poetry install
```

## Run program

```bash
poetry run python src/wc_python [OPTIONS] [FILE]
```

## Options

-v, --version: Show version details and exit

-h, --help: Show help page and exit

-l, --lines: Print the newline count for FILE

-c, --bytes: Print the byte count for FILE

-m, --chars: Print the character count for FILE

--files0-from: read input from the files specified by NUL-terminated names in file F; If F is - then read names from standard input

FILE: the file to be processed, if not provided or is - STDIN will be process instead
