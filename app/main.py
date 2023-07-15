from app.reading_a_file import reading_a_file
from app.users_generator import print_users
from app.users_generator import users_generator
from app.who_is_there import get_astronaut_count
from app.average import average


def main():
    print('Task №1: Reading a file')
    reading_a_file()
    print('\n')

    print('Task №2: Users generator')
    users = users_generator()
    print_users(users, True)
    print('\n')

    print('Task №3: Who is there?\nNumber of astronauts at the moment:')
    get_astronaut_count()
    print('\n')

    print('Task №4: Average')
    average()
    print('\n')