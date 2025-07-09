from enum import Enum

class StateCode(Enum):
    BYTES = 1
    CHARS = 2

def get_state(args):
    state = 0
    state |= args.bytes * StateCode.BYTES.value
    state |= args.chars * StateCode.CHARS.value

    return state

def report(state, details, file_name = ""):
    if state & StateCode.BYTES.value:
        print(f"{details['bytes']:4}", end="\t")
    if state & StateCode.CHARS.value:
        print(f"{details['chars']:4}", end="\t")
    
    print(file_name)
