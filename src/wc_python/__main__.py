import argparse
from utils import file_utils, stdin_utils

def main():
    # Command line arguments
    parser = argparse.ArgumentParser("wc_python", description="A recreation of Unix WC utility in python")
    parser.add_argument("-v", "--version", action="store_true", help="Show version details and exit")
    parser.add_argument("FILE", type=str, nargs="*", help="the file to be processed, if - the STDIN will be used")

    args = parser.parse_args()
    
    # Version details
    if args.version:
        print("wc_pyhon version 0.2.0")
        print("Written by BlackDandel10n")
        print("Summer 2025")
        quit()

    # No FILE
    if not args.FILE:
        details = stdin_utils.get_details()
        quit()

    # With FILE
    for f in args.FILE:
        # STDIN
        if f == "-":
            details = stdin_utils.get_details()
        else:
            # File
            # Check file availability
            meta_data = file_utils.get_metadata(f)
            if not meta_data["exists"]:
                print(f"{parser.prog}: No such file or directory: {f}")
                continue
            elif not meta_data["is_file"]:
                print(f"{parser.prog}: {f}: Is a directory")
                continue

            details = file_utils.get_details(f)

if __name__ == "__main__":
    main()
