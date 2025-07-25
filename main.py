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

    # for line in lines:   #temporary check
    #     print(f"- {line}")

    for line in lines:
        shape = define_shape(line)
        if shape:
            shape_type = type(shape).__name__
            print(f"{shape_type} Perimeter {format_number(shape.perimeter)} Area {format_number(shape.area)}")

           #temporary check
            # if hasattr(shape, "side"):
            #     print(f"Side: {shape.side}")
            #
            # if hasattr(shape, "width"):
            #     print(f"Width: {shape.width}")
            #
            # if hasattr(shape, "height"):
            #     print(f"Height: {shape.height}")
            #
            # if hasattr(shape, "position"):
            #     print(f"Position: {shape.position}")
            #
            # if hasattr(shape, "coords"):
            #     print(f"coords: {shape.coords}")
            #
            # if hasattr(shape, "radius"):
            #     print(f"Radius: {shape.radius}")
            #
            # print("--------")

if __name__ == "__main__":
    main()
