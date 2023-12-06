import tkinter as tk
import tkinter.ttk as ttk
from data import *
from functions import ButtonEventHandlers, UIUpdater, Interpolation, UIInitializer
from tkinter import BooleanVar


root = tk.Tk()

root.geometry("1000x900")
root.title("Word Constructor")

buttons_frame = tk.Frame(root)
buttons_frame.grid(row=0, column=0, rowspan=len(letter_rows), sticky="nw")
buttons = {}

state_label = tk.Label(root, text="", font=("Helvetica", "20"))
state_label.grid(row=3, column=3, sticky="nw", padx=50)

sequence_label = tk.Text(
    root, font=("Helvetica", "32"), height=1, width=20, cursor="xterm"
)
sequence_label.bind("<1>", lambda event: sequence_label.focus_set())
sequence_label.tag_config("red", foreground="red")
sequence_label.tag_config("black", foreground="black")
sequence_label.tag_configure("sel", background="yellow")
sequence_label.grid(row=2, column=3, sticky="w")

scrollbar = tk.Scrollbar(root)
scrollbar.grid(row=8, column=4, sticky="ns")

start_position_label = tk.Label(root, text="", font=("Helvetica", "20"))
start_position_label.grid(row=0, column=3, sticky="w")

end_positions_label = tk.Label(root, text="", font=("Helvetica", "20"))
end_positions_label.grid(row=1, column=3, sticky="w")  # change row to 3

saved_label = tk.Label(root, text="Saved:", font=("Helvetica", "20"))
saved_label.grid(row=7, column=3, sticky="w")

sequence_clear_button = tk.Button(
    root, text="Clear", height=2, width=4, font=("Helvetica", "20")
)
sequence_clear_button.grid(row=5, column=2, sticky="w", padx=50)

auto_fill_mode = tk.BooleanVar(value=False)
auto_fill_checkbox = tk.Checkbutton(
    root, text="Autofill Mode", variable=auto_fill_mode, font=("Helvetica", "20")
)
auto_fill_checkbox.grid(row=3, column=3, sticky="nw", pady=(0, 20))

interpolation_label = tk.Label(root, text="Type a Word:", font=("Helvetica", "20"))
interpolation_input = tk.Entry(root, font=("Helvetica", "20"))
interpolation_button = tk.Button(
    root, text="Generate", width=8, font=("Helvetica", "20")
)

saved_text = tk.Text(root, font=("Helvetica", "20"), height=8, width=30)
saved_text.grid(row=8, column=3, sticky="w")
saved_text.config(state="disabled")
saved_text.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=saved_text.yview)

save_button = tk.Button(root, text="Save", height=1, width=4, font=("Helvetica", "20"))
save_button.grid(row=6, column=2, sticky="w", padx=50)

button_frame = tk.Frame(root)
button_frame.grid(row=9, column=3)  # place frame at row 9, column 3

clear_saved_button = tk.Button(
    button_frame, text="Clear", height=1, width=4, font=("Helvetica", "20")
)
clear_saved_button.pack(side="left")  # add clear button to the left side of the frame

copy_saved_button = tk.Button(
    button_frame, text="Copy", height=1, width=4, font=("Helvetica", "20")
)
copy_saved_button.pack(side="left")

context_menu_sequence = tk.Menu(root, tearoff=0)
context_menu_sequence.add_command(
    label="Copy", command=lambda: button_event_handler.copy_text(sequence_label)
)

context_menu_saved = tk.Menu(root, tearoff=0)
context_menu_saved.add_command(
    label="Copy", command=lambda: button_event_handler.copy_text(saved_text)
)

random_word_length_label = tk.Label(root, text="Word length:", font=("Helvetica", "20"))
random_word_length_input = tk.Entry(root, font=("Helvetica", "20"))
random_word_button = tk.Button(
    root, text="Generate Random Word", height=1, width=20, font=("Helvetica", "20")
)
random_word_length_label.grid(row=10, column=3, sticky="w")
random_word_length_input.grid(row=11, column=3, sticky="w")
random_word_button.grid(row=12, column=3, sticky="w")

end_at_start_position_var = BooleanVar()

# Create the checkbox
circular_word_checkbox = tk.Checkbutton(
    root,
    font=("Helvetica", "20"),
    text="Circular Word",
    variable=end_at_start_position_var,
)
circular_word_checkbox.grid(
    row=13, column=3, sticky="w"
)  # Change row and column values accordingly

start_letters = [row[0] for row in letter_rows]

style = ttk.Style()
style.configure("TButton", font=("Helvetica", "20"), anchor="center")

saved_text.tag_config("red", foreground="red")
saved_text.tag_config("black", foreground="black")

for i, row in enumerate(letter_rows):
    row_frame = tk.Frame(buttons_frame)
    row_frame.grid(row=i, column=0, sticky="w")
    for letter in row:
        button = tk.Button(
            row_frame,
            text=letter,
            height=1,
            width=2,
            font=("Helvetica", "20"),
            background="gray",
            foreground="black",
        )

        button.pack(side=tk.LEFT)
        buttons[letter] = button

interpolation = Interpolation(
    sequence_label,
    start_position_label,
    end_positions_label,
    interpolation_input,
    auto_fill_mode,
    start_letters,
    positions,
)
ui_updater = UIUpdater(
    root,
    sequence_label,
    saved_text,
    state_label,
    start_position_label,
    end_positions_label,
    buttons,
    scrollbar,
    auto_fill_mode,
    interpolation,
)
interpolation.set_ui_updater(ui_updater)
button_event_handler = ButtonEventHandlers(
    root,
    buttons,
    ui_updater,
    interpolation,
    auto_fill_mode,
    interpolation_label,
    interpolation_input,
    interpolation_button,
    context_menu_sequence,
    context_menu_saved,
    sequence_label,
    saved_text,
    end_positions_label,
    random_word_length_input,
    end_at_start_position_var,
)
ui_initializer = UIInitializer(
    root,
    buttons,
    interpolation,
    interpolation_label,
    interpolation_input,
    interpolation_button,
    button_event_handler,
    auto_fill_mode,
    random_word_button,
)
ui_initializer.initialize_ui()

sequence_clear_button.config(command=lambda: ui_updater.clear_sequence())
sequence_label.bind(
    "<Button-3>",
    lambda event: button_event_handler.show_context_menu(
        event, sequence_label, context_menu_sequence
    ),
)
sequence_label.bind("<KeyPress>", button_event_handler.on_key_press)
auto_fill_checkbox.config(command=button_event_handler.on_auto_fill_mode_toggle)
saved_text.bind(
    "<Button-3>",
    lambda event: button_event_handler.show_context_menu(event, saved_text),
)

save_button.config(command=lambda: ui_updater.save_sequence())
clear_saved_button.config(command=lambda: ui_updater.clear_saved())
copy_saved_button.config(command=button_event_handler.copy_saved_text)
random_word_button.config(command=button_event_handler.generate_random_word)

root.mainloop()


import tkinter as tk
import random
from data import *
import tkinter as tk
import random
from data import *


class UIInitializer:
    def __init__(
        self,
        root: tk.Tk,
        buttons: dict,
        interpolation,
        interpolation_label: tk.Label,
        interpolation_input: tk.Entry,
        interpolation_button: tk.Button,
        event_handler,
        auto_fill_mode: tk.BooleanVar,
        random_word_button: tk.Button,
    ):
        self.buttons = buttons
        self.interpolation = interpolation
        self.interpolation_label = interpolation_label
        self.interpolation_input = interpolation_input
        self.interpolation_button = interpolation_button
        self.event_handler = event_handler
        self.auto_fill_mode = auto_fill_mode
        self.random_word_button = random_word_button
        self.random_word_button.config(
            command=lambda: event_handler.generate_random_word()
        )
        random_word_button.config(command=lambda: event_handler.generate_random_word())

    def initialize_ui(self):
        self.interpolation_input.bind(
            "<Return>", lambda event: self.interpolation.interpolate_sequence()
        )
        self.interpolation_button.config(
            command=lambda: self.interpolation.interpolate_sequence()
        )

        for letter, button in self.buttons.items():
            button.config(
                command=lambda letter=letter: self.interpolation.update_state(
                    letter, self.auto_fill_mode
                )
            )
            button.bind("<Enter>", lambda e: self.event_handler.on_enter(e))
            button.bind("<Leave>", lambda e: self.event_handler.on_leave(e))


class UIUpdater:
    def __init__(
        self,
        root: tk.Tk,
        sequence_label: tk.Label,
        saved_text: tk.Text,
        state_label: tk.Label,
        start_position_label: tk.Label,
        end_positions_label: tk.Label,
        buttons: dict,
        scrollbar: tk.Scrollbar,
        auto_fill_mode: tk.BooleanVar,
        interpolation,
    ):
        self.root = root
        self.sequence_label = sequence_label
        self.saved_text = saved_text
        self.state_label = state_label
        self.start_position_label = start_position_label
        self.end_positions_label = end_positions_label
        self.buttons = buttons
        self.scrollbar = scrollbar
        self.auto_fill_mode = auto_fill_mode
        self.interpolation = interpolation

        self.bind_button_events()

    def bind_button_events(self):
        for letter, button in self.buttons.items():
            button.bind(
                "<Enter>", lambda e, lt=letter: self.show_positional_outcome(e, lt)
            )
            button.bind("<Leave>", self.restore_positional_outcome)

    def restore_positional_outcome(self, event: tk.Event):
        if event.type == "8":  # Mouse leaves the button
            self.update_end_positions_label()

    def save_sequence(self):
        saved_words.append(state["sequence"].copy())
        self.update_saved_words_label()
        self.clear_sequence()

    def update_end_positions_label(self):
        end_positions_str = self.interpolation.get_positional_outcome(state["sequence"])
        self.end_positions_label.config(text=end_positions_str)

    def update_saved_words_label(self):
        self.saved_text.config(state="normal")
        self.saved_text.delete("1.0", tk.END)
        for word in saved_words:
            for letter in word:
                if letter[1]:
                    self.saved_text.insert("end", letter[0], "red")
                else:
                    self.saved_text.insert("end", letter[0], "black")
            self.saved_text.insert("end", "\n")
        self.saved_text.config(state="disabled")

        # Check if scrollbar is needed
        self.check_scrollbar_needed()

    def check_scrollbar_needed(self):
        yview = self.saved_text.yview(tk.END)
        if yview and yview[1] > 1:
            self.scrollbar.pack(
                side="right", fill="y"
            )  # pack the scrollbar to make it visible
        else:
            self.scrollbar.pack_forget()  # forget the scrollbar to hide it

    def update_buttons(self):
        for letter, button in self.buttons.items():
            if not state[
                "sequence"
            ]:  # If sequence is empty, then all 'alpha', 'beta', and 'gamma' start positions are possible
                button["state"] = "normal"
                button[
                    "foreground"
                ] = "black"  # Add this line to change the button text color to black
            elif self.auto_fill_mode.get():  # Auto-fill mode is enabled
                last_letter = state["sequence"][-1]
                if (
                    positions[last_letter[0]][1] == positions[letter][0]
                ):  # Can follow without interpolation
                    button["state"] = "normal"
                    button["foreground"] = "black"
                else:  # Needs interpolation
                    button["state"] = "normal"
                    button["foreground"] = "white"
            else:  # Auto-fill mode is not enabled
                if self.interpolation.can_follow(
                    letter
                ):  # Can follow without interpolation
                    button["state"] = "normal"
                    button["foreground"] = "black"
                else:  # Cannot follow
                    button["state"] = "disabled"
                    button["foreground"] = "black"

    def update_state_label(self, letter, auto_fill_mode):
        self.state_label.config(text=positions[letter][1])
        self.auto_fill_mode = auto_fill_mode

    def clear_sequence(self):
        state["sequence"].clear()
        self.sequence_label.config(state="normal")
        self.sequence_label.delete("1.0", tk.END)
        self.sequence_label.config(state="disabled")
        self.start_position_label.config(text="")
        self.update_buttons()
        self.end_positions_label.config(text="")

        if len(saved_words) == 0:
            self.scrollbar.config(state="disabled")

    def clear_saved(self):
        self.saved_text.config(state="normal")
        self.saved_text.delete("1.0", tk.END)
        self.saved_text.config(state="disabled")
        saved_words.clear()
        # Check if scrollbar is needed
        self.check_scrollbar_needed()


class ButtonEventHandlers:
    def __init__(
        self,
        root,
        buttons,
        ui_updater,
        interpolation,
        auto_fill_mode,
        interpolation_label,
        interpolation_input,
        interpolation_button,
        context_menu_sequence,
        context_menu_saved,
        sequence_label,
        saved_text,
        end_positions_label,
        random_word_length_input,
        end_at_start_position_var,
    ):
        self.root = root
        self.buttons = buttons
        self.ui_updater = ui_updater
        self.interpolation = interpolation
        self.auto_fill_mode = auto_fill_mode
        self.interpolation_label = interpolation_label
        self.interpolation_input = interpolation_input
        self.interpolation_button = interpolation_button
        self.context_menu_sequence = context_menu_sequence
        self.context_menu_saved = context_menu_saved
        self.sequence_label = sequence_label
        self.saved_text = saved_text
        self.end_positions_label = end_positions_label
        self.random_word_length_input = random_word_length_input
        self.end_at_start_position_var = end_at_start_position_var

    def copy_saved_text(self):
        saved_sequences = self.saved_text.get(
            "1.0", "end-1c"
        )  # Get the text from the "Saved Sequences" textbox
        self.root.clipboard_clear()  # Clear the clipboard
        self.root.clipboard_append(saved_sequences)  # Append the text to the clipboard

    def on_auto_fill_mode_toggle(self):
        if self.auto_fill_mode.get():
            self.interpolation_label.grid(row=4, column=3, sticky="w")  # show the label
            self.interpolation_input.grid(row=5, column=3, sticky="w")  # show the input
            self.interpolation_button.grid(
                row=6, column=3, sticky="w"
            )  # show the button
        else:
            self.interpolation_label.grid_remove()  # hide the label
            self.interpolation_input.grid_remove()  # hide the input
            self.interpolation_button.grid_remove()  # hide the button
        self.ui_updater.update_buttons()

    def show_context_menu(self, event, widget):
        if widget == self.sequence_label:
            self.context_menu_sequence.tk_popup(event.x_root, event.y_root)
        elif widget == self.saved_text:
            self.context_menu_saved.tk_popup(event.x_root, event.y_root)

    def copy_text(self, widget):
        try:
            selected_text = widget.get("sel.first", "sel.last")
            self.root.clipboard_clear()
            self.root.clipboard_append(selected_text)
        except tk.TclError:
            pass  # Nothing selected, do nothing

    def on_key_press(self, event):
        if (
            event.char.upper() in self.buttons
        ):  # if the key pressed is one of the letters
            self.interpolation.update_state(event.char.upper(), self.auto_fill_mode)
        elif event.keysym == "BackSpace":  # if the backspace key is pressed
            state["sequence"].pop()
            self.sequence_label.config(state="normal")
            self.sequence_label.delete("end - 2c")  # remove the last character
            self.sequence_label.config(state="disabled")

    def show_positional_outcome(self, event, letter):
        if event.type == "7":  # Mouse enters the button
            self.end_positions_label.config(
                text=self.interpolation.append_positional_outcome(letter)
            )
        elif event.type == "8":  # Mouse leaves the button
            self.ui_updater.update_end_positions_label()

    def on_enter(self, e):
        letter = e.widget.cget("text")

        # Check if the letter is valid
        if self.interpolation.can_follow(letter):
            self.original_end_positions = self.end_positions_label.cget("text")

            # Get the outcome as a string
            outcome = self.interpolation.append_positional_outcome(letter)

            # Replace position names with Greek variables
            outcome = (
                outcome.replace("alpha", "α").replace("beta", "β").replace("gamma", "Γ")
            )

            # Append the new outcome to the original sequence
            new_positions = f"{outcome}"

            # Set the label text
            self.end_positions_label.config(text=new_positions)

    def on_leave(self, e):
        self.ui_updater.update_end_positions_label()

    def generate_random_word(self):
        if self.random_word_length_input.get().isdigit():
            word_length = int(self.random_word_length_input.get())
        else:
            word_length = 4
        if self.end_at_start_position_var.get():
            word = self.interpolation.generate_word_ending_at_start_position(
                word_length
            )  # If checkbox is checked, generate word ending at start position
        else:
            word = self.interpolation.generate_word(
                word_length
            )  # If checkbox is not checked, generate word normally

        # Add the generated word to the saved_words list
        saved_words.append(
            [(char, False) for char in word]
        )  # We are adding the word as a list of tuples (letter, interpolated)

        # Update the saved_words label
        self.ui_updater.update_saved_words_label()


class Interpolation:
    def __init__(
        self,
        sequence_label,
        start_position_label,
        end_positions_label,
        interpolation_input,
        auto_fill_mode,
        start_letters,
        positions,
    ):
        self.sequence_label = sequence_label
        self.start_position_label = start_position_label
        self.end_positions_label = end_positions_label
        self.interpolation_input = interpolation_input
        self.auto_fill_mode = auto_fill_mode
        self.start_letters = start_letters
        self.positions = positions

    def set_ui_updater(self, ui_updater):
        self.ui_updater = ui_updater

    def find_interpolation(self, start, end):
        valid_letters = [
            letter
            for letter, pos in positions.items()
            if pos[0] == positions[start][1] and pos[1] == positions[end][0]
        ]
        if valid_letters:
            return random.choice(valid_letters)
        return None

    def find_intermediate_letters(self, start, end):
        return [
            letter
            for letter, pos in positions.items()
            if pos[0] == start and pos[1] == end
        ]

    def interpolate_sequence(self):
        sequence = self.interpolation_input.get().upper()
        self.interpolation_input.delete(0, "end")  # clear the input field
        interpolated_sequence = []
        for i in range(len(sequence) - 1):
            start = sequence[i]
            end = sequence[i + 1]
            interpolated_sequence.append(
                (start, False)
            )  # the user-typed letters are not interpolated
            if (
                positions[start][1] != positions[end][0]
            ):  # checks if the end position of current letter != start position of next letter
                interpolated = self.find_interpolation(start, end)  # use self here
                if interpolated:
                    interpolated_sequence.append(
                        (interpolated, True)
                    )  # the interpolated letters are marked as interpolated
        interpolated_sequence.append((sequence[-1], False))  # append the last letter
        # save the interpolated sequence
        saved_words.append(interpolated_sequence)
        self.ui_updater.update_saved_words_label()  # use self.ui_updater

    def update_state(self, letter, auto_fill_mode):
        if not state["sequence"] or self.can_follow(letter):  # use self here
            state["sequence"].append((letter, False))
            self.sequence_label.config(state="normal")
            self.sequence_label.insert("end", letter, "black")
            self.sequence_label.config(state="disabled")
        elif self.auto_fill_mode.get():
            prev_letter = state["sequence"][-1]
            intermediate_letters = self.find_intermediate_letters(
                positions[prev_letter[0]][1], positions[letter][0]
            )  # use self here
            if intermediate_letters:
                intermediate_letter = random.choice(intermediate_letters)
                state["sequence"].append((intermediate_letter, True))
                self.sequence_label.config(state="normal")
                self.sequence_label.insert("end", intermediate_letter, "red")
                self.sequence_label.config(state="disabled")
                state["sequence"].append((letter, False))
                self.sequence_label.config(state="normal")
                self.sequence_label.insert("end", letter, "black")
                self.sequence_label.config(state="disabled")
        else:
            return
        self.ui_updater.update_end_positions_label()
        if len(state["sequence"]) == 1:  # if it's the first character
            start_position_str = (
                positions[letter][0]
                .replace("alpha", "α")
                .replace("beta", "β")
                .replace("gamma", "Γ")
            )
            self.start_position_label.config(text=f"Start: {start_position_str}")
        self.ui_updater.update_buttons()

    def can_follow(self, letter):
        if not state["sequence"]:
            return positions[letter][0] in ["alpha", "beta", "gamma"]
        last_letter = state["sequence"][-1]
        return positions[last_letter[0]][1] == positions[letter][0]

    def get_positional_outcome(self, sequence):
        end_positions = [positions[lt[0]][1] for lt in sequence]
        return (
            " ".join(end_positions)
            .replace("alpha", "α")
            .replace("beta", "β")
            .replace("gamma", "Γ")
        )

    def append_positional_outcome(self, letter):
        end_positions = [
            positions[lt[0]][1] for lt in state["sequence"].copy()
        ]  # create a copy of the sequence
        end_positions.append(positions[letter][1])
        end_positions_str = (
            " ".join(end_positions)
            .replace("alpha", "α")
            .replace("beta", "β")
            .replace("gamma", "Γ")
        )
        return end_positions_str

    def generate_word(self, word_length):
        # Pick a random start letter
        start_letter = random.choice(self.start_letters)
        word = [start_letter]

        # Get the start and end position of the start letter
        start_position, end_position = positions[start_letter]

        # Generate the rest of the word
        while len(word) < word_length:
            # Pick a random letter whose start position is the current end position
            next_letters = [
                letter for letter, pos in positions.items() if pos[0] == end_position
            ]
            next_letter = random.choice(next_letters)

            word.append(next_letter)

            # Update the end position
            end_position = positions[next_letter][1]

        return word  # return a list of letters, not a string

    def generate_word_ending_at_start_position(self, word_length):
        if word_length == 1:
            return random.choice(self.start_letters)
        word = [random.choice(self.start_letters)]
        for _ in range(word_length - 2):
            current_position = self.positions[word[-1]][1]

            possible_letters = [
                letter
                for letter, pos in self.positions.items()
                if pos[0] == current_position
            ]
            letter = random.choice(possible_letters)
            word.append(letter)

        start_position = self.positions[word[0]][0]
        possible_end_letters = [
            letter
            for letter, pos in self.positions.items()
            if pos[0] == self.positions[word[-1]][1] and pos[1] == start_position
        ]
        letter = random.choice(possible_end_letters)
        word.append(letter)

        return "".join(word)


positions = {
    "A": ("alpha", "alpha"),
    "B": ("alpha", "alpha"),
    "C": ("alpha", "alpha"),
    "D": ("beta", "alpha"),
    "E": ("beta", "alpha"),
    "F": ("beta", "alpha"),
    "G": ("beta", "beta"),
    "H": ("beta", "beta"),
    "I": ("beta", "beta"),
    "J": ("alpha", "beta"),
    "K": ("alpha", "beta"),
    "L": ("alpha", "beta"),
    "M": ("gamma", "gamma"),
    "N": ("gamma", "gamma"),
    "O": ("gamma", "gamma"),
    "P": ("gamma", "gamma"),
    "Q": ("gamma", "gamma"),
    "R": ("gamma", "gamma"),
    "S": ("gamma", "gamma"),
    "T": ("gamma", "gamma"),
    "U": ("gamma", "gamma"),
    "V": ("gamma", "gamma"),
    "W": ("gamma", "alpha"),
    "X": ("gamma", "alpha"),
    "Y": ("gamma", "beta"),
    "Z": ("gamma", "beta"),
    "Σ": ("alpha", "gamma"),
    "Δ": ("alpha", "gamma"),
    "θ": ("beta", "gamma"),
    "Ω": ("beta", "gamma"),
    "Φ": ("beta", "alpha"),
    "Ψ": ("alpha", "beta"),
    "Λ": ("gamma", "gamma"),
    "W-": ("gamma", "alpha"),
    "X-": ("gamma", "alpha"),
    "Y-": ("gamma", "beta"),
    "Z-": ("gamma", "beta"),
    "Σ-": ("beta", "gamma"),
    "Δ-": ("beta", "gamma"),
    "θ-": ("alpha", "gamma"),
    "Ω-": ("alpha", "gamma"),
    "Φ-": ("alpha", "alpha"),
    "Ψ-": ("beta", "beta"),
    "Λ-": ("gamma", "gamma"),
    "α": ("alpha", "alpha"),
    "β": ("beta", "beta"),
    "Γ": ("gamma", "gamma"),
}


letter_rows = [
    ["A", "B", "C"],
    ["D", "E", "F"],
    ["G", "H", "I"],
    ["J", "K", "L"],
    ["M", "N", "O"],
    ["P", "Q", "R"],
    ["S", "T", "U", "V"],
    ["W", "X", "Y", "Z"],
    ["Σ", "Δ", "θ", "Ω"],
    ["Φ", "Ψ", "Λ"],
    ["W-", "X-", "Y-", "Z-"],
    ["Σ-", "Δ-", "θ-", "Ω-"],
    ["Φ-", "Ψ-", "Λ-"],
    ["α", "β", "Γ"],
]

saved_words = []
state = {
    "sequence": [],
}
