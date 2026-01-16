def steps(number):
    current_number = number
    number_of_steps = 0
    if number < 1:
        raise ValueError("Only positive integers are allowed")
        
    while current_number > 1:
        if current_number % 2 == 0:
            current_number = current_number / 2
        else:
            current_number = (current_number * 3) + 1
        number_of_steps += 1
        print(f"Current number is: {current_number}")
        
    return number_of_steps