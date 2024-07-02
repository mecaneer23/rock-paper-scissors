#!/usr/bin/env python3
"""Implementation of a rock paper scissors game using PyQt5"""

from functools import partial

from PyQt5.QtWidgets import (
    QApplication,
    QGridLayout,
    QLabel,
    QPushButton,
    QWidget,
)

from rps_cli import main_logic, str_to_rps


def button_handler(name: str, label: QLabel) -> None:
    """Handle a button press"""
    label.setText(str(main_logic(str_to_rps(name))))


def main() -> None:
    """Entry point for the rock, paper, scissors PyQt5 implementation"""
    app = QApplication([])
    root = QWidget()
    root.setWindowTitle("Rock, Paper, Scissors")
    layout = QGridLayout()
    label = QLabel()
    layout.addWidget(label, 1, 1)
    for column, name in enumerate(("Rock", "Paper", "Scissors")):
        button = QPushButton(name)
        button.clicked.connect(partial(button_handler, name, label))
        layout.addWidget(button, 0, column)
    root.setLayout(layout)
    root.show()
    app.exec_()


if __name__ == "__main__":
    main()
