def normalise(text):
    return text.replace(" ", "").replace("-", "").upper()

def is_valid(reg):
    if len(reg) not in (9, 10):
        return False
    if not reg[0:2].isalpha():
        return False
    if not reg[2:4].isdigit():
        return False
    series_len = len(reg) - 8
    if series_len not in (1, 2):
        return False
    if not reg[4:4 + series_len].isalpha():
        return False
    if not reg[4 + series_len:].isdigit():
        return False
    return True

def format_reg(reg):
    reg = normalise(reg)
    if not is_valid(reg):
        return "INVALID"
    series_len = len(reg) - 8
    return reg[:2] + " " + reg[2:4] + " " + reg[4:4+series_len] + " " + reg[4+series_len:]
