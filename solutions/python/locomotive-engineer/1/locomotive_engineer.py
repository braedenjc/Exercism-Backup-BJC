"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return [*args]


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    wrong_car_0, wrong_car_1, mandatory_1st_car, *rest_of_cars = each_wagons_id
    combined_wagons = mandatory_1st_car, *missing_wagons, *rest_of_cars, wrong_car_0, wrong_car_1
    return [*combined_wagons]


def add_missing_stops(route, **kwargs):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    updated_dict = {**route, "stops": [*kwargs.values()]}
    
    return updated_dict


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    updated_dict = {**route, **more_route_information}
    return updated_dict


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    
    """What is happening here: 
        We unpack the list of lists of tuples using zip. This looks like:
        [(x), (y), (z)],
        [(a), (b), (c)],
        [(d), (e), (f)]
        Once unpacked, we then group tuples together.
        (x), (a), (d)
        Which then gets popped into its ...own..tuple? Why?
        It's becoming an iterator becoming a tuple?
        ((x), (a) , d))
    """
    zipped_wagons = zip(*wagons_rows)
    wagon_list = []

    """So, let's go into the tuple of tuples, and create a list from each tuple, and pack that list into a new list."""
    for wagons in zipped_wagons:
        """For each wagon tuples of tuples inside of the zipped_wagons,
            We will pack an existing, originally empty list, with tuples that have been turned into a new list.
            The python syntax below is saying: 
                wagon list, when packed, will be a list.
                Pack the existing contents of the list with the zip iterator wagons, into a list.
        """
        *wagon_list, = *wagon_list, list(wagons)
        #print(*wagon_list)
        #print("\n")
    return [*wagon_list]
