import sys

DEFAULT_FILENAME = "GeometryCalculator_TestData.txt"

def standard_input():
    print("Enter the shapes")
    lines = []
    while True:
        try:
            line = input()
            if not line.strip():
                break
            lines.append(line)
        except EOFError:
            break
    return lines

def file_input(filename):
    try:
        with open(filename, 'r') as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"File '{filename}' not found")
        return []


def main():

    if len(sys.argv) > 1:
        filename = sys.argv[1]
        print("Reading file {filename}")
        lines = file_input(filename)
    else:
        print("Choose input type: \n1. Keyboard \n2. File")
        choice = input()

        if choice == "1":
            lines = standard_input()
        elif choice == "2":
            print("OK")
            filename = input("Enter filename: ").strip()
            if not filename:
                filename = DEFAULT_FILENAME
            print(f"Reading file {filename}")
            lines = file_input(filename)
        else:
            print("Wrong input")
            return

    if not lines:
        print("No data found")
        return

    for line in lines:   #temporary check
        print(f"- {line}")

if __name__ == "__main__":
    main()
