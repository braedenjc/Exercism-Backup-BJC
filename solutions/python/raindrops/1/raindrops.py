PLING = "Pling"
PLANG = "Plang"
PLONG = "Plong"
def convert(number):
    raindrop_noise = ""
    is_divisible_by_3 = number % 3 == 0
    is_divisible_by_5 = number % 5 == 0
    is_divisible_by_7 = number % 7 == 0
    
    if is_divisible_by_3:
        raindrop_noise += PLING
    if is_divisible_by_5:
        raindrop_noise += PLANG
    if is_divisible_by_7:
        raindrop_noise += PLONG

    if raindrop_noise == "":
        return str(number)
    else:
        return raindrop_noise
        