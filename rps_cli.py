#!/usr/bin/env python3

from random import choice


def letter_to_name(letter):
    names = {"r": "Rock", "p": "Paper", "s": "Scissors", "q": "Quit"}
    if letter in names:
        return names[letter]
    else:
        print("Invalid input!")
        main()


def main(
    user_move=None,
    computer_move=choice(["r", "p", "s"]),
):
    if user_move is None:
        user_move = input("Rock, Paper, or Scissors? (r, p, s), q to quit: ")
    if user_move == "q":
        return {
            "user_move": user_move,
            "computer_move": computer_move,
            "result": "Goodbye!",
        }

    if user_move == computer_move:
        return {
            "user_move": user_move,
            "computer_move": computer_move,
            "result": "Tie!",
        }
    elif (
        (user_move == "r" and computer_move == "s")
        or (user_move == "p" and computer_move == "r")
        or (user_move == "s" and computer_move == "p")
    ):
        return {
            "user_move": user_move,
            "computer_move": computer_move,
            "result": "You win!",
        }
    elif (
        (user_move == "r" and computer_move == "p")
        or (user_move == "p" and computer_move == "s")
        or (user_move == "s" and computer_move == "r")
    ):
        return {
            "user_move": user_move,
            "computer_move": computer_move,
            "result": "You lose!",
        }


if __name__ == "__main__":
    result = main()
    print(
        f"User's move: {letter_to_name(result['user_move'])}\
        \nComputer's move: {letter_to_name(result['computer_move'])}\
        \n{result['result']}"
    )
