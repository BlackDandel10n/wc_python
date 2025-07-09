from sys import stdin
INT_ERROR_CODE = 130

def get_details():
    details = {
        "bytes": 0,
        "chars": 0,
        "lines": 0,
        "max_length": 0,
    }
    try:
        data = stdin.read()
    except KeyboardInterrupt:
        quit(INT_ERROR_CODE)
    except Exception:
        return None
    
    curr_line_length = 0
    for char in data:
        if char == "\n":
            details["max_length"] = max(details["max_length"], curr_line_length)
            curr_line_length = -1
            details["lines"] += 1
        details["bytes"] += len(char.encode("utf-8"))
        details["chars"] += 1
        curr_line_length += 1
    details["max_length"] = max(details["max_length"], curr_line_length)
    
    return details
