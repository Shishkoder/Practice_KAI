from random import choice

from .settings import Params


class RSA:
    @classmethod
    def create_keys(cls) -> tuple[list[int, int], list[int, int]]:
        p, q = choice(Params.PRIME_DIGITS_TUPLE), choice(Params.PRIME_DIGITS_TUPLE)
        cls.__n: int = p * q
        cls.__phi: int = (p - 1) * (q - 1)

        return cls.__create_public_key(), cls.__create_private_key()

    @classmethod
    def __create_public_key(cls) -> list[int, int]:
        cls.__e: int = 1
        while not cls.__phi % cls.__e:
            cls.__e += 1
        return [cls.__e, cls.__n]

    @classmethod
    def __create_private_key(cls) -> list[int, int]:
        cls.__d: int = 1
        while ((cls.__d * cls.__e) % cls.__phi != 1):
            cls.__d += 1

        return [cls.__d, cls.__n]

    @staticmethod
    def __convert_to_code(source_message: str) -> tuple:
        source_message_tuple: tuple = tuple(Params.ALL_SYMBOLS_DICT[char] \
                                            for char in source_message)

        return source_message_tuple

    @staticmethod
    def __convert_to_string(source_code: tuple) -> str:
        message: str = ''
        for char in source_code:
            message += list(Params.ALL_SYMBOLS_DICT.keys())\
                [list(Params.ALL_SYMBOLS_DICT.values()).index(char)]

        return message

    @classmethod
    def encode_message(cls, decoded_message: str, public_key: list[int, int]) -> tuple:
        source_message_tuple: tuple = cls.__convert_to_code(decoded_message)
        encoded_message_tuple: tuple = tuple(pow(code, public_key[0], public_key[1]) \
                                       for code in source_message_tuple)

        return encoded_message_tuple

    @classmethod
    def decode_message(cls, encoded_message: tuple, private_key: list[int, int]) -> str:
        decode_message: tuple = tuple(pow(code, private_key[0], private_key[1]) \
                                      for code in encoded_message)

        message: str = cls.__convert_to_string(decode_message)

        return message
