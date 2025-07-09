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
            "lines": 0,
        }

        with open(path, "r") as file:
            for line in file:
                for char in line:
                    if char == "\n":
                        details["lines"] += 1
                    details["chars"] += 1

        return details
    except Exception:
        return None

def read_nul_terminated_file(path):
    files = []
    
    try:
        with open(path, "r") as file:
            curr = ""
            
            for line in file:
                for char in line:
                    if char == "\0":
                        files.append(curr)
                        curr = ""
                        continue
                    curr += char
            if len(curr) > 0:
                files.append(curr)
            
            return files
    except Exception:
        return None
