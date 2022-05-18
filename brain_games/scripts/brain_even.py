#!/usr/bin/env python

from brain_games.game_frame import run_game
from brain_games.games import even


def main():
    print('Welcome to the Brain Games!')
    run_game(even)


if __name__ == '__main__':
    main()
