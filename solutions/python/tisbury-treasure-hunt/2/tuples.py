"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    :param record: tuple - with a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """
    #Since every tuple being passed is a pair, we simply return the second entry in the tuple
    return record[1]


def convert_coordinate(coordinate):
    """Split the given coordinate into tuple containing its individual components.

    :param coordinate: str - a string map coordinate
    :return: tuple - the string coordinate split into its individual components.
    """ 
    #Since we are given a string and strings are iterable, we will just pass out a new tuple using a tuple constructor
    return tuple(coordinate)


def compare_records(azara_record, rui_record):
    """Compare two record types and determine if their coordinates match.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, tuple(coordinate_1, coordinate_2), quadrant) trio.
    :return: bool - do the coordinates match?
    """

    #Line 33 takes in a tuple and gets the second value, known as a coordinate, which is a string made of a pair of characters. 
    #Usually in the form of something like "F3"
    azara_coordinate = get_coordinate(azara_record)

    #Line 34 takes the coordinate string and breaks it into a tuple. For example, string "F3" becomes ("F", "3")
    converted_coordinate = convert_coordinate(azara_coordinate)

    #Use the "in" operator to compare the tuple with the values inside of the rui_record tuple. If a tuple inside of rui_record exists that matches,
    #return true!
    return converted_coordinate in rui_record #HOLY SMOKES YOU CAN CHECK FOR TUPLES EXISTING IN OTHER TUPLES


def create_record(azara_record, rui_record):
    """Combine the two record types (if possible) and create a combined record group.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: tuple or str - the combined record (if compatible), or the string "not a match" (if incompatible).
    """
    is_there_a_matching_record = compare_records(azara_record, rui_record)
    if is_there_a_matching_record:
        return azara_record + rui_record
        
    return "not a match"


def clean_up(combined_record_group):
    """Clean up a combined record group into a multi-line string of single records.

    :param combined_record_group: tuple - everything from both participants.
    :return: str - everything "cleaned", excess coordinates and information are removed.

    The return statement should be a multi-lined string with items separated by newlines.

    (see HINTS.md for an example).
    """
    cleaned_record = ""
    for record_tuple in combined_record_group:
        treasure_name = record_tuple[0]
        location_name = record_tuple[2]
        coordinate_tuple = record_tuple[3]
        quadrant_color = record_tuple[4]
        formatted_record = f"""('{treasure_name}', '{location_name}', ('{coordinate_tuple[0]}', '{coordinate_tuple[1]}'), '{quadrant_color}')""" + "\n"
        cleaned_record += formatted_record 
    return cleaned_record