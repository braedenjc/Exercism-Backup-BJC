MAX_SQUARES = 64
MIN_SQUARES = 1
BASE_FOR_EACH_SQUARE = 2
def square(number):
    if MIN_SQUARES > number or number > MAX_SQUARES:
        raise ValueError("square must be between 1 and 64")
    square_value = 1
    for x in range(1, number):
        square_value *= 2

    return square_value
    


def total():
    total = 0;
    for x in range(MIN_SQUARES, MAX_SQUARES + 1):
        total += square(x)
    return total