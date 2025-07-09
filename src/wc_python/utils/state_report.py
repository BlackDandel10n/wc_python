from enum import Enum

class StateCode(Enum):
    BYTES = 1

def get_state(args):
    state = 0
    state |= args.bytes * StateCode.BYTES.value

    return state
