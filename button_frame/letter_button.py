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
        self._setup_animations()

    def _setup_button(self) -> None:
        self.setFixedSize(40, 40)
        self.is_enlarged = False
        self.setStyleSheet(
            "background-color: #ffffff; border: 1px solid #000000; font-size: 20px;"
        )

    def _setup_animations(self):
        self.animation_adjustment = 5  # self.Adjustment for animation

        self.enlarge_animation = QPropertyAnimation(self, b"geometry")
        self.enlarge_animation.setDuration(150)
        self.enlarge_animation.setEasingCurve(QEasingCurve.Type.OutBack)

        self.shrink_animation = QPropertyAnimation(self, b"geometry")
        self.shrink_animation.setDuration(150)
        self.shrink_animation.setEasingCurve(QEasingCurve.Type.InQuad)

    def animate_enlarge(self):
        if not self.is_enlarged:
            new_geometry = self.geometry().adjusted(
                -self.animation_adjustment,
                -self.animation_adjustment,
                self.animation_adjustment,
                self.animation_adjustment,
            )
            self.enlarge_animation.setStartValue(self.geometry())
            self.enlarge_animation.setEndValue(new_geometry)
            self.enlarge_animation.start()
            self.is_enlarged = True

    def animate_shrink(self):
        if self.is_enlarged:
            new_geometry = self.geometry().adjusted(
                self.animation_adjustment,
                self.animation_adjustment,
                -self.animation_adjustment,
                -self.animation_adjustment,
            )
            self.shrink_animation.setStartValue(self.geometry())
            self.shrink_animation.setEndValue(new_geometry)
            self.shrink_animation.start()
            self.is_enlarged = False

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
                background-color: #7cb7f7;
            }
            QPushButton:pressed {
                background-color: gray;
            }
            QPushButton:disabled {
                background-color: darkgray;
            }
            """
        )
        self.setFlat(True)
        font = QFont()
        font.setPointSize(14)
        self.setFont(font)
        self.installEventFilter(self)
