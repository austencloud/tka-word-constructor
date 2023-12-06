from PyQt6.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt6.QtGui import QIcon, QPixmap, QPainter, QFont
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QColor
from PyQt6.QtSvg import QSvgRenderer
from data.letter_data import letter_types
from TypeChecking.TypeChecking import Letters, Dict, TYPE_CHECKING
if TYPE_CHECKING:
    from widgets.main_widget import MainWidget

LETTER_SVG_DIR = "resources/images/letters/"


class ButtonFrame(QFrame):
    def __init__(self, main_widget: 'MainWidget') -> None:
        super().__init__()
        self.main_widget = main_widget
        self.interpolation_handler = main_widget.interpolation_handler
        self.init_letter_buttons_layout()
        self.setFixedHeight(self.main_widget.height())

    def init_letter_buttons_layout(self) -> None:
        self.buttons: Dict[Letters, QPushButton] = {}
        letter_buttons_layout = QVBoxLayout()
        self.spacing = 10
        letter_buttons_layout.setSpacing(self.spacing)
        letter_buttons_layout.setAlignment(
            Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignCenter
        )
        self.setContentsMargins(0, 0, 0, 0)
        letter_buttons_layout.setContentsMargins(0, 0, 0, 0)
        letter_rows = [
            # Type 1 - Dual-Shift
            ["A", "B", "C"],
            ["D", "E", "F"],
            ["G", "H", "I"],
            ["J", "K", "L"],
            ["M", "N", "O"],
            ["P", "Q", "R"],
            ["S", "T", "U", "V"],
            # Type 2 - Shift
            ["W", "X", "Y", "Z"],
            ["Σ", "Δ", "θ", "Ω"],
            # Type 3 - Cross-Shift
            ["W-", "X-", "Y-", "Z-"],
            ["Σ-", "Δ-", "θ-", "Ω-"],
            # Type 4 - Dash
            ["Φ", "Ψ", "Λ"],
            # Type 5 - Dual-Dash
            ["Φ-", "Ψ-", "Λ-"],
            # Type 6 - Static
            ["α", "β", "Γ"],
        ]

        for row in letter_rows:
            row_layout = QHBoxLayout()

            for letter in row:
                letter_type = self.get_letter_type(letter)
                icon_path = self.get_icon_path(letter_type, letter)
                button = self.create_button(icon_path)
                row_layout.addWidget(button)
                self.buttons[letter] = button
                button.clicked.connect(lambda _, l=letter: self.interpolation_handler.update_sequence(l))

            letter_buttons_layout.addLayout(row_layout)

        self.letter_buttons_layout = letter_buttons_layout
        self.setLayout(letter_buttons_layout)

    def get_letter_type(self, letter: str) -> str:
        for letter_type in letter_types:
            if letter in letter_types[letter_type]:
                return letter_type
        return ""

    def get_icon_path(self, letter_type: str, letter: str) -> str:
        return f"{LETTER_SVG_DIR}/{letter_type}/{letter}.svg"

    def create_button(self, icon_path: str) -> QPushButton:
        renderer = QSvgRenderer(icon_path)
        pixmap = QPixmap(renderer.defaultSize())
        pixmap.fill(QColor(Qt.GlobalColor.transparent))
        painter = QPainter(pixmap)
        renderer.render(painter)
        painter.end()
        button = QPushButton(QIcon(pixmap), "", self.main_widget)

        button.setStyleSheet(
            """
            QPushButton {
                background-color: white;
                border: none;
                border-radius: 0px;
                padding: 0px;
            }
            QPushButton:hover {
                background-color: #e6f0ff;
            }
            QPushButton:pressed {
                background-color: #cce0ff;
            }
            """
        )
        button.setFlat(True)
        font = QFont()
        font.setPointSize(int(20))
        button.setFont(font)
        return button

    def update_letter_buttons_size(self) -> None:
        self.button_row_count = self.letter_buttons_layout.count()
        self.button_column_count = 0  # Initialize to 0

        for i in range(self.button_row_count):
            item = self.letter_buttons_layout.itemAt(i)
            if item is not None:
                row_layout: QHBoxLayout = item.layout()
                column_count = row_layout.count()
                if column_count > self.button_column_count:
                    self.button_column_count = column_count

        available_height = (
            self.height() - (self.button_row_count + 1) * 10
        )  # Subtract spacing
        self.button_size = int(available_height / self.button_row_count)
        for i in range(self.button_row_count):
            item = self.letter_buttons_layout.itemAt(i)
            if item is not None:
                row_layout: QHBoxLayout = item.layout()
                for j in range(row_layout.count()):
                    button_item = row_layout.itemAt(j)
                    if button_item is not None:
                        button: QPushButton = button_item.widget()
                        button.setFixedSize(self.button_size, self.button_size)
                        icon_size = int(self.button_size * 0.9)
                        button.setIconSize(QSize(icon_size, icon_size))

    def update_size(self) -> None:
        self.setFixedHeight(self.main_widget.height())
        self.update_letter_buttons_size()
