import argparse
from utils import file_utils, stdin_utils, state_report

GENERAL_ERROR_CODE = 1

def main():
    # Command line arguments
    parser = argparse.ArgumentParser("wc_python", description="A recreation of Unix WC utility in python")
    parser.add_argument("-c", "--bytes", action="store_true", help="Print the byte count for FILE")
    parser.add_argument("-v", "--version", action="store_true", help="Show version details and exit")
    parser.add_argument("FILE", type=str, nargs="*", help="the file to be processed, if - the STDIN will be used")

    args = parser.parse_args()
    
    # Version details
    if args.version:
        print("wc_pyhon version 0.3.0")
        print("Written by BlackDandel10n")
        print("Summer 2025")
        quit()

    # Get program state
    state = state_report.get_state(args)

    # No FILE
    if not args.FILE:
        details = stdin_utils.get_details()
        if details is None:
            print(f"{parser.prog}: Something went wrong")
            quit(GENERAL_ERROR_CODE)

        state_report.report(state, details)
        quit()

    # With FILE
    for f in args.FILE:
        # STDIN
        if f == "-":
            details = stdin_utils.get_details()
            if details is None:
                print(f"{parser.prog}: Something went wrong")
                continue
        else:
            # File
            # Check file availability
            meta_data = file_utils.get_metadata(f)
            is_error = False
            if not meta_data:
                print(f"{parser.prog}: {f}: Something went wrong")
                is_error = True
            elif not meta_data["exists"]:
                print(f"{parser.prog}: No such file or directory: {f}")
                is_error = True
            elif not meta_data["is_file"]:
                print(f"{parser.prog}: {f}: Is a directory")
                is_error = True
            
            if is_error:
                continue

            details = file_utils.get_details(f)
            if details is None:
                print(f"{parser.prog}: {f}: Something went wrong")
                continue

        state_report.report(state, details, f)

if __name__ == "__main__":
    main()
