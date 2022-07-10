from .simple_rsa import RSA


class User:
    def __init__(self) -> None:
        self.__private_key, self.__public_key = RSA.create_keys()

    def send_message(self, message: str, public_key: list[str, str]) -> tuple:
        public_key: list[int, int] = list(map(int, public_key))
        return RSA.encode_message(message, public_key)

    def show_message(self, encoded_message: str, private_key: list[str, str]) -> str:
        private_key: list[int, int] = list(map(int, private_key))
        converted_tuple: tuple = tuple(map(int, encoded_message.replace(' ', '')[1:-1].split(',')))
        return RSA.decode_message(converted_tuple, private_key)

    @property
    def private_key(self) -> list[int, int]:
        return self.__private_key

    @property
    def public_key(self) -> list[int, int]:
        return self.__public_key
