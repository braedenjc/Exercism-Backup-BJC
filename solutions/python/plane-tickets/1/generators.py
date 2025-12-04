"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """
    seat_letter_list = ["A", "B", "C", "D"]
    for index in range(number):
        yield seat_letter_list[index%len(seat_letter_list)]


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """
    MAX_NUMBER_SEATS_ROW = 4
    BANNED_ROW = 13
    current_row = 1
    letters = generate_seat_letters(number) #This is a looping, finite generator that returns ['A', 'B', 'C', 'D'], looping.
    
    for seat in range(number): 
        if current_row == BANNED_ROW:
            current_row += 1           
        yield str(current_row) + next(letters)      
        if seat % MAX_NUMBER_SEATS_ROW == 3 and seat > 0:
            current_row += 1    

def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """
    seating_dict = {}
    seat = generate_seats(len(passengers))
    for passenger in passengers:
        seating_dict[passenger] = next(seat)
    return seating_dict
    
def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """
    CODE_LENGTH = 12
    for seat in seat_numbers:
        primary_code = seat+flight_id
        number_of_zeroes_to_add = CODE_LENGTH - len(primary_code)
        generated_zeroes = '0' * number_of_zeroes_to_add
        final_code = primary_code + generated_zeroes
        yield final_code
