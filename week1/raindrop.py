"""Code for raindrop challenge using if statement in function. """
def convert(number: int):
    """Function converting number into its corresponding raindrop sound. """
    if number % 3 == 0 and number % 5 == 0 and number % 7 == 0:
        return "PlingPlangPlong"
    if number % 3 == 0 and number % 5 == 0:
        return "PlingPlang"
    if number % 3 == 0 and number % 7 == 0:
        return "PlingPlong"
    if number % 5 == 0 and number % 7 == 0:
        return "PlangPlong"
    if number % 3 == 0:
        return "Pling"
    if number % 5 == 0:
        return "Plang"
    if number % 7 == 0:
        return "Plong"
    return str(number)
print(convert(15))