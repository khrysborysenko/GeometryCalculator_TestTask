import sys
from parser import define_shape
from utils import format_number

DEFAULT_FILENAME = "GeometryCalculator_TestData.txt"

def standard_input():   #read lines from keyboard
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

def file_input(filename):   #read lines from file
    try:
        with open(filename, 'r') as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"File '{filename}' not found")
        return []


def main():   #choose input type or open default file, print results
    input_from_file = False

    if len(sys.argv) > 1:   #check the arguments of running
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
            if not filename:   #run default text file
                filename = DEFAULT_FILENAME
            print(f"Reading file {filename}")
            try:
                lines = file_input(filename)
                input_from_file = True
            except FileNotFoundError:
                print("File '{filename}' not found")
                return
        else:
            print("Invalid input")
            return

    if not lines:
        print("No data found")
        return

    if input_from_file:   #output of results and errors after input from file
        for i, line in enumerate(lines, start=1):   #iterate rows to show in case of error
            try:
                shape = define_shape(line)
                if shape is None:
                    raise ValueError("Unknown or invalid shape")
                shape_type = type(shape).__name__
                print(f"{shape_type} Perimeter {format_number(shape.perimeter)} Area {format_number(shape.area)}")
            except Exception as e:
                print(f"Error in line {i}. {e}")
    else:
        for line in lines:   #output of results and errors after standard input
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
