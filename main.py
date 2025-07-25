

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


def main():
    lines = []
    print("Choose input type: \n1. Keyboard \n2. File")
    choice = input()

    if choice == "1":
        lines = standard_input()
    elif choice == "2":
        print("OK")
    else:
        print("Wrong input")
        return

    for line in lines:   #temporary check
        print(f"- {line}")

if __name__ == "__main__":
    main()
