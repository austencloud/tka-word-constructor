from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
)
import sys
from widgets.main_widget import MainWidget


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self._configure_window()
        self._init_main_window()

    def _init_main_window(self) -> None:
        self.setMinimumSize(self.main_window_width, self.main_window_height)
        self.main_widget = MainWidget(self)
        self.installEventFilter(self.main_widget)
        self.setCentralWidget(self.main_widget)
        self.show()
        self.setWindowTitle("Word Constructor")

    def _configure_window(self) -> None:
        screens = QApplication.screens()
        if len(screens) > 1:
            screen = screens[1]
        else:
            screen = QApplication.primaryScreen()

        screen_geometry = screen.geometry()
        self.main_window_width = int(screen_geometry.width() * 0.4)
        self.main_window_height = int(screen_geometry.height() * 0.6)

        self.move(
            screen_geometry.x()
            + (screen_geometry.width() - self.main_window_width) // 2
            - 50,
            screen_geometry.y()
            + (screen_geometry.height() - self.main_window_height) // 2
            - 50,
        )


# Application execution
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
