def is_armstrong_number(number):
    number_string = str(number)
    exponent = len(number_string)
    __sum__ = 0
    for x in number_string:
        __sum__ += int(x) ** exponent
    return number == __sum__