from faker import Faker
from typing import NamedTuple


class User(NamedTuple):
    name: str
    email: str


faker = Faker()


def user_generator() -> User:
    return User(faker.first_name(), faker.email())


def users_generator(amount: int = 100):
    return (user_generator() for _ in range(amount))


def print_users(users, is_print_index=False):
    for index, user in enumerate(users):
        result = f"{index} " if is_print_index else ""
        result += f"Name: {user.name}, email: {user.email}"
        print(result)
