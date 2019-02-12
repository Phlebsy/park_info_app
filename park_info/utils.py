# Validate input - Must be alphabetical string of length 4 to be a valid abbreviation
def check_park_code(input):
    return type(input) is str and input.isalpha() and len(input) == 4
