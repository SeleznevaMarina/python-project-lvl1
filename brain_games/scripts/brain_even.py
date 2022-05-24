#!/usr/bin/env python

from brain_games.game_frame import run
from brain_games.games import even


def main():
    print('Welcome to the Brain Games!')
    run(even)


if __name__ == '__main__':
    main()
