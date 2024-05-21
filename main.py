from src.ecosystem import Ecosystem
from src.display import Display

WINDOW_SIZE = 800

organism_colors = ["red", "blue", "yellow", "purple", "orange", "green", "pink", "brown", "gray", "cyan", "fuchsia", "lime", "maroon", "navy", "olive", "teal", "aqua", "silver"]

ecosystem = Ecosystem(WINDOW_SIZE, organism_colors)

display = Display(WINDOW_SIZE)

while display.is_running:
    display.update(ecosystem)