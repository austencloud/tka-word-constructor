from PyQt6.QtWidgets import QPushButton
from PyQt6.QtWidgets import QPushButton
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import (
    QPropertyAnimation,
    QEasingCurve,
)
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from widgets.main_widget import MainWidget


class LetterButton(QPushButton):
    def __init__(self, icon: QIcon, text: str, main_widget: "MainWidget") -> None:
        super().__init__(icon, text, main_widget)
        self._setup_button()

    def _setup_button(self) -> None:
        self.setFixedSize(40, 40)
        self.setStyleSheet(
            "background-color: #ffffff; border: 1px solid #000000; font-size: 20px;"
        )
        self.enlarge_animation = QPropertyAnimation(self, b"geometry")
        self.enlarge_animation.setDuration(150)
        self.enlarge_animation.setEasingCurve(QEasingCurve.Type.OutBack)

        self.shrink_animation = QPropertyAnimation(self, b"geometry")
        self.shrink_animation.setDuration(150)
        self.shrink_animation.setEasingCurve(QEasingCurve.Type.InBack)

        self.setStyleSheet(
            """
            QPushButton {
                background-color: white;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: lightgray;
            }
            QPushButton:pressed {
                background-color: teal;
            }
            QPushButton:disabled {
                background-color: lightgray;
            }
            """
        )
        self.setFlat(True)
        font = QFont()
        font.setPointSize(14)
        self.setFont(font)
        self.installEventFilter(self)
