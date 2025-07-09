from sys import stdin

def get_details():
    details = {
        "bytes": 0,
    }

    data = stdin.read()
    for char in data:
        details["bytes"] += len(char.encode("utf-8"))
    
    return details
