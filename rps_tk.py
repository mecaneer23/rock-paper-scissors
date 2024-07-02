#!/usr/bin/env python3
"""Implementation of a rock paper scissors game using Tkinter"""

from functools import partial
from tkinter import Tk, ttk

from rps_cli import main_logic, str_to_rps


def button_handler(button: str, root: Tk) -> None:
    """Handle a button press"""
    for old_label in root.grid_slaves(1, 0):
        old_label.grid_forget()
    ttk.Label(root, text=str(main_logic(str_to_rps(button)))).grid(
        row=1,
        column=0,
        columnspan=3,
    )


def main() -> None:
    """Entry point for the rock, paper, scissors tkinter implementation"""
    root = Tk()
    root.title("Rock, Paper, Scissors")

    for column, name in enumerate(("Rock", "Paper", "Scissors")):
        ttk.Button(
            root,
            text=name,
            command=partial(button_handler, name, root),
        ).grid(
            row=0,
            column=column,
        )

    root.mainloop()


if __name__ == "__main__":
    main()
