#!/usr/bin/env python3

from tkinter import Tk, ttk, StringVar
import rps_cli




def main():
    def button_handler(button):
        result = rps_cli.main(button)
        string.set(f"User's move: {rps_cli.letter_to_name(result['user_move'])}\n\
        Computer's move: {rps_cli.letter_to_name(result['computer_move'])}")
        string.set(result['result'])

    root = Tk()
    root.title("Rock, Paper, Scissors")

    string = StringVar(root, value="Rock, Paper, Scissors")

    ttk.Label(root, textvariable=string).grid(row=0, column=0, columnspan=3)
    ttk.Label(root).grid(row=1, column=0, columnspan=3)

    ttk.Style().configure("TButton", padding=10, relief="raised")
    ttk.Button(root, text="Rock", command=lambda: button_handler("r")).grid(
        row=3, column=0
    )
    ttk.Button(root, text="Paper", command=lambda: button_handler("p")).grid(
        row=3, column=1
    )
    ttk.Button(root, text="Scissors", command=lambda: button_handler("s")).grid(
        row=3, column=2
    )

    root.mainloop()


if __name__ == "__main__":
    main()
