import argparse

def main():
    # Command line arguments
    parser = argparse.ArgumentParser("wc_python", description="A recreation of Unix WC utility in python")
    parser.add_argument("-v", "--version", action="store_true", help="Show version details and exit")

    args = parser.parse_args()
    
    # Version details
    if args.version:
        print("wc_pyhon version 0.1.0")
        print("Written by BlackDandel10n")
        print("Summer 2025")
        quit()

if __name__ == "__main__":
    main()
