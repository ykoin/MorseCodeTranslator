# Morse Code Digit Decoder

This Python tool decodes messages encoded in Morse code using digits. It maps Morse code sequences (e.g., ".----" for "1") to their corresponding numeric values, concatenates them into a string, converts that string to an integer, and then decodes that integer into an ASCII (or Unicode) character.

**Note:** This tool was developed to solve one of the challenges from a CTF competition at WAT (Wojskowa Akademia Techniczna).

## Features

- **Morse-to-Digit Mapping:** Translates Morse code for digits into their numeric equivalents.
- **Group Separation:** Splits the Morse code input into groups using two or more spaces as delimiters.
- **Decoding Process:** Converts each group into a number string, then to an integer, and finally to a character using `chr()`.
- **File Input:** Reads the Morse code message from a file named `telegraf.txt`.

## How It Works

1. **Input Reading:**  
   The script reads the content of `telegraf.txt`.

2. **Morse Code Splitting:**  
   It splits the Morse code text into groups by detecting sequences of two or more spaces.

3. **Decoding Process:**  
   For each group:
   - Splits it into individual Morse tokens.
   - Maps each token to its corresponding digit.
   - Joins the digits into a number string, converts it to an integer, and then decodes it to an ASCII/Unicode character.

4. **Output:**  
   The decoded characters are concatenated and printed as the final decoded message.

## Requirements

- Python 3.x

## Usage

1. Place the `telegraf.txt` file in the same directory as the script.
2. Run the script:
   ```bash
   python decode_morse.py
   ```
3. The decoded message will be printed to the console.

## License

This project is licensed under the MIT License.
