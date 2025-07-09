from enum import Enum

class StateCode(Enum):
    BYTES = 1

def get_state(args):
    state = 0
    state |= args.bytes * StateCode.BYTES.value

    return state

def report(state, details, file_name = ""):
    if state & StateCode.BYTES.value:
        print(f"{details['bytes']:4}", end="\t")
    print(file_name)
