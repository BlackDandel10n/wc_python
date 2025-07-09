from sys import stdin
INT_ERROR_CODE = 130

def get_details():
    details = {
        "bytes": 0,
    }
    try:
        data = stdin.read()
    except KeyboardInterrupt:
        quit(INT_ERROR_CODE)
    except Exception:
        return None

    for char in data:
        details["bytes"] += len(char.encode("utf-8"))
    
    return details
