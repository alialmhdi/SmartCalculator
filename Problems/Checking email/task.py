def check_email(string):
    if len(string) != 0:
        symbol_free = is_include_symbol(string)
        if symbol_free:
            if is_one_at(string):
                return bool(is_one_dot_after_at(string))
            return False
        return False
    return False


def is_one_dot_after_at(text):
    dot_index = text.strip().find(".", text.index("@"))
    last_char = text.strip().find(".")
    return bool(dot_index and last_char != dot_index)


def is_one_at(text):
    return bool(text.find("@") and text.count("@") == 1)


def is_include_symbol(text):
    symbol_list = ["/", ":", "\\", "&", "*", "+", "%", "!", ",", " "]
    for symbol in symbol_list:
        if symbol in text.strip():
            return False
    return True
