from PyQt6.QtWidgets import QPushButton
from PyQt6.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt6.QtGui import QIcon, QPixmap, QPainter, QFont
from PyQt6.QtCore import (
    QPropertyAnimation,
    QRect,
    QSequentialAnimationGroup,
    QEasingCurve,
    Qt,
    QSize,
    QEvent,
)
from PyQt6.QtGui import QColor
from PyQt6.QtSvg import QSvgRenderer
from data.letter_data import letter_types
from TypeChecking.TypeChecking import Letters, Dict, TYPE_CHECKING


class LetterButton(QPushButton):
    def __init__(self, letter, parent=None):
        super().__init__(letter, parent)
        self.letter = letter
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
