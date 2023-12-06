from typing import List, Tuple
from PyQt6.QtCore import QObject, pyqtSignal
import random
from typing import TYPE_CHECKING, List, Tuple
if TYPE_CHECKING:
    from widgets.main_widget import MainWidget
from data.letter_data import positions, letters

class InterpolationHandler(QObject):
    sequenceUpdated = pyqtSignal()
    savedWordsUpdated = pyqtSignal()

    def __init__(self, main_widget: 'MainWidget') -> None:
        super().__init__()
        self.main_widget = main_widget
        self.sequence: List[
            Tuple[str, bool]
        ] = []  # Stores the sequence of letters and whether they are interpolated
        self.saved_words: List[List[Tuple[str, bool]]] = []
        self.auto_fill_mode: bool = False

        
    def update_sequence(self, letter: str) -> None:
        if not self.sequence:
            self.sequence.append((letter, False))
        else:
            last_letter, _ = self.sequence[-1]
            if (
                positions[last_letter][1] == positions[letter][0]
                or self.auto_fill_mode
            ):
                if (
                    self.auto_fill_mode
                    and positions[last_letter][1] != positions[letter][0]
                ):
                    interpolated_letter = self.find_interpolation(last_letter, letter)
                    if interpolated_letter:
                        self.sequence.append((interpolated_letter, True))
                self.sequence.append((letter, False))
            else:
                return  # Invalid sequence, do nothing

        self.sequenceUpdated.emit()
        self.main_widget.letter_buttons.update_button_appearance()

    def find_interpolation(self, start_letter: str, next_letter: str) -> str:
        for letter, pos in positions.items():
            if (
                pos[0] == positions[start_letter][1]
                and pos[1] == positions[next_letter][0]
            ):
                return letter
        return None  # No interpolation found

    def get_last_letter(self):
        return self.sequence[-1][0] if self.sequence else None

    def is_valid_next_letter(self, last_letter, next_letter):
        if not last_letter:
            return True
        return positions[last_letter][1] == positions[next_letter][0] or self.auto_fill_mode


    def clear_sequence(self) -> None:
        self.sequence.clear()
        self.sequenceUpdated.emit()

    def save_current_sequence(self) -> None:
        self.saved_words.append(self.sequence.copy())
        self.clear_sequence()
        self.savedWordsUpdated.emit()

    def clear_saved_words(self) -> None:
        self.saved_words.clear()
        self.savedWordsUpdated.emit()

    def set_auto_fill_mode(self, mode: bool) -> None:
        self.auto_fill_mode = mode
        self.sequenceUpdated.emit()  # Update sequence as auto-fill mode might change the sequence validity

    def get_saved_words(self) -> List[List[str]]:
        return self.saved_words

    def get_sequence(self) -> List[Tuple[str, bool]]:
        return self.sequence
    
    def get_end_position(self, letter: str) -> str:
        position = positions[letter][1]
        return position.replace("alpha", "α").replace("beta", "β").replace("gamma", "Γ")

    def generate_word(self, length: int, end_at_start: bool) -> List[str]:
        if length == 1:
            return [random.choice(letters)]

        word = [random.choice(letters)]
        while len(word) < length:
            next_position = positions[word[-1]][1]
            possible_letters = [
                l for l, pos in positions.items() if pos[0] == next_position
            ]
            word.append(random.choice(possible_letters))

        if end_at_start:
            start_position = positions[word[0]][0]
            word[-1] = random.choice(
                [l for l, pos in positions.items() if pos[1] == start_position]
            )

        self.saved_words.append(word)
        return word
