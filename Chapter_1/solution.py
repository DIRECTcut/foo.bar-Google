"""Foo.Bar Chapter 1 Solution"""

from timer import time_function


@time_function
def solution(j):
    return "".join([encode_char(char) for _, char in enumerate(j)])


def is_capital_letter(letter):
    return letter != " " and letter == letter.capitalize()


def encode_char(char):
    encoding_table = {
        "a": "100000",
        "b": "110000",
        "c": "100100",
        "d": "100110",
        "e": "100010",
        "f": "110100",
        "g": "110110",
        "h": "110010",
        "i": "010100",
        "j": "010110",
        "k": "101000",
        "l": "111000",
        "m": "101100",
        "n": "101110",
        "o": "101010",
        "p": "111100",
        "q": "111110",
        "r": "111010",
        "s": "011100",
        "t": "011110",
        "u": "101001",
        "v": "111001",
        "w": "010111",
        "x": "101101",
        "y": "101111",
        "z": "101011",
        " ": "000000",
        "CAP": "000001",
    }
    available_characters = encoding_table.keys()

    if (
        char not in available_characters
        and char.capitalize() not in available_characters
        and char.lower() not in available_characters
    ):
        raise ValueError(f"No encoding for character: {char}")

    capital_prefix = encoding_table.get("CAP")
    if is_capital_letter(char):
        return "".join([capital_prefix, encoding_table.get(char.lower())])

    return encoding_table.get(char.lower())
