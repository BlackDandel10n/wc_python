import argparse
from utils import file_utils, stdin_utils, state_report

GENERAL_ERROR_CODE = 1

def main():
    # Command line arguments
    parser = argparse.ArgumentParser("wc_python", description="A recreation of Unix WC utility in python")
    parser.add_argument("-l", "--lines", action="store_true", help="Print the newline count for FILE")
    parser.add_argument("-c", "--bytes", action="store_true", help="Print the byte count for FILE")
    parser.add_argument("-m", "--chars", action="store_true", help="Print the character count for FILE")
    parser.add_argument("--files0-from", type=str, nargs="+", help="read input from the files specified by NUL-terminated names in file F; If F is - then read names from standard input")
    parser.add_argument("-L", "--max-line-length", action="store_true", help="Print the maximum line length from FILE")
    parser.add_argument("-w", "--words", action="store_true", help="Print the word count for FILE")
    parser.add_argument("--total", type=str, help="when to print a line with total counts; can be: auto, always, only, never")
    parser.add_argument("-v", "--version", action="store_true", help="Show version details and exit")
    parser.add_argument("FILE", type=str, nargs="*", help="the file to be processed, if - the STDIN will be used")

    args = parser.parse_args()
    
    # Version details
    if args.version:
        print("wc_pyhon version 0.9.0")
        print("Written by BlackDandel10n")
        print("Summer 2025")
        quit()

    # Get total state
    total_state = "auto"
    if args.total:
        if args.total not in ["auto", "always", "only", "never"]:
            print(f"{parser.prog}: Invalid value for total: {args.total}")
            quit(GENERAL_ERROR_CODE)
        total_state = args.total

    # Get program state
    state = state_report.get_state(args)

    # Get all FILEs
    all_files = []
    for file in args.FILE:
        all_files.append(file)

    # Read NUL-terminated files
    if args.files0_from:
        for file in args.files0_from:
            nul_term_files = file_utils.read_nul_terminated_file(file)
            
            meta_data = file_utils.get_metadata(file)
            
            if not meta_data["exists"]:
                print(f"{parser.prog}: No such file or directory: {file}")
                quit(GENERAL_ERROR_CODE)
            elif not meta_data["is_file"]:
                print(f"{parser.prog}: {file}: Is a directory")
                quit(GENERAL_ERROR_CODE)

            if nul_term_files is None:
                print(f"{parser.prog}: {file}: Something went wrong")
                quit(GENERAL_ERROR_CODE)
            all_files += nul_term_files

    # No FILE
    if not all_files:
        details = stdin_utils.get_details()
        if details is None:
            print(f"{parser.prog}: Something went wrong")
            quit(GENERAL_ERROR_CODE)

        state_report.report(state, details)
        quit()

    total_details = {
            "bytes": 0,
            "chars": 0,
            "lines": 0,
            "max_length": 0,
            "words": 0,
        }

    # With FILE
    for f in all_files:
        # STDIN
        if f == "-":
            details = stdin_utils.get_details()
            if details is None:
                print(f"{parser.prog}: {f}: Something went wrong")
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
        
        # Add to total
        for key in details.keys():
            total_details[key] += details[key]

        if total_state != "only":
            state_report.report(state, details, f)

    if total_state == "always" or total_state == "only" or (total_state != "never" and len(all_files) > 1):
        state_report.report(state, total_details, "total")

if __name__ == "__main__":
    main()
