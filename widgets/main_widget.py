from PyQt6.QtWidgets import QWidget, QHBoxLayout
from button_frame.button_frame import ButtonFrame
from widgets.results_frame import ResultsFrame
from PyQt6.QtGui import QResizeEvent

from typing import TYPE_CHECKING
from interpolation_handler import InterpolationHandler

if TYPE_CHECKING:
    from main import MainWindow


class MainWidget(QWidget):
    def __init__(self, main_window: "MainWindow") -> None:
        super().__init__()
        self.main_window = main_window

        self.resize(self.main_window.width(), self.main_window.height())

        self.interpolation_handler = InterpolationHandler(self)

        self.letter_buttons = ButtonFrame(self)
        self.results_frame = ResultsFrame(self)

        self._add_widgets_to_layouts()

    def _add_widgets_to_layouts(self) -> None:
        self.main_layout = QHBoxLayout(self)
        self.main_layout.addWidget(self.letter_buttons)
        self.main_layout.addWidget(self.results_frame)

    def resizeEvent(self, event: QResizeEvent) -> None:
        super().resizeEvent(event)
        self.resize(int(self.main_window.width()), int(self.main_window.height()))
        self.letter_buttons.update_button_frame_size()
