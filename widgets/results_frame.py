from typing import TYPE_CHECKING, List
from PyQt6.QtWidgets import (
    QLabel,
    QPushButton,
    QTextEdit,
    QLineEdit,
    QCheckBox,
    QHBoxLayout,
    QVBoxLayout,
    QFrame,
    QApplication,
)
from PyQt6.QtGui import QFont

if TYPE_CHECKING:
    from widgets.main_widget import MainWidget


class ResultsFrame(QFrame):
    def __init__(self, main_widget: "MainWidget") -> None:
        super().__init__(main_widget)
        self.main_widget = main_widget
        self.interpolation_handler = main_widget.interpolation_handler
        self._setup_widgets()
        self._setup_layout()
        self._connect_events()
        
        self.interpolation_handler.sequenceUpdated.connect(self._update_sequence_display)
        self.interpolation_handler.savedWordsUpdated.connect(self._update_saved_words_label)

    def _setup_widgets(self) -> None:
        self.action_buttons = self._setup_action_buttons()
        self.labels = self._setup_labels()
        self.sequence_box = self._setup_sequence_box()
        self.line_edits = self._setup_line_edits()
        self.checkboxes = self._setup_checkboxes()
        self.saved_words_box = self._setup_saved_words_box()

    def _setup_checkboxes(self) -> None:
        self.auto_fill_checkbox = QCheckBox("Autofill Mode", self)
        self.circular_word_checkbox = QCheckBox("Circular Word", self)
        checkboxes = [self.auto_fill_checkbox, self.circular_word_checkbox]
        font = QFont("Helvetica", 18)
        self.auto_fill_checkbox.setFont(font)
        self.circular_word_checkbox.setFont(font)
        return checkboxes

    def _connect_events(self) -> None:
        self.clear_sequence_button.clicked.connect(self._clear_sequence)
        self.save_sequence_button.clicked.connect(self._save_sequence)
        self.clear_saved_button.clicked.connect(self._clear_saved)
        self.copy_saved_button.clicked.connect(self._copy_saved_text)
        self.generate_random_word_button.clicked.connect(self._generate_random_word)
        self.auto_fill_checkbox.toggled.connect(self.interpolation_handler.set_auto_fill_mode)

    def _setup_line_edits(self) -> List[QLineEdit]:
        self.typed_word_input = QLineEdit(self)
        self.word_length_input = QLineEdit(self)
        line_edits = [
            self.typed_word_input,
            self.word_length_input,
        ]

        # Increase font size of line edits
        font = QFont("Helvetica", 18)
        for line_edit in line_edits:
            line_edit.setFont(font)

        return line_edits

    def _setup_saved_words_box(self) -> QTextEdit:
        saved_words_box = QTextEdit(self)
        saved_words_box.setFixedHeight(150)  # Adjust height as needed
        saved_words_box.setReadOnly(True)
        return saved_words_box

    def _setup_action_buttons(self) -> List[QPushButton]:
        self.clear_sequence_button = QPushButton("Clear")
        self.generate_button = QPushButton("Generate")
        self.save_sequence_button = QPushButton("Save")
        self.clear_saved_button = QPushButton("Clear")
        self.copy_saved_button = QPushButton("Copy")
        self.generate_random_word_button = QPushButton("Generate Random Word")

        action_buttons = [
            self.clear_sequence_button,
            self.generate_button,
            self.save_sequence_button,
            self.clear_saved_button,
            self.copy_saved_button,
            self.generate_random_word_button,
        ]

        # Increase font size of action buttons
        font = QFont("Helvetica", 18)
        for button in action_buttons:
            button.setFont(font)

        return action_buttons

    def _setup_labels(self) -> List[QLabel]:
        self.start_position_label = QLabel("Start:", self)
        self.end_positions_label = QLabel("", self)
        self.saved_words_label = QLabel("Saved words:", self)
        self.type_a_word_label = QLabel("Type a word:", self)
        self.word_length_label = QLabel("Word length:", self)

        labels = [
            self.start_position_label,
            self.end_positions_label,
            self.saved_words_label,
            self.type_a_word_label,
            self.word_length_label,
        ]

        # Increase font size of labels
        font = QFont("Helvetica", 18)
        self.start_position_label.setFont(font)
        self.end_positions_label.setFont(font)
        self.saved_words_label.setFont(font)
        self.type_a_word_label.setFont(font)
        self.word_length_label.setFont(font)

        return labels

    def _setup_sequence_box(self) -> QTextEdit:
        sequence_text_edit = QTextEdit(self)  # Change this from QLineEdit to QTextEdit
        sequence_text_edit.setReadOnly(True) 
        sequence_text_edit.setFixedHeight(50)
        sequence_text_edit.setFont(QFont("Helvetica", 20))
        return sequence_text_edit

    def _setup_layout(self) -> QFrame:
        
        
        autofill_save_clear_layout = QHBoxLayout()
        autofill_save_clear_layout.addWidget(self.auto_fill_checkbox)
        autofill_save_clear_layout.addWidget(self.save_sequence_button)
        autofill_save_clear_layout.addWidget(self.clear_sequence_button)
        
        typed_word_generate_button_layout = QHBoxLayout()
        typed_word_generate_button_layout.addWidget(self.typed_word_input)
        typed_word_generate_button_layout.addWidget(self.generate_button)
        
        clear_copy_layout = QHBoxLayout()
        clear_copy_layout.addWidget(self.clear_saved_button)
        clear_copy_layout.addWidget(self.copy_saved_button)

        results_layout = QVBoxLayout(self)
        results_layout.addWidget(self.start_position_label)
        results_layout.addWidget(self.end_positions_label)
        results_layout.addWidget(self.sequence_box)
        results_layout.addLayout(autofill_save_clear_layout)
        results_layout.addWidget(self.type_a_word_label)
        results_layout.addLayout(typed_word_generate_button_layout)
        results_layout.addWidget(self.saved_words_label)
        results_layout.addWidget(self.saved_words_box)
        results_layout.addLayout(clear_copy_layout)
        results_layout.addWidget(self.word_length_label)
        results_layout.addWidget(self.word_length_input)
        results_layout.addWidget(self.generate_random_word_button)
        results_layout.addWidget(self.circular_word_checkbox)

    def _connect_events(self) -> None:
        self.clear_sequence_button.clicked.connect(self._clear_sequence)
        self.save_sequence_button.clicked.connect(self._save_sequence)
        self.clear_saved_button.clicked.connect(self._clear_saved)
        self.copy_saved_button.clicked.connect(self._copy_saved_text)
        self.generate_random_word_button.clicked.connect(self._generate_random_word)
        self.auto_fill_checkbox.toggled.connect(self._toggle_autofill_related_widgets)

    def _toggle_autofill_related_widgets(self, checked: bool) -> None:
        self.type_a_word_label.setVisible(checked)
        self.typed_word_input.setVisible(checked)
        self.generate_button.setVisible(checked)
        
    def _update_sequence_display(self) -> None:
        sequence_str = ''.join([
            f'<span style="color: {"red" if is_interpolated else "black"}">{letter}</span>' 
            for letter, is_interpolated in self.interpolation_handler.get_sequence()
        ])
        self.sequence_box.setHtml(sequence_str)
        self._update_end_positions_label()

    def _update_end_positions_label(self) -> None:
        end_positions_str = ' '.join([
            self.interpolation_handler.get_end_position(letter) 
            for letter, _ in self.interpolation_handler.get_sequence()
        ])
        self.end_positions_label.setText(end_positions_str)

    def _update_saved_words_label(self) -> None:
        self.saved_words_box.clear()
        for word in self.interpolation_handler.get_saved_words():
            formatted_word = "".join(
                [
                    f'<span style="color: {"red" if is_interpolated else "black"}">{letter}</span>'
                    for letter, is_interpolated in word
                ]
            )
            self.saved_words_box.append(formatted_word)
            
    def _clear_sequence(self) -> None:
        self.interpolation_handler.clear_sequence()
        self.sequence_box.clear()
        self._update_end_positions_label()
        self._update_buttons()

    def _save_sequence(self) -> None:
        self.interpolation_handler.save_current_sequence()
        self._clear_sequence()
        self._update_saved_words_label()

    def _clear_saved(self) -> None:
        self.interpolation_handler.clear_saved_words()
        self.saved_words_box.clear()

    def _copy_saved_text(self) -> None:
        clipboard = QApplication.clipboard()
        clipboard.setText(self.saved_words_box.toPlainText())

    def _generate_random_word(self) -> None:
        length = (
            int(self.word_length_input.text())
            if self.word_length_input.text().isdigit()
            else 4
        )
        end_at_start = self.circular_word_checkbox.isChecked()
        self.interpolation_handler.generate_word(length, end_at_start)
        self._update_saved_words_label()

    def _update_buttons(self) -> None:
        # Update the state of buttons based on the current sequence and auto-fill mode
        sequence = self.interpolation_handler.get_sequence()
        auto_fill_mode = self.auto_fill_checkbox.isChecked()
        for letter, button in self.main_widget.letter_buttons.buttons.items():
            if not sequence:
                button.setEnabled(True)
            elif auto_fill_mode and self.interpolation_handler.can_follow(letter):
                button.setEnabled(True)
            else:
                button.setEnabled(False)


