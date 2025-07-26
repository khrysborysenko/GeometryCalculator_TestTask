

def format_number(num): #format numbers: integer if possible, else with two decimals
    if num == int(num):
        return str(int(num))
    else:
        return f"{num:.2f}"