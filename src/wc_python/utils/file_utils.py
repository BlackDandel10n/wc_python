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
            "max_length": 0,
            "words": 0,
        }

        with open(path, "r") as file:
            is_word = False
            for line in file:
                curr_line_length = 0
                for char in line:
                    if char.isspace():
                        if is_word:
                            details["words"] += 1
                        is_word = False
                        if char == "\n":
                            details["max_length"] = max(details["max_length"], curr_line_length)
                            details["lines"] += 1
                    else:
                        is_word = True

                    details["chars"] += 1
                    curr_line_length += 1
            details["max_length"] = max(details["max_length"], curr_line_length)
            if is_word:
                details["words"] += 1
        
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
