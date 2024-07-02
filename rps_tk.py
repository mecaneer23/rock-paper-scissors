#!/usr/bin/env python3
"""Implementation of a rock paper scissors game using Tkinter"""

from functools import partial
from tkinter import StringVar, Tk, ttk

from rps_cli import main_logic, str_to_rps


def button_handler(button: str, string: StringVar, root: Tk) -> None:
    """Handle a button press"""
    string.set(str(main_logic(str_to_rps(button))))
    ttk.Label(root, textvariable=string).grid(row=1, column=0, columnspan=3)


def main() -> None:
    """Entry point for the rock, paper, scissors tkinter implementation"""
    root = Tk()
    root.title("Rock, Paper, Scissors")

    string = StringVar(root)

    for column, name in enumerate(("Rock", "Paper", "Scissors")):
        ttk.Button(
            root,
            text=name,
            command=partial(button_handler, name, string, root),
        ).grid(
            row=0,
            column=column,
        )

    root.mainloop()


if __name__ == "__main__":
    main()
