#!/usr/bin/env python3
"""
Logic for a Rock Paper Scissors game.
When run directly, play using a command line interface.
"""

from enum import Enum
from random import choice
from typing import Type, TypeVar


class RPS(Enum):
    """Represent a rock, paper, or scissors object"""

    ROCK = "Rock"
    PAPER = "Paper"
    SCISSORS = "Scissors"

    def __gt__(self, other: "RPS") -> bool:
        if self == other:
            return False
        return (
            (self == RPS.PAPER and other == RPS.ROCK)
            or (self == RPS.ROCK and other == RPS.SCISSORS)
            or (self == RPS.SCISSORS and other == RPS.PAPER)
        )

    def __str__(self) -> str:
        return self.value


_GenericEnum = TypeVar("_GenericEnum", bound=Enum)


def _get_first_char_dict(enum: Type[_GenericEnum]) -> dict[str, _GenericEnum]:
    """
    Return a dictionary mapping the first letter of each Enum
    item to the corresponding Enum item.
    """
    keys = [item.name for item in enum]
    return dict(zip((key[0] for key in keys), enum))


_FIRST_CHAR_DICT = _get_first_char_dict(RPS)


def _str_to_rps(string: str) -> RPS:
    if len(string) == 1:
        return _FIRST_CHAR_DICT[string.upper()]
    return RPS[string.upper()]


class Result:
    """Store a result from the rock paper scissors game"""

    def __init__(self, user_move: RPS, computer_move: RPS):
        self._user_move = user_move
        self._computer_move = computer_move
        self._result = ""

    def set_result(self, result: str) -> "Result":
        """Set a string containing how the game went"""
        self._result = result
        return self

    def __str__(self) -> str:
        return f"User's move: {self._user_move}\
        \nComputer's move: {self._computer_move}\
        \n{self._result}"


def run_as_cli() -> Result:
    """Run one turn of Rock, Paper, Scissors in the terminal"""
    user_move = input("Rock, Paper, or Scissors? (r, p, s): ")
    computer_move = choice(["r", "p", "s"])
    output = Result(_str_to_rps(user_move), _str_to_rps(computer_move))

    if user_move == computer_move:
        return output.set_result("Tie!")
    if user_move > computer_move:
        return output.set_result("You win!")
    if user_move < computer_move:
        return output.set_result("You lose!")
    raise RuntimeError("Something went wrong!")


if __name__ == "__main__":
    print(run_as_cli())
