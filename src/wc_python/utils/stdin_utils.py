from sys import stdin
INT_ERROR_CODE = 130

def get_details():
    details = {
        "bytes": 0,
        "chars": 0,
        "lines": 0,
    }
    try:
        data = stdin.read()
    except KeyboardInterrupt:
        quit(INT_ERROR_CODE)
    except Exception:
        return None

    for char in data:
        if char == "\n":
            details["lines"] += 1
        details["bytes"] += len(char.encode("utf-8"))
        details["chars"] += 1
    
    return details
