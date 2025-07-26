import sys
from parser import define_shape
from utils import format_number

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
    input_from_file = False

    if len(sys.argv) > 1:
        filename = sys.argv[1]
        print("Reading file {filename}")
        lines = file_input(filename)
        input_from_file = True
    else:
        print("Choose input type: \n1. Keyboard \n2. File")
        choice = input()

        if choice == "1":
            lines = standard_input()
        elif choice == "2":
            filename = input("Enter filename: ").strip()
            if not filename:
                filename = DEFAULT_FILENAME
            print(f"Reading file {filename}")
            lines = file_input(filename)
            input_from_file = True
        else:
            print("Invalid input")
            return

    if not lines:
        print("No data found")
        return

    if input_from_file:
        for i, line in enumerate(lines, start=1):
            try:
                shape = define_shape(line)
                if shape is None:
                    raise ValueError("Unknown or invalid shape")
                shape_type = type(shape).__name__
                print(f"{shape_type} Perimeter {format_number(shape.perimeter)} Area {format_number(shape.area)}")
            except Exception as e:
                print(f"Error in line {i}. {e}")
    else:
        for line in lines:
            while True:
                try:
                    shape = define_shape(line)
                    if shape is None:
                        raise ValueError("Unknown or invalid shape")
                    shape_type = type(shape).__name__
                    print(f"{shape_type} Perimeter {format_number(shape.perimeter)} Area {format_number(shape.area)}")
                    break
                except Exception as e:
                    print(f"Error: {e}")
                    print("Please try entering the line again:")
                    line = input().strip()

if __name__ == "__main__":
    main()
