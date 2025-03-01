# Exercise 22

import sys
script, input_encoding, error = sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline()    # reads one line from the file

    if line:    # if statement
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)   # would make it a loop, the if-statement prevents it from turining into a loop


def print_line(line, encoding, errors):    # does the actual encoding of each line from the file
    next_lang = line.strip()   # simple stripping of the trailing \n on the line string
    raw_bytes = next_lang.encode(encoding, errors=errors)   ## finally takes the language received from the file and encodes it into the raw bytes
    cooked_string = raw_bytes.decode(encoding, errors=errors)   ### inverse of line 15

    print(raw_bytes, "<===>", cooked_string)  # prints both bytes and Python string


languages = open("languages.txt", encoding="utf-8")

main(languages, input_encoding, error)

# Exercise 22: Strings, Bytes and Characters
# need to download file: languages.txt
# run: python ex22.py "utf-8" "strict"

## DBES: Decode Bytes, Encode Strings
## next_lang --> string so to get the raw bytes I must call .encode() on it to "Encode Strings"
## I pass to encode() the encoding I want and how to handle errors

### DBES: Decode Bytes, Encode Strings
### cooked_string --> variable from raw_bytes (is bytes) so to get a Python string I must call .decode() which should be the same as the next_lang variable
