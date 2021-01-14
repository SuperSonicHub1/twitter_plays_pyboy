from pyboy import WindowEvent
from typing import Dict, List, Optional

"""Maps strings to respective press and release `WindowEvent`s."""
BUTTON_INPUTS: Dict[str, List[Optional[WindowEvent]]] = {
    "up": [WindowEvent.PRESS_ARROW_UP, WindowEvent.RELEASE_ARROW_UP],
    "down": [WindowEvent.PRESS_ARROW_DOWN, WindowEvent.RELEASE_ARROW_DOWN],
    "left": [WindowEvent.PRESS_ARROW_LEFT, WindowEvent.RELEASE_ARROW_LEFT],
    "right": [WindowEvent.PRESS_ARROW_RIGHT, WindowEvent.RELEASE_ARROW_RIGHT],
    "a": [WindowEvent.PRESS_BUTTON_A, WindowEvent.RELEASE_BUTTON_A],
    "b": [WindowEvent.PRESS_BUTTON_B, WindowEvent.RELEASE_BUTTON_B],
    "start": [WindowEvent.PRESS_BUTTON_START, WindowEvent.RELEASE_BUTTON_START],
    "select": [WindowEvent.PRESS_BUTTON_SELECT, WindowEvent.RELEASE_BUTTON_SELECT],
    "pass": [None, None]
}
