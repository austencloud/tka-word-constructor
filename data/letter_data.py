from TypeChecking.TypeChecking import Letters, Dict, Tuple, Positions

positions: Dict[Letters, Tuple[Positions]] = {
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
    ['A', 'B', 'C'],
    ['D', 'E', 'F'],
    ['G', 'H', 'I'],
    ['J', 'K', 'L'],
    ['M', 'N', 'O'],
    ['P', 'Q', 'R'],
    ['S', 'T', 'U', 'V'],
    ['W', 'X', 'Y', 'Z'],
    ['Σ', 'Δ', 'θ', 'Ω'],
    ['Φ', 'Ψ', 'Λ'],
    ['W-', 'X-', 'Y-', 'Z-'],
    ['Σ-', 'Δ-', 'θ-', 'Ω-'],
    ['Φ-', 'Ψ-', 'Λ-'],
    ['α', 'β', 'Γ']
]

saved_words = []
state = {
    'sequence': [],
}

letter_types = {
    "Type 1": [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
    ],
    "Type 2": ["W", "X", "Y", "Z", "Σ", "Δ", "θ", "Ω"],
    "Type 3": ["W-", "X-", "Y-", "Z-", "Σ-", "Δ-", "θ-", "Ω-"],
    "Type 4": ["Φ", "Ψ", "Λ"],
    "Type 5": ["Φ-", "Ψ-", "Λ-"],
    "Type 6": ["α", "β", "Γ"],
}

letters = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
    "Σ",
    "Δ",
    "θ",
    "Ω",
    "Φ",
    "Ψ",
    "Λ",
    "W-",
    "X-",
    "Y-",
    "Z-",
    "Σ-",
    "Δ-",
    "θ-",
    "Ω-",
    "Φ-",
    "Ψ-",
    "Λ-",
    "α",
    "β",
    "Γ",
]