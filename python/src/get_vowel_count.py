import unittest


def get_count(input_str):
    num_vowels = 0

    vowels = ["a", "e", "i", "o", "u"]
    for char in input_str:
        if char in vowels:
            num_vowels += 1

    return num_vowels


assert get_count("abracadabra") == 5