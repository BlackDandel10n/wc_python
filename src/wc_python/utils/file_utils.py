from os.path import isfile, exists, getsize

def get_metadata(path):
    try:
        details = {
            "exists": exists(path),
            "is_file": isfile(path)
        }

        return details
    except Exception:
        return None

def get_details(path):
    try:
        details = {
            "bytes": getsize(path),
            "chars": 0,
        }

        with open(path, "r") as file:
            for line in file:
                for _ in line:
                    details["chars"] += 1

        return details
    except Exception:
        return None
