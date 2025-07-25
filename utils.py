

def format_number(num):
    if num == int(num):
        return str(int(num))
    else:
        return f"{num:.2f}"