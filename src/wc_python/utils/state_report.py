from enum import Enum

class StateCode(Enum):
    BYTES = 1
    CHARS = 2
    LINES = 4
    MAX_LENGTH = 8
    WORDS = 16

def get_state(args):
    state = 0
    state |= args.bytes * StateCode.BYTES.value
    state |= args.chars * StateCode.CHARS.value
    state |= args.lines * StateCode.LINES.value
    state |= args.max_line_length * StateCode.MAX_LENGTH.value
    state |= args.words * StateCode.WORDS.value

    return state

def report(state, details, file_name = ""):
    if state & StateCode.LINES.value:
        print(f"{details['lines']:4}", end="\t")
    if state & StateCode.WORDS.value:
        print(f"{details['words']:4}", end="\t")
    if state & StateCode.BYTES.value:
        print(f"{details['bytes']:4}", end="\t")
    if state & StateCode.CHARS.value:
        print(f"{details['chars']:4}", end="\t")
    if state & StateCode.MAX_LENGTH.value:
        print(f"{details['max_length']:4}", end="\t")
    print(file_name)
