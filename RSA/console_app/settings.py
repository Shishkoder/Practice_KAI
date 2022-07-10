from string import printable

from sympy import isprime


class Params:
    __UNTILL: int = 4096

    __PRIME_DIGITS_TUPLE: tuple = tuple(digit for digit in range(__UNTILL + 1) if isprime(digit))
    __LATIN_AND_SPEC_SYMBOLS: str = printable + chr(8470) + chr(8212) + chr(160)
    __CYRILLIC_SYMBOLS_TUPLE: tuple = \
        tuple((lambda code: chr(code))(code) for code in range(1040, 1104)) + \
        (chr(1025), chr(1105))
    __CYRILLIC_SYMBOLS: str = ''.join(__CYRILLIC_SYMBOLS_TUPLE)

    __ALL_SYMBOLS: str = __LATIN_AND_SPEC_SYMBOLS + __CYRILLIC_SYMBOLS
    __ALL_SYMBOLS_DICT: dict = {char: ord(char) for char in __ALL_SYMBOLS}

    del __CYRILLIC_SYMBOLS_TUPLE, __LATIN_AND_SPEC_SYMBOLS, __CYRILLIC_SYMBOLS, __ALL_SYMBOLS

    @classmethod
    @property
    def PRIME_DIGITS_TUPLE(cls) -> tuple:
        return cls.__PRIME_DIGITS_TUPLE

    @classmethod
    @property
    def ALL_SYMBOLS_DICT(cls) -> dict:
        return cls.__ALL_SYMBOLS_DICT
