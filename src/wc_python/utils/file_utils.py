from os.path import isfile, exists, getsize

def get_metadata(path):
    details = {
        "exists": exists(path),
        "is_file": isfile(path)
    }

    return details

def get_details(path):
    details = {
        "bytes": getsize(path),
    }

    return details
